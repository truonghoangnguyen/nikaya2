<script setup>
import { ref, watch, onMounted } from 'vue'
import { useRoute, useRouter, withBase } from 'vitepress'

const route = useRoute()
const router = useRouter()

let lookupPromise = null
function loadLookup() {
  if (!lookupPromise) {
    lookupPromise = fetch(withBase('/compare-lookup.json'))
      .then((r) => (r.ok ? r.json() : {}))
      .catch(() => ({}))
  }
  return lookupPromise
}

const target = ref(null)

async function resolveTarget() {
  const lookup = await loadLookup()
  const path = route.path.replace(/\/$/, '/index.html')
  target.value = lookup[path] || null
}

onMounted(resolveTarget)
watch(() => route.path, resolveTarget)

function goToCompare() {
  if (target.value) router.go(target.value)
}
</script>

<template>
  <div v-if="target" class="compare-button-container">
    <button class="compare-button" @click="goToCompare" title="Compare translations">
      <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M16 3l4 4-4 4"></path>
        <path d="M20 7H4"></path>
        <path d="M8 21l-4-4 4-4"></path>
        <path d="M4 17h16"></path>
      </svg>
      <span>Compare</span>
    </button>
  </div>
</template>

<style scoped>
.compare-button-container {
  display: flex;
  align-items: center;
  padding: 0 12px;
  margin: 0 4px;
  height: var(--vp-nav-height-mobile);
}

.compare-button {
  display: flex;
  align-items: center;
  gap: 6px;
  background: transparent;
  border: none;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 500;
  padding: 0;
  color: var(--vp-c-text-1);
  transition: color 0.25s, transform 0.25s;
  outline: none;
}

.compare-button:hover {
  color: var(--vp-c-brand);
  transform: scale(1.05);
}

.compare-button:active {
  transform: scale(0.95);
}

.icon {
  width: 16px;
  height: 16px;
}

@media (min-width: 768px) {
  .compare-button-container {
    height: var(--vp-nav-height);
  }
}
</style>
