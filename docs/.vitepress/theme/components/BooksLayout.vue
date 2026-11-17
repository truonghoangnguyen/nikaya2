<template>
  <div class="home-container">
    <slot name="title">
      <h1 v-if="title" style="text-align: center;">{{ title }}</h1>
      <br v-if="title"><br v-if="title">
    </slot>

    <div v-if="currentQuote || currentImage" class="hero-section">
      <div class="quote-split-layout">
        <div class="quote-content-left">
          <div v-if="currentQuote" class="quote-text-wrapper">
            <p class="quote-text">"{{ currentQuote.quote }}"</p>
            <div class="quote-author">
              <span class="author-dash"></span>
              <a v-if="currentQuote.link" :href="currentQuote.link" class="author-name">
                {{ currentQuote.name || 'Xem chi tiết' }}
              </a>
              <span v-else class="author-name">{{ currentQuote.name || 'Nikaya' }}</span>
            </div>
          </div>

          <div v-if="quotesList.length > 1" class="quote-actions">
            <button @click="prevQuote" class="action-btn btn-back">
              <svg viewBox="0 0 24 24" width="18" height="18"><path fill="currentColor" d="M20 11H7.83l5.59-5.59L12 4l-8 8l8 8l1.41-1.41L7.83 13H20v-2z"/></svg>
              <span>Back</span>
            </button>
            <button @click="nextQuote" class="action-btn btn-next">
              <span>Next</span>
              <div class="sparkle-icons">
                <svg viewBox="0 0 24 24" width="14" height="14" class="sparkle-1"><path fill="currentColor" d="M12 2l2.4 7.6L22 12l-7.6 2.4L12 22l-2.4-7.6L2 12l7.6-2.4L12 2z"/></svg>
                <svg viewBox="0 0 24 24" width="10" height="10" class="sparkle-2"><path fill="currentColor" d="M12 2l2.4 7.6L22 12l-7.6 2.4L12 22l-2.4-7.6L2 12l7.6-2.4L12 2z"/></svg>
              </div>
            </button>
          </div>
        </div>

        <div v-if="currentImage" class="quote-image-right">
          <div class="image-box">
            <picture>
              <source
                v-if="currentImage400 && currentImage700"
                :srcset="`${currentImage400} 400w, ${currentImage700} 700w`"
                sizes="(max-width: 960px) 100vw, 345px"
                type="image/webp"
              />
              <img
                :src="currentFallbackImage"
                alt="Trích dẫn Kinh Nikaya"
                class="featured-img"
                width="345" height="460"
                fetchpriority="high"
                decoding="async"
              />
            </picture>
          </div>
        </div>
      </div>
    </div>

    <div v-if="booksList.length > 0" id="book-collections" class="book-collections">
      <div class="book-grid">
        <a v-for="book in booksList" :key="book.id || book.link" :href="book.link" class="book-card">
          <div class="book-cover">
            <picture>
              <source
                :srcset="`${getCoverVariant(book.cover, 300)} 300w, ${getCoverVariant(book.cover, 600)} 600w`"
                sizes="(max-width: 640px) calc(100vw - 3rem), (max-width: 960px) calc(50vw - 3rem), 300px"
                type="image/webp"
              />
              <img
                :src="getFallbackCover(book.cover)"
                :alt="book.title + ' - Kinh Nikaya-Phật Giáo Nguyên Thủy Online (Pali - Việt - Anh)'"
                width="300" height="450"
                loading="lazy"
                decoding="async"
              >
            </picture>
          </div>
          <div class="book-info">
            <h3 class="book-title">{{ book.title }}</h3>
          </div>
        </a>
      </div>
    </div>

    <slot></slot>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  title: {
    type: String,
    default: ''
  },
  config: {
    type: [Object, Array],
    default: () => ({})
  },
  books: {
    type: Array,
    default: () => []
  },
  quotes: {
    type: Array,
    default: () => []
  },
  quoteImages: {
    type: Array,
    default: () => []
  },
  interval: {
    type: Number,
    default: 10 * 60 * 1000
  }
})

const booksList = computed(() => {
  if (Array.isArray(props.config)) return props.config
  if (props.config && Array.isArray(props.config.books)) return props.config.books
  if (Array.isArray(props.books) && props.books.length > 0) return props.books
  return []
})

const quotesList = computed(() => {
  return Array.isArray(props.quotes) ? props.quotes : []
})

const quoteImagesList = computed(() => {
  return Array.isArray(props.quoteImages) ? props.quoteImages : []
})

const currentIndex = ref(0)
const currentImage = ref('')

const currentQuote = computed(() => {
  const list = quotesList.value
  if (!list || list.length === 0) return null
  return list[currentIndex.value] || list[0]
})

const currentFallbackImage = computed(() => currentImage.value)

// Responsive image variants: /quote/foo.webp → /quote/foo-400w.webp, /quote/foo-700w.webp
const currentImage400 = computed(() => {
  if (!currentImage.value) return ''
  return currentImage.value.replace(/\.webp$/, '-400w.webp')
})

const currentImage700 = computed(() => {
  if (!currentImage.value) return ''
  return currentImage.value.replace(/\.webp$/, '-700w.webp')
})

// /covers/kinhtruongbo.webp → /covers/kinhtruongbo-300w.webp
const getCoverVariant = (cover, width) => {
  if (!cover) return ''
  return cover.replace(/\.webp$/, `-${width}w.webp`)
}

