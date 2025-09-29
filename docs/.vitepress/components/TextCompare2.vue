<!-- TextCompare.vue -->
<script setup lang="ts">
import { computed } from 'vue'

interface Props {
  // Thay đổi props: nhận trực tiếp HTML content
  leftContentHtml: string
  rightContentHtml: string
  noteContentHtml?: string // Nếu bạn muốn pre-render cả note

  // Giữ lại các props này để hiển thị title và link
  leftPath: string
  rightPath: string
  leftTitle?: string
  rightTitle?: string
}

const props = withDefaults(defineProps<Props>(), {
  leftTitle: 'Left',
  rightTitle: 'Right',
  noteContentHtml: ''
})

// Xóa toàn bộ logic fetch, markdown-it, onMounted, isLoading, error...

// Hàm này vẫn cần thiết để chia các đoạn văn
const parseHtmlByParagraphs = (html: string): string[] => {
  const paragraphRegex = /<!--pg-->/g
  const parts = html.split(paragraphRegex)
  return parts.map(part => part.trim()).filter(part => part.length > 0)
}

// Dùng computed để tính toán lại khi props thay đổi (mặc dù ở đây sẽ không đổi)
const parsedParagraphs = computed(() => {
  return {
    left: parseHtmlByParagraphs(props.leftContentHtml),
    right: parseHtmlByParagraphs(props.rightContentHtml)
  }
})

// Tính toán link gốc
const leftOriginalPath = computed(() => props.leftPath.replace(/\.md$/, ''))
const rightOriginalPath = computed(() => props.rightPath.replace(/\.md$/, ''))

const hasNote = computed(() => props.noteContentHtml.trim().length > 0)

</script>

<template>
  <div class="text-compare">
    <!-- Không cần v-if isLoading hoặc v-if error nữa -->
    <div>
      <!-- Header with titles -->
      <div class="text-compare-header">
        <div class="text-column-header">
          <h3>
            {{ leftTitle }}
            <!-- Dùng prop `leftPath` để tạo link -->
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

      <!-- Notes section -->
      <div v-if="hasNote" class="notes-container">
        <h2 class="notes-title">Notes</h2>
        <div class="notes-content" v-html="noteContentHtml"></div>
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
