---
layout: page
title: Kinh Tương Ưng Bộ (Saṃyutta Nikāya)
description: Saṃyutta Nikāya (Kinh Tương Ưng Bộ) gồm các bài kinh được nhóm theo các chủ đề hoặc đối tượng có liên hệ với nhau (saṃyutta, "tương ưng"), giúp việc tra cứu và ghi nhớ thuận tiện hơn.
head:
  - - script
    - type: application/ld+json
    - |

        {
        "@context": "https://schema.org",
        "@graph": [
          {
            "@type": "CollectionPage",
            "@id": "https://kinhnikaya.org/kinhtuongung/#webpage",
            "url": "https://kinhnikaya.org/kinhtuongung/",
            "name": "Kinh Tương Ưng Bộ - Danh sách các bản dịch",
            "isPartOf": { "@id": "https://kinhnikaya.org/#website" },
            "breadcrumb": { "@id": "https://kinhnikaya.org/kinhtuongung/#breadcrumb" },
            "mainEntity": { "@id": "https://kinhnikaya.org/kinhtuongung/#work" }
          },
          {
            "@type": "BreadcrumbList",
            "@id": "https://kinhnikaya.org/kinhtuongung/#breadcrumb",
            "itemListElement": [
              { "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "https://kinhnikaya.org/" },
              { "@type": "ListItem", "position": 2, "name": "Kinh Tương Ưng", "item": "https://kinhnikaya.org/kinhtuongung/" }
            ]
          },
          {
            "@type": "Book",
            "@id": "https://kinhnikaya.org/kinhtuongung/#work",
            "name": "Saṃyutta Nikāya",
            "description": "Saṃyutta Nikāya (Kinh Tương Ưng Bộ) gồm các bài kinh được nhóm theo các chủ đề hoặc đối tượng có liên hệ với nhau (saṃyutta, 'tương ưng'), giúp việc tra cứu và ghi nhớ thuận tiện hơn.",
            "alternateName": [
              "Kinh Tương Ưng Bộ",
              "Linked Discourses",
              "SN"
            ],
            "creator": {
              "@type": "Person",
              "@id": "https://kinhnikaya.org/#gautama-buddha",
              "name": "Gautama Buddha",
              "alternateName": [
                "Gotama Buddha",
                "Đức Phật"
              ],
              "sameAs": "https://en.wikipedia.org/wiki/Gautama_Buddha"
            },
            "about": {
              "@type": "Thing",
              "name": "Phật giáo Nguyên thủy",
              "sameAs": "https://en.wikipedia.org/wiki/Theravada"
            },
            "workExample": {
              "@id": "https://kinhnikaya.org/kinhtuongung/pali/#book"
            },
            "workTranslation": [
              { "@id": "https://kinhnikaya.org/kinhtuongung/thichminhchau/#book" },
              { "@id": "https://kinhnikaya.org/kinhtuongung/sujato-en/#book" },
              { "@id": "https://kinhnikaya.org/kinhtuongung/sujato-vi/#book" },
              { "@id": "https://kinhnikaya.org/kinhtuongung/c-sujato-tmc-vi/#book" }
            ]
          }
        ]
        }
---

<BookLayout
  title="Kinh Tương Ưng Bộ"
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
