---
layout: home
title: Kinh Phật Giáo Nguyên Thủy - Pali, Việt, Anh
description: Kinh nguyên thủy Nikaya gồm Kinh Trường Bộ (DN), Trung Bộ (MN), Tương Ưng Bộ (SN), Tăng Chi Bộ (AN), Tiểu Bộ (KN). Đọc song song Pali–Việt–Anh. 

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

<script setup>
const configBooks =
{
  "books": [
    {
      "id": "ud",
      "title": "Phật Tự Thuyết (ud)",
      "description": "Kinh tiểu bộ - Udāna",
      "cover": "/covers/kn-kinhtieubo.png",
      "link": "/kinhtieubo/c-pali-tmc-vi/ud/"
    },
    {
      "id": "iti",
      "title": "Phật Thuyết Như Vậy (iti)",
      "description": "Kinh tiểu bộ - Itivuttaka",
      "cover": "/covers/kn-phatthuyetnhuvay.png",
      "link": "/kinhtieubo/c-pali-tmc-vi/iti/"
    },
    {
      "id": "snp",
      "title": "Kinh Tập (snp)",
      "description": "Kinh tập - Suttanipāta",
      "cover": "/covers/kn-kinhtieubo.png",
      "link": "/kinhtieubo/c-pali-tmc-vi/snp/"
    }
  ]
}


const configKinh={
  "intro": "Này các Tỷ-kheo, hãy tự mình là ngọn đèn cho chính mình, hãy tự mình nương tựa nơi chính mình, chớ nương tựa một nơi nào khác.",
  "books": [
    {
      "id": "kinhtruongbo",
      "title": "Kinh Trường Bộ",
      "description": "Digha Nikaya",
      "cover": "/covers/kinhtruongbo.webp",
      "link": "/kinhtruongbo/"
    },
    {
      "id": "kinhtrungbo",
      "title": "Kinh Trung Bộ",
      "description": "Majjhima Nikaya",
      "cover": "/covers/kinhtrungbo.webp",
      "link": "/kinhtrungbo/"
    },
    {
      "id": "kinhtangchi",
      "title": "Kinh Tăng Chi Bộ",
      "description": "Anguttara Nikaya",
      "cover": "/covers/kinhtangchi.webp",
      "link": "/kinhtangchi/"
    },
    {
      "id": "kinhtuongung",
      "title": "Kinh Tương Ưng Bộ",
      "description": "Samyutta Nikaya",
      "cover": "/covers/kinhtuongung.webp",
      "link": "/kinhtuongung/"
    },
      {
      "id": "kinhtieubo",
      "title": "Kinh Tiểu Bộ",
      "description": "Khuddaka Nikaya",
      "cover": "/covers/kinhtieubo.webp",
      "link": "/kinhtieubo/"
    },
    {
      "id": "ducphatlichsu",
      "title": "Đức Phật Lịch Sử",
      "description": "Đức Phật Lịch Sử H.W. Schumann (1982) M. O'C. Walshe dịch sang Anh ngữ (1989) Nguyên Tâm Trần Phương Lan dịch Việt (1997)",
      "cover": "/covers/dpls-bia.webp",
      "link": "/ducphatlichsu/"
    },
    {
      "id": "the-life-of-the-buddha",
      "title": "Cuộc Đời Đức Phật",
      "description": "Cuộc Đời Đức Phật - The Life Of The Buddha",
      "cover": "/covers/the-life-of-the-buddha.webp", 
      "link": "/the-life-of-the-buddha/"
    },
     {
      "id": "giaolyvatongphai",
      "title": "PHẬT GIÁO: Khái Quát Giáo Lý Và Tông Phái",
      "description": "PHẬT GIÁO: Khái Quát Giáo Lý Và Tông Phái - Tác giả Hans Wolfgang Schumann, Georg Feuerstein dịch",
      "cover": "/covers/giaolytongphai.webp", 
      "link": "/giaolyvatongphai/"
    }
  ]
}

</script>


<HomePageLayout />


<!-- 
<BooksLayout
  title="Tìm hiểu về Phật Giáo"
  :config="configBooks"
/>

<BooksLayout
  title="Tìm hiểu về Phật Giáo"
  :config="configKinh"
/> -->



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