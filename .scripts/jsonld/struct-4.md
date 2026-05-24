# JSON-LD cho kinhnikaya.org — bản đầy đủ

> Mỗi khối dưới đây đặt trong một `<script type="application/ld+json">` ở `<head>` của đúng trang tương ứng.
> Các dòng `// ...` chỉ là chú thích minh họa — JSON không cho phép comment, hãy xóa chúng và liệt kê đủ 34 bài trong `hasPart`.
> Lấy Kinh Trường Bộ làm mẫu; các bộ khác (Trường Bộ, Tương Ưng…) lặp đúng khuôn này.
> "datePublished": "2026-05-16" làm ngày default, không sửa
---


Đây là kinh trường bộ, trong kinh trường bộ có 2 bản "thichminhchau" và "sujato"

// json-ld thichminhchau
{
  "@context": "https://schema.org",
  "@graph": [
      {
      "@type": "Book",
      "@id": "https://kinhnikaya.org/kinhtruongbo/thichminhchau/#book",
      "mainEntityOfPage": {
          "@type": "WebPage",
          "@id": "https://kinhnikaya.org/kinhtruongbo/thichminhchau/"
      },
      "name": "Kinh Trường Bộ — Bản dịch Tỷ kheo Thích Minh Châu",
      "bookEdition": "Bản dịch Tỷ kheo Thích Minh Châu",
      "url": "https://kinhnikaya.org/kinhtruongbo/thichminhchau/",
      "inLanguage": "vi",
      "isAccessibleForFree": true,
      "publisher": { "@id": "https://kinhnikaya.org/#org" },
      "image": "https://kinhnikaya.org/covers/kinhtruongbo.webp",
      "author": {
          "@type": "Person",
          "name": "Gotama Buddha",
          "sameAs": "https://en.wikipedia.org/wiki/Gautama_Buddha"
      },
      "translator": {
          "@type": "Person",
          "name": "Thích Minh Châu",
          "sameAs": "https://vi.wikipedia.org/wiki/Thích_Minh_Châu"
      },
      "translationOfWork": { "@id": "https://kinhnikaya.org/kinhtruongbo/#book" },
      "hasPart": [
          // tôi sẽ tự điền vào
      ]
      },
      {
      "@type": "BreadcrumbList",
      "itemListElement": [
          { "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "https://kinhnikaya.org/" },
          { "@type": "ListItem", "position": 2, "name": "Kinh Trường Bộ", "item": "https://kinhnikaya.org/kinhtruongbo/" },
          { "@type": "ListItem", "position": 3, "name": "Bản dịch Thích Minh Châu", "item": "https://kinhnikaya.org/kinhtruongbo/thichminhchau/"  }
      ]
      }
  ]
  }
// json-ld sujato
{
    "@context": "https://schema.org",
    "@graph": [
        {
        "@type": "Book",
        "@id": "https://kinhnikaya.org/kinhtruongbo/sujato-vi/#book",
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": "https://kinhnikaya.org/kinhtruongbo/sujato-vi/"
        },
        "name": "Kinh Trường Bộ — Bhikkhu Sujato (Tiếng Việt)",
        "bookEdition": "Kinh Trường Bộ Bhikkhu Sujato (Tiếng Việt)",
        "url": "https://kinhnikaya.org/kinhtruongbo/sujato-vi/",
        "inLanguage": "vi",
        "isAccessibleForFree": true,
        "publisher": { "@id": "https://kinhnikaya.org/#org" },
        "image": "https://kinhnikaya.org/covers/kinhtruongbo-sujato.webp",
        "author": {
            "@type": "Person",
            "name": "Gotama Buddha",
            "sameAs": "https://en.wikipedia.org/wiki/Gautama_Buddha"
        },
        "translator": {
            "@type": "Person",
            "name": "Bhikkhu Sujato",
            "sameAs": "https://en.wikipedia.org/wiki/Bhante_Sujato
        }
        "translationOfWork": { "@id": "https://kinhnikaya.org/kinhtruongbo/#book" },
        "hasPart": [
            // tôi sẽ tự điên vào
        ]
        },
        {
        "@type": "BreadcrumbList",
        "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "https://kinhnikaya.org/" },
            { "@type": "ListItem", "position": 2, "name": "Kinh Trường Bộ", "item": "https://kinhnikaya.org/kinhtruongbo/" },
            { "@type": "ListItem", "position": 3, "name": "Kinh Trường Bộ — Bhikkhu Sujato (Tiếng Việt)", "item": "https://kinhnikaya.org/kinhtruongbo/sujato-vi/"  }
        ]
        }
    ]
    }

Đọc sự khác biệt json-ld và viết thành python script lưu vào `.script/jsonld_layer3.ipynb`

