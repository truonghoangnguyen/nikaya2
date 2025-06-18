<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue'
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
const popupPosition = ref('lower-right') // Track current position style

// Cache for loaded notes
const notesCache = ref({})

// Parse note content into a structured object with footnote IDs as keys
function parseNoteContent2(text) {
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


function parseNoteContent(text) {
  const noteEntries = {};

  // Biểu thức chính quy (regex) để tìm tất cả các mục ghi chú.
  // Định dạng mới: [^n]: theo sau là nội dung cho đến mục ghi chú tiếp theo hoặc cuối văn bản.
  // - \[\^(\d+)\]: Khớp với "[^" theo sau là một hoặc nhiều chữ số (được bắt giữ trong group 1) và rồi "]"
  //                Ví dụ: "[^1]", "[^12]"
  // - :\s*         Khớp với dấu hai chấm ":" theo sau là không hoặc nhiều ký tự khoảng trắng (space, tab, newline).
  // - ([\s\S]*?)  Khớp với bất kỳ ký tự nào (bao gồm cả xuống dòng, \s\S) một cách "non-greedy" (lười biếng, *?).
  //                Đây là nội dung của ghi chú (bắt giữ trong group 2).
  //                Non-greedy quan trọng để nó dừng lại trước khi gặp mục ghi chú tiếp theo.
  // - (?=\[\^\d+\]:|$) Đây là một "positive lookahead assertion". Nó đảm bảo rằng những gì theo sau là:
  //                - Hoặc là sự bắt đầu của một mục ghi chú tiếp theo (\[\^\d+\]:)
  //                - Hoặc là cuối của chuỗi ($)
  //                Điều này giúp xác định điểm kết thúc của nội dung ghi chú hiện tại mà không tiêu thụ các ký tự đó.
  // - g            Cờ global, để tìm tất cả các kết quả khớp trong văn bản.
  const regex = /\[\^(\d+)\]:\s*([\s\S]*?)(?=\[\^\d+\]:|$)/g;

  let match;
  while ((match = regex.exec(text)) !== null) {
    // match[0] là toàn bộ chuỗi khớp, ví dụ: "[^1]: note 1."
    // match[1] là số thứ tự của ghi chú, ví dụ: "1"
    // match[2] là nội dung của ghi chú, ví dụ: "note 1."
    const id = `${match[1]}`; // Chuyển đổi [^1] thành định dạng _1
    const content = match[2].trim(); // Loại bỏ khoảng trắng thừa ở đầu và cuối nội dung
    noteEntries[id] = content;
  }

  return noteEntries;
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

  // Show popup and fetch content
  isVisible.value = true
  fetchContent(url)

  // We need to wait for the next tick to get the popup dimensions
  // after it becomes visible
  setTimeout(() => {
    updatePopupPosition(target)
  }, 0)
}

// Handle mouse move when popup is visible
function handleMouseMove(event) {
  // Don't update position when mouse is over the popup
  if (!isVisible.value || isMouseOverPopup.value) return

  // We don't need to update position on mouse move anymore
  // as we're using smart positioning based on the target element
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
    if (!isMouseOverPopup.value && !activeTarget.value?.matches(':hover')) {
      isVisible.value = false
    }
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

// Function to calculate and update popup position based on available space
function updatePopupPosition(target) {
  if (!popup.value || !target) return

  const targetRect = target.getBoundingClientRect()
  const popupRect = popup.value.getBoundingClientRect()

  // Get viewport dimensions
  const viewportWidth = window.innerWidth
  const viewportHeight = window.innerHeight

  // Calculate available space in different directions
  const spaceRight = viewportWidth - targetRect.right
  const spaceLeft = targetRect.left
  const spaceBelow = viewportHeight - targetRect.bottom
  const spaceAbove = targetRect.top

  // Determine the best position for the popup
  let bestPosition = 'lower-right' // Default position
  let xPos = 0
  let yPos = 0

  // Check if popup fits to the right of the target
  if (spaceRight >= popupRect.width) {
    // Right side positioning
    xPos = targetRect.right + window.scrollX

    if (spaceBelow >= popupRect.height) {
      // Lower-right positioning
      yPos = targetRect.top + window.scrollY
      bestPosition = 'lower-right'
    } else if (spaceAbove >= popupRect.height) {
      // Upper-right positioning
      yPos = targetRect.bottom - popupRect.height + window.scrollY
      bestPosition = 'upper-right'
    } else {
      // Middle-right positioning (center vertically)
      yPos = Math.max(window.scrollY, targetRect.top + window.scrollY - (popupRect.height - targetRect.height) / 2)
      // Ensure it doesn't go off-screen
      if (yPos + popupRect.height > window.scrollY + viewportHeight) {
        yPos = window.scrollY + viewportHeight - popupRect.height - 10
      }
      bestPosition = 'middle-right'
    }
  }
  // Check if popup fits to the left of the target
  else if (spaceLeft >= popupRect.width) {
    // Left side positioning
    xPos = targetRect.left - popupRect.width + window.scrollX

    if (spaceBelow >= popupRect.height) {
      // Lower-left positioning
      yPos = targetRect.top + window.scrollY
      bestPosition = 'lower-left'
    } else if (spaceAbove >= popupRect.height) {
      // Upper-left positioning
      yPos = targetRect.bottom - popupRect.height + window.scrollY
      bestPosition = 'upper-left'
    } else {
      // Middle-left positioning (center vertically)
      yPos = Math.max(window.scrollY, targetRect.top + window.scrollY - (popupRect.height - targetRect.height) / 2)
      // Ensure it doesn't go off-screen
      if (yPos + popupRect.height > window.scrollY + viewportHeight) {
        yPos = window.scrollY + viewportHeight - popupRect.height - 10
      }
      bestPosition = 'middle-left'
    }
  }
  // If it doesn't fit on either side, position below or above
  else {
    // Center horizontally
    xPos = Math.max(window.scrollX + 10, targetRect.left + window.scrollX - (popupRect.width - targetRect.width) / 2)
    // Ensure it doesn't go off-screen horizontally
    if (xPos + popupRect.width > window.scrollX + viewportWidth) {
      xPos = window.scrollX + viewportWidth - popupRect.width - 10
    }

    if (spaceBelow >= popupRect.height) {
      // Lower-middle positioning
      yPos = targetRect.bottom + window.scrollY
      bestPosition = 'lower-middle'
    } else {
      // Upper-middle positioning
      yPos = targetRect.top - popupRect.height + window.scrollY
      bestPosition = 'upper-middle'
    }
  }

  // Update position
  if (bestPosition === 'lower-left' || bestPosition === 'lower-right' || bestPosition === 'lower-middle')
    position.value = { x: xPos-20, y: yPos-10 }
  else
    position.value = { x: xPos-20, y: yPos+10 }
  popupPosition.value = bestPosition
}

// Add and remove event listeners
onMounted(() => {
  document.addEventListener('mousemove', updateMousePosition)
  document.addEventListener('mousemove', handleMouseMove)
  document.addEventListener('mouseover', handleMouseEnter)
  document.addEventListener('mouseout', handleMouseLeave)
  document.addEventListener('keydown', handleKeyDown)
  window.addEventListener('resize', () => {
    if (isVisible.value && activeTarget.value) {
      updatePopupPosition(activeTarget.value)
    }
  })

  // For debugging
  console.log("NotePopup component mounted")
})

onUnmounted(() => {
  document.removeEventListener('mousemove', updateMousePosition)
  document.removeEventListener('mousemove', handleMouseMove)
  document.removeEventListener('mouseover', handleMouseEnter)
  document.removeEventListener('mouseout', handleMouseLeave)
  document.removeEventListener('keydown', handleKeyDown)
  window.removeEventListener('resize', () => {})
})
</script>

<template>
  <div
    ref="popup"
    class="note-popup"
    v-show="isVisible"
    :class="[popupPosition]"
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
  transition: opacity 0.2s, transform 0.2s;
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

/* Position-specific styles */
.upper-left {
  transform-origin: bottom right;
}

.upper-right {
  transform-origin: bottom left;
}

.lower-left {
  transform-origin: top right;
}

.lower-right {
  transform-origin: top left;
}

.upper-middle {
  transform-origin: bottom center;
}

.lower-middle {
  transform-origin: top center;
}

.middle-left {
  transform-origin: center right;
}

.middle-right {
  transform-origin: center left;
}
</style>
