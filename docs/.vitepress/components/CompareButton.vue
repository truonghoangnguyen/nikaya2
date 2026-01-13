<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vitepress'

const route = useRoute()
const router = useRouter()

// Lấy dữ liệu từ Vite define
const BOOK_NAV = typeof __BOOK_NAV__ !== 'undefined' ? __BOOK_NAV__ : {}

const MAP_CONFIG = {
  'kinhtrungbo/thichminhchau': {
    refKey: 'kinhtrungbo/thichminhchau',
    targetBase: '/kinhtrungbo/c-nm-tmc-vi/',
    idLength: 3
  },
  'kinhtrungbo/nanamoli-bodhi-vi': {
    refKey: 'kinhtrungbo/thichminhchau',
    targetBase: '/kinhtrungbo/c-nm-tmc-vi/',
    idLength: 3
  },

  'kinhtruongbo/thichminhchau': {
    refKey: 'kinhtruongbo/thichminhchau',
    targetBase: '/kinhtruongbo/c-sujato-tmc-vi/',
    idLength: 3
  },
   'kinhtruongbo/sujato-vi': {
    refKey: 'kinhtruongbo/thichminhchau',
    targetBase: '/kinhtruongbo/c-sujato-tmc-vi/',
    idLength: 3
  },
}

const targetUrl = computed(() => {
  const path = route.path

  // 1. Tìm cấu hình mapping khớp với URL hiện tại
  const currentKey = Object.keys(MAP_CONFIG).find(key => path.includes(key))
  console.log(currentKey)
  if (!currentKey) return null

  const config = MAP_CONFIG[currentKey]

  // 2. Trích xuất ID với độ dài linh hoạt
  // Tạo Regex động: ví dụ len = 2 thì thành /\/(\d{2})-/
  const len = config.idLength || 3 // Mặc định là 3 nếu không khai báo
  const dynamicRegex = new RegExp(`\\/(\\d{${len}})-`)
  const idMatch = path.match(dynamicRegex)

  if (!idMatch) return null
  const id = idMatch[1]
  console.log(id)
  // 3. Tìm slug chuẩn trong bộ tham chiếu (Thích Minh Châu)
  const refList = BOOK_NAV[config.refKey] || []
  const refEntry = refList.find(item => {
    // Lấy tên file từ link (ví dụ: /kinhtrungbo/.../064-abc.md -> 064-abc)
    const fileName = item.link.split('/').pop().replace('.md', '')
    return fileName.startsWith(id + '-')
  })

  if (!refEntry) return null

  // 4. Lấy slug chuẩn và tạo URL đích
  const finalSlug = refEntry.link.split('/').pop().replace('.md', '')

  // Đảm bảo không bị trùng dấu //
  const base = config.targetBase.endsWith('/') ? config.targetBase : config.targetBase + '/'
  return `${base}${finalSlug}.html`
})

function goToCompare() {
  if (targetUrl.value) {
    router.go(targetUrl.value)
  }
}

</script>

<template>
  <div class="compare-button-container">
    <button class="compare-button" @click="goToCompare" title="Compare translations">
      <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M16 3l4 4-4 4"></path>
        <path d="M20 7H4"></path>
        <path d="M8 21l-4-4 4-4"></path>
        <path d="M4 17h16"></path>
      </svg>
      <span>Compare</span>
    </button>
  </div>
</template>

<style scoped>
.compare-button-container {
  display: flex;
  align-items: center;
  padding: 0 12px;
  margin: 0 4px;
  height: var(--vp-nav-height-mobile);
}

.compare-button {
  display: flex;
  align-items: center;
  gap: 6px;
  background: transparent;
  border: none;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 500;
  padding: 0;
  color: var(--vp-c-text-1);
  transition: color 0.25s, transform 0.25s;
  outline: none;
}

.compare-button:hover {
  color: var(--vp-c-brand);
  transform: scale(1.05);
}

.compare-button:active {
  transform: scale(0.95);
}

.icon {
  width: 16px;
  height: 16px;
}

@media (min-width: 768px) {
  .compare-button-container {
    height: var(--vp-nav-height);
  }
}
</style>
