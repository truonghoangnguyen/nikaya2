<template>
  <div class="nav-font-size-button">
    <FontSizeControl />
  </div>
</template>

<script setup>
import FontSizeControl from '../components/FontSizeControl.vue'
</script>

<style scoped>
.nav-font-size-button {
  display: flex;
  align-items: center;
  height: var(--vp-nav-height);
  margin-left: 12px;
}
</style>
