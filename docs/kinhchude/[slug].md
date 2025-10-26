---
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


<!-- Component của bạn giữ nguyên, nó vẫn sẽ hoạt động -->
<TextCompare
  :leftPath="data.left"
  :rightPath="data.right"
  :leftTitle="data.leftTitle"
  :rightTitle="data.rightTitle"
  :leftContentHtml="data.leftHtml"
  :rightContentHtml="data.rightHtml"
  notePath=""
/>

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