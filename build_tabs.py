#!/usr/bin/env python3
"""Generate per-tab static pages from index.html for shareable URLs + SEO.

index.html itself is the Research Labs page (served at /).
This script produces /manufacturing/index.html and /entertainment/index.html,
each with the matching tab pre-selected and its own <title>/description/canonical.

Re-run after editing index.html:  python3 build_tabs.py
"""
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://meetprometheus.com"
TABS = ["research", "manufacturing", "entertainment"]

# Per-variant SEO. "research" is index.html itself and is not regenerated.
SEO = {
    "manufacturing": {
        "dir": "manufacturing",
        "title": "Prometheus Robotics — Humanoid Robots for Manufacturing",
        "desc": ("A trainable humanoid for the factory floor: end-of-line testing, "
                 "pick-and-place, and repetitive line tasks. Reconfigures in minutes "
                 "and costs less than a custom automation cell."),
    },
    "entertainment": {
        "dir": "entertainment",
        "title": "Prometheus Robotics — Humanoid Robots for Entertainment & Venues",
        "desc": ("A real interactive humanoid for theme parks, hotels, and events. "
                 "Dress it up, drive it live from VR (Meta Quest 3S), record and replay "
                 "routines, and let it greet and present to guests."),
    },
}


def set_active(html, active_id):
    for tid in TABS:
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


def set_seo(html, title, desc, url):
    block = (
        "<!-- SEO:START -->\n"
        '    <title>%s</title>\n'
        '    <meta name="description" content="%s">\n'
        '    <link rel="canonical" href="%s">\n'
        '    <meta property="og:type" content="website">\n'
        '    <meta property="og:url" content="%s">\n'
        '    <meta property="og:title" content="%s">\n'
        '    <meta property="og:description" content="%s">\n'
        "    <!-- SEO:END -->"
    ) % (title, desc, url, url, title, desc)
    return re.sub(r"<!-- SEO:START -->.*?<!-- SEO:END -->", block, html, flags=re.S)


def main():
    with open(os.path.join(ROOT, "index.html"), encoding="utf-8") as f:
        src = f.read()

    for tid, cfg in SEO.items():
        url = "%s/%s/" % (BASE, cfg["dir"])
        html = set_active(src, tid)
        html = set_seo(html, cfg["title"], cfg["desc"], url)
        out_dir = os.path.join(ROOT, cfg["dir"])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", os.path.relpath(os.path.join(out_dir, "index.html"), ROOT))

    # sitemap
    urls = [BASE + "/"] + ["%s/%s/" % (BASE, SEO[t]["dir"]) for t in SEO]
    items = "\n".join("  <url><loc>%s</loc></url>" % u for u in urls)
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               '%s\n</urlset>\n') % items
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)
    print("wrote sitemap.xml")


if __name__ == "__main__":
    main()
