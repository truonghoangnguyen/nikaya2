import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

// Get the directory name
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Configuration
const basePath = path.join(__dirname, '..', 'docs', 'kinhtrungbo', 'thichminhchau');
const totalChapters = 152;

// Function to add frontmatter to a chapter file
function addFrontmatterToChapter(chapterNumber) {
  const filePath = path.join(basePath, `${chapterNumber}.md`);
  
  // Skip if file doesn't exist
  if (!fs.existsSync(filePath)) {
    console.log(`Chapter ${chapterNumber}.md doesn't exist. Skipping.`);
    return;
  }
  
  // Read the file content
  const content = fs.readFileSync(filePath, 'utf8');
  
  // Check if frontmatter already exists
  if (content.startsWith('---')) {
    console.log(`Chapter ${chapterNumber}.md already has frontmatter. Skipping.`);
    return;
  }
  
  // Determine previous and next links
  const prevLink = chapterNumber === 1 
    ? '/kinhtrungbo/thichminhchau/' 
    : `/kinhtrungbo/thichminhchau/${chapterNumber - 1}`;
  
  const nextLink = chapterNumber === totalChapters 
    ? null 
    : `/kinhtrungbo/thichminhchau/${chapterNumber + 1}`;
  
  // Create frontmatter
  let frontmatter = '---\n';
  frontmatter += `title: "${chapterNumber}. Kinh"\n`;
  frontmatter += `prev: ${prevLink}\n`;
  
  if (nextLink) {
    frontmatter += `next: ${nextLink}\n`;
  }
  
  frontmatter += '---\n\n';
  
  // Add frontmatter to content
  const newContent = frontmatter + content;
  
  // Write back to file
  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`Added frontmatter to chapter ${chapterNumber}.md`);
}

// Process all chapters
console.log('Adding frontmatter to chapter files...');
for (let i = 1; i <= totalChapters; i++) {
  addFrontmatterToChapter(i);
}
console.log('Done!');
