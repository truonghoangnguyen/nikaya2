# Kinh Nikaya — Thư viện Kinh điển Phật giáo Nguyên thủy
**Trang chủ:** <https://kinhnikaya.org>

## Tại sao ?

Tôi đọc kinh Nikaya nhưng không hiểu: sắc là gì, tưởng là gì, thọ là gì, hành là gì, thức là gì và nhiều thứ khác.

Những Bản dịch của tôi giống như HT Thích Minh Châu nói "người đọc phải tự tìm hiểu.

Kinh Nikaya là thư viện trực tuyến mở, cung cấp toàn bộ **Kinh tạng Pāli (Nikāya)** của Phật giáo Nguyên thủy (Theravāda) với nhiều bản dịch song song và công cụ đối chiếu câu-theo-câu giữa các bản dịch.

---

## Bốn bộ Kinh (Tứ A-hàm / Bốn Nikāya chính)

Đây là bốn tuyển tập kinh chính trong Kinh tạng (Sutta Piṭaka) của Tam tạng Pāli — ghi lại lời dạy trực tiếp của Đức Phật Thích-ca Mâu-ni và các vị Đại đệ tử.

| Mã | Tên Pāli | Tên Việt | Nội dung |
|---|---|---|---|
| **DN** | Dīgha Nikāya | Kinh Trường Bộ | 34 bài kinh dài, bàn về vũ trụ luận, vua chúa, các tôn giáo đương thời, đạo đức xã hội. |
| **MN** | Majjhima Nikāya | Kinh Trung Bộ | 152 bài kinh độ dài trung bình, trọng tâm về thiền định, giải thoát, đối thoại triết học. |
| **SN** | Saṃyutta Nikāya | Kinh Tương Ưng Bộ | Khoảng 2.900 bài kinh ngắn, gom theo chủ đề (uẩn, xứ, duyên khởi, Đạo đế…). |
| **AN** | Aṅguttara Nikāya | Kinh Tăng Chi Bộ | Khoảng 2.300 bài kinh ngắn, sắp xếp theo "pháp số" tăng dần (một pháp, hai pháp, … mười một pháp). |

Truy cập:
- `/kinhtruongbo/` — Trường Bộ (DN)
- `/kinhtrungbo/` — Trung Bộ (MN)
- `/kinhtuongung/` — Tương Ưng (SN)
- `/kinhtangchi/` — Tăng Chi (AN)

---

## Các bản dịch & tác giả

Mỗi bộ kinh được cung cấp dưới nhiều bản dịch để đối chiếu:

