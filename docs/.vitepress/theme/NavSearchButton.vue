<template>
  <div class="nav-search-button-container">
    <a href="/search" class="nav-search-button" title="Tìm kiếm" @click.prevent="goToSearch">
      <div class="search-box">
        <svg
          class="icon"
          xmlns="http://www.w3.org/2000/svg"
          width="18"
          height="18"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
        <span class="search-text">Tìm kiếm</span>
        <div class="search-keyboard">
          <kbd>⌘</kbd>
          <kbd>K</kbd>
        </div>
      </div>
    </a>
  </div>
</template>

<script setup>
import { onMounted, onUnmounted } from 'vue'
import { useRouter, useData } from 'vitepress'

const router = useRouter()
const { page } = useData()

const goToSearch = () => {
  const currentPath = window.location.pathname
  const currentFull = window.location.pathname + window.location.search + window.location.hash
  
  // Tránh lưu đè nếu đã ở trang search
  if (!currentPath.endsWith('/search') && !currentPath.endsWith('/search.html')) {
    localStorage.setItem('search-back-url', currentFull)
  }
  router.go('/search')
}

const handleKeydown = (e) => {
  // Cmd+K or Ctrl+K to go to search
  if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
    e.preventDefault()
    goToSearch()
  }
  // Esc trên trang search được SearchPage.vue tự xử lý (clear query → goBack)
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown)
})
</script>

<style scoped>
.nav-search-button-container {
  display: flex;
  align-items: center;
  padding: 0 12px;
  height: var(--vp-nav-height);
}

.nav-search-button {
  display: flex;
  align-items: center;
  text-decoration: none;
}

.search-box {
  display: flex;
  align-items: center;
  gap: 8px;
  background-color: var(--vp-c-bg-mute);
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  padding: 0 10px;
  height: 32px;
  color: var(--vp-c-text-2);
  transition: border-color 0.25s, background-color 0.25s;
  cursor: pointer;
  width: 40px;
  justify-content: center;
}

.search-box:hover {
  border-color: var(--vp-c-brand);
  background-color: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
}

.icon {
  width: 16px;
  height: 16px;
  flex-shrink: 0;
}

.search-text {
  display: none;
  font-size: 0.9rem;
  font-weight: 500;
  flex-grow: 1;
}

.search-keyboard {
  display: none;
  align-items: center;
  gap: 2px;
}

@media (min-width: 768px) {
  .search-box {
    width: 180px;
    justify-content: flex-start;
  }
  .search-text {
    display: block;
  }
  .search-keyboard {
    display: flex;
  }
}

kbd {
  font-family: inherit;
  font-size: 0.75rem;
  background-color: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 4px;
  padding: 0 4px;
  min-width: 18px;
  text-align: center;
  color: var(--vp-c-text-3);
}
</style>
