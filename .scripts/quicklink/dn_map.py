import re
dn_pali={
  "1": {
    "title": "DN 1. KINH LƯỚI TRỜI",
    "slug": "dn-001-kinh-luoi-troi",
    "children": [
      "1",
      "2",
      "2.1",
      "2.2",
      "2.3",
      "3",
      "3.1",
      "3.1.1",
      "3.1.2",
      "3.1.3",
      "3.1.4",
      "3.1.5",
      "3.2",
      "3.2.1",
      "3.2.2",
      "3.2.3",
      "3.2.4",
      "3.2.5",
      "4",
      "4.1",
      "4.2",
      "4.3",
      "4.4",
      "5"
    ]
  },
  "2": {
    "title": "DN 2. KINH VỀ THÀNH QUẢ CỦA NGƯỜI TU HÀNH",
    "slug": "dn-002-kinh-ve-thanh-qua-cua-nguoi-tu-hanh",
    "children": [
      "1",
      "2",
      "3",
      "3.1",
      "3.2",
      "3.3",
      "3.4",
      "3.5",
      "3.6",
      "4",
      "4.1",
      "4.2",
      "4.3",
      "4.3.1",
      "4.3.1.1",
      "4.3.1.2",
      "4.3.1.3",
      "4.3.2",
      "4.3.2.1",
      "4.3.2.2",
      "4.3.2.3",
      "4.3.2.4",
      "4.3.2.5",
      "4.3.2.6",
      "4.3.2.7",
      "4.3.2.8",
      "4.3.3",
      "4.3.3.1",
      "4.3.3.2",
      "4.3.3.3",
      "4.3.3.4",
      "4.3.3.5",
      "4.3.3.6",
      "4.3.3.7",
      "4.3.3.8",
      "5"
    ]
  },
  "3": {
    "title": "DN 3. KINH AMBAṬṬHA",
    "slug": "dn-003-kinh-ambattha",
    "children": [
      "1",
      "2",
      "2.1",
      "2.2",
      "2.3",
      "2.4",
      "2.5",
      "3",
      "4",
      "5",
      "6",
      "7",
      "8",
      "9"
    ]
  },
  "4": {
    "title": "DN 4. KINH SOṆADAṆḌA",
    "slug": "dn-004-kinh-sonadanda",
    "children": [
      "1",
      "2",
      "3",
      "4",
      "5",
      "6",
      "7"
    ]
  },
  "5": {
    "title": "DN 5. KINH KŪṬADANTA",
    "slug": "dn-005-kinh-kutadanta",
    "children": [
      "1",
      "2",
      "3",
      "4",
      "4.1",
      "4.2",
      "4.3",
      "4.4",
      "4.5",
      "4.6",
      "5",
      "6",
      "7"
    ]
  },
  "6": {
    "title": "DN 6. KINH MAHĀLI",
    "slug": "dn-006-kinh-mahali",
    "children": [
      "1",
      "2",
      "2.1",
      "2.2",
      "2.3",
      "2.4"
    ]
  },
  "7": {
    "title": "DN 7. KINH JĀLIYA",
    "slug": "dn-007-kinh-jaliya",
    "children": []
  },
  "8": {
    "title": "DN 8. KINH TIẾNG GẦM SƯ TỬ",
    "slug": "dn-008-kinh-tieng-gam-su-tu",
    "children": [
      "1",
      "2",
      "3",
      "4",
      "5",
      "6",
      "7"
    ]
  },
  "9": {
    "title": "DN 9. KINH POṬṬHAPĀDA",
    "slug": "dn-009-kinh-potthapada",
    "children": [
      "1",
      "1.1",
      "1.2",
      "1.3",
      "2",
      "2.1",
      "2.2",
      "2.3"
    ]
  },
  "10": {
    "title": "DN 10. KINH SUBHA",
    "slug": "dn-010-kinh-subha",
    "children": [
      "1",
      "2",
      "3"
    ]
  },
  "11": {
    "title": "DN 11. KINH KEVAṬṬA",
    "slug": "dn-011-kinh-kevatta",
    "children": [
      "1",
      "2",
      "3",
      "4",
      "4.1"
    ]
  },
  "12": {
    "title": "DN 12. KINH LOHICCA",
    "slug": "dn-012-kinh-lohicca",
    "children": [
      "1",
      "2",
      "3"
    ]
  },
  "13": {
    "title": "DN 13. KINH TEVIJJA (Kinh Ba Minh)",
    "slug": "dn-013-kinh-tevijja-kinh-ba-minh",
    "children": [
      "1",
      "2",
      "2.1",
      "2.2",
      "2.3",
      "3",
      "4"
    ]
  },
  "14": {
    "title": "DN 14. KINH DÀI VỀ NGUỒN GỐC",
    "slug": "dn-014-kinh-dai-ve-nguon-goc",
    "children": [
      "1",
      "2",
      "3",
      "4",
      "5",
      "6",
      "7",
      "8",
      "9",
      "10",
      "11",
      "12",
      "13",
      "14",
      "15",
      "16",
      "17"
    ]
  },
  "15": {
    "title": "DN 15. KINH DÀI VỀ QUAN HỆ PHỤ THUỘC",
    "slug": "dn-015-kinh-dai-ve-quan-he-phu-thuoc",
    "children": [
      "1",
      "2",
      "3",
      "4",
      "5",
      "6"
    ]
  },
  "16": {
    "title": "DN 16. KINH DÀI VỀ BÁT-NIẾT-BÀN",
    "slug": "dn-016-kinh-dai-ve-bat-niet-ban",
    "children": [
      "1",
      "2",
      "3",
      "4",
      "5",
      "6",
      "7",
      "8",
      "9",
      "10",
      "11",
      "12",
      "13",
      "14",
      "15",
      "16",
      "17",
      "18",
      "19",
      "20",
      "21",
      "22",
      "23",
      "24",
      "25",
      "26",
      "27",
      "28",
      "29",
      "30",
      "31",
      "32",
      "33",
      "34",
      "35",
      "36",
      "37",
      "38",
      "39",
      "40"
    ]
  },
  "17": {
    "title": "DN 17. KINH ĐẠI THIỆN KIẾN VƯƠNG",
    "slug": "dn-017-kinh-ai-thien-kien-vuong",
    "children": [
      "1",
      "2",
      "2.1",
      "2.2",
      "2.3",
      "2.4",
      "2.5",
      "2.6",
      "2.7",
      "3",
      "4",
      "5",
      "6",
      "7",
      "8"
    ]
  },
  "18": {
    "title": "DN 18. KINH JANAVASABHA",
    "slug": "dn-018-kinh-janavasabha",
    "children": [
      "1",
      "2",
      "3",
      "4",
      "5",
      "6",
      "7",
      "8",
      "9"
    ]
  },
  "19": {
    "title": "DN 19. KINH DÀI VỀ GOVINDA",
    "slug": "dn-019-kinh-dai-ve-govinda",
    "children": [
      "1",
      "2",
      "3",
      "4",
      "5",
      "6",
      "6.1",
      "6.2",
      "6.3",
      "6.4",
      "6.5",
      "6.6",
      "6.7",
      "6.8"
    ]
  },
  "20": {
    "title": "DN 20. KINH ĐẠI HỘI",
    "slug": "dn-020-kinh-ai-hoi",
    "children": [
      "1"
    ]
  },
  "21": {
    "title": "DN 21. KINH SAKKAPAÑHA (ĐẾ THÍCH SỞ VẤN)",
    "slug": "dn-021-kinh-sakkapanha-e-thich-so-van",
    "children": [
      "1",
      "2",
      "2.1",
      "2.2",
      "2.3",
      "2.4",
      "2.5"
    ]
  },
  "22": {
    "title": "DN 22. KINH DÀI VỀ BỐN NƠI CHÚ TÂM",
    "slug": "dn-022-kinh-dai-ve-bon-noi-chu-tam",
    "children": [
      "1",
      "1.1",
      "1.2",
      "1.3",
      "1.4",
      "1.5",
      "1.6",
      "2",
      "3",
      "4",
      "4.1",
      "4.2",
      "4.3",
      "4.4",
      "4.5",
      "4.5.1",
      "4.5.2",
      "4.5.3",
      "4.5.4"
    ]
  },
  "23": {
    "title": "DN 23. KINH Pāyāsi",
    "slug": "dn-023-kinh-payasi",
    "children": [
      "1",
      "2",
      "2.1",
      "2.2",
      "2.3",
      "2.4",
      "2.5",
      "2.6",
      "2.7",
      "2.8",
      "2.9",
      "2.10",
      "2.11",
      "2.12",
      "2.13",
      "2.14",
      "3",
      "4",
      "5",
      "6"
    ]
  },
  "24": {
    "title": "DN 24. KINH PĀTHIKA",
    "slug": "dn-024-kinh-pathika",
    "children": [
      "1",
      "2",
      "3",
      "4",
      "5",
      "6"
    ]
  },
  "25": {
    "title": "DN 25. KINH UDUMBARIKA",
    "slug": "dn-025-kinh-udumbarika",
    "children": [
      "1",
      "2",
      "2.1",
      "2.2",
      "2.3",
      "2.4",
      "3",
      "4",
      "5",
      "6"
    ]
  },
  "26": {
    "title": "DN 26. KINH VUA CHUYỂN LUÂN",
    "slug": "dn-026-kinh-vua-chuyen-luan",
    "children": [
      "1",
      "2",
      "2.1",
      "2.2",
      "3",
      "4",
      "5",
      "6",
      "7",
      "8",
      "9"
    ]
  },
  "27": {
    "title": "DN 27. KINH VỀ NGUỒN GỐC TỐI SƠ",
    "slug": "dn-027-kinh-ve-nguon-goc-toi-so",
    "children": [
      "1",
      "2",
      "3",
      "4",
      "5",
      "6",
      "7",
      "8",
      "9",
      "10",
      "11",
      "12",
      "13",
      "14",
      "15"
    ]
  },
  "28": {
    "title": "DN 28. KINH NIỀM TIN TRONG SÁNG",
    "slug": "dn-028-kinh-niem-tin-trong-sang",
    "children": [
      "1",
      "1.1",
      "1.2",
      "1.3",
      "1.4",
      "1.5",
      "1.6",
      "1.7",
      "1.8",
      "1.9",
      "1.10",
      "1.11",
      "1.12",
      "1.13",
      "1.14",
      "1.15",
      "1.16",
      "1.17",
      "2"
    ]
  },
  "29": {
    "title": "DN 29. KINH RÕ RÀNG VÀ MẠCH LẠC",
    "slug": "dn-029-kinh-ro-rang-va-mach-lac",
    "children": [
      "1",
      "2",
      "3",
      "4",
      "5",
      "6",
      "7",
      "8",
      "9",
      "10",
      "11",
      "12",
      "13",
      "14",
      "15",
      "16"
    ]
  },
  "30": {
    "title": "DN 30. KINH ĐẶC ĐIỂM",
    "slug": "dn-030-kinh-ac-iem",
    "children": [
      "1",
      "2",
      "6",
      "11",
      "12",
      "13",
      "14",
      "20",
      "23",
      "30"
    ]
  },
  "31": {
    "title": "DN 31. KINH SIṄGĀLA",
    "slug": "dn-031-kinh-singala",
    "children": [
      "1",
      "2",
      "3",
      "4",
      "5",
      "6",
      "7",
      "8",
      "9",
      "10",
      "11",
      "12",
      "13"
    ]
  },
  "32": {
    "title": "DN 32. KINH ĀṬĀNĀṬIYA",
    "slug": "dn-032-kinh-atanatiya",
    "children": [
      "1",
      "2"
    ]
  },
  "33": {
    "title": "DN 33. KINH TỤNG ĐỌC CÙNG NHAU",
    "slug": "dn-033-kinh-tung-oc-cung-nhau",
    "children": [
      "1",
      "2",
      "3",
      "4",
      "5",
      "6",
      "7",
      "8",
      "9",
      "10"
    ]
  },
  "34": {
    "title": "DN 34. KINH MƯỜI PHÁP",
    "slug": "dn-034-kinh-den-muoi",
    "children": [
      "1",
      "2",
      "3",
      "4",
      "5",
      "6",
      "7",
      "8",
      "9",
      "10"
    ]
  }
}

