<script setup>
function goToIndex() {
  const parts = window.location.pathname.split('/');
  const author = parts[2];      // "nanamoli-bodhi"

  // current url is compare page, switch from compare Vi-Vi <-> En-Vi
  if (author.substring(0, 2) == 'c-'){
    const basePath = parts.join('/');
    const newUrl =`${parts[0]}/${parts[1]}/${parts[2]}/mucluc.html`;
    window.location.href = newUrl;
    return;
  }

  parts.pop();
  const basePath = parts.join('/');
  const newUrl = `${parts[0]}/${parts[1]}/${parts[2]}/meta/mucluc.html`;
  window.location.href = newUrl;
}
</script>

<template>
  <div class="index-button-container">
    <button class="index-button" @click="goToIndex" title="Mục lục">
      <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M3 5h18"></path>
        <path d="M3 12h18"></path>
        <path d="M3 19h18"></path>
      </svg>
      <span>Mục lục</span>
    </button>
  </div>
</template>

<style scoped>
.index-button-container {
  display: flex;
  align-items: center;
  padding: 0 12px;
  margin: 0 4px;
  height: var(--vp-nav-height-mobile);
}
.index-button {
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
.index-button:hover {
  color: var(--vp-c-brand);
  transform: scale(1.05);
}
.index-button:active {
  transform: scale(0.95);
}
.icon {
  width: 16px;
  height: 16px;
}
@media (min-width: 768px) {
  .index-button-container {
    height: var(--vp-nav-height);
  }
}
</style>