const getFallbackCover = (cover) => {
  return cover
}

let intervalId = null

const updateRandomImage = () => {
  const images = quoteImagesList.value
  if (images && images.length > 0) {
    const randomIndex = Math.floor(Math.random() * images.length)
    currentImage.value = images[randomIndex]
  } else {
    currentImage.value = ''
  }
}

const nextQuote = () => {
  const list = quotesList.value
  if (!list || list.length <= 1) return
  currentIndex.value = (currentIndex.value + 1) % list.length
  updateRandomImage()
  resetInterval()
}

const prevQuote = () => {
  const list = quotesList.value
  if (!list || list.length <= 1) return
  currentIndex.value = (currentIndex.value - 1 + list.length) % list.length
  updateRandomImage()
  resetInterval()
}

const resetInterval = () => {
  if (intervalId) {
    clearInterval(intervalId)
    if (props.interval > 0 && quotesList.value.length > 1) {
      intervalId = setInterval(nextQuote, props.interval)
    }
  }
}

watch(
  () => quoteImagesList.value,
  () => {
    updateRandomImage()
  },
  { immediate: true }
)

watch(
  () => quotesList.value,
  (newQuotes) => {
    if (newQuotes && newQuotes.length > 0) {
      if (currentIndex.value >= newQuotes.length) {
        currentIndex.value = 0
      }
    } else {
      currentIndex.value = 0
    }
  }
)

onMounted(() => {
  const list = quotesList.value
  if (list && list.length > 0) {
    currentIndex.value = Math.floor(Math.random() * list.length)
  }
  updateRandomImage()
  if (props.interval > 0 && list && list.length > 1) {
    intervalId = setInterval(nextQuote, props.interval)
  }
})

onUnmounted(() => {
  if (intervalId) {
    clearInterval(intervalId)
  }
})
</script>

<style scoped>
.home-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 4rem 2rem;
}

.hero-section {
  margin-bottom: 3rem;
}

.quote-split-layout {
  display: grid;
  grid-template-columns: 2.2fr 0.6fr;
  gap: 4rem;
  align-items: center;
}

.quote-content-left {
  display: flex;
  flex-direction: column;
  gap: 2.5rem;
}

.quote-text {
  font-style: italic;
  text-align: center;
  line-height: 1.5;
  color: var(--vp-c-text-1);
  font-weight: 500;
  white-space: pre-wrap;
}

.quote-author {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 2rem;
}

.author-dash {
  width: 40px;
  height: 1px;
  background: var(--vp-c-divider);
}

.author-name {
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--vp-c-text-2);
  text-decoration: none;
  font-weight: 600;
}

.author-name:hover {
  color: var(--vp-c-brand);
}

.quote-actions {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.15rem 1.5rem;
  border-radius: 4px;
  font-size: 0.95rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border: none;
}

.btn-back {
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-2);
  border: 1px solid var(--vp-c-divider);
}

.btn-back:hover {
  background: var(--vp-c-bg-mute);
  border-color: var(--vp-c-text-3);
  transform: translateX(-4px);
}

.btn-next {
  background: #2e5a42;
  color: white;
  padding: 0.75rem 2rem;
  transition: all 0.3s ease;
}

.btn-next:hover {
  background: #3c7456;
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(46, 90, 66, 0.2);
}

.sparkle-icons {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  margin-left: 0.5rem;
}

.sparkle-1 {
  opacity: 0.9;
}

.sparkle-2 {
  opacity: 0.7;
  transform: translateY(-4px);
}

.quote-image-right {
  position: relative;
}

.image-box {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  aspect-ratio: 3 / 4;
  max-height: 460px;
  width: 100%;
  margin: 0 auto;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
}

.image-box picture,
.book-cover picture {
  display: block;
  width: 100%;
  height: 100%;
}

.featured-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s ease;
}

.image-box:hover .featured-img {
  transform: scale(1.05);
}

.book-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 3rem 2rem;
}

.book-card {
  display: flex;
  flex-direction: column;
  text-decoration: none;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  align-items: center;
}

.book-card:hover {
  transform: translateY(-8px);
}

.book-cover {
  width: 100%;
  aspect-ratio: 2 / 3;
  border-radius: 4px;
  overflow: hidden;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
  margin-bottom: 1rem;
}

.book-cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.book-info {
  text-align: center;
}

.book-title {
  font-size: 1.2rem;
  font-weight: 500;
  margin: 0.5rem 0 0;
  transition: color 0.2s ease;
}

.book-card:hover .book-title {
  color: var(--vp-c-brand);
}

@media (max-width: 960px) {
  .quote-split-layout {
    grid-template-columns: 1fr;
    gap: 3rem;
  }

  .quote-content-left {
    order: 2;
  }

  .quote-image-right {
    order: 1;
  }

  .image-box {
    max-height: 400px;
    aspect-ratio: 1 / 1;
  }

  .quote-text {
    font-size: 2rem;
  }

  .book-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 640px) {
  .book-grid {
    grid-template-columns: 1fr;
  }

  .home-container {
    padding: 2rem 1.5rem;
  }

  .quote-text {
    font-size: 1.75rem;
  }

  .quote-actions {
    flex-direction: column;
  }

  .action-btn {
    width: 100%;
    justify-content: center;
  }
}
</style>