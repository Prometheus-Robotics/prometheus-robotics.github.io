#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate all static pages for the Prometheus site: per-tab + per-language.

index.html is the English Research-Labs master (served at /). This script
produces, with correct <title>/description/canonical/hreflang and the right tab
pre-selected:
  /manufacturing/  /entertainment/                          (English tabs)
  /<lang>/  /<lang>/manufacturing/  /<lang>/entertainment/   (translated)

Languages live one-per-file in translations/<code>.py, each defining
CODE, LANG, LOCALE, LABEL, CC, SEO (per-tab title/desc) and T (English->translation).

It also rewrites index.html's hreflang block and the JS LANGS array in place, and
writes sitemap.xml.

Re-run after editing index.html OR any translations/*.py:  python3 build_site.py
Add a language: drop a new translations/<code>.py, then re-run.
"""
import glob
import importlib.util
import json
import os
import re

from faq_data import FAQ, FAQ_T

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://meetprometheus.com"

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


def load_languages():
    """Load every translations/*.py module, sorted by code."""
    mods = []
    for path in sorted(glob.glob(os.path.join(ROOT, "translations", "*.py"))):
        name = os.path.splitext(os.path.basename(path))[0]
        if name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location("tr_" + name, path)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        mods.append(m)
    return mods


def esc(s):
    return s.replace("&", "&amp;")


def replace_region(html, start, end, new_block):
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


def set_hreflang(html, tab, codes):
    path = TAB_PATH[tab]
    lines = ['<link rel="alternate" hreflang="x-default" href="%s">' % (BASE + "/" + path)]
    for lang in ["en"] + codes:
        lines.append('<link rel="alternate" hreflang="%s" href="%s">' % (lang, url_for(lang, tab)))
    block = "<!-- HREFLANG:START -->\n    " + "\n    ".join(lines) + "\n    <!-- HREFLANG:END -->"
    return replace_region(html, "<!-- HREFLANG:START -->", "<!-- HREFLANG:END -->", block)


def set_langs(html, mods):
    # English stays hardcoded in index.html with a trailing comma; we emit the
    # rest between the markers (no leading comma -> no array hole).
    entries = ["            { code: '%s', cc: '%s', label: '%s' }" % (m.CODE, m.CC, m.LABEL) for m in mods]
    block = "/* LANGS:START */\n" + ",\n".join(entries) + "\n            /* LANGS:END */"
    return replace_region(html, "/* LANGS:START */", "/* LANGS:END */", block)


def faq_jsonld(pairs):
    items = [{"@type": "Question", "name": q,
              "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]
    data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def set_faq(html, pairs):
    # Localize the visible accordion (no-op for English), then emit FAQPage JSON-LD.
    for (qen, aen), (q, a) in zip(FAQ, pairs):
        html = html.replace(qen, q).replace(aen, a)
    block = "<!-- FAQ-LD:START -->\n    " + faq_jsonld(pairs) + "\n    <!-- FAQ-LD:END -->"
    return replace_region(html, "<!-- FAQ-LD:START -->", "<!-- FAQ-LD:END -->", block)


def set_active(html, active_id):
    for tid in TAB_IDS:
        pcls = "use-case-panel active" if tid == active_id else "use-case-panel"
        html = re.sub(r'<div class="use-case-panel(?: active)?" id="usecase-%s">' % tid,
                      '<div class="%s" id="usecase-%s">' % (pcls, tid), html)
        tcls = "use-case-tab active" if tid == active_id else "use-case-tab"
        html = re.sub(r'<a class="use-case-tab(?: active)?" data-tab="%s"' % tid,
                      '<a class="%s" data-tab="%s"' % (tcls, tid), html)
    return html


def set_tab_hrefs(html, lang):
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


def translate(html, table):
    for en in sorted(table.keys(), key=len, reverse=True):
        tr = table.get(en)
        if tr:
            html = html.replace(en, tr)
    return html


def write(rel_path, html):
    out = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", rel_path)


def main():
    mods = load_languages()
    codes = [m.CODE for m in mods]
    print("languages:", ", ".join(codes) if codes else "(none)")

    with open(os.path.join(ROOT, "index.html"), encoding="utf-8") as f:
        master = f.read()
    master = set_langs(master, mods)  # keep the switcher list in sync

    # English research = index.html itself: refresh SEO, hreflang, LANGS in place.
    idx = set_seo(master, EN_SEO["research"][0], EN_SEO["research"][1], url_for("en", "research"), "en_US")
    idx = set_hreflang(idx, "research", codes)
    idx = set_faq(idx, FAQ)
    write("index.html", idx)

    # English manufacturing / entertainment
    for tab in ["manufacturing", "entertainment"]:
        html = set_active(master, tab)
        html = set_seo(html, EN_SEO[tab][0], EN_SEO[tab][1], url_for("en", tab), "en_US")
        html = set_hreflang(html, tab, codes)
        html = set_faq(html, FAQ)
        write(TAB_PATH[tab] + "index.html", html)

    # Each language × each tab
    for m in mods:
        for tab in TAB_IDS:
            html = translate(master, m.T)
            html = set_active(html, tab)
            title, desc = m.SEO[tab]
            html = set_seo(html, title, desc, url_for(m.CODE, tab), m.LOCALE)
            html = set_hreflang(html, tab, codes)
            html = set_tab_hrefs(html, m.CODE)
            html = set_lang_attr(html, m.CODE)
            html = set_faq(html, FAQ_T.get(m.CODE, FAQ))
            write("%s/%sindex.html" % (m.CODE, TAB_PATH[tab]), html)

    # sitemap (tab/language pages + blog)
    urls = [url_for(lang, tab) for lang in ["en"] + codes for tab in TAB_IDS]
    blog_dir = os.path.join(ROOT, "blog")
    if os.path.isfile(os.path.join(blog_dir, "index.html")):
        urls.append(BASE + "/blog/")
        for d in sorted(glob.glob(os.path.join(blog_dir, "*", "index.html"))):
            slug = os.path.basename(os.path.dirname(d))
            urls.append(BASE + "/blog/" + slug + "/")
    items = "\n".join("  <url><loc>%s</loc></url>" % u for u in urls)
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               '%s\n</urlset>\n') % items
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)
    print("wrote sitemap.xml (%d urls)" % len(urls))


if __name__ == "__main__":
    main()
