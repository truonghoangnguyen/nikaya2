import { defineConfig } from 'vitepress'
// import footnote from 'markdown-it-footnote';
// import markdownItKatex from 'markdown-it-katex';
import { slugAnchor } from './utils';

// run 1make_filelist.ipynb first
// step 1/4: get file list
import dn_thichminhchau from '../kinhtruongbo/thichminhchau/meta/filelist';
import kinhtruongbo_sujato_en from '../kinhtruongbo/sujato-en/meta/filelist';
import kinhtruongbo_sujato_vi from '../kinhtruongbo/sujato-vi/meta/filelist';
// import kinhtruongbo_pali from '../kinhtruongbo/pali/meta/filelist';
import kinhtruongbo_pali_vi from '../kinhtruongbo/pali-vi/meta/filelist';

import mn_thichminhchau from '../kinhtrungbo/thichminhchau/meta/filelist';
import nanamoli_bodhi_en from '../kinhtrungbo/nanamoli-bodhi-en/meta/filelist';
//import nanamoli_bodhi_en_intro  from '../kinhtrungbo/nanamoli-bodhi-en/intro/filelist';
import nanamoli_bodhi_vi from '../kinhtrungbo/nanamoli-bodhi-vi/meta/filelist';
//import nanamoli_bodhi_vi_intro  from '../kinhtrungbo/nanamoli-bodhi-vi/intro/filelist';


import kinhtangchi_thichminhchau from '../kinhtangchi/thichminhchau/meta/filelist';
import kinhtangchi_sujato_en from '../kinhtangchi/sujato-en/meta/filelist';
import kinhtangchi_sujato_vi from '../kinhtangchi/sujato-vi/meta/filelist';

import kinhtuongung_thichminhchau from '../kinhtuongung/thichminhchau/meta/filelist';
import kinhtuongung_sujato_vi from '../kinhtuongung/sujato-vi/meta/filelist';
import kinhtuongung_sujato_en from '../kinhtuongung/sujato-en/meta/filelist';

import jill_whole_brain_vi from '../jill-brain/vi/meta/filelist';
import jill_stroke_vi from '../jill-stroke/vi/meta/filelist';

// import kinhtangchi_sujato_vi_intro from '../kinhtangchi/sujato-vi/intro/filelist';

//@ts-ignore
import fs from 'fs';
//@ts-ignore
import path from 'path';

