# SEO + Google AI Search Audit — kinhnikaya.org

**Site:** VitePress static site, ~614 URLs, host `kinhnikaya.org`.
**Audit date:** 2026-05-17
**Reference:** `~/.claude/skills/google-ai-search-optimization` (Google's `developers.google.com/search/docs/fundamentals/ai-optimization-guide` is canonical).

> Frame: Google AI Overviews + AI Mode = Search. No separate "AEO/GEO" lever. Improve crawl, index, understanding, trust, page experience. Reject AI-only shortcuts.

---

## 1. Executive readout

Site is technically eligible: static HTML, canonical injected per page, sitemap present, `Organization` + `WebSite` + `ScholarlyArticle` JSON-LD, no `noindex` blockers on content. Foundation solid.

Real gaps:
- **Per-sutta pages lack unique `description` meta** → site-wide description repeated across 600+ URLs. Hurts snippet relevance.
- **Sitemap `lastmod` is build date (same for all URLs)** → fake freshness signal. Replace with real per-file `git log -1` mtime.
- **Disallows `/c/` and `/dict/` in `robots.txt`** while those directories contain user-visible content (`docs/c/index.md`, `docs/dict/*.md`). Either index them or remove from the crawl path entirely.
- **`docs/public/llms.txt` exists** → Google ignores it. Harmless but signals cargo-cult SEO; keep only if you genuinely use it for other LLM tooling.
- **Compare pages (`/c/`, `/kinh*/c-*-tmc-vi/`) are dynamic Vue (`[slug].paths.js`)** → verify rendered HTML actually contains both translation texts before crawl, else they are empty shells to Google.
- **E-E-A-T thin**: no visible author byline on sutta pages, no "About / 編集者" block, no `datePublished` / `dateModified` in `ScholarlyArticle`.
- **Sitemap has `<changefreq>` + `<priority>`** → Google ignores. Cosmetic, can drop.

No critical eligibility blockers. Priorities below are ranked by impact on AI Overviews / Search snippet quality and trust.

---

## 2. Priority findings (do in order)

### P0 — Real `lastmod` per URL in sitemap

- **Evidence:** `docs/public/sitemap.xml` — every `<lastmod>` = `2026-05-17` (build date).
- **Impact:** Looks like mass content rewrite each deploy. Crawl budget waste, fake freshness flag.
- **Fix:** VitePress `sitemap` option supports custom `transformItems`. Compute `lastmod` per URL from `git log -1 --format=%cI <md-file>`. Drop `<changefreq>` and `<priority>` entirely.
- **Validate:** `curl https://kinhnikaya.org/sitemap.xml | grep lastmod | sort -u` → expect varied dates. Search Console → Sitemaps → reprocess.

### P0 — Verify compare pages render content server-side

- **Evidence:** `docs/kinhtruongbo/c-pali-tmc-vi/[slug].md` + `[slug].paths.js`. VitePress generates static HTML at build, but Vue `<TextCompare>` may hydrate client-side only.
- **Impact:** If both texts only appear after JS hydration, Googlebot sees empty page → not indexable / not snippet-eligible / invisible to AI Overviews.
- **Fix:**
  1. `pnpm build` then open `docs/.vitepress/dist/kinhtruongbo/c-pali-tmc-vi/dnc-001-kinh-pham-vong.html` in editor.
  2. Confirm Pali + Vietnamese text exist as plain HTML inside `<div id="app">`.
  3. If missing → move text loading into build time (read JSON at SSG, render via `<template>`, not `onMounted`).
- **Validate:** Search Console URL Inspection → "View crawled page" → both languages must appear in HTML.

### P0 — Audit `robots.txt` Disallows vs. real content

- **Evidence:** `docs/public/robots.txt` blocks `/c/` and `/dict/`. But `docs/c/` and `docs/dict/` both contain `.md` files (`1.md`, `2.md`, `dict-01.md`, `5 uẩn.md`, ...) that get built into pages.
- **Impact:** Either (a) wasted content nobody can index, or (b) intentional internal-only data — but then they should not be built as pages.
- **Fix:** Pick one path:
  - If pages are reference content → remove disallows and add them to sitemap.
  - If they are scaffolding for the compare feature → exclude from build via `srcExclude` in `config.ts` so no HTML is emitted (cleaner than `robots.txt`).
- **Validate:** `curl https://kinhnikaya.org/dict/dict-01.html` → expect either 404 (excluded) or 200 + indexable (allowed).

### P1 — Per-page unique meta `description`

- **Evidence:** Sample sutta `docs/kinhtruongbo/thichminhchau/dn-001-kinh-pham-vong.md` has no frontmatter `description`. VitePress falls back to site-wide description for all 600+ sutta pages.
- **Impact:** Duplicate descriptions across the corpus. Google synthesizes its own snippet from body text — usually fine, but a tailored description improves both classic snippets and AI Overview citation labels.
- **Fix:** In `transformPageData` (config.ts line ~227), if `pageData.frontmatter.description` is empty, generate one from `currentBook[currentIndex].text` + book name + translator. Example:
  ```ts
  if (!pageData.frontmatter.description && bookMeta && translatorMeta) {
    pageData.frontmatter.description =
      `${currentBook[currentIndex].text} — ${bookMeta.name} (${bookMeta.alternateName}), bản dịch ${translatorMeta.name}. Đọc song ngữ trên Kinh Nikaya.`;
  }
  ```
- **Validate:** Build → grep `<meta name="description"` across `dist/` → expect unique values per sutta.

### P1 — Add `datePublished` / `dateModified` / `author` to `ScholarlyArticle`

- **Evidence:** `config.ts:382–418`. Schema includes `translator`, `publisher`, `isPartOf` but no dates and no `author`. Translator ≠ author. Buddha is the original speaker; translator is the translator.
- **Impact:** Trust + freshness signal for AI Overviews citation ranking.
- **Fix:** Add `datePublished` from git first-commit of the file, `dateModified` from latest commit, and `author` = `{ "@type": "Person", "name": "Đức Phật Thích Ca Mâu Ni" }` (or omit author entirely — translator alone is defensible for translated scripture).
- **Validate:** Rich Results Test on a sample sutta URL.

### P1 — Decide on `llms.txt`

- **Evidence:** `docs/public/llms.txt` exists; `robots.txt` references it via comment.
- **Impact:** Google does not use it. No SEO impact. Either keep it as documentation for non-Google LLM tooling, or remove to reduce noise.
- **Recommendation:** Keep only if you actively serve it to a specific consumer. Otherwise delete and remove the comment from `robots.txt`. Do not present it as a Google AI optimization.

### P2 — Drop `<changefreq>` and `<priority>` from sitemap

- **Evidence:** Sitemap contains both fields.
- **Impact:** Google ignores them. They expand file size and signal SEO ceremony.
- **Fix:** Strip via VitePress `sitemap.transformItems`. Keep only `<loc>` + real `<lastmod>`.

### P2 — Add `<html lang>` per locale

- **Evidence:** Single site, content in Vietnamese, English, Pali. VitePress default `<html lang="en">` likely set.
- **Impact:** Misclassifies most pages. Affects language targeting and snippet selection.
- **Fix:** Set `lang: 'vi'` in `defineConfig`. For English-only pages (`sujato-en`, `nanamoli-bodhi-en`), override via frontmatter `lang: en` if VitePress supports per-page lang (else accept site-wide `vi` since they are minority).
- **Validate:** View source on sample URL.

### P2 — E-E-A-T: visible author/source block on sutta pages

- **Evidence:** Sutta pages start directly with `# 1. KINH PHẠM VÕNG` and body. No translator credit, no "về dịch giả", no source link to SuttaCentral or Viện Nghiên cứu Phật học Việt Nam.
- **Impact:** Helpful-content + E-E-A-T. Google rewards visible authorship/sourcing for religious/medical/historical material (YMYL-adjacent).
- **Fix:** Render a small footer block on each sutta via a global Vue component or `transformPageData` injection:
  - Translator name + link to translator page.
  - Source attribution (SuttaCentral URL for Sujato, Viện NCPHVN for Thích Minh Châu).
  - "Last updated" from git mtime.
- **Validate:** Spot-check 5 random sutta URLs.

### P2 — Home page content for crawl

- **Evidence:** `docs/index.md` is `<HomePageLayout />` only. Without inspecting the component, the rendered HTML must contain (a) site purpose, (b) top entry links, (c) a short description.
- **Fix:** Open `dist/index.html`, confirm it has indexable text and crawlable `<a href>` links to the four nikayas. If the layout is image-heavy or JS-rendered, add static fallback markdown above `<HomePageLayout />`.

### P3 — Open Graph + Twitter card meta

- **Evidence:** No `og:*` / `twitter:*` tags in `config.ts:head`.
- **Impact:** Zero effect on AI Overviews. Improves Facebook / Twitter / Slack link previews and Discover surface.
- **Fix:** In `transformPageData`, push `og:title`, `og:description`, `og:image` (use book cover from `/public/covers/`), `og:type=article`, `twitter:card=summary_large_image`.

### P3 — Image SEO

- **Evidence:** Book cover images exist in `docs/public/covers/`. Sutta pages have no images.
- **Fix (low priority):** Where a sutta has a natural cover (book level), reference the cover image via `og:image` and `primaryImageOfPage` in JSON-LD. No need to add stock imagery.

---

## 3. Backlog by track

### Technical
- [ ] Real per-URL `lastmod` from git in sitemap.
- [ ] Strip `<changefreq>` + `<priority>`.
- [ ] Resolve `/c/` and `/dict/` ambiguity (build-exclude or remove disallow).
- [ ] Verify compare pages render text in static HTML.
- [ ] Set `<html lang="vi">` and per-page override where useful.
- [ ] Confirm canonical injection works for compare slug pages (`[slug].md`) — `transformPageData` uses `relativePath` but dynamic paths may produce odd canonicals.

### Content
- [ ] Generate per-page meta `description` in `transformPageData`.
- [ ] Add visible translator + source footer block on sutta pages.
- [ ] Add short About / Editorial Policy page (who maintains, how translations are sourced, update cadence). Link from footer.
- [ ] On `hoi-dap.md`, keep FAQPage schema. Already good. Verify the answers match visible text exactly.

### Media
- [ ] `og:image` + `twitter:card` per page (cover at book level, default cover at site level).
- [ ] `alt` text + descriptive filenames for cover images (rename `Generated Image March 13...png.jpeg` → semantic name).

### Structured data
- [ ] Add `datePublished` + `dateModified` to `ScholarlyArticle`.
- [ ] Add `BreadcrumbList` JSON-LD (Home → Nikaya → Translator → Sutta).
- [ ] Consider `Book` (one per nikaya) with `hasPart` listing all suttas — extends what `kinhtruongbo/index.md` already does to other three nikayas.
- [ ] Validate every schema via Rich Results Test on one URL per template.

### Measurement
- [ ] Verify Search Console property (`google06c5a202be4ccfa4.html` already in `/public` → verified).
- [ ] Submit updated sitemap after `lastmod` fix.
- [ ] Track "Pages" + "Page Indexing" reports for compare slug pages over 2 weeks → confirms SSG rendering works.
- [ ] Monitor "Crawl Stats" for drops if `/c/` `/dict/` build-excluded.
- [ ] Lighthouse / PageSpeed Insights on home + one sutta + one compare page → record baseline.

---

## 4. Myths to ignore

- `llms.txt` as a Google AI ranking signal → false. Google uses Search index, not `llms.txt`.
- Special "AI-optimized" Markdown / chunked pages → false. Google retrieves from indexed pages.
- Rewriting suttas for "AI tone" → harmful. Preserves no value, dilutes canonical translations.
- Generating one page per long-tail / fan-out query variant → noise. Strong sutta pages already cover the families.
- Schema.org as an "AI rank hack" → false. Schema clarifies facts; it doesn't bypass ranking.
- Mass mentions / link building for citation in AI Overviews → not a real lever; trust comes from quality + organic links.

---

## 5. Next validation steps

1. `pnpm build`. Open three files in `docs/.vitepress/dist/`:
   - `index.html`
   - `kinhtruongbo/thichminhchau/dn-001-kinh-pham-vong.html`
   - `kinhtruongbo/c-pali-tmc-vi/dnc-001-kinh-pham-vong.html`
   Confirm full text + canonical + JSON-LD present without JS.
2. Run each through Rich Results Test (`search.google.com/test/rich-results`) and PageSpeed Insights.
3. Search Console:
   - URL Inspection on one compare URL → check "View crawled page".
   - Page Indexing report → look for "Discovered – currently not indexed" cluster (often signals duplicate descriptions or thin content).
   - Sitemap report → after `lastmod` fix, resubmit.
4. `site:kinhnikaya.org` in Google → eyeball snippet variety. If 80% snippets look identical, the per-page description fix is the right call.
5. Re-audit in 30 days with the same checklist.

---

## 6. Implementation order (suggested PR plan)

1. **PR 1 — Sitemap correctness**: real `lastmod`, drop `changefreq`/`priority`. (Smallest, validates pipeline.)
2. **PR 2 — Per-page meta description** in `transformPageData`. (High-leverage, low risk.)
3. **PR 3 — robots/build exclusion cleanup** for `/c/` `/dict/`. (Decide intent first.)
4. **PR 4 — Compare page SSG verification + fix** if rendered HTML is empty. (Investigation → code change only if needed.)
5. **PR 5 — Schema enrichment**: `datePublished`, `dateModified`, `BreadcrumbList`, OG/Twitter tags.
6. **PR 6 — Visible authorship/source footer** on sutta pages.
7. **PR 7 — Optional**: remove `llms.txt` or document its non-Google purpose.

Each PR independently mergeable, each verifiable in Search Console within 1–2 crawl cycles.