### Tiếng Pāli (nguyên bản)
- **`pali/`** — Bản Pāli gốc theo ấn bản  lấy từ [SuttaCentral](https://suttacentral.net).
- **`pali-vi/`** — Bản Pāli dịch sang tiếng Việt.

### Tiếng Việt
- **`thichminhchau/`** — **Tỷ kheo Thích Minh Châu** (1918–2012): Bản dịch Việt ngữ kinh điển nhất, được dịch trực tiếp từ Pāli trong nhiều thập niên. Nguồn tham chiếu chuẩn của Phật giáo Việt Nam hiện nay.
- **`sujato-vi/`** — Bản dịch Việt từ bản tiếng Anh của Bhikkhu Sujato.
- **`nanamoli-bodhi-vi/`** *(Trung Bộ)* — Bản dịch Việt từ bản tiếng Anh "The Middle Length Discourses" của Ñāṇamoli & Bodhi.

### Tiếng Anh
- **`sujato-en/`** — **Bhikkhu Sujato** ([SuttaCentral](https://suttacentral.net): Bản dịch hiện đại, dễ đọc — phổ biến nhất trong cộng đồng Phật giáo nói tiếng Anh ngày nay.
- **`nanamoli-bodhi-en/`** *(Trung Bộ)* — **Bhikkhu Ñāṇamoli & Bhikkhu Bodhi**: Bản dịch học thuật uy tín nhất của Trung Bộ Kinh ("The Middle Length Discourses of the Buddha").

### Trang đối chiếu song song (`c-…/`)
Mỗi bài kinh có thể mở dưới dạng **so sánh hai cột**: ví dụ Pāli ↔ Thích Minh Châu, Sujato ↔ Thích Minh Châu, hoặc Ñāṇamoli-Bodhi ↔ Thích Minh Châu. Cuộn hai cột đồng bộ để đối chiếu từng đoạn.

---

## Kỹ thuật

Trang là **static site** sinh bằng **VitePress**.

### Stack ghi chú
- Search : Fuse.js trên `docs/search-items.js` (client-side) |
- Các script hỗ trợ việc làm sách: Jupyter notebooks trong `.scripts/` (PDF→MD, tách chương, sinh filelist, mucluc, compare list) |

### Cấu trúc thư mục
```
docs/
  index.md                       # trang chủ
  <bộ-kinh>/                     # kinhtruongbo, kinhtrungbo, kinhtangchi, kinhtuongung
    <dịch-giả>/                  # thichminhchau, sujato-en, sujato-vi, pali, pali-vi, nanamoli-bodhi-en/vi
      mn-001-*.md                # mỗi bài kinh một file
      meta/filelist.js           # mảng TOC {text, link}[]
      meta/mucluc.md             # mục lục cho người đọc
    c-<a>-<b>-vi/                # thư mục đối chiếu, ví dụ c-pali-tmc-vi
      [slug].md                  # trang động dùng <TextComparePage />
      [slug].paths.js            # gọi buildComparePages(tmc, dirKey)
      tmc.js                     # mảng {slug, data:{left,right,leftTitle,rightTitle,...}}
  c/                             # đối chiếu xuyên-bộ
  search.md, search-items.js     # trang tìm kiếm + index
  .vitepress/
    config.ts                    # toàn bộ cấu hình: nav, BOOK_NAV, SEO, transformPageData
    compare-render.js            # SSG: đọc left+right MD, render HTML, inject vào params
    components/                  # TextCompare, TextComparePage, CompareButton, NotePopup, …
    theme/                       # custom theme: SuttaFooter, HomePageLayout, SearchPage
    utils.js                     # slugAnchor()
.scripts/                        # notebook chuẩn bị nội dung (không chạy lúc runtime)
scripts/                         # helper Node: import-docs, update-config, generate-sidebar
```

### Cơ chế hoạt động

**Điều hướng next/prev.** `config.ts` import mọi `meta/filelist.js` và ghép thành `BOOK_NAV` (path-prefix → mảng có thứ tự). `transformPageData()` tra `relativePath`, gán `frontmatter.title` và `next` / `prev` cho pager.

**Trang đối chiếu (SSG inline).**
1. `[slug].paths.js` mỗi compare folder gọi `buildComparePages(tmc, dirKey)` từ `compare-render.js`.
2. Khi `NODE_ENV=production`, hàm này đọc hai file MD (`data.left`, `data.right`), bỏ frontmatter, render bằng markdown-it, inject `leftHtml` / `rightHtml` vào route params.
3. `[slug].md` mount `<TextComparePage />` đọc HTML đã pre-render — HTML tĩnh xuất ra đã có đủ nội dung (tốt cho SEO).
4. Dev mode: pass-through, `TextCompare` fetch trên client.
5. Khi build, `compare-lookup.json` được sinh ra `docs/public/` để mỗi trang sutta biết URL bản đối chiếu của mình.

**SEO / Schema.org.** `transformPageData()` rẽ nhánh theo path:
- Trang compare → `ScholarlyArticle` với mảng `translator[]` từ `COMPARE_META`.
- Trang dịch giả đơn → `ScholarlyArticle` + `isPartOf` Book.
- Luôn có: `canonical`, OG/Twitter meta, `BreadcrumbList`.
- `dateModified` lấy từ map `git log --name-only` build một lần lúc load config.
- Schema cấp site (`WebSite` + `Organization`) tiêm qua `head`.

**Tìm kiếm.** `.scripts/5sitemap-search-file.ipynb` quét mọi `filelist.js`, gom `{text, link}` thành `docs/search-items.js`. `search.md` mount `SearchPage.vue` (Fuse.js). URL quay lại được lưu vào `localStorage` mỗi khi đổi route.

**Markdown thô.** Vite plugin `copy-markdown-files` trong `config.ts` copy mọi `.md` của 3 bộ lớn sang `dist/` sau khi build, cho phép fetch nguồn gốc.

### Chạy

```bash
pnpm install
pnpm dev          # vitepress dev docs
pnpm build        # node --max-old-space-size=4096 vitepress build docs
pnpm preview      # phục vụ dist/
pnpm test:seo     # .scripts/test-seo.js — kiểm tra schema/meta
pnpm fulltest     # test trước khi public
```

Yêu cầu: Node.js + pnpm. Build cần ~4 GB heap (đã set `--max-old-space-size=4096`).

### Thêm nội dung mới
1. Bỏ file `.md` đã dịch vào `docs/<bộ-kinh>/<dịch-giả>/`.
2. Chạy `.scripts/3make_mucluc.ipynb` để sinh lại `meta/filelist.js` + `meta/mucluc.md`.
3. Import `filelist.js` mới trong `docs/.vitepress/config.ts` và thêm vào `BOOK_NAV`.
4. Thêm bản đối chiếu mới: tạo `c-<a>-<b>-vi/` với `tmc.js`, `[slug].md`, `[slug].paths.js`; chạy `.scripts/4make_compare_list.ipynb`; đăng ký vào `COMPARE_SOURCES` + `COMPARE_META`.
5. Chạy `.scripts/5sitemap-search-file.ipynb` để cập nhật `search-items.js`.

---

## Đóng góp

Repo: <https://github.com/truonghoangnguyen/nikaya2>. PR và issue đều hoan nghênh — đặc biệt là báo lỗi chính tả, sai chú thích, hay đóng góp bản dịch mới.

## Giấy phép
- **Nội dung:** Theo từng dịch giả. Phần lớn dưới CC0 / phạm vi công cộng. Chi tiết xem `docs/license.md`.
