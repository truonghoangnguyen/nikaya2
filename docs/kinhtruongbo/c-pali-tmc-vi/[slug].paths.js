import tmcmnvi from './tmc.js';
import { buildComparePages } from '../../.vitepress/compare-render.js';

export default {
  paths: async () => {
    const pages = await buildComparePages(tmcmnvi, 'kinhtruongbo/c-pali-tmc-vi');
    return pages.map((page) => ({
      ...page,
      params: { ...page.params, data: { ...page.params.data, titleSuffix: 'Kinh Trường Bộ Pali-Thích Minh Châu' } },
    }));
  },
};
