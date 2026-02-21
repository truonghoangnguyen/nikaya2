// [slug].paths.js

import tmcmnvi from './tmc.js';
import fs from 'node:fs/promises';
import path from 'node:path';
import MarkdownIt from 'markdown-it';
import anchor from 'markdown-it-anchor';
import markdownItAttrs from 'markdown-it-attrs';

// --- Bắt đầu: Phần khởi tạo MarkdownIt ---
// Đảm bảo phần này giống hệt cấu hình bạn muốn
const slugAnchor = (s) => {
  // Đây là một hàm slugify cơ bản, bạn có thể thay thế bằng hàm của riêng bạn
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
// --- Kết thúc: Phần khởi tạo MarkdownIt ---


/**
 * Hàm helper để đọc file, xóa frontmatter và render thành HTML.
 * @param {string} relativePath - Đường dẫn tương đối từ thư mục docs (ví dụ: /kinhtrungbo/...)
 * @param {MarkdownIt} mdInstance - Instance của MarkdownIt để sử dụng
 * @returns {Promise<string>} - Chuỗi HTML đã được render
 */
async function readAndRenderMarkdown(relativePath, mdInstance) {
  try {
    // VitePress chạy từ thư mục gốc của project.
    // Giả sử các file markdown của bạn nằm trong thư mục `docs`.
    // Nếu thư mục của bạn có tên khác, hãy thay 'docs' bằng tên đúng.
    const fullPath = path.resolve(process.cwd(), 'docs', relativePath.startsWith('/') ? relativePath.substring(1) : relativePath);

    let content = await fs.readFile(fullPath, 'utf-8');

    // Xóa frontmatter
    content = content.replace(/^---[\s\S]*?---\n/, '');

    return mdInstance.render(content);
  } catch (e) {
    console.error(`Lỗi khi đọc hoặc render file: ${relativePath}`, e);
    return '<p>Lỗi khi tải nội dung.</p>'; // Trả về thông báo lỗi
  }
}

export default {
  async paths() {
    // Dùng Promise.all để xử lý tất cả các trang song song, tăng tốc độ
    const pages = tmcmnvi.map(async (page) => {
      // Chỉ pre-render HTML khi đang trong quá trình build
      if (process.env.NODE_ENV === 'production') {
        const { data } = page.params;

        // Đọc và render nội dung cho cả hai cột
        const [leftHtml, rightHtml] = await Promise.all([
          readAndRenderMarkdown(data.left, mdLeft),
          readAndRenderMarkdown(data.right, mdRight)
        ]);

        // Trả về params mới với dữ liệu HTML đã được thêm vào
        return {
          params: {
            ...page.params,
            data: {
              ...data,
              leftHtml, // Thêm prop leftHtml
              rightHtml, // Thêm prop rightHtml
            }
          }
        };
      } else {
        // Trong môi trường dev, trả về dữ liệu gốc không thay đổi.
        // Component sẽ tự fetch và render phía client.
        return page;
      }
    });

    return Promise.all(pages);
  }
}