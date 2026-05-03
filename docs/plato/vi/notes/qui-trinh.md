Ghi lại những bước để dịch, vì để lâu sẽ quên

# notes
vì sách có ghi-chú ở dưới chân trang ví dụ:
goddess,[^1]

sau đó trong source sẽ có:
[1]: Hê theos: Most probably—as 354a10–11 implies—the Thracian goddess Bendis,
whose cult had recently been introduced in Piraeus. However, for Athenians, Athena
is hê theos.

thì copy tất cả những ghi chú chân vào 1 file notes/1.md, 2.md...

sau đó đổi nội dung (search and replace)
`goddess,[^1]` -> `goddess,[1](/plato/vi/notes/01#1){.note}`  để đỡ tốn token, sẽ làm sau khi dịch
