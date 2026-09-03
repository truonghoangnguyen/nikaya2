
// Kinh tăng chi là case đặc biệt không có anchor nên bản so sánh dùng luôn của tmc
import an_tmc from './link-an-tmc'
// import an_sujato_vi from './link-an-sujato-vi'
// import mn_tmc from './link-mn-tmc'
import mn_pali_tmc_vi from './link-mn-pali-tmc-vi'
import dn_pali_tmc_vi from './link-dn-pali-tmc-vi'
import sn_sujato_tmc_vi from './link-sn-sujato-tmc'
import kn from './link-kn'
import mv from './link-mv'

// kinh tiểu bộ sẽ ra rất nhiều mã
export default {
  ...kn,
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

  mn: {
    folder: "kinhtrungbo",
    name: "Kinh Trung Bộ",
    editions: {
      pali_tmc: {
        label: "Trung Bộ: Pali - TM Châu",
        path: "c-pali-tmc-vi",
        index_length: 2,
        items: mn_pali_tmc_vi
      },
      nm_tmc: {
        label: "Trung Bộ: Nanamoli - TM Châu",
        path: "c-nm-tmc-vi",
        index_length: 2,
        items: mn_pali_tmc_vi
      }
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

  "vin.mv": {
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
  "vin.cv": {
    folder: "vinaya-vi",
    name: "Luật",
    editions: {
      pali: {
        label: "Luật: Pali (Việt)",
        path: "kd/cv",
        index_length: 2,
        items: {
          "9": {
            "title": "Vin CV 9",
            "slug": "pli-tv-kd-19-patimokkhatthapanakkhandhaka"
          },
          "5": {
            "title": "Vin CV 5",
            "slug": "pli-tv-kd-15-khuddakavatthukkhandhaka"

          }

        }
      }
    }
  },

  "vin.sv.para": {
    folder: "vinaya-vi",
    name: "Luật",
    editions: {
      pali: {
        label: "Luật: Pali (Việt)",
        path: "sv/bu/pj",
        index_length: 2,
        items: {
          "1": {
            "title": "VIN.SV.PARA 1",
            "slug": "pli-tv-bu-vb-pj-1-pathamaparajikasikkhapada"
          }
        }
      }
    }
  }


};

//"title": "VIN.SV.PARA 1", có thể phân chia lại folder, vì các chú thích không phân chia thành bu/bi
/*Cv. 1  → kd-11
Cv. 2  → kd-12
...
Cv. 8  → kd-18
Cv. 9  → kd-19  ✓
Cv. 10 → kd-20
Cv. 11 → kd-21
Cv. 12 → kd-22 */