config-ví dụ {
  'kinhtruongbo': {
    'sujato': {"name": "Kinh Trường Bộ — Bhikkhu Sujato (Tiếng Việt)}
    'thichminhchau': {"name": "Kinh Trường Bộ — Hòa thượng thích minh châu}
    ...
  'kinhtuongung': {
    'nanamoli': {"name": "Kinh trung Bộ — Bhikkhu nanamoli (Tiếng Việt)}
    'thichminhchau': {"name": "Kinh trung Bộ — Hòa thượng thích minh châu}

     những thông tin này bạn tự điền, tôi sẽ chỉnh lại nếu cần

```
để khi tôi nhập:
kinh='kinhtruongbo'
author='thichminhchau' sẽ in ra json-ld của thichminhchau,
author='sujato' sẽ in ra json-ld của sujato

## Trang chủ — `/` xong, không làm gì
```json
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
```

---

## Tầng 2 — Kinh Trường Bộ (tác phẩm trừu tượng) — `/kinhtruongbo/` xong, không làm gì

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Book",
      "@id": "https://kinhnikaya.org/kinhtruongbo/#book",
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://kinhnikaya.org/kinhtruongbo/"
      },
      "name": "Kinh Trường Bộ",
      "alternateName": "Dīgha Nikāya",
      "numberOfChapters":34,
      "url": "https://kinhnikaya.org/kinhtruongbo/",
      "isAccessibleForFree": true,
      "publisher": { "@id": "https://kinhnikaya.org/#org" },
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
        { "@id": "https://kinhnikaya.org/kinhtruongbo/thichminhchau/#book" },
        { "@id": "https://kinhnikaya.org/kinhtruongbo/sujato-en/#book" },
        { "@id": "https://kinhnikaya.org/kinhtruongbo/sujato-vi/#book" },
        { "@id": "https://kinhnikaya.org/kinhtruongbo/pali-vi/#book" },
        { "@id": "https://kinhnikaya.org/kinhtruongbo/c-sujato-tmc-vi/#book" },
        { "@id": "https://kinhnikaya.org/kinhtruongbo/c-pali-tmc-vi/#book" },
]
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "https://kinhnikaya.org/" },
        { "@type": "ListItem", "position": 2, "name": "Kinh Trường Bộ", "item": "https://kinhnikaya.org/kinhtruongbo/"  }
      ]
    }
  ]
}
```

---

## Tầng 3 — Bản dịch Thích Minh Châu — `/kinhtruongbo/thichminhchau/` xong, không làm gì

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Book",
      ;"@id": "https://kinhnikaya.org/kinhtruongbo/thichminhchau/#book",
      "mainEntityOfPage": {
        "@type": "WebPage",
      ;  "@id": "https://kinhnikaya.org/kinhtruongbo/thichminhchau/"
      },
      ;"name": "Kinh Trường Bộ — Bản dịch Thích Minh Châu",
      ;"bookEdition": "Bản dịch Thích Minh Châu",
      ;"url": "https://kinhnikaya.org/kinhtruongbo/thichminhchau/",
      ;"inLanguage": "vi",
      "isAccessibleForFree": true,
      "publisher": { "@id": "https://kinhnikaya.org/#org" },
      "author": {
        "@type": "Person",
        "name": "Gotama Buddha",
        "sameAs": "https://en.wikipedia.org/wiki/Gautama_Buddha"
      },
      "translator": {
      ;  "@type": "Person",
      ;  "name": "Thích Minh Châu",
      ;  "sameAs": "https://vi.wikipedia.org/wiki/Thích_Minh_Châu"
      },
      ;"translationOfWork": { "@id": "https://kinhnikaya.org/kinhtruongbo/#book" },
      ;"hasPart": [
        { "@id": "https://kinhnikaya.org/kinhtruongbo/thichminhchau/dn-001#chapter" }
        // ... 33 bài còn lại
      ]
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "https://kinhnikaya.org/" },
        { "@type": "ListItem", "position": 2, "name": "Kinh Trường Bộ", "item": "https://kinhnikaya.org/kinhtruongbo/" },
        { "@type": "ListItem", "position": 3, "name": "Bản dịch Thích Minh Châu", "item": "https://kinhnikaya.org/kinhtruongbo/thichminhchau/"  }
      ]
    }
  ]
}
```

---

## Tầng 3 — Bản dịch Sujato — `/kinhtruongbo/sujato-en/` xong, không làm gì

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Book",
      "@id": "https://kinhnikaya.org/kinhtruongbo/sujato-en/#book",
      "name": "Dīgha Nikāya — Sujato translation",
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://kinhnikaya.org/kinhtruongbo/sujato-en/"
      },
      "bookEdition": "Sujato translation",
      "url": "https://kinhnikaya.org/kinhtruongbo/sujato-en/",
      "inLanguage": "en",
      "isAccessibleForFree": true,
      "publisher": { "@id": "https://kinhnikaya.org/#org" },
      "author": {
        "@type": "Person",
        "name": "Gotama Buddha",
        "sameAs": "https://en.wikipedia.org/wiki/Gautama_Buddha"
      },
      "translator": {
        "@type": "Person",
        "name": "Bhikkhu Sujato",
        "sameAs": "https://en.wikipedia.org/wiki/Bhante_Sujato
      }
      "translationOfWork": { "@id": "https://kinhnikaya.org/kinhtruongbo/#book" },
      "hasPart": [
        { "@id": "https://kinhnikaya.org/kinhtruongbo/sujato-en/dn-001#chapter" }
        // ... 33 bài còn lại
      ]
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "https://kinhnikaya.org/" },
        { "@type": "ListItem", "position": 2, "name": "Kinh Trường Bộ", "item": "https://kinhnikaya.org/kinhtruongbo/" },
        { "@type": "ListItem", "position": 3, "name": "Bản dịch Sujato", "item": "https://kinhnikaya.org/kinhtruongbo/sujato-en/" }
      ]
    }
  ]
}
```

---

## Tầng 3 — Bản So sánh Sujato - Thích Minh Châu — `/kinhtruongbo/c-sujato-tmc-vi/` xong, không làm gì

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Book",
      "@id": "https://kinhnikaya.org/kinhtruongbo/c-sujato-tmc-vi/#book",
      "name": "Bản So sánh Kinh Trường Bộ Sujato-Thích Minh Châu",
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://kinhnikaya.org/kinhtruongbo/c-sujato-tmc-vi/"
      },
      "bookEdition": "Sujato translation",
      "url": "https://kinhnikaya.org/kinhtruongbo/c-sujato-tmc-vi/",
      "inLanguage": "vi",
      "isAccessibleForFree": true,
      "publisher": { "@id": "https://kinhnikaya.org/#org" },
      "author": {
        "@type": "Person",
        "name": "Gotama Buddha",
        "sameAs": "https://en.wikipedia.org/wiki/Gautama_Buddha"
      },
      "translator": [
        { "@type": "Person", "name": "Bhikkhu Sujato" },
        { "@type": "Person", "name": "Thích Minh Châu" }
      ],

      "translationOfWork": { "@id": "https://kinhnikaya.org/kinhtruongbo/#book" },
      "hasPart": [
        { "@id": "https://kinhnikaya.org/kinhtruongbo/c-sujato-tmc-vi/dn-001#chapter" }
        // ... 33 bài còn lại
      ]
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "https://kinhnikaya.org/" },
        { "@type": "ListItem", "position": 2, "name": "Kinh Trường Bộ", "item": "https://kinhnikaya.org/kinhtruongbo/" },
        { "@type": "ListItem", "position": 3, "name": "Bản dịch Sujato", "item": "https://kinhnikaya.org/kinhtruongbo/c-sujato-tmc-vi/" }
      ]
    }
  ]
}
```
---

## Tầng 4 — Bài kinh TMC — `/kinhtruongbo/thichminhchau/dn-001`

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://kinhnikaya.org/kinhtruongbo/thichminhchau/dn-001",
      "url": "https://kinhnikaya.org/kinhtruongbo/thichminhchau/dn-001",
      "name": "DN 1. Kinh Phạm Võng — Bản dịch Thích Minh Châu",
      "inLanguage": "vi",
      "datePublished": "2026-05-16",
      "dateModified": "2026-05-20",
      "isPartOf": { "@id": "https://kinhnikaya.org/#website" },
      "mainEntity": { "@id": "https://kinhnikaya.org/kinhtruongbo/thichminhchau/dn-001#chapter" }
    },
    {
      "@type": ["Chapter", "ScholarlyArticle"],
      "@id": "https://kinhnikaya.org/kinhtruongbo/thichminhchau/dn-001#chapter",
      "name": "DN 1. Kinh Phạm Võng",
      "alternateName": "Brahmajālasutta",
      "position": 1,
      "url": "https://kinhnikaya.org/kinhtruongbo/thichminhchau/dn-001",
      "inLanguage": "vi",
      "translator": { "@type": "Person", "name": "Thích Minh Châu" },
      "isPartOf": { "@id": "https://kinhnikaya.org/kinhtruongbo/thichminhchau/#book" }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "https://kinhnikaya.org/" },
        { "@type": "ListItem", "position": 2, "name": "Kinh Trường Bộ", "item": "https://kinhnikaya.org/kinhtruongbo/" },
        { "@type": "ListItem", "position": 3, "name": "Bản dịch Thích Minh Châu", "item": "https://kinhnikaya.org/kinhtruongbo/thichminhchau/" },
        { "@type": "ListItem", "position": 4, "name": "DN 1. Kinh Phạm Võng", "item": "https://kinhnikaya.org/kinhtruongbo/thichminhchau/dn-001"  }
      ]
    }
  ]
}
```

