import { defineConfig } from 'vitepress'
import footnote from 'markdown-it-footnote';
// import markdownItKatex from 'markdown-it-katex';
import { slugAnchor } from './utils';

// run 1make_filelist.ipynb first
// step 1/4: get file list
import dn_thichminhchau         from '../kinhtruongbo/thichminhchau/meta/filelist';
import mn_thichminhchau         from '../kinhtrungbo/thichminhchau/filelist';
import nanamoli_bodhi_en        from '../kinhtrungbo/nanamoli-bodhi-en/filelist';
import nanamoli_bodhi_en_intro  from '../kinhtrungbo/nanamoli-bodhi-en/intro/filelist';
import nanamoli_bodhi_vi        from '../kinhtrungbo/nanamoli-bodhi-vi/filelist';
import nanamoli_bodhi_vi_intro  from '../kinhtrungbo/nanamoli-bodhi-vi/intro/filelist';

import kinhtangchi_thichminhchau from '../kinhtangchi/thichminhchau/meta/filelist';
import kinhtangchi_sujato_en from '../kinhtangchi/sujato-en/meta/filelist';
import kinhtangchi_sujato_vi from '../kinhtangchi/sujato-vi/meta/filelist';

import kinhtuongung_thichminhchau from '../kinhtuongung/thichminhchau/meta/filelist';
import kinhtuongung_sujato_vi from '../kinhtuongung/sujato-vi/meta/filelist';
import kinhtuongung_sujato_en from '../kinhtuongung/sujato-en/meta/filelist';

// import kinhtangchi_sujato_vi_intro from '../kinhtangchi/sujato-vi/intro/filelist';

//@ts-ignore
import fs from 'fs';
//@ts-ignore
import path from 'path';

const BOOK_NAV = {
  'kinhtrungbo/thichminhchau': mn_thichminhchau,
  'kinhtrungbo/nanamoli-bodhi-en': nanamoli_bodhi_en,
  'kinhtrungbo/nanamoli-bodhi-en/intro': nanamoli_bodhi_en_intro,
  'kinhtrungbo/nanamoli-bodhi-vi': nanamoli_bodhi_vi,
  'kinhtrungbo/nanamoli-bodhi-vi/intro': nanamoli_bodhi_vi_intro,

  'kinhtruongbo/thichminhchau': dn_thichminhchau,

  'kinhtangchi/thichminhchau': kinhtangchi_thichminhchau,
//  'kinhtangchi/bodhi-vi': kinhtangchi_bodhi_vi,
//  'kinhtangchi/bodhi-en': kinhtangchi_bodhi_en,
  'kinhtangchi/sujato-en': kinhtangchi_sujato_en,
  'kinhtangchi/sujato-en/intro': kinhtangchi_sujato_en,
  'kinhtangchi/sujato-vi': kinhtangchi_sujato_vi,
  'kinhtangchi/sujato-vi/intro': kinhtangchi_sujato_vi,


  'kinhtuongung/thichminhchau'    : kinhtuongung_thichminhchau,
  'kinhtuongung/sujato-en/intro'  : kinhtuongung_sujato_en,
  'kinhtuongung/sujato-en'        : kinhtuongung_sujato_en,
  'kinhtuongung/sujato-vi/intro'  : kinhtuongung_sujato_vi,
  'kinhtuongung/sujato-vi'        : kinhtuongung_sujato_vi,


};

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Kinh Nikaya",
  description: "Trò chuyện cùng Phật",

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
    plugins: [
      {
        /**
         * This function for compare markdown files, using when build
         */
        name: 'copy-markdown-files',
        // This hook runs at the end of the build process
        closeBundle() {
          //return;
          const sourceDirs = ['./docs/kinhtruongbo/', './docs/kinhtrungbo/', './docs/kinhtangchi/']; // Directories with your MD files
          //@ts-ignore
          const outputDir = path.resolve(__dirname, 'dist/');

          // Create the output directory if it doesn't exist
          if (!fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
          }

          // Function to recursively copy files
          function copyMarkdownFiles(sourceDir, targetDir) {
            const files = fs.readdirSync(sourceDir);

            files.forEach(file => {
              const sourcePath = path.join(sourceDir, file);
              const targetPath = path.join(targetDir, file);

              if (fs.statSync(sourcePath).isDirectory()) {
                // Create corresponding directory in target
                if (!fs.existsSync(targetPath)) {
                  fs.mkdirSync(targetPath, { recursive: true });
                }
                // Recurse into directory
                copyMarkdownFiles(sourcePath, targetPath);
              } else if (file.endsWith('.md')) {
                // Copy markdown file
                fs.copyFileSync(sourcePath, targetPath);
              }
            });
          }

          // Copy files from each source directory
          sourceDirs.forEach(dir => {
            const targetDir = path.join(outputDir, path.basename(dir));
            if (!fs.existsSync(targetDir)) {
              fs.mkdirSync(targetDir, { recursive: true });
            }
            copyMarkdownFiles(dir, targetDir);
          });

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
    // --- Configuration ---


    // --- Input Validation and Parsing ---

    if (!pageData || !pageData.relativePath) {
      console.warn('transformPageData: Invalid pageData or missing relativePath.');
      return pageData; // Return original data if essential info is missing
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
    ['base', { target: '_blank' }],
    ['link',{
        rel: 'preconnect',
        href: 'https://fonts.googleapis.com'
      }
    ],
    ['link',{
        rel: 'preconnect',
        href: 'https://fonts.gstatic.com',
        crossorigin: ''
      }
    ],
    ['link', {
        rel: 'preload',
        as: 'style',

        href: 'https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,100..900;1,100..900&display=swap',
        onload: "this.onload=null;this.rel='stylesheet'"
    }],

    ['noscript', {}, '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,100..900;1,100..900&display=swap">']
  ],

  // Theme configuration
  themeConfig: {
    search: {
      provider: 'local'
    },
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      {
        text: 'Kinh',
        items: [
          { text: 'Kinh Trường Bộ', link: '/kinhtruongbo/' },
          { text: 'Kinh Trung Bộ', link: '/kinhtrungbo/' },
          { text: 'Kinh Tương Ưng', link: '/kinhtuongung/' },
          { text: 'Kinh Tăng Chi Bộ', link: '/kinhtangchi/' }
        ]
      },

    ],

    sidebar: {
    },

    // Enable document footer with prev/next navigation
    // docFooter: {
    //   prev: 'Previous Page',
    //   next: 'Next Page'
    // },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/truonghoangnguyen/nikaya2' }
    ]
  }
})


// href: 'https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,100..900;1,100..900&display=swap',
 //['noscript', {}, '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,100..900;1,100..900&display=swap">']