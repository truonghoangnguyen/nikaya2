---
title: Translation2 Comparisons
layout: page
---

# Translation2 Comparisons

This page lists all available translation comparisons.

<script setup>
import { data as pathsData } from './[slug].paths.js'

const comparisons = pathsData.paths().map(item => ({
  slug: item.params.slug,
  title: item.frontmatter.title
}))
</script>

<div class="comparisons-list">
  <ul>
    <li v-for="comparison in comparisons" :key="comparison.slug">
      <a :href="`/c/${comparison.slug}`">{{ comparison.title }}</a>
    </li>
  </ul>
</div>

<style>
.comparisons-list ul {
  list-style-type: disc;
  padding-left: 1.5rem;
}

.comparisons-list li {
  margin-bottom: 0.5rem;
}
</style>
