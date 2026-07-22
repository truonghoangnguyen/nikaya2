---
layout: page
title: Kinh Trung Bộ (Majjhima Nikāya)
description: Kinh Trung Bộ (tiếng Pali Majjhima Nikāya) là bộ kinh thứ hai trong tuyển tập Năm bộ kinh Nikāya thuộc Tạng kinh của Phật giáo Nguyên thủy (Nam truyền). Bộ kinh gồm 152 bài kinh có độ dài trung bình của Đức Phật. Bản dịch của Tỷ kheo Thích Minh Châu, Bhikkhu Ñāṇamoli & Bhikkhu Bodhi (Việt) và  Bhikkhu Ñāṇamoli & Bhikkhu Bodhi (Tiếng Anh)
head:
  - - script
    - type: application/ld+json
    - |

        {
          "@context": "https://schema.org",
          "@graph": [
            {
              "@type": "CollectionPage",
              "@id": "https://kinhnikaya.org/kinhtrungbo/#webpage",
              "url": "https://kinhnikaya.org/kinhtrungbo/",
              "name": "Kinh Trung Bộ - Danh sách các bản dịch",
              "isPartOf": {
                "@id": "https://kinhnikaya.org/#website"
              },
              "breadcrumb": {
                "@id": "https://kinhnikaya.org/kinhtrungbo/#breadcrumb"
              },
              "mainEntity": {
                "@id": "https://kinhnikaya.org/kinhtrungbo/#work"
              }
            },
            {
              "@type": "BreadcrumbList",
              "@id": "https://kinhnikaya.org/kinhtrungbo/#breadcrumb",
              "itemListElement": [
                {
                  "@type": "ListItem",
                  "position": 1,
                  "name": "Trang chủ",
                  "item": "https://kinhnikaya.org/"
                },
                {
                  "@type": "ListItem",
                  "position": 2,
                  "name": "Kinh Trung Bộ",
                  "item": "https://kinhnikaya.org/kinhtrungbo/"
                }
              ]
            },
            {
              "@type": "Book",
              "@id": "https://kinhnikaya.org/kinhtrungbo/#work",
              "name": "Majjhima Nikāya",
              "description": "Kinh Trung Bộ Kinh tập hợp 152 bài kinh có độ dài vừa (khi so với Kinh Trường Bộ)",
              "alternateName": [
                "Kinh Trung Bộ",
                "Middle-length Discourses",
                "MN"
              ],
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
                {
                  "@id": "https://kinhnikaya.org/kinhtrungbo/pali-vi/#book"
                },
                {
                  "@id": "https://kinhnikaya.org/kinhtrungbo/thichminhchau/#book"
                },
                {
                  "@id": "https://kinhnikaya.org/kinhtrungbo/nanamoli-bodhi-en/#book"
                },
                {
                  "@id": "https://kinhnikaya.org/kinhtrungbo/nanamoli-bodhi-vi/#book"
                },
                {
                  "@id": "https://kinhnikaya.org/kinhtrungbo/c-nm-tmc-vi/#book"
                },
                {
                  "@id": "https://kinhnikaya.org/kinhtrungbo/c-pali-tmc-vi/#book"
                }
              ],
              "workExample": {
                "@id": "https://kinhnikaya.org/kinhtrungbo/pali/#book"
              }
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
    <div class="section-item">
      <div class="section-title"><a href="/kinhtrungbo/c-nm-tmc-vi/">Thích Minh Châu & Nanamoli-Bodhi (Việt)</a></div>
      <div class="section-subtitle">So sánh bản dịch của Tỷ kheo Thích Minh Châu và Bhikkhu Nanamoli & Bhikkhu Bodhi .</div>
    </div>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtrungbo/thichminhchau/">Tỷ kheo Thích Minh Châu</a></div>
      <div class="section-subtitle">Kinh Trung Bộ của Tỷ kheo Thích Minh Châu.</div>
    </div>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtrungbo/nanamoli-bodhi-vi/">Nanamoli & Bodhi (Tiếng Việt)</a></div>
      <div class="section-subtitle">Bản dịch tiếng Việt "The Middle Length Discourses Of The Buddha" của Bhikkhu Nanamoli và Bhikkhu Bodhi.</div>
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
