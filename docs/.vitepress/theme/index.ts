import Theme from 'vitepress/theme'
import { h, onMounted, watch, nextTick } from 'vue'
import { useRoute } from 'vitepress'

// import TranslationCompare from '../components/TranslationCompare.vue'
// import ChapterCompare from '../components/ChapterCompare.vue'
import TextCompare from '../components/TextCompare.vue'
import CompareButton from '../components/CompareButton.vue'
import NotePopup from '../components/NotePopup.vue'
import NavFontSizeButton from './NavFontSizeButton.vue'
import HomePageLayout from './components/HomePageLayout.vue'
import Home2Page from './components/Home2Page.vue'
import IndexButton from '../components/IndexButton.vue'
import DocTags from './components/DocTags.vue'
import BookLayout from './components/BookLayout.vue'
import SuttaFooter from './components/SuttaFooter.vue'
import NavSearchButton from './NavSearchButton.vue'
import './style.css'

export default {
  extends: Theme,
  setup() {
    const route = useRoute()

    // Lưu path hiện tại để SearchPage biết đường quay lại.
    // Bỏ qua /search và mọi biến thể (search.html, /search?q=...).
    const isSearchPath = (p: string) =>
      p === '/search' || p === '/search.html' ||
      p.endsWith('/search') || p.endsWith('/search.html')

    const saveBackUrl = () => {
      if (typeof window === 'undefined') return
      const path = window.location.pathname
      if (isSearchPath(path)) return
      const full = path + window.location.search + window.location.hash
      localStorage.setItem('search-back-url', full)
    }
    const scrollToHash = async () => {
      if (typeof window === 'undefined') return

      const hash = window.location.hash
      if (!hash) return

      const id = decodeURIComponent(hash.slice(1))

      // Đợi Vue/VitePress render page mới
      await nextTick()

      setTimeout(() => {
        const el = document.getElementById(id)

        if (el) {
          el.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          })
        }
      }, 100)
    }

    onMounted(() => {
      // Cold load
      saveBackUrl()
      scrollToHash()
    })

    // SPA navigation: cập nhật mỗi lần đổi route (trừ vào /search)
    watch(
      () => [route.path, route.hash],
      async () => {
        saveBackUrl()
        await scrollToHash()
      }
    )
  },
  enhanceApp({ app }) {
    //app.component('TranslationCompare', TranslationCompare)
    //app.component('ChapterCompare', ChapterCompare)
    app.component('TextCompare', TextCompare)
    app.component('CompareButton', CompareButton)
    app.component('NotePopup', NotePopup)
    app.component('HomePageLayout', HomePageLayout)
    app.component('Home2Page', Home2Page)
    app.component('IndexButton', IndexButton)
    app.component('DocTags', DocTags)
    app.component('BookLayout', BookLayout)
  },
  Layout() {
    return h(Theme.Layout, null, {
      'doc-before': () => h(DocTags),
      'layout-bottom': () => [h(NotePopup)],
      'nav-bar-content-before': () => h(NavSearchButton),
      'nav-bar-content-after': () => h('div', { class: 'nav-controls' }, [
        h(CompareButton),
        h(IndexButton),
        h(NavFontSizeButton)
      ])
    })
  }
}
// 'layout-bottom': () => [h(SuttaFooter), h(NotePopup)],