# Prometheus Robotics — landing site

Single-page marketing site for a humanoid robot platform. Hosted on **GitHub Pages**
(static, no server) at **https://meetprometheus.com** (see `CNAME`).

- Repo: `Prometheus-Robotics/prometheus-robotics.github.io`, branch `main`.
- Deploys automatically on push to `main`; GitHub Pages build takes ~1–2 min.
- `git remote` uses **SSH** (`git@github.com:...`). HTTPS push fails (no creds on this
  machine). Set local git identity if a fresh clone: `ilia.pavlenkov@outlook.com`.

## Layout

- `index.html` — the entire site (HTML + inline `<style>` + inline `<script>`). This file
  IS the **Research Labs** page, served at `/`. ~1700 lines, everything lives here.
- Assets at repo root, referenced with **root-absolute paths** (`/robot.png`, `/logo.svg`,
  `/hero.mp4`, ...) so they work from sub-directory pages too. Keep new asset refs absolute.
- `hero.mp4` — background video on the hero (autoplay/muted/loop/playsinline).
- `logo.svg` — flame-only mark, white, transparent background (square backdrop was stripped).

## Page sections (in `index.html`, inside `#home-page`)

hero → `research-ready` (the **tabs**) → `specifications` (robot image + specs table +
modules) → `manipulators` → bottom CTA. Separate `#contacts-page` div toggled by `showPage()`.

## Use-case tabs — IMPORTANT

The `research-ready` section has 3 tabs: **Research Labs** (`research`, default),
**Manufacturing**, **Entertainment**. Each is a `.use-case-panel` (`#usecase-<id>`) toggled
by `.use-case-tab` anchors. Each panel = capability grid + a "Why X choose Prometheus"
value-prop block.

Each tab has its own **real URL** for sharing + SEO:
- `/` → research, `/manufacturing/` → manufacturing, `/entertainment/` → entertainment.
- Clicking a tab toggles client-side AND updates the URL via History API (`showUseCase`).

## Languages (i18n)

English master = `index.html` (served at `/`). Other languages get their own real
pages with hreflang, e.g. `/de/`, `/de/manufacturing/`, `/fr/entertainment/`.
Currently generated: **21 languages** — en, de, fr, es, it, nl, pl, hu, sv, no, fi, cs, da, ro, bg, lt, lv, et, sk, sl, hr.

- All non-English pages + the English sub-tab pages are **GENERATED** by `build_site.py`.
  Do NOT edit generated files by hand — edit `index.html` / `i18n_data.py` and regenerate.
- `i18n_data.py` holds `LANG_META`, per-tab `SEO`, and `TRANS` (English string → per-lang
  translation). Translation is **longest-first literal string replacement** over the HTML,
  so a `TRANS` key must be the EXACT English text in `index.html` (incl. `&amp;`). Avoid
  short ambiguous keys (e.g. `SDK`, `Pi0`, `URDF` are intentionally NOT translated).
- The nav language switcher is built client-side from the `LANGS` array in `index.html`'s
  inline `<script>` (flag icons via the `flag-icons` CDN). `window.SITE_LANG` comes from
  `<html data-site-lang>`. Tab/URL routing is language-aware via `window.LANG_BASE`.

### ⚠️ After editing `index.html` OR `i18n_data.py`, regenerate everything:

```
python3 build_site.py
```

This rewrites the English sub-tab pages, every `/<lang>/...` page, the in-place hreflang
block of `index.html`, and `sitemap.xml`. **Forgetting this leaves pages stale.** Commit
the regenerated files together. Per-page SEO blocks are delimited by
`<!-- SEO:START -->`/`<!-- SEO:END -->`; hreflang by `<!-- HREFLANG:START/END -->`.

### Adding a language
1. Add `{ code, cc, label }` to `LANGS` in `index.html` (`cc` = flag-icons country code).
2. Add the code to `LANG_META` + `SEO`, and a translation for EVERY `TRANS` key, in `i18n_data.py`.
3. Run `python3 build_site.py`, then commit.

`sitemap.xml` (generated), `robots.txt`, OG/Twitter meta and JSON-LD (in `index.html` head,
outside the SEO block) exist for SEO.

## Conventions / gotchas

- Header (`nav`) is **transparent at top**, gains dark bg + blur on scroll via `nav.scrolled`
  (toggled by a scroll listener). The "Made in EU" badge border only shows when scrolled.
- Dark theme; colors via CSS vars in `:root` (`--color-accent` is `#3b82f6`).
- No build step / framework / package.json — plain HTML/CSS/JS edited directly.
- To verify a deploy: `curl -s "https://meetprometheus.com/?cb=$RANDOM" | grep <marker>`
  (cache-bust with a random query param; WebFetch caches 15 min).
- `unzip`/`file`/`pip`/`PIL`/`cairosvg` are NOT available here; use `python3` (stdlib) for
  zip extraction etc.
