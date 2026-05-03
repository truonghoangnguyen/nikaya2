import tmcmnvi from './tmc.js';
import { buildComparePages } from '../../.vitepress/compare-render.js';

export default {
  paths: () => buildComparePages(tmcmnvi, 'kinhtuongung/c-sujato-tmc-vi'),
};
