<template>
  <div class="book-layout">
    <div class="book-hero">
      <div class="hero-left">
        <div class="text-content">
          <h1 class="book-title">{{ title }}</h1>
          <p class="book-description" v-if="description">{{ description }}</p>
          
          <div class="sections-list">
            <slot name="sections"></slot>
          </div>
        </div>
      </div>
      <div class="hero-right">
        <div class="cover-wrapper">
          <div class="cover-container">
            <img :src="cover" :alt="title" class="book-cover-img" />
          </div>
        </div>
      </div>
    </div>
    
    <div class="additional-content">
      <slot></slot>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    default: ''
  },
  cover: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
.book-layout {
  max-width: 1152px;
  margin: 0 auto;
  padding: 48px 32px;
}

.book-hero {
  display: flex;
  flex-direction: row;
  gap: 64px;
  align-items: flex-start;
}

.hero-left {
  flex: 1;
}

.hero-right {
  flex: 0 0 400px;
  position: sticky;
  top: 100px;
}

.book-title {
  margin: 0 0 16px;
  letter-spacing: -0.02em;
  line-height: 40px;
  font-size: 32px;
  font-weight: 700;
  color: var(--vp-c-text-1);
}

@media (min-width: 768px) {
  .book-title {
    line-height: 56px;
    font-size: 48px;
  }
}

.book-description {
  margin-bottom: 48px;
  font-size: 18px;
  font-weight: 500;
  color: var(--vp-c-text-2) !important;
  line-height: 28px;
  max-width: 600px;
}

.cover-wrapper {
  width: 100%;
}

.cover-container {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: var(--vp-shadow-3);
  background-color: var(--vp-c-bg-soft);
}

.book-cover-img {
  width: 100%;
  height: auto;
  display: block;
}

.sections-list {
  display: flex;
  flex-direction: column;
  gap: 40px;
}

/* Internal Section Styles using VitePress standard variables */
:deep(.section-item) {
  border-bottom: 1px solid var(--vp-c-divider);
  padding-bottom: 24px;
}

:deep(.section-item:last-child) {
  border-bottom: none;
}

:deep(.section-title) {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 4px;
}

:deep(.section-title a) {
  color: var(--vp-c-brand);
  text-decoration: none;
  transition: opacity 0.25s;
}

:deep(.section-title a:hover) {
  opacity: 0.8;
  text-decoration: underline;
}

:deep(.section-subtitle) {
  font-size: 15px;
  color: var(--vp-c-text-2);
  line-height: 1.5;
}

/* Responsiveness */
@media (max-width: 959px) {
  .book-hero {
    flex-direction: column-reverse;
    gap: 48px;
  }

  .hero-right {
    flex: none;
    width: 100%;
    max-width: 320px;
    margin: 0 auto;
    position: static;
  }

  .hero-left {
    width: 100%;
  }
}

.additional-content {
  margin-top: 64px;
}

:deep(blockquote) {
  margin: 32px 0;
  border-left: 4px solid var(--vp-c-brand);
  padding: 16px 24px;
  background-color: var(--vp-c-bg-soft);
  font-style: italic;
  font-size: 18px;
  color: var(--vp-c-text-2);
}
</style>
