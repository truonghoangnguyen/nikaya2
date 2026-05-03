import tmcmnvi from './tmc.js';
import { buildComparePages } from '../../.vitepress/compare-render.js';

export default {
  paths: () => buildComparePages(tmcmnvi, 'kinhtangchi/c-sujato-tmc-vi'),
};
