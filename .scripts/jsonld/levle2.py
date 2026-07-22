"""
Sinh JSON-LD cấp Level-2 (trang danh sách bản dịch của 1 Nikāya) cho 4 trang còn lại
của kinhnikaya.org, theo đúng pattern đã dùng cho kinhtuongung/ (Saṃyutta Nikāya).

Cấu trúc mỗi trang gồm 3 node trong @graph:
  - CollectionPage (#webpage)
  - BreadcrumbList (#breadcrumb)
  - Book (#work) — bản work trừu tượng, có workTranslation trỏ tới các edition (#book)
    ở Level 3 (chưa sinh ở đây, vì mỗi edition có translator/image riêng).

CHỖ CẦN BẠN TỰ ĐIỀN / KIỂM TRA:
  - "description": placeholder TODO, tự viết mô tả ngắn cho từng bộ kinh.
  - "translations": danh sách slug thư mục bản dịch thật sự tồn tại trên site.
    Mình tạm điền theo đúng 4 bản đã dùng cho Tương Ưng Bộ
    (thichminhchau, sujato-en, sujato-vi, c-sujato-tmc-vi) — CẦN KIỂM TRA LẠI,
    vì không chắc Trường Bộ/Trung Bộ/Tăng Chi có đủ 4 bản y hệt.
  - Riêng KINH TIỂU BỘ (Khuddaka Nikāya): đây là tuyển tập nhiều tác phẩm độc lập
    (Pháp Cú, Kinh Tập, Trưởng Lão Tăng Kệ, Trưởng Lão Ni Kệ, Bổn Sanh...),
    KHÔNG giống cấu trúc "1 work – nhiều bản dịch song song" như 4 Nikāya kia.
    Mình để "translations" rỗng — nhiều khả năng bạn cần model khác
    (ví dụ hasPart trỏ tới nhiều Book con thay vì workTranslation).
    Đừng dùng thẳng output kinhtieubo.jsonld.json mà chưa xem lại phần này.
"""

import json
import os

SITE = "https://kinhnikaya.org"
WEBSITE_ID = f"{SITE}/#website"
OUT_DIR = "lev2"

NIKAYAS = [
    {
        "slug": "kinhtruongbo",
        "pali_name": "Dīgha Nikāya",
        "vi_full_name": "Kinh Trường Bộ",
        "alt_names": ["Kinh Trường Bộ", "Long Discourses", "DN"],
        "description": "Kinh Trường Bộ, bộ kinh tập hợp 34 bài kinh có độ dài lớn (khi so với Kinh Trung Bộ)",
        "translations": ["pali-vi", "thichminhchau", "sujato-en", "sujato-vi", "c-sujato-tmc-vi", "c-pali-tmc-vi"],
        "workexample": "pali"
    },
    {
        "slug": "kinhtrungbo",
        "pali_name": "Majjhima Nikāya",
        "vi_full_name": "Kinh Trung Bộ",
        "alt_names": ["Kinh Trung Bộ", "Middle-length Discourses", "MN"],
        "description": "Kinh Trung Bộ Kinh tập hợp 152 bài kinh có độ dài vừa (khi so với Kinh Trường Bộ)",
        "translations": ["pali-vi", "thichminhchau", "nanamoli-bodhi-en", "nanamoli-bodhi-vi", "c-nm-tmc-vi", "c-pali-tmc-vi"],
        "workexample": "pali"
    },
    {
        "slug": "kinhtangchi",
        "pali_name": "Aṅguttara Nikāya",
        "vi_full_name": "Kinh Tăng Chi Bộ",
        "alt_names": ["Kinh Tăng Chi Bộ", "Numbered Discourses", "AN"],
        "description": "Aṅguttara Nikāya (Kinh Tăng Chi Bộ) gồm các bài kinh được sắp xếp theo số lượng các pháp được trình bày, như một pháp, hai pháp, ba pháp... đến mười một pháp, giúp việc ghi nhớ và học tập.",
        "translations": ["thichminhchau", "sujato-en", "sujato-vi", "c-sujato-tmc-vi"],
        "workexample": "pali"
    },
    {
        "slug": "kinhtieubo",
        "pali_name": "Khuddaka Nikāya",
        "vi_full_name": "Kinh Tiểu Bộ",
        "alt_names": ["Kinh Tiểu Bộ", "Minor Collection", "KN"],
        "description": (
            "Tiểu Bộ gồm nhiều tác phẩm độc lập (Pháp Cú, Kinh Tập, "
            "Trưởng Lão Tăng Kệ...). Cân nhắc model riêng thay vì workTranslation phẳng."
        ),
        "translations": ["thichminhchau"],  # cố ý để trống — xem ghi chú đầu file
        "workexample": None
        
    },
]


def make_page(n: dict) -> dict:
    base = f"{SITE}/{n['slug']}"
    # dùng đúng vi_full_name cho breadcrumb để khỏi lệch tên như đã thấy ở kinhtuongung
    breadcrumb_label = n["vi_full_name"]

    workexample = None
    if n.get("workexample"):
        workexample = { "@id": f"{base}/{n["workexample"]}/#book"}

    work_translation = [
        {"@id": f"{base}/{slug}/#book"} for slug in n["translations"]
    ]

    work_node = {
        "@type": "Book",
        "@id": f"{base}/#work",
        "name": n["pali_name"],
        "description": n["description"],
        "alternateName": n["alt_names"],
        "author": {
            "@type": "Person",
            "name": "Gotama Buddha",
            "sameAs": "https://en.wikipedia.org/wiki/Gautama_Buddha",
        },
        "about": {
            "@type": "Thing",
            "name": "Phật giáo Nguyên thủy",
            "sameAs": "https://en.wikipedia.org/wiki/Theravada",
        },
    }
    if work_translation:
        work_node["workTranslation"] = work_translation
    if workexample:
        work_node["workExample"] = workexample

    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "CollectionPage",
                "@id": f"{base}/#webpage",
                "url": f"{base}/",
                "name": f"{n['vi_full_name']} - Danh sách các bản dịch",
                "isPartOf": {"@id": WEBSITE_ID},
                "breadcrumb": {"@id": f"{base}/#breadcrumb"},
                "mainEntity": {"@id": f"{base}/#work"},
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{base}/#breadcrumb",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Trang chủ",
                        "item": f"{SITE}/",
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": breadcrumb_label,
                        "item": f"{base}/",
                    },
                ],
            },
            work_node,
        ],
    }
    return graph


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for n in NIKAYAS:
        data = make_page(n)
        out_path = os.path.join(OUT_DIR, f"{n['slug']}.jsonld.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Đã tạo: {out_path}")


if __name__ == "__main__":
    main()