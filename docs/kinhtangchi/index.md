---
layout: page
title: Kinh Tăng Chi Bộ (Aṅguttara Nikāya)
description: Aṅguttara Nikāya (Kinh Tăng Chi Bộ) gồm hơn 8.000 bài kinh sắp xếp theo số lượng pháp từ 1 đến 11. Bản dịch Thích Minh Châu và Bhikkhu Sujato.
head:
  - - script
    - type: application/ld+json
    - |

        {
        "@context": "https://schema.org",
        "@graph": [
          {
            "@type": "WebPage",
            "@id": "https://kinhnikaya.org/kinhtangchi/#webpage",
            "url": "https://kinhnikaya.org/kinhtangchi/",
            "mainEntity": {
              "@id": "https://kinhnikaya.org/kinhtangchi/#book"
            },
            "isPartOf":{"@id":"https://kinhnikaya.org/#website"}
          },
          {
            "@type": "Book",
            "@id": "https://kinhnikaya.org/kinhtangchi/#book",
            "name": "Kinh Tăng Chi Bộ",
            "alternateName": "Aṅguttara Nikāya",
            "numberOfChapters": 186,
            "url": "https://kinhnikaya.org/kinhtangchi/",
            "isAccessibleForFree": true,
            "publisher": { "@id": "https://kinhnikaya.org/#org" },
            "image": "https://kinhnikaya.org/covers/kinhtangchi.webp",
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
              { "@id": "https://kinhnikaya.org/kinhtangchi/thichminhchau/#book" },
              { "@id": "https://kinhnikaya.org/kinhtangchi/sujato-en/#book" },
              { "@id": "https://kinhnikaya.org/kinhtangchi/sujato-vi/#book" },
              { "@id": "https://kinhnikaya.org/kinhtangchi/c-sujato-tmc-vi/#book" }]
          },
          {
            "@type": "BreadcrumbList",
            "itemListElement": [
              { "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "https://kinhnikaya.org/" },
              { "@type": "ListItem", "position": 2, "name": "Kinh Tăng Chi Bộ", "item": "https://kinhnikaya.org/kinhtangchi/"  }
            ]
          }
        ]
        }
---

<BookLayout
  title="Kinh Tăng Chi Bộ"
  description="Aṅguttara Nikāya - Bộ sưu tập các bài kinh được sắp xếp theo số lượng pháp từ một đến mười một, ghi lại những lời dạy súc tích và thiết thực của Đức Phật về đạo đức, đời sống gia đình và các phương pháp tu tập tâm linh."
  cover="/covers/kinhtangchi.webp"
>
  <template #sections>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtangchi/c-sujato-tmc-vi/">Thích Minh Châu & Bhikkhu Sujato (Việt)</a></div>
      <div class="section-subtitle">So sánh bản dịch của Tỷ kheo Thích Minh Châu và Bhikkhu Sujato.</div>
    </div>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtangchi/thichminhchau/">Tỷ kheo Thích Minh Châu</a></div>
      <div class="section-subtitle">Tỷ kheo Thích Minh Châu.</div>
    </div>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtangchi/sujato-vi/">Bhikkhu Sujato (Tiếng Việt)</a></div>
      <div class="section-subtitle">Bản dịch tiếng Việt từ tác phẩm "Numbered Discourses" của Bhikkhu Sujato.</div>
    </div>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtangchi/sujato-en/">Bhikkhu Sujato (English)</a></div>
      <div class="section-subtitle">Numbered Discourses - A sensible translation of the Aṅguttara Nikāya by Bhikkhu Sujato.</div>
    </div>
  </template>

  <div class="closing-quote">
    <blockquote>
      "Này các Tỷ-kheo, khó có được là sự xuất hiện của hai hạng người ở đời. Thế nào là hai? Người có lòng biết ơn và người biết đền ơn."
    </blockquote>
  </div>
</BookLayout>
