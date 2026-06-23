---
layout: page
title: Tìm kiếm Kinh điển Nikaya
description: Công cụ tra cứu và tìm kiếm nhanh các bài Kinh trong bộ Nikaya (Trường Bộ DN, Trung Bộ MN, Tương Ưng SN, Tăng Chi AN, tiểu bộ KN).
---

<script setup>
import SearchPage from './.vitepress/theme/components/SearchPage.vue'
import { searchItems } from '/search-items.js'
</script>

<SearchPage :items="searchItems" />