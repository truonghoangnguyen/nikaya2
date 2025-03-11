import { defineConfig } from 'vitepress'
import footnote from 'markdown-it-footnote';
import thichminhchau from '../kinhtrungbo/thichminhchau/filelist';
import nanamoli_bodhi from '../kinhtrungbo/nanamoli-bodhi/filelist';

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Kinh Nikaya",
  description: "Trò chuyện cùng Phật",
  markdown: {
    // Your existing markdown config...

    config: (md) => {
      // Add the footnote plugin
      md.use(footnote);

      // Any other markdown-it plugins you're using
    }
  },
  ignoreDeadLinks: true,
  // Transform page data to add automatic next/previous links
  transformPageData(pageData) {
    const relativePath = pageData.relativePath;
    const authors = ['thichminhchau', 'nanamoli-bodhi']; // Define the list of authors

    // 1. Check if the path contains any of the authors
    const currentAuthor = authors.find(author => relativePath.includes(author));

    if (currentAuthor) {
      console.log('currentAuthor', currentAuthor);
      // 2. Extract file ID
      const fileName = relativePath.split('/').pop() || ''; // Get the filename
      const fileIdString = fileName.split('-')[0]; // Get '001'
      const fileId = parseInt(fileIdString, 10); // Convert to integer: 1

      // 3. Use imported author data
      const authorData = {
        thichminhchau: thichminhchau,  // Use the imported data
        'nanamoli-bodhi': nanamoli_bodhi, // Use the imported data
      };

      // 4. Get the navigation data for the current author
      const currentAuthorNav = authorData[currentAuthor];

      if (currentAuthorNav) {
        const currentIndex = currentAuthorNav.findIndex(item => item.link.includes(fileName));

        if (currentIndex !== -1) {
          const nextIndex = currentIndex + 1;
          const prevIndex = currentIndex - 1;

          if (!pageData.frontmatter) {
            pageData.frontmatter = {};
          }

          if (nextIndex < currentAuthorNav.length) {
            pageData.frontmatter.next = {
              text: currentAuthorNav[nextIndex].text,
              link: currentAuthorNav[nextIndex].link
            };
          } else {
            pageData.frontmatter.next = undefined;
          }

          if (prevIndex >= 0) {
            pageData.frontmatter.prev = {
              text: currentAuthorNav[prevIndex].text,
              link: currentAuthorNav[prevIndex].link
            };
          } else {
            pageData.frontmatter.prev = undefined;
          }
        }
      }
    }

    return pageData;

  },
  // Enable Vue template features in markdown
  // vue: {
  //   template: {
  //     compilerOptions: {
  //       isCustomElement: (tag) => tag.startsWith('translation-')
  //     }
  //   }
  // },

  head: [
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
        text: 'Collections',
        items: [
          { text: 'Kinh Trung Bộ', link: '/kinhtrungbo/' },
          { text: 'Kinh Trường Bộ', link: '/kinhtruongbo/' },
          { text: 'Kinh Tương Ưng', link: '/kinhtuongung/' }
        ]
      },
      { text: 'Compare', link: '/compare/' },
      { text: 'Dynamic Compare', link: '/c/' }
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
