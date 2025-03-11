<script setup>
import thichminhchau from '../../kinhtrungbo/thichminhchau/filelist'
import nanamoli_bodhi from '../../kinhtrungbo/nanamoli-bodhi/filelist';

function handleButtonClick(url) {
  const supportedAuthors = ['nanamoli-bodhi', 'nanamoli-bodhi-vi'];
  const authorCompareMap = {
    'nanamoli-bodhi': 'c-nm-tmc',
    'nanamoli-bodhi-vi': 'c-nm-tmc-vi'
  };

  // (1) Parse the URL
  const urlParts = url.split('/');
  //   console.log(urlParts);  // Output: ['', 'kinhtrungbo', 'nanamoli-bodhi', '001-the-root-of-all-things']

  if (urlParts.length < 4) {
    //console.error("Invalid URL format.");
    return null; // Or handle the error as needed
  }

  const kinhTrungBo = urlParts[1];  // "kinhtrungbo"
  const author = urlParts[2];      // "nanamoli-bodhi"
  const filename = urlParts[3];    // "001-the-root-of-all-things"

  if (!supportedAuthors.includes(author)) {
    //console.error("Unsupported author:", author);
    return null; // Or handle the error
  }

  const fileIdStr = filename.split('-')[0]; // "001"
    //console.log(fileIdStr);
  const fileId = parseInt(fileIdStr, 10);
   // console.log(fileId);

  if (isNaN(fileId)) {
    //console.error("Invalid file ID:", fileIdStr);
    return null; // Or handle the error
  }

  // (2) Get data (already provided in the problem statement)

  // (3) Get the corresponding link from thichminhchau
  if (fileId > thichminhchau.length || fileId < 1) {
      console.error("fileId out of range", fileId);
      return null;
  }
  const thichMinhChauLink = thichminhchau[fileId - 1].link;
    // console.log(thichMinhChauLink); // /kinhtrungbo/thichminhchau/001-kinh-phap-mon-can-ban.md
  const tmcFilename = thichMinhChauLink.split('/').pop().replace(".md", ""); // "001-kinh-phap-mon-can-ban"
     //console.log(tmcFilename);

  // (4) Generate the final URL
  const compareAuthor = authorCompareMap[author];
//   console.log(compareAuthor); //c-nm-tmc
  const finalURL = `/${kinhTrungBo}/${compareAuthor}/${tmcFilename}`;

  return finalURL;
}

function sayHello() {
  const currentURL = window.location.pathname; // Get the current URL from the browser
    //  console.log(currentURL);

  const newURL = handleButtonClick(currentURL);

  if (newURL) {
    console.log("Generated URL:", newURL);
    window.location.href = newURL;
    // You can now use this newURL to:
    // 1. Redirect the user: window.location.href = newURL;
    // 2. Update a link on the page: document.getElementById('someLinkId').href = newURL;
    // 3. Display it in a text field: document.getElementById('someTextField').value = newURL;
    // 4.  send to server.
  }

  // pathname: window.location.pathname, // e.g., "/path/to/page.html"
        // search: window.location.search,     // e.g., "?param1=value1¶m2=value2" (query parameters)
  // http://localhost:5173/kinhtrungbo/nanamoli-bodhi/001-the-root-of-all-things
  // http://localhost:5173/kinhtrungbo/nanamoli-bodhi-vi/001-the-root-of-all-things.vi
  // http://localhost:5173/kinhtrungbo/thichminhchau/001-kinh-phap-mon-can-ban
  // http://localhost:5173/kinhtrungbo/c-nm-tmc-vi/tmc-mn-bodhi-001-kinh-phap-mon-can-ban.html

  //alert('Hello World!');
}
</script>

<template>
  <div class="compare-button-container">
    <button class="compare-button" @click="sayHello" title="Compare translations">
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
