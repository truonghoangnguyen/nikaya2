<script setup>
import { useData } from 'vitepress'

const { frontmatter } = useData()
</script>

<template>
  <div v-if="frontmatter.tags" class="doc-tags-container">
    <a
      v-for="tag in frontmatter.tags"
      :key="tag"
      :href="`/tags?tag=${encodeURIComponent(tag)}`"
      class="doc-tag-item"
    >
      {{ tag }}
    </a>
  </div>
</template>

<style scoped>
.doc-tags-container {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 12px;
  margin-bottom: 24px; /* Tạo khoảng cách với nội dung bài viết */
}

.doc-tag-item {
  display: inline-block;
  font-size: 0.8rem; /* Kích thước chữ vừa phải */
  font-weight: 500;
  padding: 4px 10px;
  border-radius: 6px;

  /* Màu sắc theo biến CSS của VitePress để hợp với Dark/Light mode */
  border: 1px solid var(--vp-c-divider);
  background-color: var(--vp-c-bg-soft);
  color: var(--vp-c-text-2);

  text-decoration: none !important; /* Bỏ gạch chân mặc định của link */
  transition: all 0.2s ease;
}

.doc-tag-item:hover {
  /* Hiệu ứng khi rê chuột */
  border-color: var(--vp-c-brand);
  color: var(--vp-c-brand);
  background-color: var(--vp-c-bg-mute);
  transform: translateY(-1px); /* Nổi lên nhẹ */
}
</style>