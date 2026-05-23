---
layout: page
title: Kinh Trung Bộ (Majjhima Nikāya)
description: Majjhima Nikāya (Kinh Trung Bộ) gồm 152 bài kinh của Đức Phật, chứa đựng những giáo lý thực hành cốt lõi về thiền định và giải thoát. Bản dịch Nanamoli-Bodhi và Thích Minh Châu.
head:
  - - script
    - type: application/ld+json
    - |

        {
        "@context": "https://schema.org",
        "@graph": [
          {
            "@type": "Book",
            "@id": "https://kinhnikaya.org/kinhtrungbo/#book",
            "mainEntityOfPage": {
              "@type": "WebPage",
              "@id": "https://kinhnikaya.org/kinhtrungbo/"
            },
            "name": "Kinh Trung Bộ",
            "alternateName": "Majjhima Nikāya",
            "numberOfChapters":34,
            "url": "https://kinhnikaya.org/kinhtrungbo/",
            "isAccessibleForFree": true,
            "publisher": { "@id": "https://kinhnikaya.org/#org" },
            "image": "https://kinhnikaya.org/covers/kinhtrungbo.webp",
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
              { "@id": "https://kinhnikaya.org/kinhtrungbo/thichminhchau/#book" },
              { "@id": "https://kinhnikaya.org/kinhtrungbo/nanamoli-bodhi-en/#book" },
              { "@id": "https://kinhnikaya.org/kinhtrungbo/nanamoli-bodhi-vi/#book" },
              { "@id": "https://kinhnikaya.org/kinhtrungbo/c-nm-tmc-vi/#book" }]
          },
          {
            "@type": "BreadcrumbList",
            "itemListElement": [
              { "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "https://kinhnikaya.org/" },
              { "@type": "ListItem", "position": 2, "name": "Kinh Trung Bộ", "item": "https://kinhnikaya.org/kinhtrungbo/"  }
            ]
          }
        ]
        }
---

<BookLayout
  title="Kinh Trung Bộ"
  description="Majjhima Nikāya - Bộ sưu tập 152 bài kinh trung bình, chứa đựng những giáo lý căn bản và quan trọng nhất về con đường giải thoát, tâm lý học Phật giáo và thực hành thiền định."
  cover="/covers/kinhtrungbo.jpeg"
>
  <template #sections>
    <!-- <div class="section-item">
      <div class="section-title"><a href="/kinhtrungbo/c-pali-tmc-vi/mucluc">Pali & Thích Minh Châu</a></div>
      <div class="section-subtitle">Đối chiếu bản dịch tiếng Việt từ tiêng Pali và tiếng Việt của Tỷ kheo Thích Minh Châu.</div>
    </div> -->
    <div class="section-item">
      <div class="section-title"><a href="/kinhtrungbo/c-nm-tmc-vi/">Thích Minh Châu & Nanamoli-Bodhi (Việt)</a></div>
      <div class="section-subtitle">Bản đọc song song của Tỷ kheo Thích Minh Châu và Bhikkhu Nanamoli & Bhikkhu Bodhi .</div>
    </div>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtrungbo/thichminhchau/">Tỷ kheo Thích Minh Châu</a></div>
      <div class="section-subtitle">Kinh Trung Bộ của Tỷ kheo Thích Minh Châu.</div>
    </div>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtrungbo/nanamoli-bodhi-vi/">Nanamoli & Bodhi (Tiếng Việt)</a></div>
      <div class="section-subtitle">Bản dịch tiếng Việt từ tác phẩm "The Middle Length Discourses Of The Buddha" của Bhikkhu Nanamoli và Bhikkhu Bodhi.</div>
    </div>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtrungbo/nanamoli-bodhi-en/">Bhikkhu Nanamoli & Bhikkhu Bodhi (English)</a></div>
      <div class="section-subtitle">"The Middle Length Discourses of the Buddha" by Nanamoli and Bodhi.</div>
    </div>
  </template>

  <div class="closing-quote">
    <blockquote>
      "Xưa cũng như nay, ta chỉ dạy một điều: Khổ và Sự Diệt Khổ."
    </blockquote>
  </div>
</BookLayout>
