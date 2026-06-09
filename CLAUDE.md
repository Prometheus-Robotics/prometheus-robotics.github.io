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
- `/manufacturing/index.html` and `/entertainment/index.html` are **GENERATED COPIES** of
  `index.html` (matching tab pre-activated + own `<title>`/description/canonical/OG).
- Clicking a tab toggles client-side AND updates the URL via History API (`showUseCase`).

### ⚠️ After editing `index.html`, regenerate the sub-pages:

```
python3 build_tabs.py
```

This rewrites `manufacturing/index.html`, `entertainment/index.html`, and `sitemap.xml`
from `index.html`. **Forgetting this leaves the sub-pages stale.** Commit the regenerated
files together with the `index.html` change. Per-page SEO text lives in the `SEO` dict in
`build_tabs.py`; the head block is delimited by `<!-- SEO:START -->` / `<!-- SEO:END -->`.

`sitemap.xml` (generated) and `robots.txt` exist for indexing.

## Conventions / gotchas

- Header (`nav`) is **transparent at top**, gains dark bg + blur on scroll via `nav.scrolled`
  (toggled by a scroll listener). The "Made in EU" badge border only shows when scrolled.
- Dark theme; colors via CSS vars in `:root` (`--color-accent` is `#3b82f6`).
- No build step / framework / package.json — plain HTML/CSS/JS edited directly.
- To verify a deploy: `curl -s "https://meetprometheus.com/?cb=$RANDOM" | grep <marker>`
  (cache-bust with a random query param; WebFetch caches 15 min).
- `unzip`/`file`/`pip`/`PIL`/`cairosvg` are NOT available here; use `python3` (stdlib) for
  zip extraction etc.
