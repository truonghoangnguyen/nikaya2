<script setup>
import { computed } from 'vue'
import { useRoute, withBase } from 'vitepress'

const breadcrumbConfig = {
  // Khớp theo thư mục
  '/kinhtrungbo/': {
    name: 'Kinh Trung Bộ',
    '/c-nm-tmc-vi/': {
      name: 'Nanamoli−TMC',
    },
    '/c-pali-tmc-vi/': {
      name: 'Pali−TMC',
    },
    '/thichminhchau/': {
      name: 'Thích Minh Châu',
    },
  },
  '/kinhtieubo/': {
    name: 'Kinh Tiểu Bộ',
    '/c-pali-tmc-vi/': {
      name: 'Pali—TMC',
      '/iti/': {
        name: 'Kinh Phật Thuyết Như Vậy (Itivuttaka)',
      },
      '/ud/': {
        name: 'Kinh Phật Tự Thuyết (Udāna)',
      },
      '/snp/': {
        name: 'Kinh Tập (Suttanipāta)',
      }
    },
    '/pali-vi/': {
      name: 'Pali (Việt)',
      '/iti/': {
        name: 'Kinh Phật Thuyết Như Vậy (Itivuttaka)',
      },
      '/ud/': {
        name: 'Kinh Phật Tự Thuyết (Udāna)',
      },
      '/snp/': {
        name: 'Kinh Tập (Suttanipāta)',
      },
       '/mil/': {
        name: 'Nāgasena và Vua Milinda (Mi Tiên vấn Đáp)',
      },

    },
    '/thichminhchau/': {
      name: 'Thích Minh Châu',
      '/kn-001-tap-1-kinh-tieu-tung*': {
        name: 'Kinh Tiểu Tụng',
      },
      '/kn-003-tap-3-*': {
        name: 'Kinh Phật Tự Thuyết',
        url: 'kn-003-tap-3-kinh-phat-tu-thuyet',
      },
    },
  },
}

const route = useRoute()

const PRIORITY = {
  exact: 3,
  wildcard: 2,
  directory: 1,
}

const RESERVED_KEYS = new Set(['name', 'url'])

