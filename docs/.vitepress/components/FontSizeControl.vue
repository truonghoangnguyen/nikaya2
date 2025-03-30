<script setup lang="ts">
import { ref, watch, onMounted } from 'vue'

// Define font size options
const fontSizeOptions = [
  { label: 'A', value: '100%', description: 'Normal' },
  { label: 'A', value: '125%', description: 'Medium' },
  { label: 'A', value: '150%', description: 'Large' }
]

// Initialize with default font size
const selectedFontSize = ref('100%')

// Apply font size to translation content
const applyFontSize = (size: string) => {
  // #VPContent > div > div
  //const translationElements = document.querySelectorAll('.translation-content')
  const translationElements = document.querySelectorAll('.vp-doc')
  translationElements.forEach(element => {
    (element as HTMLElement).style.fontSize = size
  })
}

// Watch for changes in selected font size
watch(selectedFontSize, (newSize) => {
  applyFontSize(newSize)
  // Save preference to localStorage
  console.log(newSize)
  localStorage.setItem('preferred-font-size', newSize)
})

// Load saved preference on mount
onMounted(() => {
  const savedSize = localStorage.getItem('preferred-font-size')
  if (savedSize && fontSizeOptions.some(option => option.value === savedSize)) {
    selectedFontSize.value = savedSize
    applyFontSize(savedSize)
  }
})
</script>

<template>
  <div class="font-size-control">
    <div class="font-size-label">Text:</div>
    <div class="font-size-buttons">
      <label
        v-for="(option, index) in fontSizeOptions"
        :key="option.value"
        :class="['font-size-option', { active: selectedFontSize === option.value }]"
        :title="option.description"
      >
        <input
          type="radio"
          name="font-size"
          :value="option.value"
          v-model="selectedFontSize"
          class="sr-only"
        >
        <span class="option-label" :style="{ fontWeight: index > 0 ? 'bold' : 'normal', fontSize: `${1 + index * 0.2}em` }">
          {{ option.label }}
        </span>
      </label>
    </div>
  </div>
</template>

<style scoped>
.font-size-control {
  display: flex;
  align-items: center;
  height: var(--vp-nav-height-mobile);
  padding: 0 12px;
  margin: 0 4px;
}

.font-size-label {
  margin-right: 8px;
  font-size: 0.9rem;
  color: var(--vp-c-text-2);
}

.font-size-buttons {
  display: flex;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  overflow: hidden;
}

.font-size-option {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 28px;
  cursor: pointer;
  background-color: var(--vp-c-bg-soft);
  color: var(--vp-c-text-2);
  transition: all 0.2s ease;
  position: relative;
}

.font-size-option:not(:last-child) {
  border-right: 1px solid var(--vp-c-divider);
}

.font-size-option.active {
  background-color: var(--vp-c-brand-soft);
  color: var(--vp-c-brand);
}

.font-size-option:hover:not(.active) {
  background-color: var(--vp-c-bg-mute);
}

.sr-only {
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

@media (min-width: 768px) {
  .font-size-control {
    height: var(--vp-nav-height);
  }
}
</style>
