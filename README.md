# Tài liệu đa ngôn ngữ (Kinh Nikaya)

Một trang tài liệu dựa trên VitePress dành cho bộ sưu tập Kinh Nikaya, tập trung vào việc so sánh song ngữ các văn bản Phật giáo và các tài liệu liên quan. Trang web được cấu hình dưới dạng tệp tĩnh với nội dung được lưu trữ bằng Markdown trong thư mục `docs/`.


### Tính năng chính
- Lưu trữ nhiều bộ sưu tập kinh điển và văn bản liên quan trong `docs/`.
- Hỗ trợ các trang so sánh song song (ví dụ: `compare.html`).
- Xây dựng thanh điều hướng động từ các nguồn `meta/filelist` của từng bộ sưu tập.
- Tạo slug/anchor nhất quán cho các tiêu đề thông qua một công cụ tiện ích tùy chỉnh.
- Sao chép nội dung Markdown thô vào đầu ra khi chạy `vitepress build`.
- Cung cấp máy chủ phát triển VitePress để xem và chỉnh sửa cục bộ.

### Cấu trúc hoạt động
- Nội dung nằm trong các tệp Markdown dưới thư mục `docs/` với các bộ sưu tập như `kinhtruongbo`, `kinhtrungbo`, `kinhtangchi`, và `kinhtuongung`.
- VitePress được cấu hình trong `docs/.vitepress/config.ts` với dữ liệu điều hướng tùy chỉnh (`BOOK_NAV`) được xây dựng từ các module `meta/filelist`.
- Một plugin build của VitePress sẽ quét các bộ sưu tập nguồn và sao chép các tệp Markdown vào thư mục `docs/.vitepress/dist/` để truy cập trực tiếp.
- Dữ liệu trang được biến đổi tại thời điểm build để thiết lập tiêu đề và điều hướng tiếp theo/trước đó dựa trên đường dẫn bộ sưu tập.

## Kỹ thuật
### Tìm kiếm Search
Thay vì sử dụng bộ tìm kiếm mặc định của VitePress, dự án này sử dụng một hệ thống tìm kiếm tùy chỉnh để tối ưu hóa hiệu suất và phù hợp với cấu trúc dữ liệu đặc thù:
- **Tạo dữ liệu tìm kiếm**: Script `.scripts/5make-search-file.ipynb` được sử dụng để quét tất cả các file `filelist.js` trong các bộ sưu tập. Nó tổng hợp tiêu đề (`text`) và đường dẫn (`link`) thành một file duy nhất tại `docs/search-items.js`.
- **Hoạt động**: File `docs/search.md` sử dụng component `SearchPage.vue` và nạp dữ liệu từ `search-items.js` để thực hiện tìm kiếm ở phía client. Điều này giúp việc tìm kiếm cực nhanh và không phụ thuộc vào cấu trúc index phức tạp của các công cụ tìm kiếm mặc định.

### Cách chạy dự án
- Yêu cầu: Node.js và `pnpm`.
- Cài đặt thư viện: `pnpm install`.
- Chạy server phát triển: `pnpm docs:dev`.
- Build sản phẩm: `pnpm docs:build`.

