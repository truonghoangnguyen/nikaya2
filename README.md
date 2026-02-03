# Multilingual Docs (Kinh Nikaya)

**What It Is**
A VitePress-based documentation site for the Kinh Nikaya collection, focused on side-by-side multilingual comparison of Buddhist texts and related materials.
It is configured as a static site with content stored as Markdown under `docs/`.

**Who It’s For**
Readers, translators, and researchers who want to compare Buddhist texts across multiple Vietnamese and English translations.

**What It Does**
- Hosts multiple collections of Buddhist scriptures and related texts in `docs/`.
- Enables side-by-side comparison pages (e.g., `compare.html`).
- Builds dynamic navigation from per-collection `meta/filelist` sources.
- Generates consistent slugs/anchors for headings via a custom slug utility.
- Copies raw Markdown content into the build output during `vitepress build`.
- Provides a VitePress dev server for local browsing and iteration.

**How It Works**
- Content lives as Markdown files under `docs/` with collections such as `kinhtruongbo`, `kinhtrungbo`, `kinhtangchi`, and `kinhtuongung`.
- VitePress is configured in `docs/.vitepress/config.ts` with custom nav data (`BOOK_NAV`) built from `meta/filelist` modules.
- A VitePress build plugin scans the source collections and copies Markdown files into the `docs/.vitepress/dist/` output for raw access.
- Page data is transformed at build time to set titles and next/prev navigation based on the collection path.
- Not found in repo: external services, APIs, or backend components.

**How To Run**
- Prerequisites: Node.js (version not found in repo) and `pnpm`.
- Install dependencies: `pnpm install`.
- Start the dev server: `pnpm docs:dev`.
- Build for production: `pnpm docs:build` (optional).

