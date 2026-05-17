

## 7. Cấu trúc thư mục tham khảo (Folder Structure Reference for AI Agent)

Hệ thống thư mục được tổ chức theo phân cấp **Home -> Sách -> Dịch giả/Nguồn -> File nội dung**. AI Agent cần tham khảo cấu trúc này để tự động nhận diện metadata (tên sách, tác giả, ngôn ngữ) trong bước Implementation (như tự động sinh `description`, trích xuất tác giả cho `Schema.org`, hoặc gắn `E-E-A-T footer`).


### 7.1. Các Sách (Books/Nikayas)
Bao gồm 4 thư mục kinh chính:
- `kinhtruongbo/`: Kinh Trường Bộ (Digha Nikaya)
- `kinhtrungbo/`: Kinh Trung Bộ (Majjhima Nikaya)
- `kinhtangchi/`: Kinh Tăng Chi (Anguttara Nikaya)
- `kinhtuongung/`: Kinh Tương Ưng (Samyutta Nikaya)

Trong mỗi folder đều có file `mucluc.md` đó là file chứa index table

### 7.2. Tác giả & Bản dịch (Authors & Translations)
Bên trong mỗi thư mục bộ kinh là các thư mục con phân chia theo nguồn văn bản hoặc tác giả dịch:
- `thichminhchau/` (hoặc viết tắt `tmc`): Bản dịch của Hòa thượng Thích Minh Châu.
- `nm/`: Bản tiếng Anh của Bhikkhu Nanamoli và Bhikkhu Bodhi.
- `nm-vi/`: Bản dịch tiếng Anh của Bhikkhu Nanamoli và Bhikkhu Bodhi.
- `sujato/`: Bản tiếng Anh của Bhikkhu Sujato.
- `sujato-vi/`: Bản dịch tiếng Anh của Bhikkhu Sujato.
- `pali/`: Văn bản gốc tiếng Pali.
- `pali-vi/`: Bản dịch tiếng Pali.

*Lưu ý: Các bản dịch sang tiếng Việt từ văn bản gốc Pali, hay từ bản tiếng Anh của Sujato, Nanamoli đều do đội ngũ kinhnikaya.org thực hiện.*

### 7.3. Các bản so sánh / song song (Parallel / Compare Versions)
Bất kỳ thư mục nào có tiền tố `c-` (compare) ở đầu đều là bản đọc song song 2 bản dịch hoặc 2 ngôn ngữ, dùng để so sánh đối chiếu giữa các bản dịch:
- **Cú pháp:** Thường có dạng `c-{nguồn_1}-{nguồn_2}...`
- **Ví dụ 1:** `c-nm-tmc` = Bản so sánh giữa dịch giả Nanamoli Bodhi (`nm`) và Thích Minh Châu (`tmc`).
- **Ví dụ 2:** `c-pali-tmc-vi` = Bản so sánh giữa bản tiếng Pali, bản Thích Minh Châu (`tmc`), và bản dịch tiếng Việt (`vi`).

## BreadcrumbList
Home
 Kinh Trung Bô
   Thích Minh Châu
   nanamoli-bodhi-en (Nanamoli Bodhi tiếng anh)
   nanamoli-bodhi-vi (Nanamoli Bodhi tiếng việt)
   pali-vi (dịch từ pali sang tiếng việt)
   c-pali-tmc (bản so sánh pali và thích minh châu)
 Tương tự cho các kinh còn lại

## Quy tắc datePublished & dateModified
datePublished = 2026-05-03
dateModified = git commit date hoặc 2026-05-03

## Author:
Chúng ta sẽ bỏ qua trường author, chỉ dùng trường translator
