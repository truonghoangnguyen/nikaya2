<template>
  <div class="search-page">
    <div class="search-header">
      <div class="search-box">
        <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8"/>
          <path d="m21 21-4.35-4.35"/>
        </svg>
        <input
          v-model="query"
          type="text"
          placeholder="Tìm kiếm kinh văn... (vd: MN 1, Tứ Niệm Xứ)"
          class="search-input"
          autofocus
          @keydown.escape="query = ''"
        />
        <button v-if="query" class="clear-btn" @click="query = ''">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path d="M18 6L6 18M6 6l12 12"/>
          </svg>
        </button>
      </div>

      <div class="search-meta">
        <span v-if="query" class="result-count">
          {{ filteredItems.length }} kết quả
          <span class="for-query">cho "{{ query }}"</span>
        </span>
        <span v-else class="result-count">{{ props.items.length }} kinh văn — nhập từ khóa để tìm kiếm</span>
      </div>
    </div>

    <div class="results-container">
      <TransitionGroup name="list" tag="ul" class="results-list">
        <li
          v-for="(result, index) in filteredItems"
          :key="result.item.link"
          class="result-item"
          :style="{ '--delay': `${Math.min(index * 30, 300)}ms` }"
        >
          <a :href="result.item.link" class="result-link">
            <div class="result-content">
              <span class="result-text" v-html="highlight(result)" />
              <span class="result-arrow">→</span>
            </div>
            <span class="result-path">{{ result.item.link }}</span>
          </a>
        </li>
      </TransitionGroup>

      <div v-if="query && filteredItems.length === 0" class="empty-state">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <circle cx="11" cy="11" r="8"/>
          <path d="m21 21-4.35-4.35"/>
        </svg>
        <p>Không tìm thấy kết quả cho "<strong>{{ query }}</strong>"</p>
        <span>Thử tìm với từ khác hoặc kiểm tra chính tả</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import Fuse from 'fuse.js'

// ── Props ────────────────────────────────────────────────────────────────────
const props = defineProps({
  items: {
    type: Array,
    default: () => [],
    // Mỗi phần tử: { text: string, link: string }
  },
})

// ── State ────────────────────────────────────────────────────────────────────
const query = ref('')

// ── Fuse instance ─────────────────────────────────────────────────────────────
const fuse = computed(() => new Fuse(props.items, {
  keys: ['text'],
  threshold: 0.3,      // 0 = khớp chính xác, 1 = khớp tất cả
  distance: 200,       // tìm trong chuỗi dài
  ignoreLocation: true, // không quan tâm vị trí khớp trong chuỗi
  includeMatches: true, // trả về vị trí ký tự khớp để highlight
}))

// ── Computed ─────────────────────────────────────────────────────────────────
const filteredItems = computed(() => {
  if (!query.value.trim()) return []
  return fuse.value.search(query.value)
  // Mỗi phần tử: { item: { text, link }, matches: [...] }
})

// ── Helpers ──────────────────────────────────────────────────────────────────
// Highlight dựa trên indices từ Fuse (chính xác hơn regex)
function highlight(fuseResult) {
  const text = fuseResult.item.text
  const match = fuseResult.matches?.find(m => m.key === 'text')
  if (!match?.indices?.length) return text

  let result = ''
  let lastIndex = 0

  // Fuse trả về mảng [start, end] đã được sắp xếp
  for (const [start, end] of match.indices) {
    result += escape(text.slice(lastIndex, start))
    result += `<mark>${escape(text.slice(start, end + 1))}</mark>`
    lastIndex = end + 1
  }
  result += escape(text.slice(lastIndex))
  return result
}

function escape(str) {
  return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
}
</script>

<style scoped>
.search-page {
  max-width: 760px;
  margin: 0 auto;
  padding: 2.5rem 1.5rem 4rem;
  font-family: 'Georgia', serif;
}

.search-header { margin-bottom: 2rem; }

