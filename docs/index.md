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
            "alternateName": "Kinh điển Phật giáo Nguyên thủy",
            "url": "https://kinhnikaya.org/",
            "inLanguage": "vi",
            "publisher": { "@id": "https://kinhnikaya.org/#org" },
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