---
layout: home
title: Kinh Nikaya - Phật Giáo Nguyên Thủy Online 
description: Đoc Kinh Nikaya trọn bộ online, (Kinh Trường Bộ DN, Kinh Trung Bộ MN, Kinh Tương Ưng SN, Kinh Tăng Chi AN, Kinh Tiểu Bộ KN), Bản dịch Thích Minh Châu, Bhikkhu Sujato, Bhikkhu Nanamobi & Bodhi. Pali - Việt - Anh. Tìm kiếm bài kinh bất kỳ. 
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
            "url": "https://kinhnikaya.org/",
             "logo":{"@type":"ImageObject","url":"https://kinhnikaya.org/favicon.svg"}
            },
            {
            "@type": "WebSite",
            "@id": "https://kinhnikaya.org/#website",
            "name": "Kinh Nikāya",
            "alternateName": "Kinh Nikaya Phật giáo Nguyên thủy đọc online",
            "url": "https://kinhnikaya.org/",
            "inLanguage": ["vi"],
            "publisher": { "@id": "https://kinhnikaya.org/#org" },
            "hasPart": [{
                "@type": "Book",
                "@id": "https://kinhnikaya.org/kinhtruongbo/#book",
                "url": "https://kinhnikaya.org/kinhtruongbo/"
            },
            {
                "@type": "Book",
                "@id": "https://kinhnikaya.org/kinhtrungbo/#book",
            "url": "https://kinhnikaya.org/kinhtrungbo/"
            },
            {
                "@type": "Book",
                "@id": "https://kinhnikaya.org/kinhtuongungbo/#book",
                "url": "https://kinhnikaya.org/kinhtuongungbo/"
            },
            {
                "@type": "Book",
                "@id": "https://kinhnikaya.org/kinhtangchibo/#book",
                "url": "https://kinhnikaya.org/kinhtangchibo/"
            },
            {
                "@type": "Book",
                "@id": "https://kinhnikaya.org/kinhtieubo/#book",
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