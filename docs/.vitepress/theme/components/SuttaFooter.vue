<script setup lang="ts">
import { useData } from 'vitepress'
import { computed } from 'vue'

const { frontmatter } = useData()

type TranslatorRef = { name: string; url?: string }
type SuttaFooterData = {
  translators: TranslatorRef[]
  dateModified: string
  compareLabel?: string
}

const info = computed<SuttaFooterData | undefined>(() => {
  const raw = (frontmatter.value as any).suttaFooter
  if (!raw || !Array.isArray(raw.translators) || raw.translators.length === 0) return undefined
  return raw as SuttaFooterData
})
</script>

<template>
  <div v-if="info" class="sutta-footer">
    <span v-if="info.compareLabel" class="sutta-footer__label">Bản đối chiếu:</span>
    <span v-else class="sutta-footer__label">Bản dịch:</span>

    <span class="sutta-footer__translators">
      <template v-for="(t, i) in info.translators" :key="i">
        <a v-if="t.url" :href="t.url" rel="noopener" target="_blank">{{ t.name }}</a>
        <span v-else>{{ t.name }}</span>
        <span v-if="i < info.translators.length - 1" class="sutta-footer__sep"> &amp; </span>
      </template>
    </span>

    <span class="sutta-footer__sep"> · </span>
    <span>Cập nhật: <time :datetime="info.dateModified">{{ info.dateModified }}</time></span>
  </div>
</template>

<style scoped>
.sutta-footer {
  max-width: 720px;
  margin: 2rem auto 0;
  padding: 0.75rem 1rem;
  border-top: 1px solid var(--vp-c-divider);
  font-size: 0.85rem;
  line-height: 1.5;
  color: var(--vp-c-text-2);
  text-align: center;
}
.sutta-footer__label {
  font-weight: 500;
  margin-right: 0.25rem;
}
.sutta-footer a {
  color: var(--vp-c-text-2);
  text-decoration: underline;
  text-decoration-color: var(--vp-c-divider);
}
.sutta-footer a:hover {
  color: var(--vp-c-brand-1);
  text-decoration-color: currentColor;
}
.sutta-footer__sep {
  opacity: 0.6;
}
</style>
