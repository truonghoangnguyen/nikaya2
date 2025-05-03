<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import MarkdownIt from 'markdown-it'


// Initialize markdown-it instance with enhanced configuration
const mdLeft = new MarkdownIt({
  html: true,
  linkify: true,
  typographer: true,
  //breaks: false, // Changed from true to false to not convert line breaks to <br>
  // Ensure lists are properly rendered
  //listIndent: 2
}).disable('list')


const mdRight = new MarkdownIt({
  html: true,
  linkify: true,
  typographer: true,
  //breaks: false, // Changed from true to false to not convert line breaks to <br>
  // Ensure lists are properly rendered
  //listIndent: 2
}).disable('list')

// mdRight.renderer.rules.ordered_list_open = (tokens, idx, options, env, self) => {
//   return tokens[idx].markup; // Keep the original Markdown text
// };
// mdLeft.renderer.rules.ordered_list_open = (tokens, idx, options, env, self) => {
//   return tokens[idx].markup; // Keep the original Markdown text
// };


interface Props {
  leftPath: string
  rightPath: string
  leftTitle?: string
  rightTitle?: string
}

const props = withDefaults(defineProps<Props>(), {
  leftTitle: 'Translation 1',
  rightTitle: 'Translation 2'
})

// Compute the original file paths for links (removing part indicators like .p1.md and the .md extension)
const leftOriginalPath = computed(() => {
  return props.leftPath.replace(/\.p\d+\.md$/, '').replace(/\.md$/, '')
})

const rightOriginalPath = computed(() => {
  return props.rightPath.replace(/\.p\d+\.md$/, '').replace(/\.md$/, '')
})

const leftContent = ref<string>('')
const rightContent = ref<string>('')
const leftHtml = ref<string>('')
const rightHtml = ref<string>('')
const isLoading = ref<boolean>(true)
const error = ref<string | null>(null)

onMounted(async () => {
  try {
    isLoading.value = true

    // Fetch both markdown files
    const [leftResponse, rightResponse] = await Promise.all([
      fetch(props.leftPath),
      fetch(props.rightPath)
    ])
    console.log(props)
    if (!leftResponse.ok) throw new Error(`Failed to load ${props.leftPath}`)
    if (!rightResponse.ok) throw new Error(`Failed to load ${props.rightPath}`)

    leftContent.value = await leftResponse.text()
    rightContent.value = await rightResponse.text()

    // Remove frontmatter if present
    leftContent.value = leftContent.value.replace(/^---[\s\S]*?---\n/, '')
    rightContent.value = rightContent.value.replace(/^---[\s\S]*?---\n/, '')

    // Convert markdown to HTML
    leftHtml.value = mdLeft.render(leftContent.value)
    rightHtml.value = mdRight.render(rightContent.value)

    // console.log(leftHtml.value, rightHtml.value)

  } catch (e) {
    error.value = e instanceof Error ? e.message : 'Unknown error loading translations'
    console.error(error.value)
  } finally {
    isLoading.value = false
  }
})
</script>

<template>
  <div class="translation-compare">
    <div v-if="isLoading" class="loading">
      Loading translations...
    </div>

    <div v-else-if="error" class="error">
      {{ error }}
    </div>

    <div v-else class="translation-container">
      <div class="translation-column">
        <h3>
          {{ leftTitle }}
          <a :href="leftOriginalPath" target="_blank" class="source-link">[link]</a>
        </h3>
        <div class="translation-content" v-html="leftHtml"></div>
      </div>

      <div class="translation-column">
        <h3>
          {{ rightTitle }}
          <a :href="rightOriginalPath" target="_blank" class="source-link">[link]</a>
        </h3>
        <div class="translation-content" v-html="rightHtml"></div>
      </div>
    </div>
  </div>
</template>

<style>
/* Non-scoped styles for proper markdown rendering */
.translation-content ul {
  padding-left: 2em;
  margin: 1em 0;
}

.translation-content li {
  display: list-item;
  list-style-type: disc;
  margin: 0.5em 0;
}

.translation-content li p {
  margin: 0;
}

/* Footnote styles */
.translation-content .footnotes {
  margin-top: 2rem;
  padding-top: 1rem;
  border-top: 1px solid var(--vp-c-divider);
  font-size: 0.9em;
}

.translation-content .footnote-ref {
  font-size: 0.8em;
  vertical-align: super;
  line-height: 0;
  margin: 0 0.2em;
}

.translation-content .footnote-backref {
  text-decoration: none;
  margin-left: 0.3em;
}
</style>

<style scoped>
.translation-compare {
  margin: 1px 0;
}

.translation-container {
  display: flex;
  gap: 1px;
}

.translation-column {
  flex: 1;
  min-width: 0;
  border: 1px solid var(--vp-c-divider);
  padding: 1rem;
  border-radius: 8px;
  background-color: var(--vp-c-bg-soft);
}

.source-link {
  font-size: 0.8em;
  margin-left: 0.5rem;
  opacity: 0.7;
  font-weight: normal;
}

/* Base styling for all text in translation content */
.translation-content {
  overflow-wrap: break-word;
  line-height: 1.6;
  white-space: normal;
}

/* Fix for paragraph line breaks in source markdown */
.translation-content :deep(p) {
  margin: 1rem 0;
  line-height: 1.7;
  white-space: normal;
}

/* Regular strong text */
.translation-content :deep(strong) {
  display: inline-block;
  margin: 0.5rem 0;
  font-weight: 600;
}

/* Section headers (like NGƯỜI PHÀM PHU) */
.translation-content :deep(p > strong:only-child) {
  display: block;
  margin: 2rem 0 1.5rem;
  font-size: 1.2em;
  /* color: var(--vp-c-brand);
  padding: 0.75rem;
  background-color: var(--vp-c-bg-alt);
  border-radius: 6px;
  border: 1px solid var(--vp-c-divider-light);
  text-align: center; */
  letter-spacing: 0.05em;
}

/* Improve paragraph spacing */
.translation-content :deep(p) {
  margin: 1rem 0;
  line-height: 1.7;
}

/* Add more space between paragraphs */
.translation-content :deep(p + p) {
  margin-top: 1.25rem;
}

/* Improve spacing for numbered paragraphs */
.translation-content :deep(p:first-line) {
  line-height: 2;
}

.translation-content :deep(h1) {
  margin-top: 2rem;
  margin-bottom: 1.5rem;
  font-size: 2em;
  font-weight: 700;
  line-height: 1.3;
}

.translation-content :deep(h2) {
  margin-top: 1.8rem;
  margin-bottom: 1.2rem;
  font-size: 1.7em;
  font-weight: 600;
  line-height: 1.35;
}

.translation-content :deep(h3) {
  margin-top: 1.6rem;
  margin-bottom: 1rem;
  font-size: 1.5em;
  font-weight: 600;
  line-height: 1.4;
}

.translation-content :deep(h4) {
  margin-top: 1.4rem;
  margin-bottom: 0.8rem;
  font-size: 1.3em;
  font-weight: 600;
}

.translation-content :deep(h5) {
  margin-top: 1.2rem;
  margin-bottom: 0.6rem;
  font-size: 1.2em;
  font-weight: 600;
}

.translation-content :deep(h6) {
  margin-top: 1rem;
  margin-bottom: 0.5rem;
  font-size: 1.1em;
  font-weight: 600;
}

.loading, .error {
  padding: 1rem;
  border-radius: 8px;
  background-color: var(--vp-c-bg-soft);
  text-align: center;
}

.error {
  color: var(--vp-c-danger);
}

@media (max-width: 768px) {
  .translation-container {
    flex-direction: column;
  }
}
</style>
