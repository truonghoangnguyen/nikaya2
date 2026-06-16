---
layout: page
title: Kinh Tiểu Bộ (Khuddaka Nikāya)
description: Khuddaka Nikāya (Kinh Tiểu Bộ) là bộ kinh thứ năm trong Năm Bộ Kinh (Nikàya) thuộc Kinh tạng Pali của Phật giáo Nam truyền (Nguyên thủy). Mặc dù mang tên là "Tiểu Bộ", đây lại là bộ kinh có số lượng tập văn bản lớn nhất với nội dung vô cùng phong phú và đa dạng bản dịch của Tỷ Kheo Thích Minh Châu và Giáo sư Trần Phương Lan.
head:
  - - script
    - type: application/ld+json
    - |

        {
        "@context": "https://schema.org",
        "@graph": [
          {
            "@type": "Book",
            "@id": "https://kinhnikaya.org/kinhtieubo/#book",
            "mainEntityOfPage": {
              "@type": "WebPage",
              "@id": "https://kinhnikaya.org/kinhtieubo/"
            },
            "name": "Kinh Tiểu Bộ",
            "alternateName": "Khuddaka Nikāya",
            "url": "https://kinhnikaya.org/kinhtieubo/",
            "isAccessibleForFree": true,
            "publisher": { "@id": "https://kinhnikaya.org/#org" },
            "image": "https://kinhnikaya.org/covers/kinhtieubo.webp",
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
           "workTranslation": [{
              "@type": "Book",
              "@id": "https://kinhnikaya.org/kinhtieubo/thichminhchau-tranphuonglan/#book",
              "name": "Kinh Tiểu Bộ (Bản dịch Thích Minh Châu & Trần Phương Lan)",
              "translator": [{
                "@type": "Person",
                "name": "Thích Minh Châu",
                "sameAs": "https://vi.wikipedia.org/wiki/Thích_Minh_Châu"
              },
              {
                "@type": "Person",
                "name": "Trần Phương Lan",
                "sameAs": "https://quangduc.com/author/about/931/gs-tran-phuong-lan"
              }
              ]
              }
            ]
          },
          {
            "@type": "BreadcrumbList",
            "itemListElement": [
              { "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "https://kinhnikaya.org/" },
              { "@type": "ListItem", "position": 2, "name": "Kinh Tiểu Bộ", "item": "https://kinhnikaya.org/kinhtieubo/"  }
            ]
          }
        ]
        }
---

<BookLayout
  title="Kinh Tiểu Bộ"
  description="Khuddaka Nikāya - Là tập kinh thứ năm và cũng là tập kinh có số lượng văn bản lớn nhất trong Năm Bộ Kinh Nikàya thuộc Kinh tạng của Phật giáo Nam truyền (Thượng tọa bộ). Dù mang tên là Tiểu Bộ (với ý nghĩa tập hợp các bài kinh ngắn hoặc đa dạng chủ đề), bộ kinh này lại đồ sộ nhất khi chứa tới 15 tập (hoặc 18 tập theo truyền thống Myanmar).Tại Việt Nam, toàn bộ Kinh Tiểu Bộ đã được cố Hòa thượng Thích Minh Châu và Giáo sư Trần Phương Lan dịch sang tiếng Việt từ nguyên tác tiếng Pali.."
  cover="/covers/kinhtieubo.webp"
>
  <template #sections>
    <div class="section-item">
      <div class="section-title"><a href="/kinhtieubo/thichminhchau/">Tỷ kheo Thích Minh Châu</a></div>
      <div class="section-subtitle">Tỷ kheo Thích Minh Châu.</div>
    </div>
  </template>

  <div class="closing-quote">
    <blockquote>
      “Ý dẫn đầu các pháp,<br>
Ý làm chủ, ý tạo;<br>
Nếu với ý ô nhiễm,<br>
Nói lên hay hành động,<br>
Khổ não bước theo sau,<br>
Như xe, chân vật kéo “.
    </blockquote>
  </div>
</BookLayout>
