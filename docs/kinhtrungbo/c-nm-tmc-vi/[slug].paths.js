import tmcmnvi from './tmc.js';
import { buildComparePages } from '../../.vitepress/compare-render.js';

export default {
  paths: () => buildComparePages(tmcmnvi, 'kinhtrungbo/c-nm-tmc-vi'),
};
