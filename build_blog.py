#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the (English-only) blog: article pages + the /blog/ index.

Each post's body is an HTML fragment in blog/_content/<slug>.html. Metadata lives
in POSTS below. This script wraps them in the shared template, auto-builds the
"related articles" cross-links and the /blog/ listing, and emits JSON-LD.

Run after editing a fragment or POSTS:  python3 build_blog.py
(then run build_site.py too so the sitemap picks up blog URLs.)
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://meetprometheus.com"

# Order here = order on the /blog/ index (most important first).
POSTS = [
    {
        "slug": "collecting-teleoperation-data-imitation-learning-pi07",
        "title": "Collecting Teleoperation Data for Imitation Learning on a Consumer GPU (π0.7)",
        "h1": "Collecting Teleoperation Data for Imitation Learning on a Consumer GPU with π0.7",
        "crumb": "Teleoperation data for π0.7",
        "eyebrow": "Guide · Vision-Language-Action",
        "description": "Record teleoperation demonstrations on the Prometheus humanoid and fine-tune a π0.7 vision-language-action policy on a single consumer GPU — cameras, dataset format, and training in one workflow.",
        "date": "2026-06-09",
        "date_human": "June 9, 2026",
    },
    {
        "slug": "collecting-teleoperation-data-imitation-learning-act",
        "title": "Collecting Teleoperation Data for Imitation Learning on a Consumer GPU (ACT)",
        "h1": "Collecting Teleoperation Data for Imitation Learning on a Consumer GPU with ACT",
        "crumb": "Teleoperation data for ACT",
        "eyebrow": "Guide · Imitation Learning",
        "description": "A practical walkthrough: record teleoperation demonstrations on the Prometheus humanoid and train an ACT (Action Chunking with Transformers) policy end-to-end on a single consumer GPU.",
        "date": "2026-06-09",
        "date_human": "June 9, 2026",
    },
]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Urbanist:wght@300;400;500;600&display=swap" rel="stylesheet">')

HEADER = (
    '<header class="blog-nav">\n'
    '    <a class="logo" href="/"><img src="/logo.svg" alt="Prometheus Robotics logo"> Prometheus Robotics</a>\n'
    '    <div class="nav-right">\n'
    '        <a href="/blog/">Blog</a>\n'
    '        <a class="hide-sm" href="/">Platform</a>\n'
    '        <a class="blog-cta" href="https://calendar.app.google/SquetjZENQ37ZrCv6" target="_blank" rel="noopener">Book Call</a>\n'
    '    </div>\n'
    '</header>'
)

FOOTER = '<footer class="blog-footer">© 2026 Prometheus Engineering Kft. · <a href="/">meetprometheus.com</a></footer>'

CTA = (
    '<div class="article-cta">\n'
    '    <h3>Run this on a real humanoid</h3>\n'
    '    <p>Prometheus ships with the teleoperation pipeline, stereo + wrist cameras, URDF, simulator, and SDK you need to start collecting data on day one.</p>\n'
    '    <a class="btn" href="https://forms.gle/G5cSyxhieorj9oACA" target="_blank" rel="noopener">Buy Humanoid Robot</a>\n'
    '    <a class="btn secondary" href="/">Explore the platform</a>\n'
    '</div>'
)


def url_for(slug):
    return BASE + "/blog/" + slug + "/"


def json_ld(post):
    url = url_for(post["slug"])
    return ('{"@context":"https://schema.org","@type":"BlogPosting",'
            '"headline":"%s","description":"%s","datePublished":"%s","dateModified":"%s",'
            '"author":{"@type":"Organization","name":"Prometheus Robotics"},'
            '"publisher":{"@type":"Organization","name":"Prometheus Robotics",'
            '"logo":{"@type":"ImageObject","url":"https://meetprometheus.com/logo.png"}},'
            '"image":"https://meetprometheus.com/robot.png","mainEntityOfPage":"%s","inLanguage":"en"}'
            ) % (post["h1"].replace('"', "'"), post["description"].replace('"', "'"),
                 post["date"], post["date"], url)


def related_block(current):
    others = [p for p in POSTS if p["slug"] != current["slug"]]
    if not others:
        return ""
    cards = []
    for p in others:
        cards.append(
            '    <a class="related-card" href="%s">\n'
            '        <div class="rc-title">%s</div>\n'
            '        <div class="rc-desc">%s</div>\n'
            '    </a>' % (url_for(p["slug"]), p["h1"], p["description"])
        )
    return '<div class="related">\n    <h3>Related reading</h3>\n' + "\n".join(cards) + "\n</div>"


