import { defineConfig } from 'vitepress'
import footnote from 'markdown-it-footnote';
// import markdownItKatex from 'markdown-it-katex';
import mn_thichminhchau from '../kinhtrungbo/thichminhchau/filelist';
import dn_thichminhchau from '../kinhtruongbo/thichminhchau/filelist';
import nanamoli_bodhi_en from '../kinhtrungbo/nanamoli-bodhi-en/filelist';

import nanamoli_bodhi_en_intro from '../kinhtrungbo/nanamoli-bodhi-en/intro/filelist';
import nanamoli_bodhi_vi from '../kinhtrungbo/nanamoli-bodhi-vi/filelist';
import nanamoli_bodhi_vi_intro from '../kinhtrungbo/nanamoli-bodhi-vi/intro/filelist';

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

    // List of supported book identifiers (derived from the first part of the path)
    const SUPPORTED_BOOKS = ['kinhtruongbo', 'kinhtrungbo'];

    // List of supported author/translator identifiers found in paths.
    // IMPORTANT: List paths from most specific to least specific to ensure correct matching.
    // e.g., 'nanamoli-bodhi-en/intro' must come before 'nanamoli-bodhi-en'.
    const SUPPORTED_AUTHORS = [
      'thichminhchau',
      'nanamoli-bodhi-vi/intro',
      'nanamoli-bodhi-vi',
      'nanamoli-bodhi-en/intro',
      'nanamoli-bodhi-en',
    ];

    // Mapping of book identifiers to their respective author navigation data.
    // Assumes `mn_thichminhchau`, `dn_thichminhchau`, etc., are imported arrays
    // of objects like { text: 'Chapter Title', link: '/path/to/chapter.md' }
    const BOOK_AUTHOR_NAV_DATA = {
      kinhtrungbo: {
        'thichminhchau': mn_thichminhchau,
        'nanamoli-bodhi-en': nanamoli_bodhi_en,
        'nanamoli-bodhi-en/intro': nanamoli_bodhi_en_intro,
        'nanamoli-bodhi-vi': nanamoli_bodhi_vi,
        'nanamoli-bodhi-vi/intro': nanamoli_bodhi_vi_intro,
      },
      kinhtruongbo: {
        'thichminhchau': dn_thichminhchau,
        // Add other authors for kinhtruongbo here if needed
      },
    };

    // --- Input Validation and Parsing ---

    if (!pageData || !pageData.relativePath) {
      console.warn('transformPageData: Invalid pageData or missing relativePath.');
      return pageData; // Return original data if essential info is missing
    }

    const { relativePath } = pageData;
    const pathParts = relativePath.split('/');
    const currentBook = pathParts[0];

    // Exit early if the book is not supported
    if (!SUPPORTED_BOOKS.includes(currentBook)) {
      return undefined; // Or return pageData if you prefer to keep unsupported pages
    }

    // Find the matching author identifier within the path
    const currentAuthor = SUPPORTED_AUTHORS.find(author => relativePath.includes(author));

    // Exit if no supported author is found in the path
    if (!currentAuthor) {
      return pageData;
    }

    // --- Navigation Logic ---

    // Get the navigation data for the current book and author
    const authorNavDataForBook = BOOK_AUTHOR_NAV_DATA[currentBook];
    const currentAuthorNav = authorNavDataForBook ? authorNavDataForBook[currentAuthor] : undefined;

    // Proceed only if navigation data exists for this author/book combination
    if (currentAuthorNav && Array.isArray(currentAuthorNav)) {
      const fileName = pathParts[pathParts.length - 1]; // Get the filename (e.g., '001-something.md')

      // Find the index of the current page within the navigation array
      const currentIndex = currentAuthorNav.findIndex(item => item.link.includes(fileName));

      if (currentIndex !== -1) {
        // Ensure frontmatter object exists
        pageData.frontmatter = pageData.frontmatter || {};

        // Set the page title from the navigation data
        pageData.frontmatter.title = currentAuthorNav[currentIndex].text;

        // Determine the next page
        const nextIndex = currentIndex + 1;
        if (nextIndex < currentAuthorNav.length) {
          pageData.frontmatter.next = {
            text: currentAuthorNav[nextIndex].text,
            link: currentAuthorNav[nextIndex].link,
          };
        } else {
          pageData.frontmatter.next = undefined; // No next page
        }

        // Determine the previous page
        const prevIndex = currentIndex - 1;
        if (prevIndex >= 0) {
          pageData.frontmatter.prev = {
            text: currentAuthorNav[prevIndex].text,
            link: currentAuthorNav[prevIndex].link,
          };
        } else {
          pageData.frontmatter.prev = undefined; // No previous page
        }
      } else {
          //console.warn(`transformPageData: Could not find file "${fileName}" in navigation data for author "${currentAuthor}" in book "${currentBook}".`);
      }
    } else {
        console.warn(`transformPageData: Missing navigation data for author "${currentAuthor}" in book "${currentBook}".`);
    }

    // Return the potentially modified pageData
    return pageData;
  },
  /* Transform page data to add automatic next/previous links */
  // transformPageData(pageData) {
  //   const supportBooks= ['kinhtruongbo', 'kinhtrungbo'];
  //   // important note !, write longest path first eg: 'nanamoli-bodhi-en/intro' before 'nanamoli-bodhi-en'
  //   const supportAuthors = ['thichminhchau', 'nanamoli-bodhi-vi/intro', 'nanamoli-bodhi-vi', 'nanamoli-bodhi-en/intro', 'nanamoli-bodhi-en']; // Define the list of authors
  //   const relativePath = pageData.relativePath;
  //   const pathPart = relativePath.split('/');
  //   const currentBook = pathPart[0];

  //   const isSupported = supportBooks.includes(currentBook);
  //   if (!isSupported)
  //     return;

  //   // 1. Check if the path contains any of the authors
  //   const currentAuthor = supportAuthors.find((author) => {
  //     return relativePath.includes(author);
  //   });
  //   if (currentAuthor) {
  //     // 2. Extract file ID
  //     const fileName = relativePath.split('/').pop() || ''; // Get the filename
  //     const fileIdString = fileName.split('-')[0]; // Get '001'
  //     const fileId = parseInt(fileIdString, 10); // Convert to integer: 1

  //     // 3. Use imported author data
  //     const authorData_kinhtrungbo = {
  //       'thichminhchau': mn_thichminhchau,  // Use the imported data
  //       'nanamoli-bodhi-en': nanamoli_bodhi_en, // Use the imported data
  //       'nanamoli-bodhi-en/intro': nanamoli_bodhi_en_intro,
  //       'nanamoli-bodhi-vi': nanamoli_bodhi_vi,
  //       'nanamoli-bodhi-vi/intro': nanamoli_bodhi_vi_intro,
  //     };
  //     const authorData_kinhtruongbo = {
  //       'thichminhchau': dn_thichminhchau,  // Use the imported data
  //     };
  //     console.log(currentBook);
  //     let currentAuthorNav;
  //     // 4. next/back navigation
  //     if (currentBook=='kinhtrungbo'){
  //       currentAuthorNav = authorData_kinhtrungbo[currentAuthor];
  //     }
  //     else if (currentBook=='kinhtruongbo'){
  //       currentAuthorNav = authorData_kinhtruongbo[currentAuthor];
  //     }
  //     console.log(currentBook);
  //     // if (!pageData.frontmatter) {
  //     //   pageData.frontmatter = {};
  //     // }
  //     // pageData.frontmatter.layout = 'home'

  //     if (currentAuthorNav) {
  //       const currentIndex = currentAuthorNav.findIndex(item => item.link.includes(fileName));

  //       if (currentIndex !== -1) {
  //         const nextIndex = currentIndex + 1;
  //         const prevIndex = currentIndex - 1;

  //         pageData.frontmatter.title = currentAuthorNav[currentIndex].text;
  //         console.log(pageData.frontmatter.title)
  //         if (nextIndex < currentAuthorNav.length) {
  //           pageData.frontmatter.next = {
  //             text: currentAuthorNav[nextIndex].text,
  //             link: currentAuthorNav[nextIndex].link
  //           };
  //         } else {
  //           pageData.frontmatter.next = undefined;
  //         }

  //         if (prevIndex >= 0) {
  //           pageData.frontmatter.prev = {
  //             text: currentAuthorNav[prevIndex].text,
  //             link: currentAuthorNav[prevIndex].link
  //           };
  //         } else {
  //           pageData.frontmatter.prev = undefined;
  //         }
  //       }
  //     }
  //   }

  //   return pageData;

  // },
  // Enable Vue template features in markdown
  // vue: {
  //   template: {
  //     compilerOptions: {
  //       isCustomElement: (tag) => tag.startsWith('translation-')
  //     }
  //   }
  // },

  head: [
    ['base', { target: '_blank' }],
    [
      'link',
      {
        rel: 'preconnect',
        href: 'https://fonts.googleapis.com'
      }
    ],
    [
      'link',
      {
        rel: 'preconnect',
        href: 'https://fonts.gstatic.com',
        crossorigin: ''
      }
    ],
    [
      'link',
      {
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
          // { text: 'Kinh Tương Ưng', link: '/kinhtuongung/' }
        ]
      },
      // { text: 'Compare', link: '/compare/' },
      // { text: 'Dynamic Compare', link: '/c/' }
    ],

    sidebar: {
      // '/kinhtrungbo/': [
      //   {
      //     text: 'Kinh Trung Bộ',
      //     items: [
      //       {
      //         text: 'Nanamoli-Bodhi (English)',
      //         link: '/kinhtrungbo/nanamoli-bodhi/'
      //       },
      //       {
      //         text: 'Nanamoli-Bodhi (Vietnamese)',
      //         link: '/kinhtrungbo/nanamoli-bodhi-vi/'
      //       },
      //       {
      //         text: 'Thich Minh Chau',
      //         link: '/kinhtrungbo/thichminhchau/'
      //       }
      //     ]
      //   }
      // ],
      // '/kinhtruongbo/': [
      //   {
      //     text: 'Kinh Trường Bộ',
      //     items: [
      //       {
      //         text: 'Bodhi (English)',
      //         link: '/kinhtruongbo/bodhi/'
      //       },
      //       {
      //         text: 'Bodhi (Vietnamese)',
      //         link: '/kinhtruongbo/bodhi-vi/'
      //       },
      //       {
      //         text: 'Thich Minh Chau',
      //         link: '/kinhtruongbo/thichminhchau/'
      //       }
      //     ]
      //   }
      // ],
      // '/kinhtuongung/': [
      //   {
      //     text: 'Kinh Tương Ưng',
      //     items: [
      //       {
      //         text: 'Bodhi (English)',
      //         link: '/kinhtuongung/bodhi/'
      //       },
      //       {
      //         text: 'Bodhi (Vietnamese)',
      //         link: '/kinhtuongung/bodhi-vi/'
      //       },
      //       {
      //         text: 'Thich Minh Chau',
      //         link: '/kinhtuongung/thichminhchau/'
      //       }
      //     ]
      //   }
      // ],
      // '/compare/': [
      //   {
      //     text: 'Compare Translations',
      //     items: []
      //   }
      // ],
      // '/c/': [
      //   {
      //     text: 'Dynamic Comparisons',
      //     items: []
      //   }
      // ],
      // '/kinhtrungbo/thichminhchau/': createChapterNavigation(152)
    },

    // Enable document footer with prev/next navigation
    docFooter: {
      prev: 'Previous Page',
      next: 'Next Page'
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/truonghoangnguyen/nikaya2' }
    ]
  }
})

// Function to generate chapter navigation
// function createChapterNavigation(totalChapters: number) {
//   const items = [
//     { text: 'Introduction', link: '/kinhtrungbo/thichminhchau/' }
//   ]

//   for (let i = 1; i <= totalChapters; i++) {
//     items.push({
//       text: `Chapter ${i}`,
//       link: `/kinhtrungbo/thichminhchau/${i}`
//     })
//   }

//   return [
//     {
//       text: 'Kinh Trung Bộ - Thích Minh Châu',
//       items
//     }
//   ]
// }
