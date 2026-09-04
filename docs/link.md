---
title: Quick Link
outline: false
---

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { withBase } from 'vitepress'

// Đường dẫn tới file dữ liệu — chỉnh lại theo vị trí thật của file này
// và của quicklink-data.js trong repo của bạn.
import quicklinkData from './.vitepress/data/quicklink-data.js'

// ---------- Resolver logic ----------

// Lấy danh sách tất cả các viết tắt và folder từ dữ liệu
function getAbbreviations(data) {
  if (!data) return []
  return Object.entries(data).map(([code, nikaya]) => {
    const editions = nikaya?.editions
      ? Object.values(nikaya.editions).map((e) => e.label).filter(Boolean)
      : []
    return {
      code,
      folder: nikaya?.folder || '',
      editions
    }
  })
}

// Tìm nikaya không phân biệt hoa thường (hỗ trợ SN, sn, Thag, thag, ...)
function findNikaya(data, code) {
  if (!data || !code) return null
  const codeLower = code.toLowerCase()
  const foundKey = Object.keys(data).find((k) => k.toLowerCase() === codeLower)
  return foundKey ? data[foundKey] : null
}

// "dn 1.2"   -> { code: "dn", rest: "1.2" }
// "dn 1 2.1" -> { code: "dn", rest: "1 2.1" }
// "sn2.2"    -> { code: "sn", rest: "2.2" }
// "?"        -> { isHelp: true }
function parseQuery(raw) {
  const str = (raw || '').trim().toLowerCase()
  if (!str) return null
  if (str === '?') return { isHelp: true }

  const codeMatch = str.match(/^[a-z]+/i)
  if (!codeMatch) return null
  const code = codeMatch[0].toLowerCase()

  const rest = str.slice(code.length).replace(/^[\s.:\-_#]+/, '').trim()
  if (!rest || !/\d/.test(rest)) return null

  return { code, rest }
}

function buildUrl(folder, editionPath, slug, anchor) {
  const base = `/${folder}/${editionPath}/${slug}`.replace(/\/+/g, '/')
  return anchor ? `${base}#${anchor}` : base
}

// Tìm bài kinh trong items (hỗ trợ số thường hoặc có padding 01, 001)
function findItem(items, key) {
  if (!items || !key) return null
  const k = String(key).trim()
  if (items[k]) return { item: items[k], key: k }

  const parts = k.split('.')
  const normalizedKey = parts
    .map((p) => {
      const n = Number(p)
      return isNaN(n) ? p : String(n)
    })
    .join('.')
  if (items[normalizedKey]) return { item: items[normalizedKey], key: normalizedKey }

  if (parts.length === 1) {
    const n = Number(k)
    if (!isNaN(n)) {
      const s = String(n)
      const pad2 = s.padStart(2, '0')
      if (items[pad2]) return { item: items[pad2], key: pad2 }
      const pad3 = s.padStart(3, '0')
      if (items[pad3]) return { item: items[pad3], key: pad3 }
    }
  }
  return null
}

// Tìm mục con / đoạn trong children (mảng chuỗi ["1", "2", "2.1", ...])
function findChild(children, target) {
  if (!Array.isArray(children) || !target) return null
  const targetStr = String(target).trim()

  const direct = children.find((c) => String(c).trim() === targetStr)
  if (direct !== undefined) return String(direct).trim()

  const normalize = (val) =>
    String(val)
      .trim()
      .split('.')
      .map((p) => {
        const n = Number(p)
        return isNaN(n) ? p : String(n)
      })
      .join('.')

  const normalizedTarget = normalize(targetStr)
  const normalizedMatch = children.find((c) => normalize(c) === normalizedTarget)
  if (normalizedMatch !== undefined) return String(normalizedMatch).trim()

  return null
}

// Tìm chương trong items của AN (hỗ trợ số thường hoặc padding 01)
function findChapter(items, key) {
  if (!items || !key) return null
  const k = String(key).trim()
  if (items[k]) return items[k]

  const n = Number(k)
  if (!isNaN(n)) {
    const norm = String(n)
    if (items[norm]) return items[norm]
    const pad2 = norm.padStart(2, '0')
    if (items[pad2]) return items[pad2]
  }
  return null
}

// Kiểm tra edition có dùng cấu trúc AN (chương có danh sách files) hay không
function isAnEdition(edition) {
  if (!edition || !edition.items) return false
  return Object.values(edition.items).some((item) => item && Array.isArray(item.files))
}

// Xử lý riêng cho cấu trúc AN:
// - "an 1"   -> trả về danh sách tất cả file trong chương 1
// - "an 1.5" -> tìm file có chứa kinh 5 trong children, gắn anchor #5
function resolveAnEdition(nikaya, edition, queryStr) {
  if (!edition || !edition.items || !queryStr) return null

  const items = edition.items
  const parts = queryStr.trim().split(/[\s.\-_#]+/).filter(Boolean)
  if (parts.length === 0) return null

  const chapterKey = parts[0]
  const chapter = findChapter(items, chapterKey)
  if (!chapter) return null

  // Khi chỉ nhập số chương (vd: an 1): hiển thị danh sách các file/phẩm thuộc chương đó
  if (parts.length === 1) {
    if (!Array.isArray(chapter.files)) return null
    return chapter.files.map((file) => ({
      title: `${chapter.title} - ${file.title}`,
      url: buildUrl(nikaya.folder, edition.path, file.slug, undefined)
    }))
  }

  // Khi nhập chương và kinh (vd: an 1.5 hoặc an 1 5)
  const suttaPart = parts[1]
  const extraPart = parts.slice(2).join('.')
  const suttaNum = Number(suttaPart)
  const targetStr = String(suttaPart).trim()

  for (const file of chapter.files || []) {
    if (!Array.isArray(file.children)) continue
    const found = file.children.find((c) => {
      if (!isNaN(suttaNum) && Number(c) === suttaNum) return true
      return String(c).trim() === targetStr
    })

    if (found !== undefined) {
      const anchor = extraPart ? `${suttaPart}.${extraPart}` : String(found)
      return {
        title: `${chapter.title} - ${file.title}`,
        url: buildUrl(nikaya.folder, edition.path, file.slug, anchor)
      }
    }
  }

  return null
}

// Tìm bài kinh theo cấu trúc mới:
// item trong items có: title, slug, children (mảng string các mục/đoạn)
function resolveEdition(nikaya, edition, queryStr) {
  if (!edition || !edition.items || !queryStr) return null

  // Phân nhánh nếu là định dạng AN
  if (isAnEdition(edition)) {
    return resolveAnEdition(nikaya, edition, queryStr)
  }

  const items = edition.items

  // 1. Nếu có khoảng trắng hoặc '#' phân cách kinh và đoạn (vd: "1 2", "1 2.1", "1#2.1")
  const spaceParts = queryStr.trim().split(/[\s#]+/)
  if (spaceParts.length >= 2) {
    const suttaPart = spaceParts[0]
    const childPart = spaceParts.slice(1).join('.')

    const found = findItem(items, suttaPart)
    if (found) {
      const matchedChild = findChild(found.item.children, childPart)
      return {
        title: found.item.title,
        url: buildUrl(nikaya.folder, edition.path, found.item.slug, matchedChild || undefined)
      }
    }
  }

  // 2. Tách theo dấu chấm / gạch nối (vd: "1.2.1", "1.2", "56.11", "1")
  const dotParts = queryStr.trim().split(/[.\-_]+/)

  // 2a. Khớp trực tiếp toàn bộ queryStr làm key kinh (vd: "56.11" hoặc "1")
  const directItem = findItem(items, queryStr.trim()) || findItem(items, dotParts.join('.'))
  if (directItem) {
    return {
      title: directItem.item.title,
      url: buildUrl(nikaya.folder, edition.path, directItem.item.slug, undefined)
    }
  }

  // 2b. Thử tách suttaKey và childTarget theo các vị trí dấu chấm
  let fallback = null
  for (let i = 1; i < dotParts.length; i++) {
    const suttaKey = dotParts.slice(0, i).join('.')
    const childTarget = dotParts.slice(i).join('.')

    const found = findItem(items, suttaKey)
    if (found) {
      if (!fallback) fallback = found
      const matchedChild = findChild(found.item.children, childTarget)
      if (matchedChild) {
        return {
          title: found.item.title,
          url: buildUrl(nikaya.folder, edition.path, found.item.slug, matchedChild)
        }
      }
    }
  }

  // 2c. Nếu tìm thấy sutta nhưng không khớp child nào, fallback về bài kinh gốc
  if (fallback) {
    return {
      title: fallback.item.title,
      url: buildUrl(nikaya.folder, edition.path, fallback.item.slug, undefined)
    }
  }

  // 2d. Fallback kiểm tra phần tử đầu tiên làm bài kinh
  if (dotParts.length > 0) {
    const firstFound = findItem(items, dotParts[0])
    if (firstFound) {
      return {
        title: firstFound.item.title,
        url: buildUrl(nikaya.folder, edition.path, firstFound.item.slug, undefined)
      }
    }
  }

  return null
}

function resolveAll(raw, data) {
  const parsed = parseQuery(raw)
  if (!parsed) return { error: 'invalid', code: null, results: [] }

  if (parsed.isHelp) {
    return { type: 'help', abbreviations: getAbbreviations(data), results: [] }
  }

  const nikaya = findNikaya(data, parsed.code)
  if (!nikaya) return { error: 'unknown-nikaya', code: parsed.code, results: [] }

  const results = []
  for (const [editionKey, edition] of Object.entries(nikaya.editions || {})) {
    const r = resolveEdition(nikaya, edition, parsed.rest)
    if (r) {
      if (Array.isArray(r)) {
        for (const item of r) {
          results.push({ editionKey, label: edition.label, ...item })
        }
      } else {
        results.push({ editionKey, label: edition.label, ...r })
      }
    }
  }

  if (results.length === 0) {
    return { error: 'not-found', code: parsed.code, results: [] }
  }
  return { error: null, code: parsed.code, results }
}

// ---------- UI state ----------

const input = ref('')
const submitted = ref('')
const searchInputRef = ref(null)

const allAbbreviations = computed(() => getAbbreviations(quicklinkData))

// Hiển thị chế độ trợ giúp khi ô input hoặc submitted là '?'
const isHelpMode = computed(() => {
  const current = (input.value || '').trim()
  const lastSubmitted = (submitted.value || '').trim()
  return current === '?' || lastSubmitted === '?'
})

const result = computed(() => {
  if (isHelpMode.value) {
    return { type: 'help', abbreviations: allAbbreviations.value, results: [] }
  }
  return submitted.value ? resolveAll(submitted.value, quicklinkData) : null
})

function onSearch() {
  submitted.value = input.value
}

function showHelp() {
  input.value = '?'
  submitted.value = '?'
  searchInputRef.value?.focus()
}

function selectAbbreviation(code) {
  input.value = `${code.toLowerCase()} `
  submitted.value = ''
  searchInputRef.value?.focus()
}

function onKeydown(e) {
  if (e.key === '?' && document.activeElement !== searchInputRef.value) {
    e.preventDefault()
    showHelp()
  }
}

// Hỗ trợ /link/?q=mn%207.3 hoặc /link/?q=?
onMounted(() => {
  window.addEventListener('keydown', onKeydown)
  const params = new URLSearchParams(window.location.search)
  const q = params.get('q')
  if (q) {
    input.value = q
    submitted.value = q
  }
})

onUnmounted(() => {
  window.removeEventListener('keydown', onKeydown)
})
</script>

<div class="quicklink">
  <h1>Quick Link</h1>
  <p class="hint">
    Nhập ký hiệu kinh, ví dụ <code>mn 7.3</code> hoặc <code>sn 2.2</code>.
    Nhấn <button type="button" class="help-btn-inline" title="Xem danh sách viết tắt" @click="showHelp"><code>?</code></button> để xem danh sách tất cả các viết tắt.
  </p>

  <form class="search-box" @submit.prevent="onSearch">
    <input
      ref="searchInputRef"
      v-model="input"
      type="text"
      placeholder="vd: sn 2.2 hoặc '?' để xem danh sách mã"
      autofocus
      autocomplete="off"
    />
    <button type="submit">Tìm</button>
  </form>

  <div v-if="result" class="result-area">
    <!-- Bảng danh sách viết tắt khi nhấn '?' -->
    <div v-if="result.type === 'help'" class="abbrev-container">
      <div class="abbrev-header">
        <span class="abbrev-title">Danh sách chữ viết tắt & thư mục</span>
        <span class="abbrev-count">{{ result.abbreviations.length }} mã</span>
      </div>
      <p class="abbrev-subhint">
        Chọn một mã kinh dưới đây để bắt đầu tìm kiếm nhanh:
      </p>
      <div class="abbrev-grid">
        <button
          v-for="item in result.abbreviations"
          :key="item.code"
          type="button"
          class="abbrev-card"
          @click="selectAbbreviation(item.code)"
        >
          <div class="abbrev-card-header">
            <span class="abbrev-code">{{ item.code }}</span>
            <span class="abbrev-sep">-</span>
            <span class="abbrev-folder">{{ item.folder }}</span>
          </div>
          <div v-if="item.editions && item.editions.length" class="abbrev-editions">
            <span v-for="ed in item.editions" :key="ed" class="edition-badge">{{ ed }}</span>
          </div>
        </button>
      </div>
    </div>
    <ul v-else-if="result.results && result.results.length" class="results">
      <li v-for="(r, idx) in result.results" :key="r.editionKey + '-' + r.url + '-' + idx">
        <a :href="withBase(r.url)">
          <span class="edition">{{ r.label }}</span>
          <span class="title">{{ r.title }}</span>
        </a>
      </li>
    </ul>
    <p v-else-if="result.error === 'invalid'" class="empty">
      Không đọc được cú pháp "<strong>{{ submitted }}</strong>". Ví dụ hợp lệ: <code>mn 7.3</code>, <code>sn 2.2</code> (hoặc gõ <code>?</code> để xem danh sách).
    </p>
    <p v-else-if="result.error === 'unknown-nikaya'" class="empty">
      Không nhận diện được bộ kinh "<strong>{{ result.code }}</strong>". Nhấn <button type="button" class="help-btn-inline" @click="showHelp"><code>?</code></button> để xem danh sách mã hợp lệ.
    </p>
    <p v-else-if="result.error === 'not-found'" class="empty">
      Chưa có dữ liệu cho "<strong>{{ submitted }}</strong>" trong bộ "<strong>{{ result.code }}</strong>".
    </p>
  </div>
</div>

<style scoped>
.quicklink {
  max-width: 680px;
  margin: 0 auto;
  padding: 32px 0 64px;
}

.hint {
  color: var(--vp-c-text-2);
  margin-bottom: 24px;
}

.hint code {
  font-size: 0.9em;
}

.help-btn-inline {
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  vertical-align: baseline;
}

.help-btn-inline code {
  background: var(--vp-c-brand-soft, rgba(16, 185, 129, 0.14));
  color: var(--vp-c-brand-1);
  font-weight: 600;
  padding: 2px 6px;
  border-radius: 4px;
  border: 1px solid var(--vp-c-brand-soft, rgba(16, 185, 129, 0.3));
  transition: all 0.2s ease;
}

.help-btn-inline:hover code {
  background: var(--vp-c-brand-1);
  color: #fff;
}

.search-box {
  display: flex;
  gap: 8px;
  margin-bottom: 24px;
}

.search-box input {
  flex: 1;
  padding: 10px 14px;
  font-size: 16px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
}

.search-box input:focus {
  outline: 2px solid var(--vp-c-brand-1);
  outline-offset: 1px;
}

.search-box button {
  padding: 10px 18px;
  font-size: 16px;
  font-weight: 600;
  border-radius: 8px;
  border: none;
  background: var(--vp-c-brand-1);
  color: var(--vp-c-white, #fff);
  cursor: pointer;
}

.search-box button:hover {
  background: var(--vp-c-brand-2);
}

/* Danh sách chữ viết tắt & folder */
.abbrev-container {
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
  padding: 18px 20px;
  background: var(--vp-c-bg-soft);
}

.abbrev-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 6px;
}

.abbrev-title {
  font-weight: 700;
  font-size: 1.05rem;
  color: var(--vp-c-text-1);
}

.abbrev-count {
  font-size: 0.8rem;
  font-weight: 600;
  padding: 2px 8px;
  background: var(--vp-c-brand-soft, rgba(16, 185, 129, 0.14));
  color: var(--vp-c-brand-1);
  border-radius: 12px;
}

.abbrev-subhint {
  font-size: 0.85rem;
  color: var(--vp-c-text-2);
  margin-bottom: 16px;
}

.abbrev-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 10px;
}

.abbrev-card {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 6px;
  padding: 12px 14px;
  background: var(--vp-c-bg-alt, var(--vp-c-bg));
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  text-align: left;
  cursor: pointer;
  transition: all 0.2s ease;
  width: 100%;
}

.abbrev-card:hover {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-bg-elv, var(--vp-c-bg-soft));
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.abbrev-card-header {
  display: flex;
  align-items: center;
  gap: 8px;
  width: 100%;
}

.abbrev-code {
  font-family: var(--vp-font-family-mono, monospace);
  font-weight: 700;
  font-size: 0.95rem;
  color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft, rgba(16, 185, 129, 0.1));
  padding: 2px 7px;
  border-radius: 4px;
}

.abbrev-sep {
  color: var(--vp-c-text-3);
  font-weight: 500;
}

.abbrev-folder {
  font-family: var(--vp-font-family-mono, monospace);
  font-size: 0.88rem;
  color: var(--vp-c-text-1);
  font-weight: 500;
  word-break: break-all;
}

.abbrev-editions {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
}

.edition-badge {
  font-size: 0.72rem;
  padding: 1px 6px;
  border-radius: 4px;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  color: var(--vp-c-text-2);
}

/* Kết quả danh sách */
.results {
  list-style: none;
  padding: 0;
  margin: 0;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  overflow: hidden;
}

.results li + li {
  border-top: 1px solid var(--vp-c-divider);
}

.results a {
  display: flex;
  align-items: baseline;
  gap: 10px;
  padding: 12px 16px;
  text-decoration: none;
  color: var(--vp-c-text-1);
}

.results a:hover {
  background: var(--vp-c-bg-soft);
}

.results .edition {
  flex-shrink: 0;
  font-size: 0.75em;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.03em;
  color: var(--vp-c-brand-1);
  min-width: 90px;
}

.results .title {
  color: var(--vp-c-text-1);
}

.empty {
  color: var(--vp-c-text-2);
  padding: 12px 0;
}
</style>