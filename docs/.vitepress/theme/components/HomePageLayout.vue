<template>
  <div class="nikaya-container">
    <div class="nikaya-sidebar">
      <h3>Bộ sưu tập Kinh</h3>
      <ul class="nikaya-sidebar-nav">
        <li class="active"><a href="#kinhtrungbo" @click.prevent="showSection('kinhtrungbo', $event)">Kinh Trung Bộ</a></li>
        <li><a href="#kinhtruongbo" @click.prevent="showSection('kinhtruongbo', $event)">Kinh Trường Bộ</a></li>
        <li><a href="#kinhtuongung" @click.prevent="showSection('kinhtuongung', $event)">Kinh Tương Ưng</a></li>
        <li><a href="#kinhtangchi" @click.prevent="showSection('kinhtangchi', $event)">Kinh Tăng Chi</a></li>
        <li><a href="#kinhtieubo" @click.prevent="showSection('kinhtieubo', $event)">Kinh Tiểu Bộ</a></li>
      </ul>

      <div class="sidebar-info">
        <h4>Về Kinh Nikaya</h4>
        <p>Kinh Nikaya là bộ sưu tập các bài giảng của Đức Phật, được bảo tồn trong truyền thống Phật giáo Nguyên thủy.</p>
        <p>Trang web này cung cấp nhiều bản dịch khác nhau để giúp bạn hiểu sâu hơn về lời dạy của Đức Phật.</p>
      </div>
    </div>

    <div class="nikaya-main" id="book-collections">
      <section id="kinhtrungbo" class="book-section active">
        <h2>Kinh Trung Bộ (Majjhima Nikaya)</h2>
        <p>Bộ sưu tập 152 bài kinh có độ dài trung bình, bao gồm nhiều chủ đề quan trọng trong giáo lý của Đức Phật.</p>

        <div class="book-grid">
          <div class="book-card">
            <div class="book-cover">
              <img src="/kinhtrungbo-tmc.jpeg" alt="Kinh Trung Bộ - Thích Minh Châu">
            </div>
            <div class="book-info">
              <h3>Thích Minh Châu</h3>
              <p>Bản dịch tiếng Việt của Hòa thượng Thích Minh Châu, một trong những bản dịch đầu tiên và phổ biến nhất.</p>
              <a href="/kinhtrungbo/thichminhchau/" class="book-link">Đọc bản dịch</a>
            </div>
          </div>

          <div class="book-card">
            <div class="book-cover">
              <img src="/Discourses-of-the-Buddha-nanamoli-bodhi.webp" alt="Kinh Trung Bộ - Nanamoli-Bodhi">
            </div>
            <div class="book-info">
              <h3>Nanamoli-Bodhi</h3>
              <p>Bản dịch tiếng Anh của Bhikkhu Nanamoli và Bhikkhu Bodhi, được đánh giá cao về tính chính xác và rõ ràng.</p>
              <a href="/kinhtrungbo/nanamoli-bodhi/" class="book-link">Đọc bản gốc</a>
            </div>
          </div>

          <div class="book-card">
            <div class="book-cover">
              <img src="/Discourses-of-the-Buddha-nanamoli-bodhi.webp" alt="Kinh Trung Bộ - Nanamoli-Bodhi (Tiếng Việt)">
            </div>
            <div class="book-info">
              <h3>Nanamoli-Bodhi (Tiếng Việt)</h3>
              <p>Bản dịch tiếng Việt từ bản tiếng Anh của Bhikkhu Nanamoli và Bhikkhu Bodhi.</p>
              <a href="/kinhtrungbo/nanamoli-bodhi-vi/" class="book-link">Đọc bản dịch</a>
            </div>
          </div>

          <div class="book-card comparison">
            <div class="book-cover comparison-cover">
              <div class="comparison-icon">
                <span>⟷</span>
              </div>
            </div>
            <div class="book-info">
              <h3>So sánh các bản dịch</h3>
              <p>Xem các bản dịch khác nhau song song để hiểu rõ hơn về nội dung và ý nghĩa của kinh.</p>
              <a href="/c/tmc-mn-tat-ca-cac-lau-hoac" class="book-link">So sánh bản dịch</a>
            </div>
          </div>
        </div>
      </section>

      <section id="kinhtruongbo" class="book-section">
        <h2>Kinh Trường Bộ (Digha Nikaya)</h2>
        <p>Bộ sưu tập 34 bài kinh dài, bao gồm nhiều chủ đề về triết học, xã hội và lịch sử.</p>

        <div class="book-grid">
          <div class="book-card">
            <div class="book-cover">
              <img src="/kinh-truong-bo.jpg" alt="Kinh Trường Bộ - Thích Minh Châu">
            </div>
            <div class="book-info">
              <h3>Thích Minh Châu</h3>
              <p>Bản dịch tiếng Việt của Hòa thượng Thích Minh Châu.</p>
              <a href="/kinhtruongbo/thichminhchau/" class="book-link">Đọc bản dịch</a>
            </div>
          </div>

          <div class="book-card">
            <div class="book-cover">
              <img src="/kinh-truong-bo.jpg" alt="Kinh Trường Bộ - Bhikkhu Bodhi (Tiếng Việt)">
            </div>
            <div class="book-info">
              <h3>Bhikkhu Bodhi (Tiếng Việt)</h3>
              <p>Bản dịch tiếng Việt từ bản tiếng Anh của Bhikkhu Bodhi.</p>
              <a href="/kinhtruongbo/bodhi-vi/" class="book-link">Đọc bản dịch</a>
            </div>
          </div>
        </div>
      </section>

      <section id="kinhtuongung" class="book-section">
        <h2>Kinh Tương Ưng (Samyutta Nikaya)</h2>
        <p>Bộ sưu tập các bài kinh được sắp xếp theo chủ đề, gồm 56 chương với hơn 2.800 bài kinh ngắn.</p>
        <div class="book-grid">
          <div class="book-card">
            <div class="book-cover">
              <img src="/kinh-truong-bo.jpg" alt="Kinh Tương Ưng - Thích Minh Châu">
            </div>
            <div class="book-info">
              <h3>Thích Minh Châu</h3>
              <p>Bản dịch tiếng Việt của Hòa thượng Thích Minh Châu.</p>
              <a href="/kinhtuongung/thichminhchau/" class="book-link">Đọc bản dịch</a>
            </div>
          </div>
        </div>
      </section>

      <section id="kinhtangchi" class="book-section">
        <h2>Kinh Tăng Chi (Anguttara Nikaya)</h2>
        <p>Bộ sưu tập các bài kinh được sắp xếp theo chủ đề, gồm 56 chương với hơn 2.800 bài kinh ngắn.</p>
        <div class="book-grid">
          <div class="book-card">
            <div class="book-cover">
              <img src="/kinh-truong-bo.jpg" alt="Kinh Tương Ưng - Thích Minh Châu">
            </div>
            <div class="book-info">
              <h3>Thích Minh Châu</h3>
              <p>Bản dịch tiếng Việt của Hòa thượng Thích Minh Châu.</p>
              <a href="/kinhtangchi/thichminhchau/" class="book-link">Đọc bản dịch</a>
            </div>
          </div>
          <div class="book-card comparison">
            <div class="book-cover comparison-cover">
              <div class="comparison-icon">
                <span>⟷</span>
              </div>
            </div>
            <div class="book-info">
              <h3>Bodhi-Thich Minh Châu </h3>
              <p>Xem các bản dịch khác nhau song song để hiểu rõ hơn về nội dung và ý nghĩa của kinh.</p>
              <a href="/kinhtangchi/c-bodhi-tmc-vi/mucluc.html" class="book-link">So sánh bản dịch</a>
            </div>
          </div>

        </div>

      </section>

      <section id="kinhtieubo" class="book-section">
        <h2>Kinh Tiểu Bộ (Khuddaka Nikaya)</h2>
        <p>Đang cập nhật...</p>
      </section>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';

