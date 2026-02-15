import { h } from 'vue'
import Theme from 'vitepress/theme'
// import TranslationCompare from '../components/TranslationCompare.vue'
// import ChapterCompare from '../components/ChapterCompare.vue'
import TextCompare from '../components/TextCompare.vue'
import TextCompare2 from '../components/TextCompare2.vue'
import CompareButton from '../components/CompareButton.vue'
import NotePopup from '../components/NotePopup.vue'
import NavFontSizeButton from './NavFontSizeButton.vue'
import HomePageLayout from './components/HomePageLayout.vue'
import Home2Page from './components/Home2Page.vue'
import IndexButton from '../components/IndexButton.vue'
import DocTags from './components/DocTags.vue'
import './style.css'

export default {
  extends: Theme,
  enhanceApp({ app }) {
    //app.component('TranslationCompare', TranslationCompare)
    //app.component('ChapterCompare', ChapterCompare)
    app.component('TextCompare', TextCompare)
    app.component('TextCompare2', TextCompare2)
    app.component('CompareButton', CompareButton)
    app.component('NotePopup', NotePopup)
    app.component('HomePageLayout', HomePageLayout)
    app.component('Home2Page', Home2Page)
    app.component('IndexButton', IndexButton)
    app.component('DocTags', IndexButton)
  },
  Layout() {
    return h(Theme.Layout, null, {
      'doc-before': () => h(DocTags),
      'layout-bottom': () => h(NotePopup),
      'nav-bar-content-after': () => h('div', { class: 'nav-controls' }, [
        h(CompareButton),
        h(IndexButton),
        h(NavFontSizeButton)
      ])
    })
  }
}
