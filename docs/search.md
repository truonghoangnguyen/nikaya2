---
layout: page
---

<script setup>
import SearchPage from './.vitepress/theme/components/SearchPage.vue'
import { searchItems } from '/search-items.js'
</script>

<SearchPage :items="searchItems" />