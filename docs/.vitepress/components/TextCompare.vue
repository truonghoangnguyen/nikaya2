<!-- TextCompare.vue -->
<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import MarkdownIt from 'markdown-it'
import anchor from 'markdown-it-anchor'
import markdownItAttrs from 'markdown-it-attrs'
import { slugAnchor } from '../utils';


interface Props {
  leftPath: string
  rightPath: string
  notePath?: string
  leftTitle?: string
  rightTitle?: string

  // Production: rendered HTML inlined via route params (from compare-render.js).
  // Empty in dev — dev path fetches raw markdown client-side.
  leftContentHtml?: string
  rightContentHtml?: string
  noteContentHtml?: string
}

const props = withDefaults(defineProps<Props>(), {
  leftTitle: 'Left',
  rightTitle: 'Right',
  notePath: '',
  leftContentHtml: '',
  rightContentHtml: '',
  noteContentHtml: '',
})

// --- State ---
const finalLeftHtml = ref(props.leftContentHtml || '')
const finalRightHtml = ref(props.rightContentHtml || '')
const finalNoteHtml = ref(props.noteContentHtml || '')

const isLoading = ref(
  !props.leftContentHtml && !props.rightContentHtml && import.meta.env.DEV
)
const error = ref<string | null>(null)


// Hàm này dùng để chia chuỗi HTML thành các đoạn theo comment <!--pg-->
const parseHtmlByParagraphs = (html: string): string[] => {
  const paragraphRegex = /<!--pg-->/g
  const parts = html.split(paragraphRegex)
  return parts.map(part => part.trim()).filter(part => part.length > 0)
}

// Computed property để tự động chia đoạn văn khi final HTML thay đổi
const parsedParagraphs = computed(() => ({
  left: parseHtmlByParagraphs(finalLeftHtml.value),
  right: parseHtmlByParagraphs(finalRightHtml.value)
}))

const leftOriginalPath = computed(() => props.leftPath.replace(/\.md$/, ''))
const rightOriginalPath = computed(() => props.rightPath.replace(/\.md$/, ''))
const hasNote = computed(() => finalNoteHtml.value.trim().length > 0)

onMounted(async () => {
  // Already have HTML inline (production SSG path)
  if (props.leftContentHtml && props.rightContentHtml) {
    isLoading.value = false
    return
  }

  // Dev: fetch raw markdown and render client-side
  if (import.meta.env.DEV) {
    try {
      const mdLeft = new MarkdownIt({ html: true, linkify: true, typographer: true })
        .use(anchor, {
          permalink: anchor.permalink.ariaHidden({ symbol: '', placement: 'before' }),
          slugify: (s) => slugAnchor(s),
        })
        .use(markdownItAttrs)

      const mdRight = new MarkdownIt({ html: true, linkify: true, typographer: true })
        .use(anchor, {
          permalink: anchor.permalink.ariaHidden({ symbol: '', placement: 'before' }),
          slugify: (s) => slugAnchor(s),
        })
        .use(markdownItAttrs)

      const [leftResponse, rightResponse] = await Promise.all([
        fetch(props.leftPath),
        fetch(props.rightPath),
      ])

      if (!leftResponse.ok) throw new Error(`Failed to load ${props.leftPath}`)
      if (!rightResponse.ok) throw new Error(`Failed to load ${props.rightPath}`)

      let leftContent = await leftResponse.text()
      let rightContent = await rightResponse.text()

      leftContent = leftContent.replace(/^---[\s\S]*?---\n/, '')
      rightContent = rightContent.replace(/^---[\s\S]*?---\n/, '')

      finalLeftHtml.value = mdLeft.render(leftContent)
      finalRightHtml.value = mdRight.render(rightContent)
    } catch (e) {
      error.value = e instanceof Error ? e.message : 'Unknown error loading files'
      console.error(error.value)
    } finally {
      isLoading.value = false
    }
  }
})
</script>

