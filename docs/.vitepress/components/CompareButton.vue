<script setup>
// import thichminhchau from '../../kinhtrungbo/thichminhchau/meta/filelist'
// import nanamoli_bodhi from '../../kinhtrungbo/nanamoli-bodhi-en/filelist';

/**
 * 2 loại so sánh:
 * 1. từ tác giả vd:
 *    - /kinhtangchi/sujato-vi/acb.html -> /kinhtangchi/c-sujato-tmc-vi/acb.html
 *    - /kinhtangchi/thichminhchau/acb.html -> /kinhtangchi/c-sujato-tmc-vi/acb.html
 *    - /kinhtrungbo/nanamoli-bodhi-vi/acb.html -> /kinhtrungbo/c-nm-tmc-vi/acb.html
 * 2. từ so sánh vd:
 *    - /kinhtangchi/c-sujato-tmc-vi/acb.html -> /kinhtangchi/c-sujato-tmc-en/acb.html
 *    - /kinhtangchi/c-sujato-tmc-en/acb.html -> /kinhtangchi/c-sujato-tmc-vi/acb.html
 *    - /kinhtrungbo/c-nm-tmc-vi/acb.html -> /kinhtrungbo/c-nm-tmc-en/acb.html
 * Parses the URL, extracts relevant information, and generates a comparison URL.
 * @param {string} url - /kinhtrungbo/nanamoli-bodhi/001-the-root-of-all-things
 * @returns {string|null} The generated comparison URL or null if invalid.
 */

function toHomeCompare(url) {
  // this is support paths, allow to compare
  //const compareBooks = ['c-nm-tmc-en', 'c-nm-tmc-vi']
  const baseBooks = ['nanamoli-bodhi-vi', 'nanamoli-bodhi-en', 'thichminhchau'];
  // const authorCompareMap = {
  //   'nanamoli-bodhi': 'c-nm-tmc',
  //   'nanamoli-bodhi-vi': 'c-nm-tmc-vi'
  // };

  // (1) Parse the URL
  const urlParts = url.split('/');
  //   console.log(urlParts);  // Output: ['', 'kinhtrungbo', 'nanamoli-bodhi', '001-the-root-of-all-things']

  if (urlParts.length < 4) {
    //console.error("Invalid URL format.");
    return null; // Or handle the error as neededxxxxx
  }

  const book = urlParts[1];  // "kinhtrungbo"
  const author = urlParts[2];      // "nanamoli-bodhi"
  const filename = urlParts[3];    // "001-the-root-of-all-things"

  // current url is compare page, switch from compare Vi-Vi <-> En-Vi
  if (author.substring(0, 2) == 'c-'){
    const last2Chars = author.slice(-2);
    const newLast2Chars = last2Chars === 'vi' ? 'en' : 'vi';
    const newBook = author.slice(0, -2) + newLast2Chars;
    return `/${book}/${newBook}/${filename}`;
  }

  if (!baseBooks.includes(author)) {
    //console.error("Unsupported author:", author);
    return null; // Or handle the error
  }


  function findIndexByFilename(filename, listfile) {
    const baseFilename = filename.split('?')[0].replace(/\.html$/, '');

    // Create a regular expression from the base filename.  Escape special characters for safety.
    const regex = new RegExp(baseFilename.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));

    for (let i = 0; i < listfile.length; i++) {
        if (listfile[i].link && regex.test(listfile[i].link)) {
            return i;
        }
    }
    return -1;
  }
  const fileId = findIndexByFilename(filename, thichminhchau);
  if (fileId == -1){
    console.error("fileId out of range", filename);
    return null;
  }
  const thichMinhChauLink = thichminhchau[fileId - 1].link;

    // console.log(thichMinhChauLink); // /kinhtrungbo/thichminhchau/001-kinh-phap-mon-can-ban.md
  const tmcFilename = thichMinhChauLink.split('/').pop().replace(".md", ""); // "001-kinh-phap-mon-can-ban"
     //console.log(tmcFilename);

  // (4) Generate the final URL
  const homeCompare = 'c-nm-tmc-vi' //authorCompareMap[author];
//   console.log(compareAuthor); //c-nm-tmc
  const finalURL = `/${book}/${homeCompare}/${tmcFilename}`;

  return finalURL;
}

function toComparePage() {
  const currentURL = window.location.pathname; // Get the current URL from the browser
    //  console.log(currentURL);

  const newURL = toHomeCompare(currentURL);

  if (newURL) {
    console.log("Generated URL:", newURL);
    window.open(newURL, '_blank');
  }
  else{
    window.location.href = "/compare.html";
  }
}
</script>

<template>
  <div class="compare-button-container">
    <button class="compare-button" @click="toComparePage" title="Compare translations">
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
