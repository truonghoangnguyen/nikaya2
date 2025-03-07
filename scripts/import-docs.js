#!/usr/bin/env node

/**
 * This script helps import markdown files into the VitePress structure
 * and generates comparison pages automatically.
 * 
 * Usage: node scripts/import-docs.js <source-dir>
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

// Get current directory in ESM
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Configuration
const config = {
  sourceDir: process.argv[2] || './source-docs',
  targetDir: './docs',
  authors: [
    { 
      id: 'nanamoli-bodhi', 
      name: 'Nanamoli-Bodhi',
      language: 'en',
      title: 'Original English'
    },
    { 
      id: 'nanamoli-bodhi-vi', 
      name: 'Nanamoli-Bodhi (Vietnamese)',
      language: 'vi',
      title: 'Vietnamese Translation 1'
    },
    { 
      id: 'thichminhchau', 
      name: 'Thich Minh Chau',
      language: 'vi',
      title: 'Vietnamese Translation 2'
    }
  ]
};

// Helper function to ensure directory exists
async function ensureDir(dir) {
  try {
    await fs.promises.mkdir(dir, { recursive: true });
  } catch (err) {
    if (err.code !== 'EEXIST') throw err;
  }
}

// Helper function to get all markdown files in a directory
async function getMarkdownFiles(dir) {
  const files = await fs.promises.readdir(dir);
  const markdownFiles = [];

  for (const file of files) {
    const filePath = path.join(dir, file);
    const fileStat = await fs.promises.stat(filePath);
    
    if (fileStat.isDirectory()) {
      const nestedFiles = await getMarkdownFiles(filePath);
      markdownFiles.push(...nestedFiles);
    } else if (file.endsWith('.md')) {
      markdownFiles.push(filePath);
    }
  }

  return markdownFiles;
}

// Helper function to get the relative path within a directory
function getRelativePath(fullPath, baseDir) {
  return path.relative(baseDir, fullPath);
}

// Helper function to create a comparison page
async function createComparisonPage(docId, translations) {
  if (translations.length < 2) {
    console.log(`Skipping comparison for ${docId} - not enough translations`);
    return;
  }

  // Get Vietnamese translations (if available)
  const viTranslations = translations.filter(t => t.language === 'vi');
  
  if (viTranslations.length < 2) {
    console.log(`Skipping comparison for ${docId} - not enough Vietnamese translations`);
    return;
  }

  // Get English original (if available)
  const enOriginal = translations.find(t => t.language === 'en');
  
  const compareDir = path.join(config.targetDir, 'compare');
  await ensureDir(compareDir);
  
  const compareFilePath = path.join(compareDir, `${docId}.md`);
  
  // Create comparison content
  let content = `---
title: Compare Translations - ${docId}
---

# Compare Translations: ${docId}

Below you can compare the two Vietnamese translations side by side.

## Vietnamese Translations Comparison

<TranslationCompare 
  leftPath="/${viTranslations[0].authorId}/${docId}.md" 
  rightPath="/${viTranslations[1].authorId}/${docId}.md"
  leftTitle="${viTranslations[0].authorName}" 
  rightTitle="${viTranslations[1].authorName}"
/>
`;

  // Add English original if available
  if (enOriginal) {
    content += `
## Original English Text

For reference, here is the original English text:

<div class="translation-card">
  <div class="translation-content">

\`\`\`md
${await fs.promises.readFile(enOriginal.filePath, 'utf8')}
\`\`\`

  </div>
</div>`;
  }

  await fs.promises.writeFile(compareFilePath, content, 'utf8');
  console.log(`Created comparison page: ${compareFilePath}`);
}

// Main function
async function main() {
  try {
    console.log('Starting document import...');
    
    // Create necessary directories
    for (const author of config.authors) {
      const authorDir = path.join(config.targetDir, author.id);
      await ensureDir(authorDir);
    }
    
    await ensureDir(path.join(config.targetDir, 'compare'));
    
    // Process each author's documents
    const docMap = new Map(); // Map to track documents across authors
    
    for (const author of config.authors) {
      const sourceAuthorDir = path.join(config.sourceDir, author.id);
      
      try {
        const markdownFiles = await getMarkdownFiles(sourceAuthorDir);
        
        for (const filePath of markdownFiles) {
          const relativePath = getRelativePath(filePath, sourceAuthorDir);
          const docId = path.basename(relativePath, '.md');
          const targetFilePath = path.join(config.targetDir, author.id, relativePath);
          
          // Ensure target directory exists
          await ensureDir(path.dirname(targetFilePath));
          
          // Copy the file
          await fs.promises.copyFile(filePath, targetFilePath);
          console.log(`Copied: ${filePath} -> ${targetFilePath}`);
          
          // Track this document for comparison
          if (!docMap.has(docId)) {
            docMap.set(docId, []);
          }
          
          docMap.get(docId).push({
            authorId: author.id,
            authorName: author.name,
            language: author.language,
            filePath: targetFilePath
          });
        }
      } catch (err) {
        if (err.code === 'ENOENT') {
          console.warn(`Warning: Author directory not found: ${sourceAuthorDir}`);
        } else {
          throw err;
        }
      }
    }
    
    // Create comparison pages
    for (const [docId, translations] of docMap.entries()) {
      await createComparisonPage(docId, translations);
    }
    
    // Update sidebar configuration
    console.log('Import completed successfully!');
    
  } catch (err) {
    console.error('Error during import:', err);
    process.exit(1);
  }
}

main();
