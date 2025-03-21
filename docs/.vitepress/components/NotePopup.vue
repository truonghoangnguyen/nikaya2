<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import MarkdownIt from 'markdown-it'

const md = new MarkdownIt({
  html: true,
  linkify: true,
  typographer: true
})

const popup = ref(null)
const content = ref('')
const isVisible = ref(false)
const position = ref({ x: 0, y: 0 })
const loading = ref(false)
const error = ref(null)
const isMouseOverPopup = ref(false)
const activeTarget = ref(null)
const currentMousePosition = ref({ x: 0, y: 0 })

// Cache for loaded notes
const notesCache = ref({})

// Parse note content into a structured object with footnote IDs as keys
function parseNoteContent(text) {
  const noteEntries = {}

  // Use regex to find all footnote entries
  // Format: ###### [^n] followed by content until the next footnote or end of text
  const regex = /###### \[\^(\d+)\]([\s\S]*?)(?=###### \[\^|$)/g

  let match
  while ((match = regex.exec(text)) !== null) {
    const id = `_${match[1]}` // Convert [^1] to _1 format
    const content = match[2].trim()
    noteEntries[id] = content
  }

  return noteEntries
}

// Function to fetch content from the URL
async function fetchContent(url) {
  loading.value = true
  error.value = null

  try {
    // Parse URL to separate the base URL from the hash fragment
    const [baseUrl, hash] = url.split('#')

    // Convert HTML URL to markdown URL if needed
    let fetchUrl = baseUrl
    if (baseUrl.endsWith('.html')) {
      fetchUrl = baseUrl.replace('.html', '.md')
    } else if (!baseUrl.endsWith('.md')) {
      // If no extension, try adding .md
      fetchUrl = `${baseUrl}.md`
    }

    // Check if we already have this note in cache
    if (notesCache.value[fetchUrl]) {
      console.log('Using cached note:', fetchUrl)

      if (hash) {
        // Display only the specific footnote
        const noteContent = notesCache.value[fetchUrl][hash]
        if (noteContent) {
          content.value = md.render(noteContent)
        } else {
          content.value = `<div class="error">Note reference #${hash} not found</div>`
        }
      } else {
        // Display all notes if no hash specified
        const allNotes = Object.entries(notesCache.value[fetchUrl])
          .map(([id, text]) => `###### [^${id.substring(1)}]\n${text}`)
          .join('\n\n')
        content.value = md.render(allNotes)
      }

      loading.value = false
      return
    }

    console.log('Fetching from:', fetchUrl)

    const response = await fetch(fetchUrl)
    if (!response.ok) {
      throw new Error(`Failed to fetch content: ${response.status}`)
    }

    const text = await response.text()

    // Parse note content and store in cache
    const parsedNotes = parseNoteContent(text)
    notesCache.value[fetchUrl] = parsedNotes

    if (hash && parsedNotes[hash]) {
      // Display only the specific footnote
      content.value = md.render(parsedNotes[hash])
    } else if (hash && !parsedNotes[hash]) {
      // Hash specified but not found in parsed notes
      content.value = `<div class="error">Note reference #${hash} not found</div>`
    } else {
      // No hash or hash not found, display all content
      content.value = md.render(text)
    }
  } catch (err) {
    console.error("Error fetching content:", err)
    error.value = err.message
    content.value = `<div class="error">Error loading note: ${err.message}</div>`
  } finally {
    loading.value = false
  }
}

// Track mouse position globally
function updateMousePosition(event) {
  currentMousePosition.value = {
    x: event.clientX,
    y: event.clientY
  }
}

// Handle mouse enter on note links
function handleMouseEnter(event) {
  const target = event.target.closest('.note')
  if (!target) return

  const url = target.getAttribute('href')
  if (!url) return

  // Store the active target
  activeTarget.value = target

  // Set position to fixed value for testing
  position.value = {
    x: 0,
    y: 0
  }
  const rect = target.getBoundingClientRect()
  position.value = {
    x: rect.left,
    y: rect.bottom + window.scrollY
  }

  // Show popup and fetch content
  isVisible.value = true
  fetchContent(url)
}

// Handle mouse move when popup is visible
function handleMouseMove(event) {
  // Don't update position at all for testing
  return;

  // Don't update position when mouse is over the popup
  if (!isVisible.value || isMouseOverPopup.value) return

  // Update position to follow the cursor - no offset
  position.value = {
    x: event.clientX + window.scrollX,
    y: event.clientY + window.scrollY
  }
}