function showSection(targetId, event) {

  // Remove active class from all links and add to clicked one
  document.querySelectorAll('.nikaya-sidebar-nav li').forEach(item => {
    item.classList.remove('active');
  });
  // Add active class to the parent li of the clicked link
  if (event && event.target && event.target.parentElement) {
     event.target.parentElement.classList.add('active');
  }

  // Hide all sections and show the target one
  document.querySelectorAll('.book-section').forEach(section => {
    section.classList.remove('active');
  });
  const targetElement = document.getElementById(targetId);
  if (targetElement) {
      targetElement.classList.add('active');
  }
}

// Optional: If you need to ensure the first section is shown on mount,
// although the initial template already has the active class set.
onMounted(() => {
  // Ensure the default section is active if needed
  const defaultSection = document.querySelector('.nikaya-sidebar-nav li.active a');
  if (defaultSection) {
    const targetId = defaultSection.getAttribute('href').substring(1);
    showSection(targetId, null); // Pass null for event as it's not a click
  }
});

</script>

<style scoped>
.nikaya-container {
  display: flex;
  margin-top: 2rem;
  min-height: 800px;
}

.nikaya-sidebar {
  width: 250px;
  padding: 1rem;
  /* background-color: #f8f8f8; */
  border-radius: 8px;
  margin-right: 2rem;
  position: sticky;
  top: 80px; /* Adjust based on nav height */
  align-self: flex-start;
  max-height: calc(100vh - 100px); /* Adjust based on nav height + padding */
  overflow-y: auto;
}