const BOOK_NAV = {
  'kinhtrungbo/thichminhchau': mn_thichminhchau,
  'kinhtrungbo/nanamoli-bodhi-en': nanamoli_bodhi_en,
  'kinhtrungbo/nanamoli-bodhi-en/intro': nanamoli_bodhi_en,
  'kinhtrungbo/nanamoli-bodhi-vi': nanamoli_bodhi_vi,
  'kinhtrungbo/nanamoli-bodhi-vi/intro': nanamoli_bodhi_vi,

  'kinhtruongbo/thichminhchau': dn_thichminhchau,
  'kinhtruongbo/sujato-en': kinhtruongbo_sujato_en,
  'kinhtruongbo/sujato-vi': kinhtruongbo_sujato_vi,
  'kinhtruongbo/pali-vi': kinhtruongbo_pali_vi,

  'kinhtangchi/thichminhchau': kinhtangchi_thichminhchau,
  //  'kinhtangchi/bodhi-vi': kinhtangchi_bodhi_vi,
  //  'kinhtangchi/bodhi-en': kinhtangchi_bodhi_en,
  'kinhtangchi/sujato-en': kinhtangchi_sujato_en,
  'kinhtangchi/sujato-en/intro': kinhtangchi_sujato_en,
  'kinhtangchi/sujato-vi': kinhtangchi_sujato_vi,
  'kinhtangchi/sujato-vi/intro': kinhtangchi_sujato_vi,


  'kinhtuongung/thichminhchau': kinhtuongung_thichminhchau,
  'kinhtuongung/sujato-en/intro': kinhtuongung_sujato_en,
  'kinhtuongung/sujato-en': kinhtuongung_sujato_en,
  'kinhtuongung/sujato-vi/intro': kinhtuongung_sujato_vi,
  'kinhtuongung/sujato-vi': kinhtuongung_sujato_vi,

  'jill-brain/vi': jill_whole_brain_vi,
  'jill-stroke/vi': jill_stroke_vi,

};

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Kinh Nikaya",
  description: "Khám phá bộ sưu tập Kinh điển Nikaya với bản dịch song ngữ Pali - Việt. Thư viện tra cứu kinh điển Phật giáo Nguyên thủy đầy đủ và chính xác.",
  sitemap: {
    hostname: 'https://kinhnikaya.org'
  },

  markdown: {
    anchor: {
      slugify: (s) => slugAnchor(s),
    },
    // Your existing markdown config...

    config: (md) => {
      // Add the footnote plugin
      //md.use(footnote);
      // md.use(markdownItKatex);
      // Any other markdown-it plugins you're using
    }
  },

  vite: {
    define: {
      // __BOOK_NAV__: BOOK_NAV,
    },
    plugins: [
      {
        /**
         * This function for compare markdown files, using when build
         */
        name: 'copy-markdown-files',
        // This hook runs at the end of the build process
        async closeBundle() {
          const sourceDirs = ['./docs/kinhtruongbo/', './docs/kinhtrungbo/', './docs/kinhtangchi/']; // Directories with your MD files

          // Fix for ESM __dirname
          const fs = await import('node:fs/promises');
          const { fileURLToPath } = await import('url');
          const __dirname = path.dirname(fileURLToPath(import.meta.url));
          const outputDir = path.resolve(__dirname, 'dist/');

          console.log('Starting async file copy...');
          console.time('copyMarkdownFiles');

          // Create the output directory if it doesn't exist
          try {
            await fs.mkdir(outputDir, { recursive: true });
          } catch (e) {
            // ignore if exists
          }

          // Function to recursively scan for files
          async function scanFiles(sourceDir: string, targetDir: string, fileList: { src: string, dest: string }[] = []) {
            try {
              const entries = await fs.readdir(sourceDir, { withFileTypes: true });

              for (const entry of entries) {
                const sourcePath = path.join(sourceDir, entry.name);
                const targetPath = path.join(targetDir, entry.name);

                if (entry.isDirectory()) {
                  // Ensure target directory exists
                  await fs.mkdir(targetPath, { recursive: true });
                  // Recurse
                  await scanFiles(sourcePath, targetPath, fileList);
                } else if (entry.isFile() && entry.name.endsWith('.md')) {
                  fileList.push({ src: sourcePath, dest: targetPath });
                }
              }
            } catch (err) {
              console.error(`Error scanning ${sourceDir}:`, err);
            }
            return fileList;
          }

          // 1. Scan and collect files
          const allFiles: { src: string, dest: string }[] = [];
          for (const dir of sourceDirs) {
            const dirName = path.basename(dir);
            const targetDir = path.join(outputDir, dirName);
            await fs.mkdir(targetDir, { recursive: true });
            await scanFiles(dir, targetDir, allFiles);
          }

          console.log(`Found ${allFiles.length} markdown files to copy.`);

          // 2. Batched Copying to prevent EMFILE/segfaults
          const BATCH_SIZE = 50;
          for (let i = 0; i < allFiles.length; i += BATCH_SIZE) {
            const batch = allFiles.slice(i, i + BATCH_SIZE);
            await Promise.all(batch.map(f => fs.copyFile(f.src, f.dest)));
          }

          console.timeEnd('copyMarkdownFiles');
          console.log('Markdown files copied to dist/raw/');
        }
      },
    ]
  },

  // ignoreDeadLinks: true,
  /**
   * Transforms page data, specifically adding navigation (next/prev) and title
   * information based on the page's relative path within supported books and authors.
   *
   * @param {object} pageData - The page data object, expected to have `relativePath` and `frontmatter` properties.
   * @returns {object | undefined} The modified pageData object, or undefined if the book is not supported.
   */
  transformPageData(pageData) {
    // --- Dynamic title ---
    if (pageData.params?.data?.title) {
      pageData.title = pageData.params.data.title
    }

    // --- Input Validation and Parsing ---

    if (!pageData || !pageData.relativePath) {
      console.warn('transformPageData: Invalid pageData or missing relativePath.');
      return pageData; // Return original data if essential info is missing
    }

    // --- Global Canonical URL ---
    let cleanPath = pageData.relativePath.replace(/\.md$/, '.html');
    // For index.md files, the canonical URL should point to the directory root
    if (cleanPath.endsWith('index.html')) {
      cleanPath = cleanPath.replace(/index\.html$/, '');
    }
    const canonicalUrl = `https://kinhnikaya.org/${cleanPath}`;

    pageData.frontmatter = pageData.frontmatter || {};
    pageData.frontmatter.head = pageData.frontmatter.head || [];

    const hasCanonical = pageData.frontmatter.head.some(
      (tag: any) => tag[0] === 'link' && tag[1] && tag[1].rel === 'canonical'
    );

    if (!hasCanonical) {
      pageData.frontmatter.head.push([
        'link',
        { rel: 'canonical', href: canonicalUrl }
      ]);
    }

    function getPath(url) {
      const parts = url.split('/');
      parts.pop(); // remove the last part (the filename)
      return parts.join('/');
    }

    const { relativePath } = pageData;
    const pathParts = relativePath.split('/');
    //const currentBook = pathParts[0];
    const path = getPath(relativePath);

    const currentBook = BOOK_NAV[path];

    // Find the matching author identifier within the path
    if (!currentBook) {
      console.log(relativePath, 'notfound');
      return pageData;
    }
    //console.log('currentAuthor', currentAuthor);

    // --- Navigation Logic ---
    // Proceed only if navigation data exists for this author/book combination
    if (currentBook && Array.isArray(currentBook)) {
      const fileName = pathParts[pathParts.length - 1]; // Get the filename (e.g., '001-something.md')

      // Find the index of the current page within the navigation array
      const currentIndex = currentBook.findIndex(item => item.link.includes(fileName));

      if (currentIndex !== -1) {
        // Ensure frontmatter object exists
        pageData.frontmatter = pageData.frontmatter || {};

        // Set the page title from the navigation data
        pageData.frontmatter.title = currentBook[currentIndex].text;

        // Determine the next page
        const nextIndex = currentIndex + 1;
        if (nextIndex < currentBook.length) {
          pageData.frontmatter.next = {
            text: currentBook[nextIndex].text,
            link: currentBook[nextIndex].link,
          };
        } else {
          pageData.frontmatter.next = undefined; // No next page
        }

        // Determine the previous page
        const prevIndex = currentIndex - 1;
        if (prevIndex >= 0) {
          pageData.frontmatter.prev = {
            text: currentBook[prevIndex].text,
            link: currentBook[prevIndex].link,
          };
        } else {
          pageData.frontmatter.prev = undefined; // No previous page
        }

        // --- ScholarlyArticle Schema Injection ---
        const bookSegment = pathParts[0]; // e.g. 'kinhtruongbo'
        const authorSegment = pathParts[1]; // e.g. 'thichminhchau'

        const BOOK_META: Record<string, { name: string; alternateName: string; url: string }> = {
          'kinhtruongbo': { name: 'Kinh Trường Bộ', alternateName: 'Dīgha Nikāya', url: 'https://kinhnikaya.org/kinhtruongbo/' },
          'kinhtrungbo': { name: 'Kinh Trung Bộ', alternateName: 'Majjhima Nikāya', url: 'https://kinhnikaya.org/kinhtrungbo/' },
          'kinhtangchi': { name: 'Kinh Tăng Chi Bộ', alternateName: 'Aṅguttara Nikāya', url: 'https://kinhnikaya.org/kinhtangchi/' },
          'kinhtuongung': { name: 'Kinh Tương Ưng Bộ', alternateName: 'Saṃyutta Nikāya', url: 'https://kinhnikaya.org/kinhtuongung/' },
        };

        const TRANSLATOR_META: Record<string, { name: string; inLanguage: string[]; url?: string; sameAs?: string[] }> = {
          'thichminhchau': {
            name: 'Thích Minh Châu',
            inLanguage: ['vi'],
            sameAs: [
              'https://vi.wikipedia.org/wiki/Th%C3%ADch_Minh_Ch%C3%A2u',
              'https://en.wikipedia.org/wiki/Thich_Minh_Chau',
            ],
          },
          'sujato-vi': {
            name: 'Bhikkhu Sujato',
            inLanguage: ['vi'],
            url: 'https://suttacentral.net/sujato',
            sameAs: [
              'https://en.wikipedia.org/wiki/Bhikkhu_Sujato',
              'https://suttacentral.net/sujato',
            ],
          },
          'sujato-en': {
            name: 'Bhikkhu Sujato',
            inLanguage: ['en'],
            url: 'https://suttacentral.net/sujato',
            sameAs: [
              'https://en.wikipedia.org/wiki/Bhikkhu_Sujato',
              'https://suttacentral.net/sujato',
            ],
          },
          'nanamoli-bodhi-en': {
            name: 'Bhikkhu Ñāṇamoli & Bhikkhu Bodhi',
            inLanguage: ['en'],
            sameAs: [
              'https://en.wikipedia.org/wiki/Bhikkhu_Bodhi',
              'https://en.wikipedia.org/wiki/Bhikkhu_Nanamoli',
            ],
          },
          'nanamoli-bodhi-vi': {
            name: 'Bhikkhu Ñāṇamoli & Bhikkhu Bodhi',
            inLanguage: ['vi'],
            sameAs: [
              'https://en.wikipedia.org/wiki/Bhikkhu_Bodhi',
              'https://en.wikipedia.org/wiki/Bhikkhu_Nanamoli',
            ],
          },
          'pali-vi': { name: 'Pali Canon (song ngữ Pali - Việt)', inLanguage: ['pi', 'vi'] },
          'pali': { name: 'Pali Canon', inLanguage: ['pi'] },
        };

        const bookMeta = BOOK_META[bookSegment];
        const translatorMeta = TRANSLATOR_META[authorSegment];

        if (bookMeta) {
          const pageUrl = `https://kinhnikaya.org/${relativePath.replace(/\.md$/, '.html')}`;
          const schema: Record<string, unknown> = {
            '@context': 'https://schema.org',
            '@type': 'ScholarlyArticle',
            'name': currentBook[currentIndex].text,
            'headline': currentBook[currentIndex].text,
            'url': pageUrl,
            'isPartOf': {
              '@type': 'Book',
              'name': bookMeta.name,
              'alternateName': bookMeta.alternateName,
              'url': bookMeta.url,
            },
            'publisher': {
              '@type': 'Organization',
              'name': 'Kinh Nikaya',
              'url': 'https://kinhnikaya.org',
            },
          };

          if (translatorMeta) {
            const translatorEntity: Record<string, unknown> = {
              '@type': 'Person',
              'name': translatorMeta.name,
            };
            if (translatorMeta.url) translatorEntity['url'] = translatorMeta.url;
            if (translatorMeta.sameAs) translatorEntity['sameAs'] = translatorMeta.sameAs;
            schema['translator'] = translatorEntity;
            schema['inLanguage'] = translatorMeta.inLanguage;
          }

          pageData.frontmatter.head = pageData.frontmatter.head || [];
          pageData.frontmatter.head.push([
            'script',
            { type: 'application/ld+json' },
            JSON.stringify(schema),
          ]);
        }
      } else {
        //console.warn(`transformPageData: Could not find file "${fileName}" in navigation data for author "${currentAuthor}" in book "${currentBook}".`);
      }
    } else {
      console.warn(`transformPageData: Missing navigation data for "${relativePath}" .`);
    }

    // Return the potentially modified pageData
    return pageData;
  },



  head: [
    //['base', { target: '_blank' }],
    ['link', {
      rel: 'preconnect',
      href: 'https://fonts.googleapis.com'
    }
    ],
    ['link', {
      rel: 'preconnect',
      href: 'https://fonts.gstatic.com',
      crossorigin: ''
    }
    ],
    ['link', {
      rel: 'preload',
      as: 'style',

      href: 'https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400..800;1,400..800&family=Libre+Baskerville:ital,wght@0,400..700;1,400..700&family=Noto+Serif:ital,wght@0,100..900;1,100..900&display=swap',
      onload: "this.onload=null;this.rel='stylesheet'"
    }],

    ['script', { type: 'application/ld+json' }, JSON.stringify({
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "WebSite",
          "@id": "https://kinhnikaya.org/#website",
          "name": "Kinh Nikaya",
          "url": "https://kinhnikaya.org",
          "description": "Thư viện Kinh điển Phật giáo Nguyên thủy với bản dịch song ngữ Pali - Việt. Bao gồm Kinh Trường Bộ, Kinh Trung Bộ, Kinh Tăng Chi Bộ và Kinh Tương Ứng.",
          "inLanguage": ["vi", "en", "pi"],
          "potentialAction": {
            "@type": "SearchAction",
            "target": {
              "@type": "EntryPoint",
              "urlTemplate": "https://kinhnikaya.org/search?q={search_term_string}"
            },
            "query-input": "required name=search_term_string"
          }
        },
        {
          "@type": "Organization",
          "@id": "https://kinhnikaya.org/#organization",
          "name": "Kinh Nikaya",
          "url": "https://kinhnikaya.org",
          "sameAs": ["https://github.com/truonghoangnguyen/nikaya2"],
          "knowsAbout": [
            "Phật giáo Nguyên thủy",
            "Kinh điển Nikaya",
            "Tiếng Pali",
            "Theravada Buddhism",
            "Pali Canon",
            "Dīgha Nikāya",
            "Majjhima Nikāya",
            "Saṃyutta Nikāya",
            "Aṅguttara Nikāya"
          ],
          "contributor": [
            {
              "@type": "Person",
              "name": "Thích Minh Châu",
              "sameAs": [
                "https://vi.wikipedia.org/wiki/Th%C3%ADch_Minh_Ch%C3%A2u",
                "https://en.wikipedia.org/wiki/Thich_Minh_Chau"
              ]
            },
            {
              "@type": "Person",
              "name": "Bhikkhu Sujato",
              "url": "https://suttacentral.net/sujato",
              "sameAs": [
                "https://en.wikipedia.org/wiki/Bhikkhu_Sujato",
                "https://suttacentral.net/sujato"
              ]
            },
            {
              "@type": "Person",
              "name": "Bhikkhu Bodhi",
              "sameAs": ["https://en.wikipedia.org/wiki/Bhikkhu_Bodhi"]
            },
            {
              "@type": "Person",
              "name": "Bhikkhu Ñāṇamoli",
              "sameAs": ["https://en.wikipedia.org/wiki/Bhikkhu_Nanamoli"]
            }
          ]
        }
      ]
    })],

    ['noscript', {}, '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,100..900;1,100..900&display=swap">']
  ],

  // Theme configuration
  themeConfig: {

    // search: {
    //   provider: 'local',
    //   options: {
    //     miniSearch: {
    //       searchOptions: {
    //         fields: ["title"],
    //         fuzzy: 0.2,
    //         prefix: true,
    //         boost: { title: 4, text: 0, titles: 0 }
    //       }
    //     }

    //     //   _render(src, env, md) {
    //     //     const html = md.render(src, env)
    //     //     if (env.frontmatter?.search === false) return ''

    //     //     // Remove H2-H6 headers to exclude them from the search index
    //     //     const content = src.replace(/^#{2,}\s.*/gm, '')
    //     //     return md.render(content, env)
    //     //   }

    //   },

    // },
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      {
        text: 'Kinh',
        items: [
          { text: 'Kinh Trường Bộ (DN)', link: '/kinhtruongbo/' },
          { text: 'Kinh Trung Bộ (MN)', link: '/kinhtrungbo/' },
          { text: 'Kinh Tương Ưng (SN)', link: '/kinhtuongung/' },
          { text: 'Kinh Tăng Chi Bộ (AN)', link: '/kinhtangchi/' }
        ]
      },
      { text: 'Hỏi & Đáp', link: '/hoi-dap' },
    ],

    sidebar: {
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/truonghoangnguyen/nikaya2' }
    ],

    footer: {
      message: '<a href="/hoi-dap.html">Về chúng tôi</a>',
    }
  }
})


// href: 'https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,100..900;1,100..900&display=swap',
//['noscript', {}, '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,100..900;1,100..900&display=swap">']
