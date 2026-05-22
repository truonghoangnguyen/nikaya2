---
layout: page
title: Kinh Trường Bộ (Dīgha Nikāya)
description: Dīgha Nikāya (Kinh Trường Bộ) gồm 34 bài kinh dài nhất của Đức Phật. Đọc song ngữ Pali - Việt, bản dịch Thích Minh Châu và Bhikkhu Sujato.
head:
  - - script
    - type: application/ld+json
    - |

        {
        "@context": "https://schema.org",
        "@graph": [
          {
            "@type": "Book",
            "@id": "https://kinhnikaya.org/kinhtruongbo/#book",
            "mainEntityOfPage": {
              "@type": "WebPage",
              "@id": "https://kinhnikaya.org/kinhtruongbo/"
            },
            "name": "Kinh Trường Bộ",
            "alternateName": "Dīgha Nikāya",
            "numberOfChapters":34,
            "url": "https://kinhnikaya.org/kinhtruongbo/",
            "isAccessibleForFree": true,
            "publisher": { "@id": "https://kinhnikaya.org/#org" },
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
      <div class="section-title"><a href="/kinhtruongbo/c-pali-tmc-vi/mucluc">Pali & Thích Minh Châu</a></div>
      <div class="section-subtitle">Đối chiếu bản dịch tiếng Việt của Hòa thượng Thích Minh Châu và Pali-Việt.</div>
    </div>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtruongbo/c-sujato-tmc-vi/mucluc">Sujato & Thích Minh Châu</a></div>
      <div class="section-subtitle">Đối chiếu bản dịch tiếng Việt của Hòa thượng Thích Minh Châu và Bhikkhu Sujato.</div>
    </div>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtruongbo/thichminhchau/cover">Hòa thượng Thích Minh Châu</a></div>
      <div class="section-subtitle">Toàn bộ Kinh Trường Bộ qua bản dịch của Hòa thượng Thích Minh Châu.</div>
    </div>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtruongbo/sujato-vi/intro/cover">Bhikkhu Sujato (Tiếng Việt)</a></div>
      <div class="section-subtitle">Bản dịch tiếng Việt từ bản Bhikkhu Sujato.</div>
    </div>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtruongbo/sujato-en/intro/cover">Bhikkhu Sujato (English)</a></div>
      <div class="section-subtitle">The complete Dīgha Nikāya in modern English translation by Bhikkhu Sujato.</div>
    </div>
  </template>

  <div class="closing-quote">
    <blockquote>
      "Này các Tỷ-kheo, hãy tự mình là ngọn đèn cho chính mình, hãy tự mình nương tựa nơi chính mình, chớ nương tựa một nơi nào khác."
    </blockquote>
  </div>
</BookLayout>
