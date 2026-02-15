<template>
  <div class="home2">
    <header class="home2-hero">
      <p class="home2-eyebrow">Tủ sách trong thư mục docs</p>
      <h1>Trang Home 2</h1>
      <p class="home2-subtitle">
        Chọn một bộ kinh để mở mục lục và đọc các bản dịch.
      </p>
    </header>

    <div class="home2-grid">
      <a v-for="book in books" :key="book.slug" class="home2-card" :href="book.href">
        <div class="home2-card__frame">
          <img :src="book.cover" :alt="book.title" loading="lazy" />
        </div>
        <div class="home2-card__meta">
          <h3>{{ book.title }}</h3>
          <p class="home2-card__series">{{ book.series }}</p>
          <p class="home2-card__author">{{ book.author }}</p>
          <span class="home2-card__cta">Mở mục lục</span>
        </div>
      </a>
    </div>
  </div>
</template>

<script setup>
const books = [
  {
    slug: 'kinhtrungbo',
    title: 'Kinh Trung Bộ',
    series: 'Majjhima Nikaya',
    author: 'Nhiều bản dịch',
    href: '/kinhtrungbo/',
    cover: '/covers/kinh-trung-bo.svg'
  },
  {
    slug: 'kinhtruongbo',
    title: 'Kinh Trường Bộ',
    series: 'Digha Nikaya',
    author: 'Nhiều bản dịch',
    href: '/kinhtruongbo/',
    cover: '/covers/kinh-truong-bo.svg'
  },
  {
    slug: 'kinhtuongung',
    title: 'Kinh Tương Ưng',
    series: 'Samyutta Nikaya',
    author: 'Nhiều bản dịch',
    href: '/kinhtuongung/',
    cover: '/covers/kinh-tuong-ung.svg'
  },
  {
    slug: 'kinhtangchi',
    title: 'Kinh Tăng Chi',
    series: 'Anguttara Nikaya',
    author: 'Nhiều bản dịch',
    href: '/kinhtangchi/',
    cover: '/covers/kinh-tang-chi.svg'
  },
  {
    slug: 'kinhchude',
    title: 'Kinh Chủ Đề',
    series: 'Chủ đề chọn lọc',
    author: 'Nhiều bản dịch',
    href: '/kinhchude/',
    cover: '/covers/kinh-chu-de.svg'
  }
]
</script>

<style scoped>
.home2 {
  margin: 2rem auto 4rem;
  max-width: 1200px;
  padding: 0 1.5rem;
}

.home2-hero {
  margin-bottom: 2.5rem;
}

.home2-eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.25em;
  font-size: 0.75rem;
  color: var(--vp-c-text-3);
  margin: 0 0 0.75rem;
  /* font-family: 'Manrope', sans-serif; */
}

.home2-hero h1 {
  /* font-family: 'Crimson Text', serif; */
  font-size: clamp(2.4rem, 3vw, 3.2rem);
  margin: 0 0 0.75rem;
  color: var(--vp-c-text-1);
}

.home2-subtitle {
  margin: 0;
  font-size: 1.05rem;
  color: var(--vp-c-text-2);
  max-width: 640px;
}

.home2-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 2.5rem;
}

.home2-card {
  display: flex;
  flex-direction: column;
  text-decoration: none;
  color: inherit;
}

.home2-card__frame {
  background: #f6f4f1;
  border-radius: 16px;
  padding: 2rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 360px;
  box-shadow: 0 12px 30px rgba(20, 20, 20, 0.08);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.home2-card__frame img {
  width: 80%;
  max-width: 220px;
  height: auto;
  box-shadow: 0 12px 25px rgba(0, 0, 0, 0.25);
  border-radius: 6px;
}

.home2-card:hover .home2-card__frame {
  transform: translateY(-6px);
  box-shadow: 0 18px 36px rgba(20, 20, 20, 0.12);
}

.home2-card__meta {
  margin-top: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.home2-card__meta h3 {
  margin: 0;
  font-size: 1.3rem;
}

.home2-card__series {
  margin: 0;
  font-style: italic;
  color: var(--vp-c-text-2);
}

.home2-card__author {
  margin: 0;
  font-size: 0.95rem;
  color: var(--vp-c-text-1);
}

.home2-card__cta {
  font-weight: 600;
  font-size: 0.95rem;
  color: var(--vp-c-brand);
}

@media (max-width: 900px) {
  .home2-grid {
    gap: 2rem;
  }

  .home2-card__frame {
    min-height: 320px;
  }
}

@media (max-width: 600px) {
  .home2-card__frame {
    padding: 1.5rem 1rem;
  }
}
</style>
