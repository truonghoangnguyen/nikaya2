import fs from 'fs';
import path from 'path';
import * as cheerio from 'cheerio';
import { globSync } from 'glob';

// ==========================================
// CẤU HÌNH BẬT/TẮT TỪNG BƯỚC TEST
// Đặt false để bỏ qua bước đó.
// ==========================================
const stepConfig = {
  'step-1-title': true,  // Thẻ <title>
  'step-2-description': true,  // Meta description
  'step-3-canonical': true,  // Canonical
  'step-4-h1-empty': true,  // H1 không rỗng
  'step-5-og': true,  // Open Graph (og:title, og:description, og:image, og:url)
  'step-6-viewport': true,  // <meta name="viewport"> (mobile-friendly)
  'step-7-jsonld': true,  // Structured data JSON-LD (Schema.org)
};

// ==========================================
// CẤU HÌNH ĐIỀU KIỆN TEST (DỄ DÀNG CẬP NHẬT)
// ==========================================
const rules = [
  {
    key: 'step-1-title',
    name: 'Phải có thẻ <title>',
    test: ($, route) => {
      const title = $('title').text();
      if (!title || title.trim() === '') return 'Thiếu hoặc rỗng thẻ <title>';
      return null;
    }
  },
  {
    key: 'step-2-description',
    name: 'Phải có thẻ Meta Description',
    test: ($, route) => {
      const desc = $('meta[name="description"]').attr('content');
      if (!desc || desc.trim() === '') return 'Thiếu hoặc rỗng thẻ meta description';
      if (desc.length < 10) return 'Meta description quá ngắn (< 10 ký tự)';
      return null;
    }
  },
  {
    key: 'step-3-canonical',
    name: 'Phải có thẻ Canonical (chống trùng lặp nội dung)',
    test: ($, route) => {
      const canonical = $('link[rel="canonical"]').attr('href');
      if (!canonical) return 'Thiếu thẻ link rel="canonical"';
      return null;
    }
  },
  {
    key: 'step-4-h1-empty',
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
  },
  {
    key: 'step-5-og',
    name: 'Phải có thẻ Open Graph (chia sẻ Facebook/Zalo)',
    test: ($, route) => {
      const required = ['og:title', 'og:description', 'og:image', 'og:url'];
      const missing = [];
      for (const prop of required) {
        const val = $(`meta[property="${prop}"]`).attr('content');
        if (!val || val.trim() === '') missing.push(prop);
      }
      if (missing.length > 0) return `Thiếu thẻ Open Graph: ${missing.join(', ')}`;
      return null;
    }
  },
  {
    key: 'step-6-viewport',
    name: 'Phải có thẻ <meta name="viewport"> (mobile-friendly)',
    test: ($, route) => {
      const viewport = $('meta[name="viewport"]').attr('content');
      if (!viewport || viewport.trim() === '') return 'Thiếu thẻ meta viewport';
      if (!/width\s*=/.test(viewport)) return 'Meta viewport thiếu thuộc tính width';
      return null;
    }
  },
  {
    key: 'step-7-jsonld',
    name: 'Phải có Structured Data JSON-LD (Schema.org)',
    test: ($, route) => {
      const scripts = $('script[type="application/ld+json"]');
      if (scripts.length === 0) return 'Thiếu thẻ <script type="application/ld+json">';

      const headScripts = $('head script[type="application/ld+json"]');
      if (headScripts.length > 1) {
        return `Có nhiều hơn 1 thẻ <script type="application/ld+json"> trong header (phát hiện ${headScripts.length})`;
      }

      let validCount = 0;
      let parseError = null;
      scripts.each((i, el) => {
        const raw = $(el).contents().text();
        if (!raw || raw.trim() === '') return;
        try {
          const data = JSON.parse(raw);
          if (data && (data['@context'] || data['@graph'])) validCount++;
          else parseError = 'JSON-LD thiếu @context hoặc @graph';
        } catch (e) {
          parseError = `JSON-LD parse lỗi: ${e.message}`;
        }
      });
      if (validCount === 0) return parseError || 'Không có JSON-LD hợp lệ';
      return null;
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
  '/kinhtrungbo/thichminhchau/mn-001-kinh-phap-mon-can-ban.md',
  '/kinhtrungbo/thichminhchau/mn-152-kinh-can-tu-tap.md',
  '/kinhtrungbo/pali-vi/',
  '/kinhtrungbo/pali-vi/mn-001.md',
  '/kinhtrungbo/pali-vi/mn-152.md',
  '/kinhtrungbo/pali/',
  '/kinhtrungbo/pali/mn-001-mulapariyayasutta.md',
  '/kinhtrungbo/pali/mn-152-indriyabhavanasutta.md',
  '/kinhtrungbo/c-pali-tmc-vi/',
  '/kinhtrungbo/c-pali-tmc-vi/mnc-001-kinh-phap-mon-can-ban',
  "/kinhtrungbo/c-pali-tmc-vi/mnc-152-kinh-can-tu-tap",
  '/kinhtrungbo/c-nm-tmc-vi/',
  "/kinhtrungbo/c-nm-tmc-vi/mnc-001-kinh-phap-mon-can-ban",
  "/kinhtrungbo/c-nm-tmc-vi/mnc-152-kinh-can-tu-tap",
  '/kinhtrungbo/nanamoli-bodhi-en/',
  "/kinhtrungbo/nanamoli-bodhi-en/mn-001-the-root-of-all-things.md",
  "/kinhtrungbo/nanamoli-bodhi-en/mn-001-the-root-of-all-things.md",
  '/kinhtrungbo/nanamoli-bodhi-vi/',
  "/kinhtrungbo/nanamoli-bodhi-vi/mn-001-the-root-of-all-things.md",
  "/kinhtrungbo/nanamoli-bodhi-vi/mn-152-the-development-of-the-faculties.md",

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
// DANH SÁCH BỎ QUA (EXCLUDE LIST)
// ==========================================
// Bỏ qua những trang không cần chạy test (ví dụ: các trang ghi chú, phụ chú...)
const excludeList = [
  '/notes/',
  '/meta/',
  '/sum/',
  '/pali/',
  '/kinhtrungbo/pali-vi/',
  'notes'
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

  // BỘ LỌC BỎ QUA CÁC TRANG TRONG EXCLUDE LIST
  if (excludeList.length > 0) {
    const shouldExclude = excludeList.some(excludeStr => route.includes(excludeStr));
    if (shouldExclude) return; // Nếu khớp với bất kỳ từ khoá nào trong excludeList thì bỏ qua
  }

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
    if (stepConfig[rule.key] === false) return; // Bỏ qua bước đã tắt
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
