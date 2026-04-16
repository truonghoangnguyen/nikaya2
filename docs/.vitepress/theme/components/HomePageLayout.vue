<template>
  <div class="home-container">
    <div class="hero-section">
      <p class="intro-text">{{ config.intro }}</p>
    </div>

    <div id="book-collections" class="book-collections">
      <div class="book-grid">
        <a v-for="book in config.books" :key="book.id" :href="book.link" class="book-card">
          <div class="book-cover">
            <img :src="book.cover" :alt="book.title">
          </div>
          <div class="book-info">
            <h3 class="book-title">{{ book.title }}</h3>
          </div>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
import config from '../../../books.config.json'
</script>

<style scoped>
.home-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 4rem 2rem;
  /* font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif; */
}

.hero-section {
  text-align: center;
  max-width: 800px;
  margin: 0 auto 4rem;
}

.intro-text {
  font-size: 1.25rem;
  line-height: 1.8;
  color: var(--vp-c-text-2);
  font-style: italic;
  font-weight: 300;
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
  .book-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 640px) {
  .book-grid {
    grid-template-columns: 1fr;
  }

  .home-container {
    padding: 2rem 1rem;
  }
}
</style>
