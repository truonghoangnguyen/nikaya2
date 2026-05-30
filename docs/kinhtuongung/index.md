---
layout: page
title: Kinh Tương Ưng Bộ (Saṃyutta Nikāya)
description: Saṃyutta Nikāya (Kinh Tương Ưng Bộ) gồm khoảng 2.900 bài kinh nhóm theo chủ đề, tập trung vào Duyên khởi, Ngũ uẩn, Lục nhập và Bát chánh đạo.
head:
  - - script
    - type: application/ld+json
    - |

        {
        "@context": "https://schema.org",
        "@graph": [
          {
            "@type": "Book",
            "@id": "https://kinhnikaya.org/kinhtuongung/#book",
            "mainEntityOfPage": {
              "@type": "WebPage",
              "@id": "https://kinhnikaya.org/kinhtuongung/"
            },
            "name": "Kinh Tương Ưng Bộ",
            "alternateName": "Saṃyutta Nikāya",
            "numberOfChapters":34,
            "url": "https://kinhnikaya.org/kinhtuongung/",
            "isAccessibleForFree": true,
            "publisher": { "@id": "https://kinhnikaya.org/#org" },
            "image": "https://kinhnikaya.org/covers/kinhtuongung.webp",
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
              { "@id": "https://kinhnikaya.org/kinhtuongung/thichminhchau/#book" },
              { "@id": "https://kinhnikaya.org/kinhtuongung/sujato-en/#book" },
              { "@id": "https://kinhnikaya.org/kinhtuongung/sujato-vi/#book" },
              { "@id": "https://kinhnikaya.org/kinhtuongung/c-sujato-tmc-vi/#book" }
             ]
          },
          {
            "@type": "BreadcrumbList",
            "itemListElement": [
              { "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "https://kinhnikaya.org/" },
              { "@type": "ListItem", "position": 2, "name": "Kinh Tương Ưng Bộ", "item": "https://kinhnikaya.org/kinhtuongung/"  }
            ]
          }
        ]
        }
---

<BookLayout
  title="Kinh Tương Ưng"
  description="Samyutta Nikāya - Bộ sưu tập các bài kinh được sắp xếp theo các chủ đề (tương ưng), tập trung sâu vào các giáo lý cốt lõi như Duyên khởi, Ngũ uẩn, Lục nhập và Bát chánh đạo."
  cover="/covers/kinhtuongung.webp"
>
  <template #sections>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtuongung/c-sujato-tmc-vi/">Thích Minh Châu & Bhikkhu Sujato (Việt)</a></div>
      <div class="section-subtitle">So sánh bản dịch của Tỷ kheo Thích Minh Châu và Bhikkhu Sujato.</div>
    </div>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtuongung/thichminhchau/">Tỷ kheo Thích Minh Châu</a></div>
      <div class="section-subtitle">Kinh Tương Ưng bộ - Tỷ kheo Thích Minh Châu.</div>
    </div>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtuongung/sujato-vi/">Bhikkhu Sujato (Tiếng Việt)</a></div>
      <div class="section-subtitle">Bản dịch tiếng Việt từ tác phẩm "Linked Discourses" của Bhikkhu Sujato.</div>
    </div>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtuongung/sujato-en/">Bhikkhu Sujato (English)</a></div>
      <div class="section-subtitle">The Linked Discourses of the Buddha translation by Bhikkhu Sujato.</div>
    </div>
  </template>

  <div class="closing-quote">
    <blockquote>
      "Như Lai không tranh luận với đời, chỉ có đời tranh luận với Như Lai."
    </blockquote>
  </div>
</BookLayout>
