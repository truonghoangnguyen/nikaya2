---
title: "aaaq"
layout: home
---
<!-- [slug].md -->
<script setup>
import { useData } from 'vitepress'
import { computed, onMounted } from 'vue'

const { params } = useData()
const data = computed(() => params.value.data);
const nextLink = data.value.nextlink
const backLink = data.value.backlink

onMounted(() => {
  if (typeof window !== 'undefined') {
    window.document.title = data.value.title
  }
})
</script>

<TextCompare
  :leftPath="data.left"
  :rightPath="data.right"
  :leftTitle="data.leftTitle"
  :rightTitle="data.rightTitle"
  :leftContentHtml="data.leftHtml"
  :rightContentHtml="data.rightHtml"
  notePath=""
/>

<!-- Bạn có thể thêm các link điều hướng ở đây nếu muốn -->
<div style="display: flex; justify-content: space-between; margin-top: 2rem;">
  <span v-if="backLink">
    <a :href="backLink.link">&laquo; {{ backLink.text }}</a>
  </span>
  <span v-if="nextLink" style="margin-left: auto;">
    <a :href="nextLink.link">{{ nextLink.text }} &raquo;</a>
  </span>
</div>