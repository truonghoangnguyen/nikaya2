// .vitepress/data/quicklink-data.js
//
// Cấu trúc: mỗi nikaya có "folder" (thư mục chung) + nhiều "editions".
// Mỗi edition có "path" (thư mục con), "index_length" (đi sâu tối đa
// bao nhiêu cấp số trước khi cắt), và "items" (dữ liệu từng kinh).
//
// URL cuối cùng = /{folder}/{edition.path}/{slug}[#anchor]
//
// Bạn chỉ cần điền/nhân bản theo mẫu 2 nikaya dưới đây cho DN, AN, KN...
// index_length của từng ô do bạn tự set theo dữ liệu đã làm sạch tới đâu.

export default {
  mn: {
    folder: "kinhtrungbo",
    editions: {
      pali: {
        label: "Pali",
        path: "nanamoli-bodhi-vi",
        index_length: 1, // MN chỉ có 1 cấp số hữu ích (số kinh); phần "đoạn" luôn bị bỏ qua
        items: {
          "7": {
            title: "MN 7. KINH VÍ DỤ TẤM VẢI",
            slug: "mn-007-the-simile-of-the-cloth"
          }
        }
      },
      tmc: {
        label: "Thích Minh Châu",
        path: "thichiminhchau",
        index_length: 1,
        items: {
          "7": {
            title: "Kinh bố dụ",
            slug: "mn-007-kinh-vi-du-tam-vai"
          }
        }
      }
    }
  },

  sn: {
    folder: "kinhtuongung",
    editions: {
      pali: {
        label: "Pali",
        path: "pali",
        index_length: 2, // SN bản Pali có code tới cấp 2 (samyutta.sutta)
        items: {
          "2": {
            title: "SN 2. Devaputtasaṁyutta",
            slug: "sn-002-devaputtasamyutta",
            children: {
              "2": { anchor: "2-2-dutiyakassapasutta" }
              // Nếu đoạn con nằm ở TRANG RIÊNG (khác trang cha), thêm "slug" ở đây:
              // "3": { slug: "sn-002-...-trang-rieng", anchor: "..." }
            }
          }
        }
      },
      tmc: {
        label: "Thích Minh Châu",
        path: "thichminhchau",
        index_length: 1, // bản TMC chưa có code tới cấp đoạn, luôn dừng ở trang kinh
        items: {
          "2": {
            title: "2. TƯƠNG ƯNG THIÊN TỬ",
            slug: "sn-02-tuong-ung-thien-tu"
          }
        }
      }
    }
  }

  // dn: { folder: "kinhtruongbo", editions: { ... } },
  // an: { folder: "kinhtangchi", editions: { ... } },
};