<template>
  <div class="text-compare">
    <div v-if="isLoading" class="loading">
      Loading content...
    </div>

    <div v-else-if="error" class="error">
      {{ error }}
    </div>

    <div v-else>
      <!-- Header with titles -->
      <div class="text-compare-header">
        <div class="text-column-header">
          <h3>
            {{ leftTitle }}
            <a :href="leftOriginalPath" target="_blank" class="source-link">[link]</a>
          </h3>
        </div>
        <div class="text-column-header">
          <h3>
            {{ rightTitle }}
            <a :href="rightOriginalPath" target="_blank" class="source-link">[link]</a>
          </h3>
        </div>
      </div>

      <!-- Paragraph comparison rows -->
      <div class="text-compare-rows">
        <div
          v-for="(_, index) in Math.max(parsedParagraphs.left.length, parsedParagraphs.right.length)"
          :key="index"
          class="text-compare-row"
        >
          <div class="text-column">
            <div
              v-if="index < parsedParagraphs.left.length"
              class="text-content"
              v-html="parsedParagraphs.left[index]"
            ></div>
          </div>
          <div class="text-column">
            <div
              v-if="index < parsedParagraphs.right.length"
              class="text-content"
              v-html="parsedParagraphs.right[index]"
            ></div>
          </div>
        </div>
      </div>

      <div v-if="hasNote" class="notes-container">
        <h2 class="notes-title">Notes</h2>
        <div class="notes-content" v-html="finalNoteHtml"></div>
      </div>
    </div>
  </div>
</template>


<style>
/* Non-scoped styles for proper markdown rendering */
.text-content ul {
  padding-left: 0em;
  margin: 0;
}

.text-content li {
  /* display: list-item;
  list-style-type: disc; */
  /* margin: 0.5em 0; */
}

.text-content li p {
  margin: 0;
}

/* Footnote styles */
.text-content .footnotes {
  margin-top: 2rem;
  padding-top: 1rem;
  border-top: 1px solid var(--vp-c-divider);
  font-size: 0.9em;
}

.text-content .footnote-ref {
  font-size: 0.8em;
  vertical-align: super;
  line-height: 0;
  margin: 0 0.2em;
}

.text-content .footnote-backref {
  text-decoration: none;
  margin-left: 0.3em;
}
</style>

<style scoped>
.text-compare {
  margin: 1px 0;
}

.text-compare-header {
  display: flex;
  gap: 1px;
  margin-bottom: 1rem;
}

.text-column-header {
  flex: 1;
  padding: 0 1rem;
}

.text-compare-rows {
  display: flex;
  flex-direction: column;
  gap: 1px;
}

.text-compare-row {
  display: flex;
  gap: 1px;
  border-top: 1px solid var(--vp-c-divider);
  padding: 1rem 0;
}

.text-column {
  flex: 1;
  min-width: 0;
  padding: 0 1rem;
}

.text-content {
  overflow-wrap: break-word;
  line-height: 1.6;
  white-space: normal;
}

.source-link {
  font-size: 0.8em;
  margin-left: 0.5rem;
  opacity: 0.7;
  font-weight: normal;
}

/* Notes styling */
.notes-container {
  margin-top: 3rem;
  padding-top: 2rem;
  border-top: 1px solid var(--vp-c-divider);
}

.notes-title {
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
  font-weight: 600;
}

.notes-content {
  background-color: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  padding: 1.5rem;
  line-height: 1.7;
  overflow-wrap: break-word;
}

/* Fix for paragraph line breaks in source markdown */
.text-content :deep(p) {
  margin: 1rem 0;
  line-height: 1.7;
  white-space: normal;
}

/* Loading and error states */
.loading, .error {
  padding: 2rem;
  text-align: center;
  background-color: var(--vp-c-bg-soft);
  border-radius: 8px;
  border: 1px solid var(--vp-c-divider);
}

.error {
  color: var(--vp-c-danger);
}
</style>
