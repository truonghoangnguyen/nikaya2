---
layout: home
title: Kinh Phật Giáo Nguyên Thủy - Pali, Việt, Anh
description: Kinh Nikaya gồm Kinh Trường Bộ (DN), Trung Bộ (MN), Tương Ưng Bộ (SN), Tăng Chi Bộ (AN), Tiểu Bộ (KN). Đọc song song Pali–Việt–Anh. 

head:
  - - script
    - type: application/ld+json
    - |

        {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "@id": "https://kinhnikaya.org/#website",
                "name": "Kinh Nikāya",
                "alternateName": "Kinh Nikaya kinh Phật giáo Nguyên thủy đọc online",
                "url": "https://kinhnikaya.org/",
                "inLanguage": "vi",
                "publisher": { "@id": "https://kinhnikaya.org/#org" },
                "potentialAction": {
                    "@type": "SearchAction",
                    "target": "https://kinhnikaya.org/search?q={search_term_string}",
                    "query-input": "required name=search_term_string"
                }
            },
            {
              "@type": "Organization",
              "@id": "https://kinhnikaya.org/#org",
              "name": "Kinh Nikāya",
              "url": "https://kinhnikaya.org/",
              "logo":{"@type":"ImageObject","url":"https://kinhnikaya.org/favicon.svg"}
            },
            {
              "@type": "CollectionPage",
              "@id": "https://kinhnikaya.org/#webpage",
              "url": "https://kinhnikaya.org/",
              "name": "Trang chủ - Danh sách Kinh Nikāya",
              "isPartOf": { "@id": "https://kinhnikaya.org/#website" },
              "hasPart": [
                {"@id": "https://kinhnikaya.org/kinhtruongbo/#work"},
                {"@id": "https://kinhnikaya.org/kinhtrungbo/#work"},
                {"@id": "https://kinhnikaya.org/kinhtuongung/#work"},
                {"@id": "https://kinhnikaya.org/kinhtangchi/#work"},
                {"@id": "https://kinhnikaya.org/kinhtieubo/#work"}
              ]
            }
        ]
        }
---

<HomePageLayout />


```
Tipiṭaka (Tam Tạng)
│
├── Vinaya Piṭaka (Vin., Tạng Luật)
│   │
│   ├── Suttavibhaṅga (Suttavib., Phân Tích Giới Luật (câu chuyện dẫn đến việc Đức Phật đặt ra giới))
│   │   ├── Pārājikapāḷi (Pār., Ba-la-di (lỗi nghiêm trọng))
│   │   └── Pācittiyapāḷi (Pāc., Ưng Đối Trị (nhóm giới còn lại))
│   │
│   ├── Khandhaka (Khand., Kiện-độ (cách tổ chức Tăng đoàn))
│   │   ├── Mahāvagga (Mv., Đại Phẩm (những sự kiện và quy định quan trọng trong giai đoạn đầu của Tăng đoàn))
│   │   └── Cullavagga (Cv., Tiểu Phẩm (quy định về quản trị và kỷ luật Tăng đoàn))
│   │
│   └── Parivāra (Pv., Phụ Tùy (hệ thống hóa và ôn tập Vinaya))
│
├── Sutta Piṭaka (Sutt., Tạng Kinh) << Chúng ta ở đây
│   ├── Dīgha Nikāya (DN, Kinh Trường Bộ)
│   ├── Majjhima Nikāya (MN, Kinh Trung Bộ)
│   ├── Saṃyutta Nikāya (SN, Kinh Tương Ưng Bộ)
│   ├── Aṅguttara Nikāya (AN, Kinh Tăng Chi Bộ)
│   └── Khuddaka Nikāya (KN, Kinh Tiểu Bộ)
│
└── Abhidhamma Piṭaka (Abhi., Tạng Vi Diệu Pháp)
```