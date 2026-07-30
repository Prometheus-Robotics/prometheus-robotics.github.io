#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate all static pages for the Prometheus site: per-page + per-language.

Two English master pages:
  index.html          -> industrial homepage, served at /
  research/index.html -> research-labs page, served at /research/

This script produces, with correct <title>/description/canonical/hreflang and
localized FAQ (visible accordion + FAQPage JSON-LD):
  /<lang>/  /<lang>/research/                (translated pages)
plus noindex redirect stubs for the retired tab URLs:
  /manufacturing/  /entertainment/  /<lang>/manufacturing/  /<lang>/entertainment/
(GitHub Pages cannot serve real 301s; the stubs use meta-refresh + canonical +
JS location.replace, which search engines treat as a permanent redirect.)

Languages live one-per-file in translations/<code>.py, each defining CODE, LANG,
LOCALE, LABEL, CC, SEO (per-page title/desc, keys "home"/"research"),
T (English->translation) and FAQ_HOME / FAQ_RESEARCH translated pairs.

It also rewrites both masters' hreflang blocks and the JS LANGS array in place,
and writes sitemap.xml.

Re-run after editing a master OR any translations/*.py:  python3 build_site.py
Add a language: drop a new translations/<code>.py, then re-run.
"""
import glob
import importlib.util
import json
import os

from faq_data import FAQ_HOME, FAQ_RESEARCH

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://meetprometheus.com"

PAGE_IDS = ["home", "research"]
PAGE_PATH = {"home": "", "research": "research/"}
MASTER = {"home": "index.html", "research": "research/index.html"}
EN_FAQ = {"home": FAQ_HOME, "research": FAQ_RESEARCH}
REDIRECT_PATHS = ["manufacturing/", "entertainment/"]

EN_SEO = {
    "home": (
        "Prometheus Robotics — Bimanual Robots for Industrial Automation | EOL Testing",
        "A stationary dual-arm robot that learns industrial tasks from demonstration: end-of-line functional testing, kitting, and machine tending. Designed and made in the EU.",
    ),
    "research": (
        "Prometheus Robotics — Humanoid Platform for Research Labs",
        "A modular humanoid robot built for robotics research: full SDK, stereo + wrist cameras, URDF, bundled simulator, and support for VLA models like Pi0 and ACT.",
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


def url_for(lang, page):
    base = "" if lang == "en" else "/" + lang
    return BASE + (base + "/" + PAGE_PATH[page] or "/")


def set_hreflang(html, page, codes):
    path = PAGE_PATH[page]
    lines = ['<link rel="alternate" hreflang="x-default" href="%s">' % (BASE + "/" + path)]
    for lang in ["en"] + codes:
        lines.append('<link rel="alternate" hreflang="%s" href="%s">' % (lang, url_for(lang, page)))
    block = "<!-- HREFLANG:START -->\n    " + "\n    ".join(lines) + "\n    <!-- HREFLANG:END -->"
    return replace_region(html, "<!-- HREFLANG:START -->", "<!-- HREFLANG:END -->", block)


def set_langs(html, mods):
    # English stays hardcoded in the master with a trailing comma; we emit the
    # rest between the markers (no leading comma -> no array hole).
    entries = ["            { code: '%s', cc: '%s', label: '%s' }" % (m.CODE, m.CC, m.LABEL) for m in mods]
    block = "/* LANGS:START */\n" + ",\n".join(entries) + "\n            /* LANGS:END */"
    return replace_region(html, "/* LANGS:START */", "/* LANGS:END */", block)


def faq_jsonld(pairs):
    items = [{"@type": "Question", "name": q,
              "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]
    data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def set_faq(html, en_pairs, pairs):
    # Localize the visible accordion (no-op for English), then emit FAQPage JSON-LD.
    for (qen, aen), (q, a) in zip(en_pairs, pairs):
        html = html.replace(qen, q).replace(aen, a)
    block = "<!-- FAQ-LD:START -->\n    " + faq_jsonld(pairs) + "\n    <!-- FAQ-LD:END -->"
    return replace_region(html, "<!-- FAQ-LD:START -->", "<!-- FAQ-LD:END -->", block)


def set_lang_hrefs(html, lang):
    """Point internal home/research links at the language's own pages."""
    if lang == "en":
        return html
    html = html.replace('href="/research/"', 'href="/%s/research/"' % lang)
    html = html.replace('href="/"', 'href="/%s/"' % lang)
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


REDIRECT_TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Prometheus Robotics</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="%(url)s">
<meta http-equiv="refresh" content="0;url=%(path)s">
<script>location.replace('%(path)s');</script>
</head>
<body><p>This page has moved: <a href="%(path)s">meetprometheus.com</a></p></body>
</html>
"""


def write_redirect(rel_dir, target_path):
    html = REDIRECT_TMPL % {"path": target_path, "url": BASE + target_path}
    write(rel_dir + "index.html", html)


def main():
    mods = load_languages()
    codes = [m.CODE for m in mods]
    print("languages:", ", ".join(codes) if codes else "(none)")

    for page in PAGE_IDS:
        with open(os.path.join(ROOT, MASTER[page]), encoding="utf-8") as f:
            master = f.read()
        master = set_langs(master, mods)  # keep the switcher list in sync

        # English master: refresh SEO, hreflang, FAQ-LD in place.
        html = set_seo(master, EN_SEO[page][0], EN_SEO[page][1], url_for("en", page), "en_US")
        html = set_hreflang(html, page, codes)
        html = set_faq(html, EN_FAQ[page], EN_FAQ[page])
        write(MASTER[page], html)

        # Each language
        for m in mods:
            seo = m.SEO.get(page) or EN_SEO[page]
            faq_t = getattr(m, "FAQ_HOME" if page == "home" else "FAQ_RESEARCH", None) or EN_FAQ[page]
            html = translate(master, m.T)
            html = set_seo(html, seo[0], seo[1], url_for(m.CODE, page), m.LOCALE)
            html = set_hreflang(html, page, codes)
            html = set_lang_hrefs(html, m.CODE)
            html = set_lang_attr(html, m.CODE)
            html = set_faq(html, EN_FAQ[page], faq_t)
            write("%s/%sindex.html" % (m.CODE, PAGE_PATH[page]), html)

    # Redirect stubs for retired tab URLs (old /manufacturing/, /entertainment/).
    for lang in ["en"] + codes:
        base = "" if lang == "en" else lang + "/"
        target = "/" if lang == "en" else "/%s/" % lang
        for rp in REDIRECT_PATHS:
            write_redirect(base + rp, target)

    # sitemap (page/language pages + blog; /demo/ is unlisted + noindex)
    urls = [url_for(lang, page) for lang in ["en"] + codes for page in PAGE_IDS]
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