// Handle mouse leave on note links
function handleMouseLeave(event) {
  // Only handle if we're leaving the active target
  if (!activeTarget.value || !event.target.closest('.note')) return

  // Add a small delay to prevent popup from disappearing immediately
  // when moving from the link to the popup
  setTimeout(() => {
    if (!isMouseOverPopup.value) {
      isVisible.value = false
    }
  }, 500)
}

function handlePopupMouseEnter() {
  isMouseOverPopup.value = true
}

function handlePopupMouseLeave() {
  isMouseOverPopup.value = false
  setTimeout(() => {
    isVisible.value = false
  }, 300)
}

// Handle keydown events for ESC key
function handleKeyDown(event) {
  if (event.key === 'Escape' && isVisible.value) {
    isVisible.value = false
  }
}

// Handle close button click
function handleCloseClick() {
  isVisible.value = false
}

// Add and remove event listeners
onMounted(() => {
  document.addEventListener('mousemove', updateMousePosition)
  document.addEventListener('mousemove', handleMouseMove)
  document.addEventListener('mouseover', handleMouseEnter)
  document.addEventListener('mouseout', handleMouseLeave)
  document.addEventListener('keydown', handleKeyDown)

  // For debugging
  console.log("NotePopup component mounted")
})

onUnmounted(() => {
  document.removeEventListener('mousemove', updateMousePosition)
  document.removeEventListener('mousemove', handleMouseMove)
  document.removeEventListener('mouseover', handleMouseEnter)
  document.removeEventListener('mouseout', handleMouseLeave)
  document.removeEventListener('keydown', handleKeyDown)
})
</script>

<template>
  <div
    ref="popup"
    class="note-popup"
    v-show="isVisible"
    :style="{
      left: `${position.x}px`,
      top: `${position.y}px`
    }"
    @mouseenter="handlePopupMouseEnter"
    @mouseleave="handlePopupMouseLeave"
  >
    <div class="note-popup-close-wrapper">
      <button class="note-popup-close" @click="handleCloseClick" title="Close (ESC)">&times;</button>
    </div>
    <div class="note-popup-content">
      <div v-if="loading" class="note-popup-loading">Loading...</div>
      <div v-else-if="error" class="note-popup-error">{{ error }}</div>
      <div v-else v-html="content"></div>
    </div>
  </div>
</template>

<style scoped>
.note-popup {
  position: absolute;
  z-index: 1000;
  min-width: 300px;
  max-width: 500px;
  width: auto;
  background-color: var(--vp-c-bg-soft, white);
  border: 1px solid var(--vp-c-divider, #ddd);
  border-radius: 6px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  padding: 0;
  font-size: 0.95rem;
  transition: opacity 0.2s;
  max-height: 80vh; /* Limit height to 80% of viewport height */
  overflow: hidden; /* Hide overflow from main container */
}

.note-popup-close-wrapper {
  position: absolute;
  top: 8px;
  right: 8px;
  z-index: 1001;
}

.note-popup-close {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background-color: var(--vp-c-bg-soft, white);
  border: 1px solid var(--vp-c-divider, #ddd);
  color: var(--vp-c-text-2, #666);
  font-size: 16px;
  line-height: 1;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  margin: 0;
  transition: all 0.2s;
}

.note-popup-close:hover {
  background-color: var(--vp-c-brand, #3498db);
  color: white;
  border-color: var(--vp-c-brand, #3498db);
}

.note-popup-content {
  padding: 16px;
  max-height: calc(80vh - 32px); /* Account for padding */
  overflow-y: auto; /* Enable scrolling */
  overscroll-behavior: contain; /* Prevent scroll chaining */
}

.note-popup-loading {
  padding: 12px;
  text-align: center;
  color: var(--vp-c-text-2, #666);
}

.note-popup-error {
  padding: 12px;
  text-align: center;
  color: var(--vp-c-danger, #e74c3c);
}

.error {
  color: var(--vp-c-danger, #e74c3c);
  padding: 10px;
}

/* Style for links inside the popup */
:deep(a) {
  color: var(--vp-c-brand, #3498db);
  text-decoration: none;
}

:deep(a:hover) {
  text-decoration: underline;
}

/* Additional styling for popup content */
:deep(h1), :deep(h2), :deep(h3), :deep(h4), :deep(h5), :deep(h6) {
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  font-size: 1.2em;
}

:deep(p) {
  margin: 0.5em 0;
}

:deep(ul), :deep(ol) {
  padding-left: 1.5em;
  margin: 0.5em 0;
}

/* Add highlight style for the target element */
:deep(.highlighted) {
  background-color: rgba(255, 255, 0, 0.2);
  border-left: 3px solid #f0ad4e;
  padding-left: 10px;
}
</style>