dn_tmc ={
  "1": {
    "title": "1. KINH PHẠM VÕNG",
    "slug": "dn-001-kinh-pham-vong",
    "children": []
  },
  "2": {
    "title": "2. KINH SA MÔN QỦA",
    "slug": "dn-002-kinh-sa-mon-qua",
    "children": []
  },
  "3": {
    "title": "3. KINH AMBATTHA (A-MA-TRÚ)",
    "slug": "dn-003-kinh-ambattha-a-ma-tru",
    "children": []
  },
  "4": {
    "title": "4. KINH SONADANDA (CHỦNG ÐỨC)",
    "slug": "dn-004-kinh-sonadanda-chung-duc",
    "children": []
  },
  "5": {
    "title": "5. KINH KÙTADANTA (CỨU-LA-ÐÀN-ÐẦU)",
    "slug": "dn-005-kinh-kutadanta-cuu-la-dan-dau",
    "children": []
  },
  "6": {
    "title": "6. KINH MAHÀLI",
    "slug": "dn-006-kinh-mahali",
    "children": []
  },
  "7": {
    "title": "7. KINH JÀLIYA",
    "slug": "dn-007-kinh-jaliya",
    "children": []
  },
  "8": {
    "title": "8. KINH CA-DIẾP SƯ TỬ HỐNG",
    "slug": "dn-008-kinh-ca-diep-su-tu-hong",
    "children": []
  },
  "9": {
    "title": "9. KINH POTTHAPÀDA (BỐ-SÁ-BÀ-LÂU)",
    "slug": "dn-009-kinh-potthapada-bo-sa-ba-lau",
    "children": []
  },
  "10": {
    "title": "10. KINH SUBHA (TU-BÀ)",
    "slug": "dn-010-kinh-subha-tu-ba",
    "children": []
  },
  "11": {
    "title": "11. KINH KEVADDHA (KIÊN CỐ)",
    "slug": "dn-011-kinh-kevaddha-kien-co",
    "children": []
  },
  "12": {
    "title": "12. KINH LOHICCA (LÔ-HI-GIA)",
    "slug": "dn-012-kinh-lohicca-lo-hi-gia",
    "children": []
  },
  "13": {
    "title": "13. KINH TEVIJJA (TAM MINH)",
    "slug": "dn-013-kinh-tevijja-tam-minh",
    "children": []
  },
  "14": {
    "title": "14. KINH ÐẠI BỔN",
    "slug": "dn-014-kinh-dai-bon",
    "children": []
  },
  "15": {
    "title": "15. KINH ÐẠI DUYÊN",
    "slug": "dn-015-kinh-dai-duyen",
    "children": []
  },
  "16": {
    "title": "16. KINH ÐẠI BÁT NIẾT BÀN",
    "slug": "dn-016-kinh-dai-bat-niet-ban",
    "children": []
  },
  "17": {
    "title": "17. KINH ÐẠI THIỆN KIẾN VƯƠNG",
    "slug": "dn-017-kinh-dai-thien-kien-vuong",
    "children": []
  },
  "18": {
    "title": "18. KINH XA-NI-SA",
    "slug": "dn-018-kinh-xa-ni-sa",
    "children": []
  },
  "19": {
    "title": "19. KINH ÐẠI ÐIỂN TÔN",
    "slug": "dn-019-kinh-dai-dien-ton",
    "children": []
  },
  "20": {
    "title": "20. KINH ÐẠI HỘI",
    "slug": "dn-020-kinh-dai-hoi",
    "children": []
  },
  "21": {
    "title": "21. KINH ÐẾ-THÍCH SỞ VẤN",
    "slug": "dn-021-kinh-de-thich-so-van",
    "children": []
  },
  "22": {
    "title": "22. KINH ÐẠI NIỆM XỨ",
    "slug": "dn-022-kinh-dai-niem-xu",
    "children": []
  },
  "23": {
    "title": "23. KINH TỆ-TÚC",
    "slug": "dn-023-kinh-te-tuc",
    "children": []
  },
  "24": {
    "title": "24. KINH BA-LÊ",
    "slug": "dn-024-kinh-ba-le",
    "children": []
  },
  "25": {
    "title": "25. KINH ƯU-ÐÀM-BÀ-LA SƯ TỬ HỐNG",
    "slug": "dn-025-kinh-uu-dam-ba-la-su-tu-hong",
    "children": []
  },
  "26": {
    "title": "26. KINH CHUYỂN LUÂN THÁNH VƯƠNG SƯ TỬ HỐNG",
    "slug": "dn-026-kinh-chuyen-luan-thanh-vuong-su-tu-hong",
    "children": []
  },
  "27": {
    "title": "27. KINH KHỞI THẾ NHÂN BỔN",
    "slug": "dn-027-kinh-khoi-the-nhan-bon",
    "children": []
  },
  "28": {
    "title": "28. KINH TỰ HOAN HỶ",
    "slug": "dn-028-kinh-tu-hoan-hy",
    "children": []
  },
  "29": {
    "title": "29. KINH THANH TỊNH",
    "slug": "dn-029-kinh-thanh-tinh",
    "children": []
  },
  "30": {
    "title": "30. KINH TƯỚNG",
    "slug": "dn-030-kinh-tuong",
    "children": []
  },
  "31": {
    "title": "31. KINH GIÁO THỌ THI-CA-LA-VIỆT",
    "slug": "dn-031-kinh-giao-tho-thi-ca-la-viet",
    "children": []
  },
  "32": {
    "title": "32. KINH A-SÁ-NANG-CHI",
    "slug": "dn-032-kinh-a-sa-nang-chi",
    "children": []
  },
  "33": {
    "title": "33. KINH PHÚNG TỤNG",
    "slug": "dn-033-kinh-phung-tung",
    "children": []
  },
  "34": {
    "title": "34. KINH THẬP THƯỢNG",
    "slug": "dn-034-kinh-thap-thuong",
    "children": []
  }
}

def merge_objects(dn_pali, dn_tmc):
    result = {}

    for key, pali_item in dn_pali.items():
        tmc_item = dn_tmc.get(key, {})

        result[key] = {
            "title": tmc_item.get("title"),
            "slug": tmc_item.get("slug"),
            "children": pali_item.get("children", [])
        }

    return result


merged = merge_objects(dn_pali, dn_tmc)

import json

# Lưu ra map.txt
with open("map.txt", "w", encoding="utf-8") as f:
    for item in merged:
        f.write(repr(item) + ",\n")

print(json.dumps(merged, ensure_ascii=False, indent=2))