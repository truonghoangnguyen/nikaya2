// Shared helper for compare-page pre-rendering.
// At build time, renders left/right markdown to HTML and inlines it into route
// params so VitePress SSG emits content directly into static HTML (for SEO).
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

/**
 * @param {Array} pages - Array of { params: { slug, data: { left, right, ... } } }
 * @param {string} dirKey - Stable directory key, e.g. 'kinhtruongbo/c-pali-tmc-vi'
 */
export async function buildComparePages(pages, dirKey) {
  if (process.env.NODE_ENV !== 'production') return pages;

  return Promise.all(
    pages.map(async (page) => {
      const { data = {} } = page.params || {};
      if (!data.left || !data.right) return page;

      const [leftHtml, rightHtml] = await Promise.all([
        readAndRender(data.left, mdLeft),
        readAndRender(data.right, mdRight),
      ]);

      return {
        params: {
          ...page.params,
          data: {
            ...data,
            leftHtml,
            rightHtml,
          },
        },
      };
    })
  );
}
