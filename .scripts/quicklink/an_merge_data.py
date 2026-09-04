import json
from util import flat_json

# Load file 1 và file 2
with open("an-index-tmc.json", "r", encoding="utf-8") as f1:
    data1 = json.load(f1)

with open("an-index.json", "r", encoding="utf-8") as f2:
    data2 = json.load(f2)

# Cập nhật children từ file2 sang file1 dựa trên thứ tự xuất hiện (index)
for key, content in data1.items():
    if key in data2:
        files1 = content.get("files", [])
        files2 = data2[key].get("files", [])

        # Ghép tương ứng theo index của mảng files
        for f1_item, f2_item in zip(files1, files2):
            if "children" in f2_item:
                f1_item["children"] = f2_item["children"]


txt = flat_json(data1)

# Lưu lại kết quả vào file mới
with open("an_updated.json", "w", encoding="utf-8") as f_out:
    f_out.write(txt)