// Chuẩn hóa URL:
// - Bỏ query và hash
// - Bổ sung dấu / đầu tiên nếu thiếu
// - Loại bỏ dấu / lặp
// - Loại bỏ dấu / cuối (trừ root '/')
function normalizePath(path) {
  let result = String(path || '/').split(/[?#]/)[0]

  if (!result.startsWith('/')) {
    result = `/${result}`
  }

  result = result.replace(/\/{2,}/g, '/')

  if (result.length > 1) {
    result = result.replace(/\/+$/, '')
  }

  return result
}

// Chuẩn hóa tiền tố nhưng giữ lại / cuối nếu có
function normalizePrefix(path) {
  const hasTrailingSlash = path.endsWith('/')
  let result = normalizePath(path)

  if (hasTrailingSlash && result !== '/') {
    result += '/'
  }

  return result
}

// Ghép đường dẫn cha và con
function joinPattern(parent, child) {
  const cleanParent = String(parent || '').replace(/\/+$/, '')
  const cleanChild = String(child || '').replace(/^\/+/, '')

  if (!cleanParent) {
    return `/${cleanChild}`
  }

  if (!cleanChild) {
    return cleanParent || '/'
  }

  return `${cleanParent}/${cleanChild}`
}

// Xác định href cho từng cấp breadcrumb
function resolveHref(parentPattern, key, customUrl) {
  // Hỗ trợ tắt link nếu khai báo url: null hoặc url: false
  if (customUrl === null || customUrl === false) {
    return undefined
  }

  // Nếu có khai báo url tùy chỉnh
  if (typeof customUrl === 'string' && customUrl.trim()) {
    const trimmedUrl = customUrl.trim()

    // Đường dẫn tuyệt đối (/...) hoặc URL ngoài (http/https)
    if (trimmedUrl.startsWith('/') || /^https?:\/\//.test(trimmedUrl)) {
      return trimmedUrl
    }

    // Đường dẫn tương đối -> tự nối vào đường dẫn cha
    return joinPattern(parentPattern, trimmedUrl)
  }

  // Mặc định tự sinh từ pattern hiện tại
  const fullPattern = joinPattern(parentPattern, key)

  // Wildcard: bỏ dấu * ở cuối (không tự thêm dấu /)
  if (fullPattern.endsWith('*')) {
    return fullPattern.slice(0, -1)
  }

  return fullPattern
}

// Biên dịch cấu trúc nested thành danh sách rule phẳng (chạy 1 lần)
function compileBreadcrumbConfig(config, parentPattern = '', parentTrail = [], rules = []) {
  for (const [key, node] of Object.entries(config)) {
    if (RESERVED_KEYS.has(key) || !node || typeof node !== 'object') {
      continue
    }

    const fullPattern = joinPattern(parentPattern, key)
    const href = resolveHref(parentPattern, key, node.url)

    const currentTrail = node.name
      ? [...parentTrail, { label: node.name, href }]
      : parentTrail

    if (currentTrail.length > 0) {
      let type
      let prefix

      if (fullPattern.endsWith('*')) {
        type = 'wildcard'
        prefix = normalizePrefix(fullPattern.slice(0, -1))
      } else if (fullPattern.endsWith('/')) {
        type = 'directory'
        prefix = normalizePrefix(fullPattern)
      } else {
        type = 'exact'
        prefix = normalizePath(fullPattern)
      }

      rules.push({
        pattern: fullPattern,
        type,
        prefix,
        specificity: prefix.length,
        trail: currentTrail,
      })
    }

    // Đệ quy xử lý các mục con
    compileBreadcrumbConfig(node, fullPattern, currentTrail, rules)
  }

  return rules
}

const compiledRules = compileBreadcrumbConfig(breadcrumbConfig)

// Tìm quy tắc khớp nhất với URL hiện tại
function findBreadcrumb(path) {
  const currentPath = normalizePath(path)
  const matches = []

  for (const rule of compiledRules) {
    let matched = false

    if (rule.type === 'wildcard') {
      matched = currentPath.startsWith(rule.prefix)
    } else if (rule.type === 'directory') {
      const directoryPath = rule.prefix === '/' ? '/' : rule.prefix.slice(0, -1)
      matched =
        currentPath === directoryPath ||
        currentPath.startsWith(rule.prefix)
    } else {
      matched = currentPath === rule.prefix
    }

    if (matched) {
      matches.push(rule)
    }
  }

  // Ưu tiên:
  // 1. Khớp chính xác (exact)
  // 2. Tiền tố dài hơn (specificity cao hơn)
  // 3. Nếu độ dài bằng nhau thì wildcard ưu tiên hơn directory
  matches.sort((a, b) => {
    const exactDiff = (b.type === 'exact' ? 1 : 0) - (a.type === 'exact' ? 1 : 0)
    return (
      exactDiff ||
      b.specificity - a.specificity ||
      PRIORITY[b.type] - PRIORITY[a.type]
    )
  })

  return matches[0]?.trail || []
}

// Tự động cập nhật khi chuyển trang bằng VitePress Router
const breadcrumbs = computed(() => {
  return findBreadcrumb(route.path)
})
</script>

<template>
  <nav
    v-if="breadcrumbs.length"
    class="custom-breadcrumb"
    aria-label="Breadcrumb"
  >
    <ol>
      <li
        v-for="(item, index) in breadcrumbs"
        :key="index"
      >
        <a
          v-if="item.href"
          :href="withBase(item.href)"
          :class="{
            'breadcrumb-current': index === breadcrumbs.length - 1
          }"
        >
          {{ item.label }}
        </a>

        <span
          v-else
          class="breadcrumb-current"
        >
          {{ item.label }}
        </span>

        <span
          v-if="index < breadcrumbs.length - 1"
          class="breadcrumb-separator"
          aria-hidden="true"
        >
          ›
        </span>
      </li>
    </ol>
  </nav>
</template>

<style scoped>
.custom-breadcrumb {
  margin-bottom: 20px;
  font-family: var(--vp-font-family-base);
  font-size: 13px;
  line-height: 1.5;
  color: var(--vp-c-text-2);
}

.custom-breadcrumb ol {
  display: flex;
  align-items: baseline; /* Canh thẳng hàng theo đường chân chữ */
  flex-wrap: wrap;
  gap: 8px;
  padding: 0;
  margin: 0;
  list-style: none;
  font-style: normal;
}

.custom-breadcrumb li {
  display: inline-flex;
  align-items: baseline; /* Canh thẳng hàng theo đường chân chữ */
  gap: 8px;
  font-style: normal;
}

.custom-breadcrumb a {
  color: var(--vp-c-text-2);
  text-decoration: none;
  font-style: normal;
}

.custom-breadcrumb a:hover {
  color: var(--vp-c-brand-1);
}

.breadcrumb-separator {
  color: var(--vp-c-text-3);
  font-style: normal;
  user-select: none;
}

.breadcrumb-current {
  color: var(--vp-c-text-1);
  font-weight: 700; /* Dùng 700 (Bold) thay vì 600 để khớp chuẩn font Serif (Georgia/Times/Noto) */
  text-decoration: none;
  font-style: normal;
}
</style>