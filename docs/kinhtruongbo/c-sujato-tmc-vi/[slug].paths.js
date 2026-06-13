import tmcmnvi from './tmc.js';
import { buildComparePages } from '../../.vitepress/compare-render.js';

// export default {
//   paths: () => buildComparePages(tmcmnvi, 'kinhtruongbo/c-sujato-tmc-vi'),
// };

export default {
  paths: async () => {
    const pages = await buildComparePages(tmcmnvi, 'kinhtruongbo/c-sujato-tmc-vi');
    return pages.map((page) => ({
      ...page,
      params: { ...page.params, data: { ...page.params.data, titleSuffix: 'Kinh Trường Bộ Sujato-Thích Minh Châu' } },
    }));
  },
};