---

## Tầng 4 — Bài kinh Sujato — `/kinhtruongbo/sujato-en/dn-001`

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://kinhnikaya.org/kinhtruongbo/sujato-en/dn-001",
      "url": "https://kinhnikaya.org/kinhtruongbo/sujato-en/dn-001",
      "name": "DN 1. The Divine Net Brahmajālasutta",
      "inLanguage": "en",
      "datePublished": "2026-05-16",
      "dateModified": "2026-05-20",
      "isPartOf": { "@id": "https://kinhnikaya.org/#website" },
      "mainEntity": { "@id": "https://kinhnikaya.org/kinhtruongbo/sujato-en/dn-001#chapter" }
    },
    {
      "@type": ["Chapter", "ScholarlyArticle"],
      "@id": "https://kinhnikaya.org/kinhtruongbo/sujato-en/dn-001#chapter",
      "name": "DN 1. The Divine Net Brahmajālasutta",
      "alternateName": "Brahmajālasutta",
      "position": 1,
      "url": "https://kinhnikaya.org/kinhtruongbo/sujato-en/dn-001",
      "inLanguage": "en",
      "translator": { "@type": "Person", "name": "Bhikkhu Sujato" },
      "isPartOf": { "@id": "https://kinhnikaya.org/kinhtruongbo/sujato-en/#book" }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "https://kinhnikaya.org/" },
        { "@type": "ListItem", "position": 2, "name": "Kinh Trường Bộ", "item": "https://kinhnikaya.org/kinhtruongbo/" },
        { "@type": "ListItem", "position": 3, "name": "Sujato translation", "item": "https://kinhnikaya.org/kinhtruongbo/sujato-en/" },
        { "@type": "ListItem", "position": 4, "name": "DN 1. The Divine Net Brahmajālasutta", "item": "https://kinhnikaya.org/kinhtruongbo/sujato-en/dn-001"}
      ]
    }
  ]
}
```

---

## Tầng 4 — Bài kinh đối chiếu — `/kinhtruongbo/c-sujato-tmc-vi/dnc-001`

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://kinhnikaya.org/kinhtruongbo/c-sujato-tmc-vi/dnc-001",
      "url": "https://kinhnikaya.org/kinhtruongbo/c-sujato-tmc-vi/dnc-001",
      "name": "DNC 1. So sánh — Kinh Phạm Võng",
      "inLanguage": "vi",
      "datePublished": "2026-05-16",
      "dateModified": "2026-05-20",
      "isPartOf": { "@id": "https://kinhnikaya.org/#website" },
      "mainEntity": { "@id": "https://kinhnikaya.org/kinhtruongbo/c-sujato-tmc-vi/dnc-001#chapter" }
    },
    {
      "@type": ["Chapter", "ScholarlyArticle"],
      "@id": "https://kinhnikaya.org/kinhtruongbo/c-sujato-tmc-vi/dnc-001#chapter",
      "name": "DNC 1. So sánh — Kinh Phạm Võng",
      "alternateName": "Brahmajālasutta",
      "position": 1,
      "url": "https://kinhnikaya.org/kinhtruongbo/c-sujato-tmc-vi/dnc-001",
      "inLanguage":"vi",
      "isPartOf": { "@id": "https://kinhnikaya.org/kinhtruongbo/c-sujato-tmc-vi/#book" },
      "isBasedOn": [
        { "@id": "https://kinhnikaya.org/kinhtruongbo/thichminhchau/dn-001#chapter" },
        { "@id": "https://kinhnikaya.org/kinhtruongbo/sujato-en/dn-001#chapter" }
      ]
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "https://kinhnikaya.org/" },
        { "@type": "ListItem", "position": 2, "name": "Kinh Trường Bộ", "item": "https://kinhnikaya.org/kinhtruongbo/" },
        { "@type": "ListItem", "position": 3, "name": "Bản đối chiếu Sujato–Thích Minh Châu", "item": "https://kinhnikaya.org/kinhtruongbo/c-sujato-tmc-vi/" },
        { "@type": "ListItem", "position": 4, "name": "DNC 1. So sánh — Kinh Phạm Võng", "item": "https://kinhnikaya.org/kinhtruongbo/c-sujato-tmc-vi/dnc-001"}
      ]
    }
  ]
}
```
