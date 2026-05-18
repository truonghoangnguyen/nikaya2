import fs from 'fs';
import path from 'path';
import * as cheerio from 'cheerio';
import { globSync } from 'glob';

// ==========================================
// CẤU HÌNH ĐIỀU KIỆN TEST (DỄ DÀNG CẬP NHẬT)
// ==========================================
const rules = [
  {
    name: 'Phải có thẻ <title>',
    test: ($, route) => {
      const title = $('title').text();
      if (!title || title.trim() === '') return 'Thiếu hoặc rỗng thẻ <title>';
      return null;
    }
  },
  {
    name: 'Phải có thẻ Meta Description',
    test: ($, route) => {
      const desc = $('meta[name="description"]').attr('content');
      if (!desc || desc.trim() === '') return 'Thiếu hoặc rỗng thẻ meta description';
      if (desc.length < 10) return 'Meta description quá ngắn (< 10 ký tự)';
      return null;
    }
  },
  {
    name: 'Phải có thẻ Canonical (chống trùng lặp nội dung)',
    test: ($, route) => {
      const canonical = $('link[rel="canonical"]').attr('href');
      if (!canonical) return 'Thiếu thẻ link rel="canonical"';
      return null;
    }
  },
  {
    name: 'Không có thẻ H1 rỗng (Accessibility)',
    test: ($, route) => {
      let h1Error = null;
      $('h1').each((i, el) => {
        if ($(el).text().trim() === '') {
          h1Error = 'Phát hiện thẻ <h1> nhưng không có nội dung chữ';
        }
      });
      return h1Error;
    }
  }
];

// ==========================================
// DANH SÁCH CÁC TRANG CẦN TEST (INCLUDE LIST)
// ==========================================
// Script sẽ CHỈ TEST những URL có chứa các chuỗi dưới đây.
// Ví dụ: '/kinhtrungbo/index.html', hoặc quét cả thư mục '/kinhtuongung/'
const includeList = [
  // 1. Kinh Trung Bộ
  '/kinhtrungbo/index.html',
  '/kinhtrungbo/thichminhchau/',
  '/kinhtrungbo/pali-vi/',
  '/kinhtrungbo/pali/',
  '/kinhtrungbo/c-pali-tmc-vi/',
  '/kinhtrungbo/c-nm-tmc-vi/',
  '/kinhtrungbo/nanamoli-bodhi-en/',
  '/kinhtrungbo/nanamoli-bodhi-vi/',

  // 2. Kinh Tăng Chi
  '/kinhtangchi/index.html',
  '/kinhtangchi/thichminhchau/',
  '/kinhtangchi/sujato-en/',
  '/kinhtangchi/sujato-vi/',
  '/kinhtangchi/c-sujato-tmc-vi/',

  // 3. Kinh Trường Bộ
  '/kinhtruongbo/index.html',
  '/kinhtruongbo/thichminhchau/',
  '/kinhtruongbo/pali-vi/',
  '/kinhtruongbo/pali/',
  '/kinhtruongbo/sujato-en/',
  '/kinhtruongbo/sujato-vi/',
  '/kinhtruongbo/c-pali-tmc-vi/',
  '/kinhtruongbo/c-sujato-tmc-vi/',

  // 4. Kinh Tương Ưng
  '/kinhtuongung/index.html',
  '/kinhtuongung/thichminhchau/',
  '/kinhtuongung/sujato-en/',
  '/kinhtuongung/sujato-vi/',
  '/kinhtuongung/c-sujato-tmc-vi/'
];


// ==========================================
// KỊCH BẢN CHẠY CHÍNH (KHÔNG CẦN SỬA)
// ==========================================
const distDir = path.resolve('docs/.vitepress/dist');
console.log('🔍 Bắt đầu chạy Kịch bản Test Tự động (Static HTML)...');

if (!fs.existsSync(distDir)) {
  console.error('❌ LỖI NGHIÊM TRỌNG: Không tìm thấy thư mục build (docs/.vitepress/dist).');
  console.error('💡 Lời khuyên: Hãy đảm bảo bạn đã chạy lệnh build trước.');
  process.exit(1);
}

const htmlFiles = globSync('**/*.html', { cwd: distDir, absolute: true });

let totalTested = 0;
let totalErrors = 0;

htmlFiles.forEach(file => {
  const route = '/' + file.replace(distDir, '').replace(/\\/g, '/').replace(/^\//, ''); // Chuẩn hoá đường dẫn
  
  // BỘ LỌC CHỈ TEST NHỮNG TRANG TRONG INCLUDE LIST
  if (includeList.length > 0) {
    const shouldTest = includeList.some(includeStr => route.includes(includeStr));
    if (!shouldTest) return; // Nếu không khớp với từ khoá nào trong includeList thì bỏ qua
  }

  totalTested++;

  const html = fs.readFileSync(file, 'utf-8');
  const $ = cheerio.load(html); 
  
  let fileHasError = false;

  rules.forEach(rule => {
    try {
      const errorMsg = rule.test($, route);
      if (errorMsg) {
        if (!fileHasError) {
          console.log(`\n📄 Lỗi tại trang: ${route}`);
          fileHasError = true;
        }
        console.log(`  ❌ FAIL: ${rule.name} -> ${errorMsg}`);
        totalErrors++;
      }
    } catch (err) {
      console.log(`\n📄 Lỗi tại trang: ${route}`);
      console.log(`  🚨 CRASH trong rule "${rule.name}": ${err.message}`);
      totalErrors++;
    }
  });
});

console.log('\n================================');
console.log(`Đã quét tổng cộng: ${totalTested} trang (dựa trên Include List)`);

if (totalErrors > 0) {
  console.error(`🚨 Phát hiện TỔNG CỘNG ${totalErrors} LỖI.`);
  console.error(`🛑 DỪNG QUÁ TRÌNH PUBLIC! Hãy khắc phục các lỗi trên.\n`);
  process.exit(1);
} else {
  console.log(`✅ TUYỆT VỜI! Tất cả ${totalTested} trang đều vượt qua bài test cơ bản.`);
  console.log(`🚀 Trang web đã SẴN SÀNG để public!\n`);
  process.exit(0);
}