.nikaya-sidebar h3 {
  margin-top: 0;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid #e0e0e0;
}

.nikaya-sidebar-nav {
  list-style: none;
  padding: 0;
  margin: 1rem 0;
}

.nikaya-sidebar-nav li {
  margin-bottom: 0.5rem;
  padding: 0.5rem;
  border-radius: 4px;
  transition: background-color 0.2s;
}

.nikaya-sidebar-nav li:hover {
  /* background-color: #f0f0f0; */
}

.nikaya-sidebar-nav li.active {
  /* background-color: var(--vp-c-brand-soft); */
}

.nikaya-sidebar-nav a {
  display: block;
  color: var(--vp-c-text-1);
  text-decoration: none;
}

.sidebar-info {
  margin-top: 2rem;
  padding-top: 1rem;
  border-top: 1px solid #e0e0e0;
  font-size: 0.9rem;
}

.nikaya-main {
  flex: 1;
  padding: 1rem;
}

.book-section {
  display: none;
  margin-bottom: 3rem;
}

.book-section.active {
  display: block;
}

.book-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 2rem;
  margin-top: 1.5rem;
}

.book-card {
  display: flex;
  flex-direction: column;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  /* transition: transform 0.3s, box-shadow 0.3s; */
  /* background-color: white; */
}

/* .book-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
} */

.book-cover {
  height: 320px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  /* background-color: #f5f5f5; */
}

.book-cover img {
  /* width: 100%; */
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s;
}

.book-card:hover .book-cover img {
  transform: scale(1.05);
}

.book-info {
  padding: 1.5rem;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.book-info h3 {
  margin-top: 0;
  margin-bottom: 0.5rem;
  font-size: 1.25rem;
}

.book-info p {
  margin-bottom: 1.5rem;
  flex: 1;
  color: var(--vp-c-text-2);
}

.book-link {
  display: inline-block;
  padding: 0.5rem 1rem;
  background-color: var(--vp-c-brand);
  color: white;
  text-decoration: none;
  border-radius: 4px;
  font-weight: 500;
  transition: background-color 0.2s;
  text-align: center;
}

.book-link:hover {
  background-color: var(--vp-c-brand-dark);
}

.comparison-cover {
  background-color: var(--vp-c-brand-soft);
  display: flex;
  align-items: center;
  justify-content: center;
}

.comparison-icon {
  font-size: 4rem;
  color: var(--vp-c-brand);
}

.placeholder-cover {
  background-color: #e0e0e0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  font-weight: bold;
  color: #999;
}

@media (max-width: 768px) {
  .nikaya-container {
    flex-direction: column;
  }

  .nikaya-sidebar {
    width: 100%;
    margin-right: 0;
    margin-bottom: 2rem;
    position: static;
  }

  .book-grid {
    grid-template-columns: 1fr;
  }
}
</style>
