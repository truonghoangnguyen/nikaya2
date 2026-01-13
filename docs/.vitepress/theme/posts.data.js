// .vitepress/theme/posts.data.js
import { createContentLoader } from 'vitepress'

// Hàm trích xuất title từ h1 trong nội dung markdown
function extractH1Title(src) {
    if (!src) return null
    // Match h1 heading: # Title (không match ## hoặc nhiều # hơn)
    const h1Match = src.match(/^#\s+(.+)$/m)
    return h1Match ? h1Match[1].trim() : null
}

export default createContentLoader('**/*.md', {
    includeSrc: true, // Bật để lấy nội dung markdown raw
    transform(raw) {
        // Lọc và trả về dữ liệu gọn nhẹ chỉ gồm title, url và tags
        return raw
            .filter(({ frontmatter }) => frontmatter.tags) // Chỉ lấy bài có tags
            .map(({ url, frontmatter, src }) => ({
                // Ưu tiên lấy title từ h1, fallback về frontmatter.title
                title: extractH1Title(src) || frontmatter.title,
                url,
                tags: frontmatter.tags,
                date: frontmatter.date // Nếu bạn muốn hiển thị ngày
            }))
    }
})