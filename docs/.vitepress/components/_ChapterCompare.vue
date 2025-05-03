<script setup lang="ts">
import { ref, onMounted } from 'vue'
import TranslationCompare from './TranslationCompare.vue'
import MarkdownIt from 'markdown-it'

// Initialize markdown-it instance with enhanced configuration
const md = new MarkdownIt({
  html: true,
  linkify: true,
  typographer: true,
  //breaks: false,
  //listIndent: 2
})

// Define the comparison item interface
interface ComparisonItem {
  leftPath: string;
  rightPath: string;
  leftTitle: string;
  rightTitle: string;
  key: string;
}

interface Props {
  // Original props
  parts: number;
  leftBasePath?: string;
  rightBasePath?: string;
  leftTitle?: string;
  rightTitle?: string;
  notePath?: string;

  // New dynamic route props
  slug?: string;
  left?: string;
  right?: string;
}

const props = withDefaults(defineProps<Props>(), {
  // Original defaults
  leftTitle: 'Left Translation',
  rightTitle: 'Right Translation',
  notePath: '',

  // New defaults
  slug: '',
  left: '',
  right: ''
})

const generateComparisons = (): ComparisonItem[] => {
  const comparisons: ComparisonItem[] = []

  // Check if we're using the new dynamic path approach
  if (props.left && props.right) {
    if (props.parts === 1) {
      // Single part comparison
      comparisons.push({
        leftPath: props.left,
        rightPath: props.right,
        leftTitle: props.leftTitle,
        rightTitle: props.rightTitle,
        key: 'part-1'
      })
    } else {
      // Multi-part comparison with .p1, .p2, etc. suffix
      for (let i = 1; i <= props.parts; i++) {
        // Extract file base and extension
        const leftBase = props.left.replace(/\.[^/.]+$/, '')
        const rightBase = props.right.replace(/\.[^/.]+$/, '')
        const leftExt = props.left.match(/\.[^/.]+$/)?.[0] || '.md'
        const rightExt = props.right.match(/\.[^/.]+$/)?.[0] || '.md'

        comparisons.push({
          leftPath: `${leftBase}.p${i}${leftExt}`,
          rightPath: `${rightBase}.p${i}${rightExt}`,
          leftTitle: props.leftTitle,
          rightTitle: props.rightTitle,
          key: `part-${i}`
        })
      }
    }
  } else {
    // Original implementation using chapter number and base paths
    for (let i = 1; i <= props.parts; i++) {
      comparisons.push({
        leftPath: `${props.leftBasePath}/${i}.md`,
        rightPath: `${props.rightBasePath}/${i}.md`,
        leftTitle: props.leftTitle,
        rightTitle: props.rightTitle,
        key: `part-${i}`
      })
    }
  }

  return comparisons
}

const comparisons = ref<ComparisonItem[]>(generateComparisons())

// Note handling
const noteContent = ref<string>('')
const noteHtml = ref<string>('')
const noteLoading = ref<boolean>(false)
const noteError = ref<string | null>(null)
const hasNote = ref<boolean>(false)

onMounted(async () => {
  // Only fetch note if a path is provided
  if (props.notePath) {
    try {
      noteLoading.value = true

      const noteResponse = await fetch(props.notePath)

      if (noteResponse.ok) {
        noteContent.value = await noteResponse.text()

        // Remove frontmatter if present
        noteContent.value = noteContent.value.replace(/^---[\s\S]*?---\n/, '')

        // Convert markdown to HTML
        noteHtml.value = md.render(noteContent.value)

        // Only show notes section if there's actual content
        hasNote.value = noteContent.value.trim().length > 0
      } else {
        // Don't show error if note file is optional
        console.log(`Note file not found: ${props.notePath}`)
        hasNote.value = false
      }
    } catch (e) {
      noteError.value = e instanceof Error ? e.message : 'Unknown error loading notes'
      console.error(noteError.value)
    } finally {
      noteLoading.value = false
    }
  }
})
</script>

<template>
  <div class="chapter-compare">
    <div v-for="comparison in comparisons" :key="comparison.key" class="part-container">
      <TranslationCompare
        :leftPath="comparison.leftPath"
        :rightPath="comparison.rightPath"
        :leftTitle="comparison.leftTitle"
        :rightTitle="comparison.rightTitle"
      />
    </div>

    <!-- Notes section -->
    <div v-if="hasNote" class="notes-container">
      <h2 class="notes-title">Notes</h2>
      <div v-if="noteLoading" class="loading">Loading notes...</div>
      <div v-else-if="noteError" class="error">{{ noteError }}</div>
      <div v-else class="notes-content translation-content" v-html="noteHtml"></div>
    </div>
  </div>
</template>

<style scoped>
.chapter-compare {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.part-container {
  border-top: 1px solid var(--vp-c-divider);
  padding-top: 1rem;
}

.part-title {
  margin-bottom: 1rem;
  font-size: 1.2rem;
  font-weight: 600;
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

.notes-content :deep(h3) {
  margin-top: 1.5rem;
  margin-bottom: 1rem;
  font-size: 1.2rem;
  font-weight: 600;
}

.notes-content :deep(p) {
  margin: 1rem 0;
  white-space: normal;
}

.loading, .error {
  padding: 1rem;
  border-radius: 8px;
  background-color: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
}

.error {
  color: var(--vp-c-danger);
}
</style>
