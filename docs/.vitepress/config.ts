import { defineConfig } from 'vitepress'
import footnote from 'markdown-it-footnote';
// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Multilingual Documentation",
  description: "Documentation with multiple translations",
  markdown: {
    // Your existing markdown config...

    config: (md) => {
      // Add the footnote plugin
      md.use(footnote);

      // Any other markdown-it plugins you're using
    }
  },
  //nguen
  transformPageData(pageData) {
    // console.log("hehehe")
    // console.log(pageData.relativePath)
    // console.log(pageData.frontmatter)
    // For dynamic routes only
    if (pageData.relativePath.startsWith('kinhtrungbo222\/c-nm-tmc')) {
      console.log("hehehe2")
      // Get the slug from the URL
      const slug = pageData.params?.slug
      if (!slug) {
        return pageData
      }
      // console.log(pageData.params.data)


      const data = pageData.params?.data
      pageData.frontmatter.title = "nguyne"+data.title

      // Set next link if available
      // pageData.frontmatter.next = data.nextlink
      // pageData.frontmatter.prev = data.backlink
      // pageData.frontmatter.next = {
      //         text: "matchingPath.params.data.title",
      //         link: "/"
      //       }




      // Find the matching data from your paths.js
      // You'll need to import your paths data here or access it somehow
      // const pathsData = pageData.params?.data/* import or get your paths data */
      // const matchingPath = pathsData.find(path => path.params.slug === slug)

      // if (matchingPath) {
      //   // Update the frontmatter
      //   pageData.frontmatter.title = matchingPath.params.data.title

      //   // Set next link if available
      //   if (matchingPath.params.data.nextlink) {
      //     pageData.frontmatter.next = {
      //       text: matchingPath.params.data.title,
      //       link: matchingPath.params.data.nextlink
      //     }
      //   }
      // }
    }
    // console.log(pageData.frontmatter)
    return pageData
  },
  ///nguyen end
  // Enable Vue template features in markdown
  vue: {
    template: {
      compilerOptions: {
        isCustomElement: (tag) => tag.startsWith('translation-')
      }
    }
  },
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
      '/kinhtrungbo/': [
        {
          text: 'Kinh Trung Bộ',
          items: [
            {
              text: 'Nanamoli-Bodhi (English)',
              link: '/kinhtrungbo/nanamoli-bodhi/'
            },
            {
              text: 'Nanamoli-Bodhi (Vietnamese)',
              link: '/kinhtrungbo/nanamoli-bodhi-vi/'
            },
            {
              text: 'Thich Minh Chau',
              link: '/kinhtrungbo/thichminhchau/'
            }
          ]
        }
      ],
      '/kinhtruongbo/': [
        {
          text: 'Kinh Trường Bộ',
          items: [
            {
              text: 'Bodhi (English)',
              link: '/kinhtruongbo/bodhi/'
            },
            {
              text: 'Bodhi (Vietnamese)',
              link: '/kinhtruongbo/bodhi-vi/'
            },
            {
              text: 'Thich Minh Chau',
              link: '/kinhtruongbo/thichminhchau/'
            }
          ]
        }
      ],
      '/kinhtuongung/': [
        {
          text: 'Kinh Tương Ưng',
          items: [
            {
              text: 'Bodhi (English)',
              link: '/kinhtuongung/bodhi/'
            },
            {
              text: 'Bodhi (Vietnamese)',
              link: '/kinhtuongung/bodhi-vi/'
            },
            {
              text: 'Thich Minh Chau',
              link: '/kinhtuongung/thichminhchau/'
            }
          ]
        }
      ],
      '/compare/': [
        {
          text: 'Compare Translations',
          items: []
        }
      ],
      '/c/': [
        {
          text: 'Dynamic Comparisons',
          items: []
        }
      ],
      // '/kinhtrungbo/thichminhchau/': createChapterNavigation(152)
    },

    // Enable document footer with prev/next navigation
    docFooter: {
      prev: 'Previous Chapter',
      next: 'Next Chapter'
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/yourusername/multilingual-docs' }
    ]
  }
})

// Function to generate chapter navigation
function createChapterNavigation(totalChapters: number) {
  const items = [
    { text: 'Introduction', link: '/kinhtrungbo/thichminhchau/' }
  ]

  for (let i = 1; i <= totalChapters; i++) {
    items.push({
      text: `Chapter ${i}`,
      link: `/kinhtrungbo/thichminhchau/${i}`
    })
  }

  return [
    {
      text: 'Kinh Trung Bộ - Thích Minh Châu',
      items
    }
  ]
}
