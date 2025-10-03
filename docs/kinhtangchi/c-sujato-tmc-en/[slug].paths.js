import tmcmnvi from './tmc.js';
import fs from 'node:fs/promises'; // Dùng fs/promises để code gọn hơn với async/await
import path from 'node:path';
import MarkdownIt from 'markdown-it';
import anchor from 'markdown-it-anchor';
import markdownItAttrs from 'markdown-it-attrs';

// --- Khởi tạo markdown-it giống hệt như trong component của bạn ---
// Bạn có thể tạo một file utils riêng để chia sẻ cấu hình này nếu muốn
const slugAnchor = (s) => {
  // Giả sử bạn có hàm slugify tương tự ở đây
  return encodeURIComponent(String(s).trim().toLowerCase().replace(/\s+/g, '-'));
};

const mdLeft = new MarkdownIt({
  html: true,
  linkify: true,
  typographer: true
}).use(anchor, {
    permalink: anchor.permalink.ariaHidden({
      symbol: '',
      placement: 'before'
    }),
    slugify: (s) => slugAnchor(s),
}).use(markdownItAttrs);

const mdRight = new MarkdownIt({
  html: true,
  linkify: true,
  typographer: true
});

// Hàm helper để đọc file và render markdown
async function readAndRenderMarkdown(filePath, mdInstance) {
  try {
    // VitePress chạy từ thư mục gốc của project, nên cần resolve path từ đó
    // Giả sử các file markdown của bạn nằm trong thư mục `docs`
    const fullPath = path.resolve(process.cwd(), 'docs', filePath.startsWith('/') ? filePath.substring(1) : filePath);

    let content = await fs.readFile(fullPath, 'utf-8');

    // Xóa frontmatter
    content = content.replace(/^---[\s\S]*?---\n/, '');

    return mdInstance.render(content);
  } catch (e) {
    console.error(`Error reading or rendering file: ${filePath}`, e);
    return 'error in slug.paths'; // Trả về chuỗi rỗng nếu có lỗi
  }
}

export default {
  // Chuyển hàm paths thành async
  async paths() {
    // Dùng Promise.all để xử lý tất cả các trang song song, tăng tốc độ build
    return Promise.all(
      tmcmnvi.map(async (page) => {
        // Lấy data gốc
        const { data } = page.params;

        // Đọc và render nội dung file left và right
        const leftHtml = await readAndRenderMarkdown(data.left, mdLeft);
        const rightHtml = await readAndRenderMarkdown(data.right, mdRight);

        // Tạo một object params mới với dữ liệu đã được pre-render
        return {
          params: {
            ...page.params, // Giữ lại slug và các params khác
            data: {
              ...data, // Giữ lại data cũ như title, link...
              // Thêm các trường mới chứa HTML đã render
              leftHtml: leftHtml,
              rightHtml: rightHtml,
              // Không cần truyền path nữa, nhưng bạn có thể giữ lại để tạo link [source]
              // left: data.left,
              // right: data.right
            }
          }
        };
      })
    );
  }
}