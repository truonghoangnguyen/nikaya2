---
layout: home

hero:
  name: Kinh Trường Bộ | Aṅguttara Nikāya
---


<div class="hero-section">
  <div class="hero-content">
    <p class="hero-description">
      Kinh Anguttara Nikàya, dịch là Kinh Trường Bộ, là bộ thứ tư trong năm bộ kinh tạng Pali: Dìgha Nikàya (Kinh Trường Bộ), Majjhima Nikàya (Kinh Trung Bộ), Samyutta Nikàya (Kinh Tương Ưng Bộ), Anguttara Nikàya (Kinh Trường Bộ), và Khuddaka Nikàya (Kinh Tiểu Bộ).
    </p>
  </div>
</div>

## Các Bản Dịch Kinh Trường Bộ

<div class="translation-collection">
  <div class="translation-card">
    <div class="translation-header">
      <h3>Thích Minh Châu</h3>
      <span class="language-tag">Tiếng Việt</span>
    </div>
    <div class="translation-content">
      <p>Bản dịch tiếng Việt của Hòa thượng Thích Minh Châu, một trong những bản dịch Kinh Trường Bộ là bộ dịch uy tín và phổ biến nhất tại Việt Nam.</p>
      <div class="card-actions">
        <a href="/kinhtruongbo/thichminhchau/cover.html" class="primary-button">Đọc</a>
      </div>
    </div>
  </div>

  <div class="translation-card">
    <div class="translation-header">
      <h3>Bhikkhu Sujato</h3>
      <span class="language-tag">Tiếng Việt</span>
    </div>
    <div class="translation-content">
      <p>Bản dịch tiếng Việt từ tác phẩm "Numbered Discourses - A sensible translation of the Aṅguttara Nikāya" của Bhikkhu Sujato.</p>
      <div class="card-actions">
        <a href="/kinhtruongbo/sujato-vi/intro/cover.html" class="primary-button">Đọc</a>
      </div>
    </div>
  </div>

  <div class="translation-card">
    <div class="translation-header">
      <h3>Bhikkhu Sujato</h3>
      <span class="language-tag">Tiếng Anh</span>
    </div>
    <div class="translation-content">
      <p>Bản dịch tiếng Anh "Numbered Discourses - A sensible translation of the Aṅguttara Nikāya" của Bhikkhu Sujato.</p>
      <div class="card-actions">
        <a href="/kinhtruongbo/sujato-en/intro/cover.html" class="primary-button">Đọc</a>
      </div>
    </div>
  </div>
</div>

## Bản đọc song song

<div class="comparison-section">
  <p class="comparison-intro">
    Việc đọc song song các bản dịch khác nhau giúp hiểu sâu hơn về ý nghĩa của kinh điển.
  </p>

  <div class="comparison-grid">
    <div class="comparison-card">
      <div class="comparison-header">
        <h3>Thích Minh Châu & Bhikkhu Sujato</h3>
        <span class="comparison-tag">Việt Việt</span>
      </div>
      <p>Việt/Việt của Tỳ Kheo Thích Minh Châu và Bhikkhu Sujato</p>
      <a href="/kinhtruongbo/c-sujato-tmc-vi/mucluc.html" class="secondary-button">Xem So Sánh</a>
    </div>

  <div class="comparison-card">
      <div class="comparison-header">
        <h3>Thích Minh Châu & Bhikkhu Sujato</h3>
        <span class="comparison-tag">Việt - Anh</span>
      </div>
      <p>Anh/Việt của Tỳ Kheo Thích Minh Châu và Bhikkhu Sujato</p>
      <a href="/kinhtruongbo/c-sujato-tmc-en/mucluc.html" class="secondary-button">Xem So Sánh</a>
    </div>
  </div>
</div>


<div class="closing-message">
  <p>Chúc bạn có những giờ phút nghiên cứu và thực hành giáo pháp an lạc!</p>
</div>

<style>
.subtitle {
  font-size: 0.6em;
  color: var(--vp-c-text-2);
  font-weight: normal;
  margin-left: 10px;
}

.hero-section {
  background-color: var(--vp-c-bg-soft);
  border-radius: 8px;
  padding: 2rem;
  margin: 2rem 0;
  border-left: 4px solid var(--vp-c-brand);
}

.hero-description {
  font-size: 1.1rem;
  line-height: 1.6;
  margin: 0;
}

.translation-collection,
.comparison-grid,
.sutra-categories {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  margin: 1.5rem 0;
}

.translation-card,
.comparison-card,
.category-card {
  background-color: var(--vp-c-bg-soft);
  border-radius: 8px;
  padding: 1.5rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 1px solid var(--vp-c-divider);
}

.translation-card:hover,
.comparison-card:hover,
.category-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.translation-header,
.comparison-header {
  margin-bottom: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.translation-header h3,
.comparison-header h3,
.category-card h3 {
  margin: 0;
  font-size: 1.2rem;
}

.language-tag,
.comparison-tag {
  background-color: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-dark);
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
  font-size: 0.8rem;
  font-weight: 500;
}

.card-actions {
  margin-top: 1rem;
}

.primary-button,
.secondary-button,
.text-button {
  display: inline-block;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  text-decoration: none;
  font-weight: 500;
  transition: background-color 0.3s ease;
}

.primary-button {
  background-color: var(--vp-c-brand);
  color: white;
}

.primary-button:hover {
  background-color: var(--vp-c-brand-dark);
}

.secondary-button {
  background-color: var(--vp-c-bg-mute);
  color: var(--vp-c-text-1);
  border: 1px solid var(--vp-c-divider);
}

.secondary-button:hover {
  background-color: var(--vp-c-bg-soft);
}

.text-button {
  color: var(--vp-c-brand);
  padding: 0.5rem 0;
}

.text-button:hover {
  text-decoration: underline;
}

.comparison-intro {
  margin-bottom: 1.5rem;
  grid-column: 1 / -1;
}

.usage-guide {
  margin: 2rem 0;
}

.guide-step {
  display: flex;
  margin-bottom: 1.5rem;
  align-items: flex-start;
}

.step-number {
  background-color: var(--vp-c-brand);
  color: white;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  margin-right: 1rem;
  flex-shrink: 0;
}

.step-content h4 {
  margin-top: 0;
  margin-bottom: 0.5rem;
}

.closing-message {
  text-align: center;
  margin: 3rem 0 1rem;
  font-style: italic;
  color: var(--vp-c-text-2);
}

@media (max-width: 768px) {
  .translation-collection,
  .comparison-grid,
  .sutra-categories {
    grid-template-columns: 1fr;
  }

  .hero-section {
    padding: 1.5rem;
  }

  .hero-description {
    font-size: 1rem;
  }
}
</style>
