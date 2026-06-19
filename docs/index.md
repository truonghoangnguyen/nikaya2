---
layout: home
title: Kinh Nikaya — Đọc Kinh Phật Giáo Nguyên Thủy Online (Pali - Việt - English)
description: Đọc toàn bộ Kinh Nikaya tiếng Việt, tra cứu và so sánh song ngữ Kinh điển Nikaya, Bản dịch Thích Minh Châu, Bhikkhu Sujato, Bhikkhu Nanamobi & Bodhi  — so sánh song ngữ Pāli. Tìm kiếm bài kinh bất kỳ.
head:
  - - script
    - type: application/ld+json
    - |

        {
        "@context": "https://schema.org",
        "@graph": [
            {
            "@type": "Organization",
            "@id": "https://kinhnikaya.org/#org",
            "name": "Kinh Nikāya",
            "url": "https://kinhnikaya.org/"
            },
            {
            "@type": "WebSite",
            "@id": "https://kinhnikaya.org/#website",
            "name": "Kinh Nikāya",
            "alternateName": "Kinh Nikaya Phật giáo Nguyên thủy đọc online",
            "url": "https://kinhnikaya.org/",
            "inLanguage": "vi",
            "publisher": { "@id": "https://kinhnikaya.org/#org" },
            "hasPart": [{
                "@type": "Book",
                "@id": "https://kinhnikaya.org/kinhtruongbo/#book",
                "name": "Kinh Trường Bộ (Dīgha Nikāya)",
                "url": "https://kinhnikaya.org/kinhtruongbo/"
            },
            {
                "@type": "Book",
                "@id": "https://kinhnikaya.org/kinhtrungbo/#book",
                "name": "Kinh Trung Bộ (Majjhima Nikāya)",
            "url": "https://kinhnikaya.org/kinhtrungbo/"
            },
            {
                "@type": "Book",
                "@id": "https://kinhnikaya.org/kinhtuongungbo/#book",
                "name": "Kinh Tương Ưng Bộ (Saṃyutta Nikāya)",
                "url": "https://kinhnikaya.org/kinhtuongungbo/"
            },
            {
                "@type": "Book",
                "@id": "https://kinhnikaya.org/kinhtangchibo/#book",
                "name": "Kinh Tăng Chi Bộ (Aṅguttara Nikāya)",
                "url": "https://kinhnikaya.org/kinhtangchibo/"
            },
            {
                "@type": "Book",
                "@id": "https://kinhnikaya.org/kinhtieubo/#book",
                "name": "Kinh Tiểu Bộ (Khuddaka Nikāya)",
                "url": "https://kinhnikaya.org/kinhtieubo/"
                }
            ],
            "potentialAction": {
                "@type": "SearchAction",
                "target": {
                "@type": "EntryPoint",
                "urlTemplate": "https://kinhnikaya.org/search?q={search_term_string}"
                },
                "query-input": "required name=search_term_string"
            }
            }
        ]
        }
---

<HomePageLayout />