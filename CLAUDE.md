# Prometheus Robotics — landing site

Marketing site for a bimanual industrial robot ("manipulation station") + humanoid
research platform. Hosted on **GitHub Pages** (static, no server) at
**https://meetprometheus.com** (see `CNAME`).

- Repo: `Prometheus-Robotics/prometheus-robotics.github.io`, branch `main`.
- Deploys automatically on push to `main`; GitHub Pages build takes ~1–2 min.
- `git remote` uses **SSH** (`git@github.com:...`). HTTPS push fails (no creds on this
  machine). Set local git identity if a fresh clone: `ilia.pavlenkov@outlook.com`.

## Positioning (since July 2026)

**Industrial-first**: the homepage sells EOL testing / bimanual manipulation stations
for factories (tier-1 automotive traction, seed-round narrative). Research labs are the
second audience on `/research/`. The Entertainment audience was removed entirely.
Honesty rules for copy: autonomy is described as *trained per task during the pilot*
(pipeline, not achieved capability); **no prices anywhere on the site**.

## Two master pages

- `index.html` — **industrial homepage** (served at `/`). Sections: hero (badges: EU ·
  NVIDIA Inception · Tier-1 traction; CTAs: Book a Call + For Research Labs) → Traction →
  Problem → The Manipulation Station → How It Works (demonstrate/train/run/compound) →
  Why Manufacturers → specs (no legs/wheels, has "Deployment Options" row) → industrial
  FAQ → Book-a-Call CTA. Separate `#contacts-page` div toggled by `showPage()`.
- `research/index.html` — **research page** (served at `/research/`). Holds the old
  research content: capability grid, "Why labs choose Prometheus", full specs (172cm on
  legs/wheels, Future Modules = legs/wheels), manipulator options, research FAQ
  (Pi0/ACT/compute/teleop), Buy button + form. Same nav/footer/JS/CSS chrome as
  `index.html` — **chrome edits must be applied to BOTH masters by hand**.
- Old tab URLs `/manufacturing/` and `/entertainment/` (and `/<lang>/...` variants) are
  **generated noindex redirect stubs** → language home. GitHub Pages can't 301; the stubs
  use meta-refresh + canonical + JS `location.replace` (SEO-equivalent of a permanent
  redirect). Don't delete them — they keep old URLs from 404ing.
- Assets at repo root, referenced with **root-absolute paths** (`/robot.png`, `/hero.mp4`)
  so they work from sub-directory pages. `hero.mp4` = hero background video (both masters).

## Languages (i18n)

21 languages: en + de, fr, es, it, nl, pl, hu, sv, no, fi, cs, da, ro, bg, lt, lv, et,
sk, sl, hr. Each gets `/<lang>/` and `/<lang>/research/` with hreflang (two clusters).

- All non-English pages + redirect stubs are **GENERATED** by `build_site.py`. Do NOT
  edit generated files by hand — edit a master / `translations/<code>.py` and regenerate.
- `translations/<code>.py` defines `CODE, LANG, LOCALE, LABEL, CC`, per-page `SEO`
  (keys `"home"`, `"research"`), `T` (English string → translation), and translated FAQ
  lists `FAQ_HOME` (4 pairs) + `FAQ_RESEARCH` (6 pairs).
- English FAQ pairs live in `faq_data.py` (`FAQ_HOME`, `FAQ_RESEARCH`); they must match
  the visible accordion text in the masters EXACTLY (that's how localization + FAQPage
  JSON-LD substitution works). No double quotes or `&` in FAQ values.
- Translation is **longest-first literal string replacement** over the whole HTML, so a
  `T` key must be the EXACT English text in the master (incl. `&amp;`). Avoid short
  ambiguous keys (`SDK`, `Pi0`, `URDF`, `NVIDIA Inception` are intentionally NOT
  translated). When a new string contains another key as substring (e.g. "For Research
  Labs" ⊃ "Research Labs"), add the longer string as its own key.
- The nav language switcher is built client-side from the `LANGS` array in each master's
  inline `<script>`; `langHref()` maps the current page (`/` ↔ `/research/`) across langs.
- `translations/_new_strings_en.txt` + `translations/_validate.py` were the July 2026
  repositioning manifest/validator (kept for reference).

### ⚠️ After editing a master, `faq_data.py` OR `translations/*.py`, regenerate:

```
python3 build_site.py
```

Rewrites both masters' SEO/hreflang/FAQ-LD blocks in place, every `/<lang>/...` page,
all redirect stubs, and `sitemap.xml`. **Forgetting this leaves pages stale.** Commit
regenerated files together. Markers: `<!-- SEO:START/END -->`, `<!-- HREFLANG:START/END -->`,
`<!-- FAQ-LD:START/END -->`, `/* LANGS:START/END */`.

### Adding a language
1. Add `{ code, cc, label }` to `LANGS` in BOTH masters (`cc` = flag-icons country code).
2. Create `translations/<code>.py` with SEO (home+research), every `T` key, FAQ_HOME,
   FAQ_RESEARCH. Check with `python3 translations/_validate.py <code>`.
3. Run `python3 build_site.py`, then commit.

## Demo page (English-only)

`/demo/index.html` is a **hand-written** standalone page (YouTube teleop-demo embed +
"Book a call" CTA) with its own inline CSS copied from the site theme — NOT generated
(only its sitemap entry is). Edit it directly.

## Blog (English-only)

Lives under `/blog/`. Generated by `build_blog.py` from HTML body fragments in
`blog/_content/<slug>.html` + the `POSTS` metadata list in `build_blog.py`. Shared
styling is `blog/blog.css`. Blog is **not** translated.

After editing a fragment or `POSTS`: `python3 build_blog.py` then `python3 build_site.py`
(the latter adds `/blog/` URLs to `sitemap.xml`). The "Blog" nav/footer links live in
the masters, so they propagate to all language pages.

## Conventions / gotchas

- Header (`nav`) is **transparent at top**, gains dark bg + blur on scroll (`nav.scrolled`).
- Dark theme; colors via CSS vars in `:root` (`--color-accent` is `#3b82f6`).
- No build framework / package.json — plain HTML/CSS/JS + the two Python generators.
- Booking link everywhere: `https://calendar.app.google/SquetjZENQ37ZrCv6`. Buy form
  (`forms.gle/G5cSyxhieorj9oACA`) appears ONLY on `/research/` pages.
- To verify a deploy: `curl -s "https://meetprometheus.com/?cb=$RANDOM" | grep <marker>`
  (cache-bust; WebFetch caches 15 min). No headless browser on this machine.
- `unzip`/`file`/`pip`/`PIL`/`cairosvg` are NOT available; use `python3` (stdlib).
- Footer year: © 2026.

## Analytics

Umami (cloud, cookieless) + Cloudflare Web Analytics load via `<script>` tags in both
masters' heads (propagate to all language pages) and via the `ANALYTICS` constant in
`build_blog.py` (blog pages). No cookie banner needed.
