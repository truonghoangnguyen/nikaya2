# SEO + Google AI Search Re-Audit — kinhnikaya.org

**Date:** 2026-05-17
**Scope:** Re-audit after implementation of `seo-ai-audit.md`. Live URL inspected: `https://kinhnikaya.org/kinhtruongbo/c-pali-tmc-vi/dnc-007-kinh-jaliya`. `/c/` and `/dict/` excluded per request.
**Reference:** `~/.claude/skills/google-ai-search-optimization` (Google's AI Search guidance is canonical).

> Frame: Google AI Overviews + AI Mode = Search. Audit lever = crawl, index, understanding, trust, page experience. Reject AI-only shortcuts.

---

## 1. Status of prior findings

| Prior item | Status | Note |
|---|---|---|
| P0 — Real per-URL `lastmod` | ✅ Done | Varied dates in `sitemap.xml`. |
| P0 — Compare-page SSG renders content | ✅ Done | Static HTML contains Pali-vi + TMC text. Googlebot eligible. |
| P0 — `/c/` `/dict/` robots cleanup | ⏭️ Skipped | Per user instruction. |
| P1 — Per-page meta `description` | ⚠️ Partial | `og:description` + `twitter:description` per-page. Standard `<meta name="description">` still site-wide. |
| P1 — `datePublished` / `dateModified` on `ScholarlyArticle` | ✅ Done | Visible in JSON-LD. |
| P1 — Decide on `llms.txt` | ⏭️ Pending | Still shipped. |
| P2 — Drop `<changefreq>` + `<priority>` | ❌ Not done | Still in sitemap. |
| P2 — `<html lang>` per locale | ✅ Done | `lang="vi-VN"`. |
| P2 — Visible author/source footer | ✅ Done | "Pali (vi) [link] HT Thích Minh Châu [link]" + "Cập nhật: YYYY-MM-DD". |
| P2 — Home indexable text | ⏭️ Not re-tested | |
| P3 — OG + Twitter meta | ✅ Done | All cards per-page. |
| P3 — Image SEO | ⏭️ Open | Cover image used as `og:image` ✓. |

Foundation now solid. No eligibility blocker. Remaining work = snippet quality + structured-data cleanup.

---

## 2. New / unresolved findings

### P1 — `<meta name="description">` still site-wide on every URL

- **Evidence:** Live `dnc-007-kinh-jaliya` and `dn-007-kinh-jaliya` both serve `<meta name="description" content="Khám phá bộ sưu tập Kinh điển Nikaya...">` — verbatim from `config.ts:271`.
- **Cause:** `buildSocialMetaTags()` (`config.ts:250`) emits only `og:*` + `twitter:*`. The computed `pageDescription` (lines 430, 549) is never bound to the standard description meta. VitePress falls back to the site default.
- **Impact:** ~600 URLs share an identical traditional description. Classic snippet + AI-Overview citation label both prefer `<meta name="description">` when present and unique. Duplicate descriptions = weaker snippet relevance + possible "Discovered – currently not indexed" pressure.
- **Fix:**
  1. Add a `description: pageDescription` line in `transformPageData` so VitePress's head pipeline renders it:
     ```ts
     pageData.description = pageDescription;
     ```
     (set inside both branches at `config.ts:430` compare and `config.ts:549` sutta).
  2. OR push it explicitly in `buildSocialMetaTags`:
     ```ts
     ['meta', { name: 'description', content: description }],
     ```
     Then verify only one `<meta name="description">` appears (drop site-wide default if duplicated).
- **Validate:** `pnpm build && grep -oE '<meta name="description"[^>]*>' docs/.vitepress/dist/kinhtruongbo/thichminhchau/dn-007-kinh-jaliya.html` → unique per URL.

### P2 — Sitemap still ships `<changefreq>` + `<priority>`

- **Evidence:** `docs/public/sitemap.xml` lines 5–7 per URL. File = 3687 lines, ~30% wasted.
- **Cause:** Sitemap generated outside VitePress, by `.scripts/5sitemap-search-file.ipynb`.
- **Impact:** Google ignores both. Pure noise. No SEO penalty, but signals SEO-by-checklist.
- **Fix:** In the sitemap notebook, strip the two fields. Keep `<loc>` + `<lastmod>` only.
- **Validate:** `curl https://kinhnikaya.org/sitemap.xml | head -10` after redeploy; resubmit in Search Console.

### P2 — Canonical / sitemap URL mismatch (extension)

- **Evidence:** `<link rel="canonical" href="...dnc-007-kinh-jaliya.html">` but `sitemap.xml` `<loc>` = `...dnc-007-kinh-jaliya` (extensionless).
- **Cause:** `cleanUrls: true` in `config.ts:272`. Canonical computed from `relativePath.replace(/\.md$/, '.html')` at `config.ts:423`. Sitemap script emits extensionless.
- **Impact:** Two equivalent URLs in Google's eyes. Pick one canonical form, keep it consistent everywhere. Mismatch causes re-canonicalization noise and split signals.
- **Fix:** Drop the `.html` from canonical generation:
  ```ts
  const pageUrl = `${SITE_ORIGIN}/${relativePath.replace(/\.md$/, '')}`;
  ```
  (matches `cleanUrls: true` + sitemap + user-visible URL bar.)
- **Validate:** Canonical, `og:url`, sitemap `<loc>`, breadcrumb `item` URLs all match exactly.

### P2 — `llms.txt` decision still pending

- **Evidence:** `docs/public/llms.txt` shipped; `robots.txt` comments it.
- **Recommendation:** If no specific non-Google LLM tool consumes it → delete the file and remove the comment from `robots.txt`. Do NOT present it as a Google ranking lever. If kept for a known tool, document the consumer in `robots.txt` so future-you knows why.

### P3 — `translator` entity on compare page is mis-modelled

- **Evidence:** Compare-page JSON-LD: `"translator":[{"@type":"Person","name":"Pali Canon (song ngữ Pali - Việt)"}, ...]`.
- **Problem:** "Pali Canon" is the source corpus, not a person. Schema.org `translator` expects Person/Organization that performed the translation.
- **Fix:** Either drop that entry (translator field still has TMC), or model the Pali side as the source/Organization that produced the gloss (e.g. SuttaCentral if applicable). When unknown, omit — half-honest > wrong entity.
- **Where:** `compareMeta.translatorKeys` map in `config.ts`; reshape the entity for the Pali key.

### P3 — `<changefreq>` `<priority>` already in P2 above

(Documented to avoid double-listing.)

### P3 — Optional: `Book` + `hasPart` on nikaya index pages

- **Why:** Strengthens corpus understanding for AI Overviews. Low effort because `BOOK_NAV` already enumerates suttas.
- **Where:** `docs/kinhtrungbo/index.md`, `docs/kinhtuongung/index.md`, `docs/kinhtangchi/index.md`. `docs/kinhtruongbo/index.md` already has a Book schema — replicate.

### P3 — Optional: `WebPage.speakable` is unset

- **Why:** Speakable hint helps Google Assistant TTS pick the right excerpts; relevant for scripture. Low value but cheap.
- **Where:** Add `"speakable":{"@type":"SpeakableSpecification","cssSelector":["h1","main"]}` inside the existing `ScholarlyArticle` (or as a sibling `WebPage`).

---

## 3. Implementation order

1. **PR A — Meta description fix** (`buildSocialMetaTags` + or `pageData.description`). High leverage, two-line change.
2. **PR B — Canonical = extensionless** (`config.ts:423`). One-line, aligns with sitemap.
3. **PR C — Sitemap script cleanup** (drop `changefreq`/`priority`).
4. **PR D — `llms.txt` decision** (keep documented, or delete).
5. **PR E — Compare-page translator entity** (cleanup).
6. **PR F — Optional: `Book` + `hasPart`, `speakable`.**

Each PR independently mergeable, each verifiable via `curl + grep` or Search Console URL Inspection.

---

## 4. Validation checklist (post-fix)

- [ ] `curl https://kinhnikaya.org/<sample-sutta> | grep 'name="description"'` → unique text per URL.
- [ ] `curl <url>` canonical matches `<loc>` in sitemap (both extensionless or both `.html`).
- [ ] `curl /sitemap.xml | head -20` → only `<loc>` + `<lastmod>`.
- [ ] Rich Results Test on one compare URL + one plain sutta → no schema errors.
- [ ] Search Console → URL Inspection → "View crawled page" → both compare-page translations visible in rendered HTML (already passing).
- [ ] Search Console Page Indexing → 30-day check for drop in "Duplicate without user-selected canonical".

---

## 5. What NOT to do (re-emphasized)

- No `llms.txt`-as-ranking-signal claims.
- No content chunking / fan-out pages.
- No AI-tone rewriting of suttas.
- No mass-mention / link-building for AI Overview citations.
- No new schema types beyond what represents real facts on the page.