.search-box {
  position: relative;
  display: flex;
  align-items: center;
  background: var(--vp-c-bg-soft);
  border: 1.5px solid var(--vp-c-divider);
  border-radius: 12px;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.search-box:focus-within {
  border-color: var(--vp-c-brand-1, #3b82f6);
  box-shadow: 0 0 0 3px color-mix(in srgb, var(--vp-c-brand-1, #3b82f6) 15%, transparent);
}

.search-icon {
  position: absolute;
  left: 1rem;
  width: 18px;
  height: 18px;
  color: var(--vp-c-text-3);
  pointer-events: none;
}

.search-input {
  width: 100%;
  padding: 0.875rem 3rem 0.875rem 3rem;
  background: transparent;
  border: none;
  outline: none;
  font-size: 1rem;
  font-family: inherit;
  color: var(--vp-c-text-1);
  caret-color: var(--vp-c-brand-1, #3b82f6);
}

.search-input::placeholder { color: var(--vp-c-text-3); }

.clear-btn {
  position: absolute;
  right: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border: none;
  background: var(--vp-c-bg-mute);
  border-radius: 50%;
  cursor: pointer;
  color: var(--vp-c-text-2);
  transition: background 0.15s, color 0.15s;
}

.clear-btn svg { width: 13px; height: 13px; }

.clear-btn:hover {
  background: var(--vp-c-danger-soft, #fef2f2);
  color: var(--vp-c-red-1, #ef4444);
}

.search-meta {
  margin-top: 0.75rem;
  font-size: 0.82rem;
  color: var(--vp-c-text-3);
  font-family: system-ui, sans-serif;
}

.for-query { color: var(--vp-c-text-2); font-style: italic; }

.results-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.result-item {
  animation: fadeSlideIn 0.25s ease both;
  animation-delay: var(--delay, 0ms);
}

@keyframes fadeSlideIn {
  from { opacity: 0; transform: translateY(6px); }
  to   { opacity: 1; transform: translateY(0); }
}

.result-link {
  display: block;
  padding: 0.875rem 1rem;
  border-radius: 10px;
  border: 1px solid transparent;
  text-decoration: none;
  transition: background 0.15s, border-color 0.15s, transform 0.15s;
  background: var(--vp-c-bg-soft);
}

.result-link:hover {
  background: var(--vp-c-bg-mute);
  border-color: var(--vp-c-divider);
  transform: translateX(3px);
}

.result-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
}

.result-text {
  font-size: 0.95rem;
  color: var(--vp-c-text-1);
  line-height: 1.5;
}

.result-text :deep(mark) {
  background: color-mix(in srgb, var(--vp-c-brand-1, #3b82f6) 20%, transparent);
  color: var(--vp-c-brand-1, #3b82f6);
  border-radius: 3px;
  padding: 0 2px;
  font-weight: 600;
}

.result-arrow {
  color: var(--vp-c-text-3);
  font-size: 0.9rem;
  transition: color 0.15s, transform 0.15s;
  flex-shrink: 0;
}

.result-link:hover .result-arrow {
  color: var(--vp-c-brand-1, #3b82f6);
  transform: translateX(3px);
}

.result-path {
  display: block;
  margin-top: 3px;
  font-size: 0.75rem;
  font-family: 'SF Mono', 'Fira Code', monospace;
  color: var(--vp-c-text-3);
}

.list-enter-active, .list-leave-active { transition: all 0.2s ease; }
.list-enter-from { opacity: 0; transform: translateX(-8px); }
.list-leave-to   { opacity: 0; transform: translateX(8px); }

.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  color: var(--vp-c-text-3);
  font-family: system-ui, sans-serif;
}

.empty-state svg {
  width: 48px;
  height: 48px;
  margin: 0 auto 1rem;
  display: block;
  opacity: 0.4;
}

.empty-state p {
  font-size: 1rem;
  color: var(--vp-c-text-2);
  margin: 0 0 0.4rem;
}

.empty-state p strong { color: var(--vp-c-text-1); }
.empty-state span { font-size: 0.85rem; }
</style>