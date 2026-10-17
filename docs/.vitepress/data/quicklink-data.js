
// Kinh tăng chi là case đặc biệt không có anchor nên bản so sánh dùng luôn của tmc
import an_tmc from './link-an-sujato-tmc'
// import an_sujato_vi from './link-an-sujato-vi'
// import mn_tmc from './link-mn-tmc'

import dn_pali_tmc_vi from './link-dn-pali-tmc-vi'
import sn_sujato_tmc_vi from './link-sn-sujato-tmc'
import kn from './link-kn'
import mv from './link-mv'
import cv from './link-cv.json'
import mn from './link-mn'

// kinh tiểu bộ sẽ ra rất nhiều mã
export default {
  ...kn,
  ...mn,
  sn: {
    folder: "kinhtuongung",
    name: "Kinh Tương Ưng",
    editions: {
      sujato_tmc: {
        label: "Sujato - TM Châu",
        path: "c-sujato-tmc-vi",
        index_length: 2,
        items: sn_sujato_tmc_vi
      },
    }
  },
  an: {
    folder: "kinhtangchi",
    name: "Kinh Tăng Chi",
    editions: {
      sujato_tmc: {
        label: "Tăng Chi: Sujato - TM Châu",
        path: "c-sujato-tmc-vi",
        index_length: 2,
        items: an_tmc
      },
    }
  },

  dn: {
    folder: "kinhtruongbo",
    name: "Kinh Trường Bộ",
    editions: {
      pali_tmc: {
        label: "Trường Bộ: Pali - TM Châu",
        path: "c-pali-tmc-vi",
        index_length: 2,
        items: dn_pali_tmc_vi
      }
    }
  },

  "mv": {
    folder: "vinaya-vi",
    name: "Luật",
    editions: {
      pali: {
        label: "Luật: Pali (Việt)",
        path: "kd/mv",
        index_length: 2,
        items: mv
      }
    }
  },
  "cv": {
    folder: "vinaya-vi",
    name: "Luật",
    editions: {
      pali: {
        label: "Luật: Pali (Việt)",
        path: "kd/cv",
        index_length: 2,
        items: cv
      }
    }
  },

  "bu.pj": {
    folder: "vinaya-vi",
    name: "Luật",
    editions: {
      pali: {
        label: "Luật: Pali (Việt)",
        path: "sv/bu/pj",
        index_length: 2,
        items: {
          "1": {
            "title": "BU BJ 1",
            "slug": "pli-tv-bu-vb-pj-1-pathamaparajikasikkhapada"
          }
        }
      }
    }
  }


};

//"title": "VIN.SV.PARA 1", có thể phân chia lại folder, vì các chú thích không phân chia thành bu/bi
/*

KN:
Kp	Khuddakapāṭha	Tiểu Tụng
Dhp	Dhammapada	Kinh Pháp Cú
Ud	Udāna	Kinh Phật Tự Thuyết
Iti	Itivuttaka	Kinh Như Thị Ngữ
Snp	Suttanipāta	Kinh Tập
Vv	Vimānavatthu	Chuyện Thiên Cung
Pv	Petavatthu	Chuyện Ngạ Quỷ
Thag	Theragāthā	Trưởng lão Tăng kệ
Thig	Therīgāthā	Trưởng lão Ni kệ
Ja	Jātaka	Bổn Sanh
Mnd	Mahāniddesa	Đại Nghĩa Thích
Cnd	Cūḷaniddesa	Tiểu Nghĩa Thích
Ps	Paṭisambhidāmagga	Vô Ngại Giải Đạo
Tha-ap	Therāpadāna	Trưởng lão sự
Thi-ap	Therī-apadāna	Trưởng lão Ni sự
Bv	Buddhavaṃsa	Phật Sử
Cp	Cariyāpiṭaka	Hạnh Tạng
Ne	Nettipakaraṇa	Netti, luận hướng dẫn giải thích giáo pháp
Pe	Peṭakopadesa	Luận hướng dẫn giải thích giáo pháp
Mil	Milindapañha	Mi Tiên Vấn Đáp

VIN

[mv/cv]
kd/	Khandhaka	Hợp Phần	Kd
  mv/	Mahāvagga	Đại Phẩm	Mv hoặc Kd 1–10
  cv/	Cūḷavagga (Cullavagga)	Tiểu Phẩm	Cv hoặc Kd 11–22

[pvr]
pvr/	Parivāra	Tập Yếu	Pvr
Parivāra có nghĩa gần với “phần tập hợp” hoặc “bản tổng hợp”. Đây là phần cuối của Luật tạng, hệ thống hóa và tóm tắt nhiều quy tắc đã trình bày trong Suttavibhaṅga và Khandhaka.

[bi/bu].[pj ss ay np pc pd sk as]
sv/	Suttavibhaṅga	Phân Tích Giới Luật	Vb
  bu/	Bhikkhu Vibhaṅga	Phân Tích Giới Tỳ-kheo	Bu
  bi/	Bhikkhunī Vibhaṅga	Phân Tích Giới Tỳ-kheo-ni	Bi

pli-tv-bu-vb-pj/	Pārājika	Ba-la-di	Bu Pj
pli-tv-bu-vb-ss/	Saṅghādisesa	Tăng tàn	Bu Ss
pli-tv-bu-vb-ay/	Aniyata	Bất định	Bu Ay
pli-tv-bu-vb-np/	Nissaggiya Pācittiya	Ni-tát-kỳ Ba-dật-đề	Bu NP
pli-tv-bu-vb-pc/	Pācittiya	Ba-dật-đề	Bu Pc
pli-tv-bu-vb-pd/	Pāṭidesanīya	Ba-la-đề-đề-xá-ni	Bu Pd
pli-tv-bu-vb-sk/	Sekhiya	Chúng học	Bu Sk
pli-tv-bu-vb-as-1-adhikaranasamatha.md	Adhikaraṇasamatha	Các pháp dàn xếp tranh sự	Bu As

*/