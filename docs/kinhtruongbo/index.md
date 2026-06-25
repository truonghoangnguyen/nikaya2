---
layout: page
title: Kinh Trường Bộ (Dīgha Nikāya)
description: Dīgha Nikāya (Kinh Trường Bộ) gồm 34 bài kinh dài nhất của Đức Phật. Đọc song ngữ Pali - Việt, bản dịch Thích Minh Châu, Bhikkhu Sujato và Pali (Việt).
head:
  - - script
    - type: application/ld+json
    - |

        {
        "@context": "https://schema.org",
        "@graph": [
          {
            "@type": "WebPage",
            "@id": "https://kinhnikaya.org/kinhtruongbo/#webpage",
            "url": "https://kinhnikaya.org/kinhtruongbo/",
            "mainEntity": {
              "@id": "https://kinhnikaya.org/kinhtruongbo/#book"
            },
            "isPartOf":{"@id":"https://kinhnikaya.org/#website"}
          },
          {
            "@type": "Book",
            "@id": "https://kinhnikaya.org/kinhtruongbo/#book",
            "name": "Kinh Trường Bộ",
            "alternateName": "Dīgha Nikāya",
            "numberOfChapters": 34,
            "url": "https://kinhnikaya.org/kinhtruongbo/",
            "isAccessibleForFree": true,
            "publisher": { "@id": "https://kinhnikaya.org/#org" },
            "image": "https://kinhnikaya.org/covers/kinhtruongbo.webp",
            "author": {
              "@type": "Person",
              "name": "Gotama Buddha",
              "sameAs": "https://en.wikipedia.org/wiki/Gautama_Buddha"
            },
            "about": {
              "@type": "Thing",
              "name": "Phật giáo Nguyên thủy",
              "sameAs": "https://en.wikipedia.org/wiki/Theravada"
            },
            "workTranslation": [
              { "@id": "https://kinhnikaya.org/kinhtruongbo/thichminhchau/#book" },
              { "@id": "https://kinhnikaya.org/kinhtruongbo/sujato-en/#book" },
              { "@id": "https://kinhnikaya.org/kinhtruongbo/sujato-vi/#book" },
              { "@id": "https://kinhnikaya.org/kinhtruongbo/pali-vi/#book" },
              { "@id": "https://kinhnikaya.org/kinhtruongbo/c-sujato-tmc-vi/#book" },
              { "@id": "https://kinhnikaya.org/kinhtruongbo/c-pali-tmc-vi/#book" }]
          },
          {
            "@type": "BreadcrumbList",
            "itemListElement": [
              { "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "https://kinhnikaya.org/" },
              { "@type": "ListItem", "position": 2, "name": "Kinh Trường Bộ", "item": "https://kinhnikaya.org/kinhtruongbo/"  }
            ]
          }
        ]
        }
---

<BookLayout
  title="Kinh Trường Bộ"
  description="Dīgha Nikāya - Bộ kinh cốt lõi ghi lại những bài giảng dài nhất của Đức Phật, chứa đựng những giáo lý căn bản và sâu sắc về đạo đức, thiền định và trí tuệ."
  cover="/covers/kinhtruongbo.jpeg"
>
  <template #sections>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtruongbo/c-pali-tmc-vi/">Pali & Thích Minh Châu</a></div>
      <div class="section-subtitle">So sánh bản dịch của Tỷ kheo Thích Minh Châu và Pali-Việt.</div>
    </div>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtruongbo/c-sujato-tmc-vi/">Sujato & Thích Minh Châu</a></div>
      <div class="section-subtitle">So sánh bản dịch của Tỷ kheo Thích Minh Châu và Bhikkhu Sujato (Việt).</div>
    </div>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtruongbo/thichminhchau/">Tỷ kheo Thích Minh Châu</a></div>
      <div class="section-subtitle">Tỷ kheo Thích Minh Châu.</div>
    </div>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtruongbo/sujato-vi/">Bhikkhu Sujato (Tiếng Việt)</a></div>
      <div class="section-subtitle">Bản dịch tiếng Việt từ bản "Long Discourses" của Bhikkhu Sujato.</div>
    </div>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtruongbo/sujato-en/">Bhikkhu Sujato (English)</a></div>
      <div class="section-subtitle">The complete Dīgha Nikāya in modern English translation by Bhikkhu Sujato.</div>
    </div>
  </template>

  <div class="closing-quote">
    <blockquote>
      "Này các Tỷ-kheo, hãy tự mình là ngọn đèn cho chính mình, hãy tự mình nương tựa nơi chính mình, chớ nương tựa một nơi nào khác."
    </blockquote>
  </div>
</BookLayout>
