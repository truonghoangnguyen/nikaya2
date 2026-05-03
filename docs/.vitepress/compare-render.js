// Shared helper for compare-page pre-rendering.
// At build time, renders left/right markdown to HTML, writes JSON to
// docs/public/compare-data/<dirKey>/<slug>.json, and returns small params
// containing only a dataUrl. Keeps HTML out of page JS bundles.
//
// In dev, returns pages untouched so TextCompare's dev-fetch path runs.

import fs from 'node:fs/promises';
import path from 'node:path';
import MarkdownIt from 'markdown-it';
import anchor from 'markdown-it-anchor';
import markdownItAttrs from 'markdown-it-attrs';
import { slugAnchor } from './utils.js';

const mdOptions = { html: true, linkify: true, typographer: true };
const anchorOptions = {
  permalink: anchor.permalink.ariaHidden({ symbol: '', placement: 'before' }),
  slugify: (s) => slugAnchor(s),
};

const mdLeft = new MarkdownIt(mdOptions).use(anchor, anchorOptions).use(markdownItAttrs);
const mdRight = new MarkdownIt(mdOptions).use(anchor, anchorOptions).use(markdownItAttrs);

async function readAndRender(relativePath, mdInstance) {
  try {
    const fullPath = path.resolve(
      process.cwd(),
      'docs',
      relativePath.startsWith('/') ? relativePath.slice(1) : relativePath
    );
    let content = await fs.readFile(fullPath, 'utf-8');
    content = content.replace(/^---[\s\S]*?---\n/, '');
    return mdInstance.render(content);
  } catch (e) {
    console.error(`compare-render: failed to render ${relativePath}`, e);
    return '<p>Lỗi khi tải nội dung.</p>';
  }
}

function safeName(value, fallback) {
  return String(value ?? fallback).replace(/[^\w.-]+/g, '_');
}

/**
 * @param {Array} pages - Array of { params: { slug, data: { left, right, ... } } }
 * @param {string} dirKey - Stable directory key, e.g. 'kinhtruongbo/c-pali-tmc-vi'
 */
export async function buildComparePages(pages, dirKey) {
  if (process.env.NODE_ENV !== 'production') return pages;

  const outDir = path.resolve(process.cwd(), 'docs/public/compare-data', dirKey);
  await fs.mkdir(outDir, { recursive: true });

  return Promise.all(
    pages.map(async (page) => {
      const { data = {}, slug } = page.params || {};
      if (!data.left || !data.right) return page;

      const [leftHtml, rightHtml] = await Promise.all([
        readAndRender(data.left, mdLeft),
        readAndRender(data.right, mdRight),
      ]);

      const fileName = `${safeName(slug, data.title)}.json`;
      await fs.writeFile(
        path.join(outDir, fileName),
        JSON.stringify({ leftHtml, rightHtml })
      );

      return {
        params: {
          ...page.params,
          data: {
            ...data,
            dataUrl: `/compare-data/${dirKey}/${fileName}`,
          },
        },
      };
    })
  );
}
