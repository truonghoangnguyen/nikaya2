# Cách chuyển đổi

1. Từ source pdf -> .md file -> clean format -> split file ->
    1.1.en               f`author-en`->3make_mucluc->f`c-author1-author2-en`->4make_compare_list->finish
    1.2.vi->translate -> f`author-vi`->3make_mucluc->f`c-author1-author2-vi`->4make_compare_list->finish

1. từ file pdf -> file .md (.scripts/0pdf2md.ipynb)
2. từ file .md thành chia thành nhiều file nhỏ (.scripts/0pdf2md.ipynb)
2.2 Các file .md cần có tiêu đề h1 `#`
## tạo NAV file
3. Tạo navfile(next-back) và index.md
## tạo So sánh
3.1 Tạo file `filelist.js`, `index.md`  trong thư mục tương ứng (.scripts/3make_filelist.ipynb)

filelist.js có format như sau:
```
const mn_thichminhchau = [
  { text: "Kinh Trung Bộ Ht. Thích Minh Châu", link: "/kinhtrungbo/thichminhchau/index.md" },
```
filelist.js dùng để tạo next-back button trong mỗi bài, vitepress chỉ có next-back khi định nghĩa ở sidebar
3.2 vào config.ts để thêm code

Nếu 2 sách có số file khác nhau thì
1 - nối file sách A : số lượng các file sẽ giống nhau
2 - chia file sách B
Chia ra hay nối lại đều giống nhau, chỉ cần đảm bảo số lượng file 2 bên giống nhau và đánh số giống nhau -> lấy theo TMC cho tiện
Và thuật toán phải được đảm bảo không cần sửa

# Dịch
- Đưa vào thư mục working
- Tạo bản so sánh (`c-author1-author2-vi`)
- Dịch và so sánh
- Vào thư mục working, copy ra ngoài
- Tạo file NAV (next-back) cho thư mục  en/vi
- Tạo bản so sánh (`c-author1-author2-vi`)
## 4. Tạo so sánh
### 4.1 tạo thư mục (sẽ là url path) vd: docs/kinhtangchi/c-bodhi-tmc-vi/
copy 2 file `[slug].paths.js` và `[slug].md` vào thư mục
### 4.2 tạo file so sánh
Tạo so sánh cần số lượng file 2 bên giống nhau
.scripts/4make_compare_list.ipynb
Chuẩn bị:
list A = danh sách những file bên phải (copy trong filelist.js)
list B = danh sách những file bên trái(copy trong filelist.js)
thứ tự theo từ trên xuống dưới.

### 4.3 sửa 2 file `[slug].paths.js` và `[slug].md`
từ file tmc.js export
```
const tmc_bodhi_vi = [...]
export default tmc_bodhi_vi;
```
và file [slug].path.js
```
import tmc_bodhi_vi from './tmc.js';

export default {
  paths() {
    const tmc =  "TK.Thích Minh Châu";
    const mn = "Bhikkhu Sujato"
    return tmc_bodhi_vi;
  }
}
```


# kinh Tăng Chi bộ 14-4-2025
- Hướng dẫn cách thực hiện:
  1. Vì các bản dịch khác nhau có cách chia phẩm khác nhau nên cách chia là lấy các phẩm gộp chia ra (tách file) chứ không làm theo kiểu gộp nhiều file lại.
  2. Tên số thứ tự của file sẽ giữ nguyên ví dụ: file đầu là 01-002-xxx (chương 1, phẩm 2) thì chia ra sẽ là 01-002-xxx-1.md, 01-002-xxx-2.md
  3. sau đó dịch eng-> vi để dò
  4. Khi đổi thì đổi bộ tiếng anh


- Bản tiếng anh chỉ tìm thấy bản dịch của Bhikkhu Sujato là đánh số tương tự như của TMC
- Việc phân chia thành từng phần gặp khó khăn về độ dài có lẽ nên chia theo https://www.budsas.org/uni/u-kinh-tangchibo/tangchi00.htm
- Dự tính nên phân chia 1 chương thành 1 file "Chương Một Pháp" "01-chuong-mot-phap.md" nếu muốn chia nhỏ nhơn thì "01-chuong-mot-phap-1.md" "01-chuong-mot-phap-2.md"
- Cách đánh số của bản tiếng anh cũng khác TMC reset lại số, bản tiêngs
- Chia lại file theo từng phẩm, mỗi phẩm 1 file, home của mỗi phẩm (một-pháp, hai-pháp, ba-pháp...) sẽ vào 1 file index riêng
- file tiếng anh phải viết lại cách chia file `AN 2.1–10` = 2 pháp, đoạn từ 1-10
```
    # The Book of the ... = 1 chương
    # The Chapter on ... = 1 phầm
```
link:
Cả 2 Sách của Bhikkhu Bodhi và Sujato có nội dung giống nhau ở Chương 1, Sách của HT TMC khác một số Phẩm
https://theravada.vn/book/the-numerical-discourses-of-the-buddha-anguttara-bhikkhu-bodhi/

Woodward-Hare:
https://theravada.vn/wp-content/uploads/2020/09/an-pts_v1.1.pdf

#### Chương 1 done
  Thích Minh Châu:
  - Chương 1, 23 phẩm
    - phẩm Thứ Mười Một -> Thành Phẩm Phi Pháp
    - Phẩm 20 Thiền Định -> Chia làm 2 Phần
        1. Sự thật Sự Là Vậy
        2. Búng ngón tay (Lấy tên theo bản tiếng anh)
    - Phẩm 21 Thiền Đinh 2 chia làm 2
        1. Thân hành niệm
        2. Bất tử (Lấy tên theo bản tiếng anh)

Các chương của thầy TMC và Woodward-Hare giống nhau, nhưng không đánh số vì vậy dùng sách của Sujato
- Phần 1 phải đổi vì các thứ tự không giống nhau ?
- Sujato
  - Chương 1, phẩm 16 chương sẽ chia làm 4 file (Four Chapters on One Thing)

  - Ngày 17-4-2025 Đổi sang sách của Bhikkhu Bodhi vì bản dịch của AI ra kết quả dễ đọc hơn
    - Chương 1 chia làm 20 phẩm, so
    - sau khi chi thành từng phẩm, thử dịch
    - Tìm tiêu đề phẩm `^#+ ([IVXLCDM]+\. .*$)`
    - Tìm đánh số phẩm `^#*\s*(\d+ .*)`
  - Ngày 20-4-2025 Chuyển lại sang sách của Sujato vì dữ liệu được nguyên bản text

#### chương 2 done
- Sujato 19 phẩm
- TMC 17 phẩm ->
  Phẩm 16 - phẫn nộ
  TMC 02-16 phẩm 1-50 = Bodhi 02-16: phẩm 1-50
  TMC 02-16 phẩm 51-100 = Bodhi 02-17: phẩm 51-100
  TMC 02-17 phẩm 1-2 =  Bodhi 02-18 phẩm 280-309
  TMC 02-17 phẩm 3-5 =  Bodhi 02-19 phẩm 310-320
  --> Chia TMC 02-16 ra 2 file, 02-16-1 (02-16), 02-16-2 (02-17)
  --> Chia TMC 02-17 ra 2 file, 02-17-1 (02-18), 02-17-2 (02-19)

#### chương 3 done
- Sujato 18 phẩm
- TMC 16 phẩm ->
  /03-004- 2 đoạn cuối không thấy bên Sujato
