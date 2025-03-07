---
title: "aaaq"
layout: page
---

<script setup>
import { useData } from 'vitepress'
import { computed, watch } from 'vue'

const { params, page } = useData()
// const slug = computed(() => params.value.slug);
const data = computed(() => params.value.data);
const nextLink = data.value.nextlink
const backLink = data.value.backlink
document.title = data.value.title
// const nextLink = computed(() => {
//   if (data.value?.nextlink) {
//     return {
//       text: data.value.title,
//       link: data.value.nextlink
//     }
//   }
//   return null
// })

// const nextInfo = {
//   text: 'aaa',
//   link: '/'
// }

// <!-- <ChapterCompare
//   :slug="slug"
//   :left="data.left"
//   :right="data.right"
//   :parts="data.parts || 1"
//   :leftTitle="data.leftTitle"
//   :rightTitle="data.rightTitle"
//   :notePath="data.notePath"
// /> -->
</script>


<TextCompare
  :leftPath="data.left"
  :rightPath="data.right"
  notePath=""
  :leftTitle="data.leftTitle"
  :rightTitle="data.rightTitle"
/>

 <!-- <div class="next">
    <span>Next Page</span>
    <a :href="nextInfo.link">{{ nextInfo.text }}</a>
  </div>
-->
<!-- <div v-if="backLink" class="next-link">
  <a :href="backLink.link">{{ backLink.text }}</a>
</div>

<div v-if="nextLink" class="next-link">
  <a :href="nextLink.link">{{ nextLink.text }}</a>
</div> -->

<nav data-v-29ec59c0="" class="prev-next" aria-labelledby="doc-footer-aria-label">
  <span data-v-29ec59c0="" class="visually-hidden" id="doc-footer-aria-label">Pager</span>
  <div v-if="backLink" data-v-29ec59c0="" class="pager">
    <a data-v-29ec59c0="" class="VPLink link pager-link prev" :href="backLink.link">
      <span data-v-29ec59c0="" class="desc">Previous</span>
      <span data-v-29ec59c0="" class="title">{{ backLink.text }}</span>
    </a>
  </div>
  <div v-if="nextLink" data-v-29ec59c0="" class="pager">
    <a data-v-29ec59c0="" class="VPLink link pager-link next" :href="nextLink.link">
      <span data-v-29ec59c0="" class="desc">Next</span>
      <span data-v-29ec59c0="" class="title">{{ nextLink.text }}</span>
    </a>
  </div>
</nav>