import { defineConfig } from 'vitepress'
import footnote from 'markdown-it-footnote';
// import markdownItKatex from 'markdown-it-katex';

// run 1make_filelist.ipynb first
// step 1/4: get file list
import dn_thichminhchau from '../kinhtruongbo/thichminhchau/filelist';

import mn_thichminhchau         from '../kinhtrungbo/thichminhchau/filelist';
import nanamoli_bodhi_en        from '../kinhtrungbo/nanamoli-bodhi-en/filelist';
import nanamoli_bodhi_en_intro  from '../kinhtrungbo/nanamoli-bodhi-en/intro/filelist';
import nanamoli_bodhi_vi        from '../kinhtrungbo/nanamoli-bodhi-vi/filelist';
import nanamoli_bodhi_vi_intro  from '../kinhtrungbo/nanamoli-bodhi-vi/intro/filelist';

import kinhtangchi_thichminhchau from '../kinhtangchi/thichminhchau/filelist';
import kinhtangchi_sujato_en from '../kinhtangchi/sujato-en/filelist';
import kinhtangchi_sujato_vi from '../kinhtangchi/sujato-vi/filelist';
import kinhtangchi_sujato_vi_intro from '../kinhtangchi/sujato-vi/intro/filelist';

//@ts-ignore
import fs from 'fs';
//@ts-ignore
import path from 'path';

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Kinh Nikaya",
  description: "Trò chuyện cùng Phật",

  markdown: {
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
          const sourceDirs = ['./docs/kinhtruongbo/', './docs/kinhtrungbo/']; // Directories with your MD files
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

    // url /<book>/<author>/<chapter(opt)>/file.md, eg: /kinhtruongbo/thichminhchau/001-mot-phap.md
    // step 2/4: add supported book identifiers (derived from the first part of the path)
    // const SUPPORTED_BOOKS = ['kinhtruongbo', 'kinhtrungbo', 'kinhtangchi'];

    // List of supported author/translator identifiers found in paths.
    // IMPORTANT: List paths from most specific to least specific to ensure correct matching.
    // e.g., 'nanamoli-bodhi-en/intro' must come before 'nanamoli-bodhi-en'.
    // step 3/4: add author/*chapter url
    // const SUPPORTED_AUTHORS = [
    //   'thichminhchau',
    //   'nanamoli-bodhi-vi/intro',
    //   'nanamoli-bodhi-vi',
    //   'nanamoli-bodhi-en/intro',
    //   'nanamoli-bodhi-en',
    //   'bhikkhu-sujato-en',
    //   'bhikkhu-sujato-vi',
    // ];

    // step 4/4: Mapping of book identifiers to their respective author navigation data.
    // Assumes `mn_thichminhchau`, `dn_thichminhchau`, etc., are imported arrays
    // of objects like { text: 'Chapter Title', link: '/path/to/chapter.md' }
    // const BOOK_AUTHOR_NAV_DATA = {
    //   kinhtrungbo: {
    //     'thichminhchau': mn_thichminhchau,
    //     'nanamoli-bodhi-en': nanamoli_bodhi_en,
    //     'nanamoli-bodhi-en/intro': nanamoli_bodhi_en_intro,
    //     'nanamoli-bodhi-vi': nanamoli_bodhi_vi,
    //     'nanamoli-bodhi-vi/intro': nanamoli_bodhi_vi_intro,
    //   },
    //   kinhtruongbo: {
    //     'thichminhchau': dn_thichminhchau,
    //     // Add other authors for kinhtruongbo here if needed
    //   },
    //   kinhtangchi: {
    //     'thichminhchau': kinhtangchi_thichminhchau,
    //   //  'bhikkhu-sujato-en': kinhtangchi_sujato_en,
    //   //  'bhikkhu-sujato-vi': kinhtangchi_sujato_vi,
    //   },
    // };

    const BOOK_AUTHOR_NAV_DATA2 = {
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
        'kinhtangchi/sujato-vi': kinhtangchi_sujato_vi,
        'kinhtangchi/sujato-vi/intro': kinhtangchi_sujato_vi_intro,

    };

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

    // console.log('ng-path', path, BOOK_AUTHOR_NAV_DATA2[path]);

    // Exit early if the book is not supported
    // if (!SUPPORTED_BOOKS.includes(currentBook)) {
    //   console.log(currentBook, 'notfound');
    //   return undefined; // Or return pageData if you prefer to keep unsupported pages
    // }

    const currentBook = BOOK_AUTHOR_NAV_DATA2[path];

    // Find the matching author identifier within the path
    //const currentAuthor = SUPPORTED_AUTHORS.find(author => relativePath.includes(author));

    // Exit if no supported author is found in the path
    if (!currentBook) {
      console.log(relativePath, 'notfound');
      return pageData;
    }
    //console.log('currentAuthor', currentAuthor);

    // --- Navigation Logic ---

    // Get the navigation data for the current book and author
    // const authorNavDataForBook = BOOK_AUTHOR_NAV_DATA[currentBook];
    //const currentBook = authorNavDataForBook ? authorNavDataForBook[currentAuthor] : undefined;

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
    ['link',{
        href: 'https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,100..900;1,100..900&display=swap',
        rel: 'stylesheet'
      }
    ]
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
          { text: 'Kinh Trung Bộ', link: '/kinhtrungbo/' },
          { text: 'Kinh Trường Bộ', link: '/kinhtruongbo/' },
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