def page(post, body):
    url = url_for(post["slug"])
    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        '    <meta charset="UTF-8">\n'
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '    <title>%s — Prometheus Robotics</title>\n'
        '    <meta name="description" content="%s">\n'
        '    <link rel="canonical" href="%s">\n'
        '    <meta name="robots" content="index, follow">\n'
        '    <meta name="theme-color" content="#0a0a0a">\n'
        '    <meta property="og:type" content="article">\n'
        '    <meta property="og:url" content="%s">\n'
        '    <meta property="og:title" content="%s">\n'
        '    <meta property="og:description" content="%s">\n'
        '    <meta property="og:image" content="https://meetprometheus.com/robot.png">\n'
        '    <meta property="og:site_name" content="Prometheus Robotics">\n'
        '    <meta name="twitter:card" content="summary_large_image">\n'
        '    <meta name="twitter:image" content="https://meetprometheus.com/robot.png">\n'
        '    %s\n'
        '    <link rel="stylesheet" href="/blog/blog.css">\n'
        '    <link rel="icon" href="/favicon.ico" type="image/x-icon">\n'
        '    <script type="application/ld+json">%s</script>\n'
        '</head>\n<body>\n%s\n'
        '<main class="article">\n'
        '    <div class="breadcrumb"><a href="/">Home</a> &rsaquo; <a href="/blog/">Blog</a> &rsaquo; %s</div>\n'
        '    <div class="eyebrow">%s</div>\n'
        '    <h1>%s</h1>\n'
        '    <div class="meta">%s · Prometheus Robotics</div>\n'
        '%s\n'
        '%s\n'
        '%s\n'
        '</main>\n%s\n</body>\n</html>\n'
    ) % (post["title"], post["description"], url, url, post["title"], post["description"],
         FONTS, json_ld(post), HEADER, post["crumb"], post["eyebrow"], post["h1"],
         post["date_human"], body, related_block(post), CTA, FOOTER)


def index_page():
    cards = []
    for p in POSTS:
        cards.append(
            '    <a class="post-card" href="%s">\n'
            '        <div class="pc-eyebrow">%s</div>\n'
            '        <h2>%s</h2>\n'
            '        <p>%s</p>\n'
            '        <div class="pc-meta">%s</div>\n'
            '    </a>' % (url_for(p["slug"]), p["eyebrow"], p["h1"], p["description"], p["date_human"])
        )
    body = (
        '<main class="blog-list">\n'
        '    <h1>Blog</h1>\n'
        '    <p class="intro">Engineering notes on building, teleoperating, and training the Prometheus humanoid — imitation learning, vision-language-action models, simulation, and deployment.</p>\n'
        + "\n".join(cards) + "\n</main>"
    )
    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        '    <meta charset="UTF-8">\n'
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '    <title>Blog — Prometheus Robotics</title>\n'
        '    <meta name="description" content="Engineering notes on building, teleoperating, and training the Prometheus humanoid: imitation learning, vision-language-action models, simulation, and deployment.">\n'
        '    <link rel="canonical" href="%s/blog/">\n'
        '    <meta name="robots" content="index, follow">\n'
        '    <meta name="theme-color" content="#0a0a0a">\n'
        '    <meta property="og:type" content="website">\n'
        '    <meta property="og:url" content="%s/blog/">\n'
        '    <meta property="og:title" content="Blog — Prometheus Robotics">\n'
        '    <meta property="og:image" content="https://meetprometheus.com/robot.png">\n'
        '    <meta property="og:site_name" content="Prometheus Robotics">\n'
        '    %s\n'
        '    <link rel="stylesheet" href="/blog/blog.css">\n'
        '    <link rel="icon" href="/favicon.ico" type="image/x-icon">\n'
        '</head>\n<body>\n%s\n%s\n%s\n</body>\n</html>\n'
    ) % (BASE, BASE, FONTS, HEADER, body, FOOTER)


def main():
    for post in POSTS:
        frag = os.path.join(ROOT, "blog", "_content", post["slug"] + ".html")
        with open(frag, encoding="utf-8") as f:
            body = f.read().strip()
        out_dir = os.path.join(ROOT, "blog", post["slug"])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(page(post, body))
        print("wrote blog/%s/index.html" % post["slug"])
    with open(os.path.join(ROOT, "blog", "index.html"), "w", encoding="utf-8") as f:
        f.write(index_page())
    print("wrote blog/index.html")


if __name__ == "__main__":
    main()
