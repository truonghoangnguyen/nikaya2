<script setup>
import { ref, computed, onMounted } from 'vue'
import { data as posts } from '../posts.data.js' // Đảm bảo file posts.data.js đã tồn tại

const selectedTag = ref('')

// 1. Tạo danh sách tags và đếm số bài (xử lý an toàn nếu tags bị null)
const tagsList = computed(() => {
  const map = {}
  for (const post of posts) {
    // Chỉ xử lý nếu tags là mảng
    if (Array.isArray(post.tags)) {
      for (const tag of post.tags) {
        if (!map[tag]) map[tag] = 0
        map[tag]++
      }
    }
  }
  return map
})

// 2. Lọc bài viết theo tag đang chọn
const filteredPosts = computed(() => {
  if (!selectedTag.value) return []
  // Lọc bài viết có chứa tag đang chọn
  return posts.filter(post =>

  Array.isArray(post.tags) && post.tags.includes(selectedTag.value)
  )
})

// 3. Hàm xử lý khi bấm vào tag
const toggleTag = (tag) => {
  selectedTag.value = tag
  // Cập nhật URL để share được link (ví dụ: /tags?tag=thọ...)
  const url = new URL(window.location)
  url.searchParams.set('tag', tag)
  window.history.pushState({}, '', url)
}

// 4. Kiểm tra URL khi mới vào trang (để giữ tag đã chọn khi refresh)
onMounted(() => {
  const urlParams = new URLSearchParams(window.location.search)
  const tagFromUrl = urlParams.get('tag')
  if (tagFromUrl) {
    selectedTag.value = tagFromUrl
  }
})

// Hàm format ngày tháng (tùy chọn, dùng nếu bài viết có date)
function formatDate(date) {
  if (!date) return ''
  // Kiểm tra nếu date là object do VitePress parse (có thuộc tính time)
  const d = date.time ? new Date(date.time) : new Date(date)
  return d.toLocaleDateString('vi-VN', { year: 'numeric', month: 'long', day: 'numeric' })
}
</script>

<template>
  <div class="tags-container">
    <h1 class="page-title">Danh mục Tags</h1>

    <div class="tags-cloud">
      <span
        v-for="(count, tag) in tagsList"
        :key="tag"
        class="tag-chip"
        :class="{ active: selectedTag === tag }"
        @click="toggleTag(tag)"
      >
        {{ tag }} <span class="count">{{ count }}</span>
      </span>
    </div>

    <div v-if="selectedTag" class="results-section">
      <div class="section-header">
        Bài viết thuộc tag: <span class="highlight">{{ selectedTag }}</span>
      </div>

      <div v-if="filteredPosts.length > 0" class="post-list">
        <a
          v-for="post in filteredPosts"
          :key="post.url"
          :href="post.url"
          class="post-item"
        >
          <div class="post-info">
            <div class="post-title">{{ post.title }}</div>
            <div v-if="post.date" class="post-date">
              {{ formatDate(post.date) }}
            </div>
          </div>
          <div class="post-arrow">→</div>
        </a>
      </div>

      <div v-else class="empty-state">
        Không có bài viết nào.
      </div>
    </div>

    <div v-else class="guide-text">
      Hãy chọn một từ khóa phía trên để xem bài viết.
    </div>
  </div>
</template>

<style scoped>
.tags-container {
  margin-top: 20px;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

.page-title {
  margin-bottom: 24px;
  font-size: 2em;
  font-weight: bold;
  letter-spacing: -0.5px;
}

/* --- Style cho các nút Tag --- */
.tags-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 40px;
}

.tag-chip {
  cursor: pointer;
  padding: 6px 16px;
  border-radius: 99px; /* Bo tròn kiểu viên thuốc */
  background-color: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  transition: all 0.2s ease;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  gap: 8px;
  user-select: none;
}

.tag-chip:hover {
  border-color: var(--vp-c-brand);
  color: var(--vp-c-brand);
  background-color: var(--vp-c-bg-mute);
}

.tag-chip.active {
  background-color: var(--vp-c-brand);
  color: white; /* Chữ trắng khi active */
  border-color: var(--vp-c-brand);
}

.tag-chip.active .count {
  background-color: rgba(255, 255, 255, 0.25);
  color: white;
}

.count {
  font-size: 0.75rem;
  background-color: var(--vp-c-bg-alt);
  padding: 2px 8px;
  border-radius: 10px;
  min-width: 20px;
  text-align: center;
}

/* --- Style cho danh sách bài viết kết quả --- */
.section-header {
  font-size: 1.1rem;
  margin-bottom: 20px;
  color: var(--vp-c-text-2);
}

.highlight {
  color: var(--vp-c-brand);
  font-weight: 700;
}

.post-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.post-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  background-color: var(--vp-c-bg-soft);
  text-decoration: none !important; /* Bỏ gạch chân mặc định */
  transition: all 0.25s;
}

.post-item:hover {
  border-color: var(--vp-c-brand);
  transform: translateY(-2px); /* Hiệu ứng nổi lên nhẹ */
  background-color: var(--vp-c-bg-mute);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.post-title {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--vp-c-text-1);
  margin-bottom: 4px;
}

.post-date {
  font-size: 0.85rem;
  color: var(--vp-c-text-2);
}

.post-arrow {
  font-size: 1.2rem;
  color: var(--vp-c-text-3);
  margin-left: 15px;
  transition: transform 0.2s;
}

.post-item:hover .post-arrow {
  transform: translateX(4px);
  color: var(--vp-c-brand);
}

.guide-text, .empty-state {
  color: var(--vp-c-text-2);
  font-style: italic;
  margin-top: 20px;
  text-align: center;
}
</style>