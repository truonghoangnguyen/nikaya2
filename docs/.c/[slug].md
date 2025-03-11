---
title: 'sosanh'
layout: page
---

<script setup>
import { useData } from 'vitepress'
import { computed, watch } from 'vue'

const { params, page } = useData()
const slug = computed(() => params.value.slug);
const data = computed(() => params.value.data);


document.title = data.value.title + ' | Your Site Name'

const nextLink = computed(() => {
  if (data.value?.nextlink) {
    return {
      text: data.value.title,
      link: data.value.nextlink
    }
  }
  return null
})

const nextInfo = {
  text: 'aaa',
  link: '/'
}

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

 <div class="next">
    <span>Next Page</span>
    <a :href="nextInfo.link">{{ nextInfo.text }}</a>
  </div>

<div v-if="nextLink" class="next-link">
  <a :href="nextLink.link">Next: {{ nextLink.text }}</a>
</div>