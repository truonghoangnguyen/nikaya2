import { h } from 'vue'
import Theme from 'vitepress/theme'
// import TranslationCompare from '../components/TranslationCompare.vue'
// import ChapterCompare from '../components/ChapterCompare.vue'
import TextCompare from '../components/TextCompare.vue'
import CompareButton from '../components/CompareButton.vue'

import './style.css'

export default {
  extends: Theme,
  enhanceApp({ app }) {
    //app.component('TranslationCompare', TranslationCompare)
    //app.component('ChapterCompare', ChapterCompare)
    app.component('TextCompare', TextCompare)
    app.component('CompareButton', CompareButton)
  },
  Layout() {
    return h(Theme.Layout, null, {
      'nav-bar-content-after': () => h(CompareButton)
    })
  }
}
