---
title: "aaaq"
layout: home
---

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

<TextCompare2
  :leftPath="data.left"
  :rightPath="data.right"
  :leftContentHtml="data.leftHtml"
  :rightContentHtml="data.rightHtml"
  :leftTitle="data.leftTitle"
  :rightTitle="data.rightTitle"
/>


<style>
.custom-prev-next {
  display: flex;
  justify-content: space-between;
  border-top: 1px solid var(--vp-c-divider);
  padding-top: 1rem;
  margin-top: 2.5rem;
}

.custom-pager {
  display: flex;
  flex-direction: column;
  max-width: 48%;
}

.custom-pager.prev {
  margin-right: auto;
}

.custom-pager.next {
  margin-left: auto;
  text-align: right;
}

.custom-pager-link {
  display: inline-block;
  font-weight: 500;
  color: var(--vp-c-brand);
  text-decoration: none;
}

.custom-pager-link:hover {
  color: var(--vp-c-brand-dark);
}

.custom-desc {
  display: block;
  color: var(--vp-c-text-2);
  font-size: 0.9em;
  margin-bottom: 0.2em;
}

.custom-title {
  display: block;
  line-height: 1.3;
}

.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}
</style>

<nav class="custom-prev-next" aria-labelledby="custom-footer-aria-label">
  <span class="visually-hidden" id="custom-footer-aria-label">Pager</span>
  <div v-if="backLink" class="custom-pager prev">
    <a class="custom-pager-link" :href="backLink.link">
      <span class="custom-desc">Previous</span>
      <span class="custom-title">{{ backLink.text }}</span>
    </a>
  </div>
  <div v-if="nextLink" class="custom-pager next">
    <a class="custom-pager-link" :href="nextLink.link">
      <span class="custom-desc">Next</span>
      <span class="custom-title">{{ nextLink.text }}</span>
    </a>
  </div>
</nav>