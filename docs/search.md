---
layout: page
title: Tìm kiếm Kinh điển Nikaya
description: Công cụ tra cứu và tìm kiếm nhanh các bài Kinh trong bộ Nikaya (Trường Bộ, Trung Bộ, Tương Ưng, Tăng Chi).
---

<script setup>
import SearchPage from './.vitepress/theme/components/SearchPage.vue'
import { searchItems } from '/search-items.js'
</script>

<SearchPage :items="searchItems" />