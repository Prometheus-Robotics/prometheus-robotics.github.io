#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate all static pages for the Prometheus site: per-tab + per-language.

index.html is the English Research-Labs master (served at /). This script
produces, with correct <title>/description/canonical/hreflang and the right tab
pre-selected:
  /manufacturing/  /entertainment/                      (English tabs)
  /<lang>/  /<lang>/manufacturing/  /<lang>/entertainment/   (translated)

It also updates index.html's hreflang block in place and writes sitemap.xml.

Re-run after editing index.html OR i18n_data.py:  python3 build_site.py
Add a language: add it to LANGS in index.html's <script>, add SEO + every TRANS
key in i18n_data.py, then re-run.
"""
import os
import re

from i18n_data import LANG_META, SEO, TRANS

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://meetprometheus.com"

# tab id -> url path segment (relative to a language root)
TAB_PATH = {"research": "", "manufacturing": "manufacturing/", "entertainment": "entertainment/"}
TAB_IDS = ["research", "manufacturing", "entertainment"]

EN_SEO = {
    "research": (
        "Prometheus Robotics — Humanoid Platform for Research Labs",
        "A modular humanoid robot built for robotics research: full SDK, stereo + wrist cameras, URDF, bundled simulator, and support for VLA models like Pi0 and ACT.",
    ),
    "manufacturing": (
        "Prometheus Robotics — Humanoid Robots for Manufacturing",
        "A trainable humanoid for the factory floor: end-of-line testing, pick-and-place, and repetitive line tasks. Reconfigures in minutes and costs less than a custom automation cell.",
    ),
    "entertainment": (
        "Prometheus Robotics — Humanoid Robots for Entertainment & Venues",
        "A real interactive humanoid for theme parks, hotels, and events. Dress it up, drive it live from VR (Meta Quest 3S), record and replay routines, and let it greet and present to guests.",
    ),
}

LANGS = list(LANG_META.keys())  # e.g. ["de", "fr"]


def esc(s):
    """Minimal HTML-attribute escaping for SEO text (source uses raw &)."""
    return s.replace("&", "&amp;")


def replace_region(html, start, end, new_block):
    """Replace start..end (inclusive) with new_block."""
    i = html.index(start)
    j = html.index(end, i) + len(end)
    return html[:i] + new_block + html[j:]


def set_seo(html, title, desc, url, locale):
    t, d = esc(title), esc(desc)
    block = (
        "<!-- SEO:START -->\n"
        '    <title>%s</title>\n'
        '    <meta name="description" content="%s">\n'
        '    <link rel="canonical" href="%s">\n'
        '    <meta property="og:type" content="website">\n'
        '    <meta property="og:url" content="%s">\n'
        '    <meta property="og:title" content="%s">\n'
        '    <meta property="og:description" content="%s">\n'
        '    <meta property="og:locale" content="%s">\n'
        "    <!-- SEO:END -->"
    ) % (t, d, url, url, t, d, locale)
    return replace_region(html, "<!-- SEO:START -->", "<!-- SEO:END -->", block)


def url_for(lang, tab):
    base = "" if lang == "en" else "/" + lang
    return BASE + (base + "/" + TAB_PATH[tab] or "/")


def set_hreflang(html, tab):
    path = TAB_PATH[tab]
    lines = ['<link rel="alternate" hreflang="x-default" href="%s">' % (BASE + "/" + path)]
    for lang in ["en"] + LANGS:
        href = url_for(lang, tab)
        lines.append('<link rel="alternate" hreflang="%s" href="%s">' % (lang, href))
    block = "<!-- HREFLANG:START -->\n    " + "\n    ".join(lines) + "\n    <!-- HREFLANG:END -->"
    return replace_region(html, "<!-- HREFLANG:START -->", "<!-- HREFLANG:END -->", block)


def set_active(html, active_id):
    for tid in TAB_IDS:
        pcls = "use-case-panel active" if tid == active_id else "use-case-panel"
        html = re.sub(
            r'<div class="use-case-panel(?: active)?" id="usecase-%s">' % tid,
            '<div class="%s" id="usecase-%s">' % (pcls, tid),
            html,
        )
        tcls = "use-case-tab active" if tid == active_id else "use-case-tab"
        html = re.sub(
            r'<a class="use-case-tab(?: active)?" data-tab="%s"' % tid,
            '<a class="%s" data-tab="%s"' % (tcls, tid),
            html,
        )
    return html


def set_tab_hrefs(html, lang):
    """Prefix the three tab anchor hrefs with /<lang> for non-English pages."""
    if lang == "en":
        return html
    for tid in TAB_IDS:
        old = 'data-tab="%s" href="/%s"' % (tid, TAB_PATH[tid])
        new = 'data-tab="%s" href="/%s/%s"' % (tid, lang, TAB_PATH[tid])
        html = html.replace(old, new)
    return html


def set_lang_attr(html, lang):
    if lang == "en":
        return html
    return html.replace('<html lang="en">', '<html lang="%s" data-site-lang="%s">' % (lang, lang))


def translate(html, lang):
    for en in sorted(TRANS.keys(), key=len, reverse=True):
        tr = TRANS[en].get(lang)
        if tr:
            html = html.replace(en, tr)
    return html


def write(rel_path, html):
    out = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", rel_path)


def main():
    with open(os.path.join(ROOT, "index.html"), encoding="utf-8") as f:
        master = f.read()

    # English research = index.html: refresh its SEO + hreflang in place.
    idx = set_seo(master, EN_SEO["research"][0], EN_SEO["research"][1], url_for("en", "research"), "en_US")
    idx = set_hreflang(idx, "research")
    write("index.html", idx)

    # English manufacturing / entertainment
    for tab in ["manufacturing", "entertainment"]:
        html = set_active(master, tab)
        html = set_seo(html, EN_SEO[tab][0], EN_SEO[tab][1], url_for("en", tab), "en_US")
        html = set_hreflang(html, tab)
        write(TAB_PATH[tab] + "index.html", html)

    # Each language × each tab
    for lang in LANGS:
        html_lang_attr, locale, _label = LANG_META[lang]
        for tab in TAB_IDS:
            html = translate(master, lang)
            html = set_active(html, tab)
            title, desc = SEO[lang][tab]
            html = set_seo(html, title, desc, url_for(lang, tab), locale)
            html = set_hreflang(html, tab)
            html = set_tab_hrefs(html, lang)
            html = set_lang_attr(html, lang)
            write("%s/%sindex.html" % (lang, TAB_PATH[tab]), html)

    # sitemap
    urls = []
    for lang in ["en"] + LANGS:
        for tab in TAB_IDS:
            urls.append(url_for(lang, tab))
    items = "\n".join("  <url><loc>%s</loc></url>" % u for u in urls)
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               '%s\n</urlset>\n') % items
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)
    print("wrote sitemap.xml (%d urls)" % len(urls))


if __name__ == "__main__":
    main()
