#!/usr/bin/env node

/**
 * This script generates the sidebar configuration for VitePress based on the available documents.
 * 
 * Usage: node scripts/generate-sidebar.js
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

// Get current directory in ESM
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Configuration
const config = {
  docsDir: path.resolve(__dirname, '../docs'),
  authors: [
    { 
      id: 'nanamoli-bodhi', 
      name: 'Nanamoli-Bodhi',
      title: 'English Original'
    },
    { 
      id: 'nanamoli-bodhi-vi', 
      name: 'Nanamoli-Bodhi (Vietnamese)',
      title: 'Vietnamese Translation'
    },
    { 
      id: 'thichminhchau', 
      name: 'Thich Minh Chau',
      title: 'Thich Minh Chau Translation'
    }
  ],
  compareDir: 'compare',
  compareTitle: 'Compare Translations'
};

// Helper function to get all markdown files in a directory
async function getMarkdownFiles(dir) {
  try {
    const files = await fs.promises.readdir(dir);
    const markdownFiles = [];

    for (const file of files) {
      if (file.startsWith('.')) continue; // Skip hidden files
      
      const filePath = path.join(dir, file);
      const fileStat = await fs.promises.stat(filePath);
      
      if (fileStat.isDirectory()) {
        const nestedFiles = await getMarkdownFiles(filePath);
        markdownFiles.push(...nestedFiles.map(f => path.join(file, f)));
      } else if (file.endsWith('.md') && file !== 'index.md') {
        markdownFiles.push(file);
      }
    }

    return markdownFiles;
  } catch (err) {
    if (err.code === 'ENOENT') {
      console.warn(`Warning: Directory not found: ${dir}`);
      return [];
    }
    throw err;
  }
}

// Helper function to extract title from markdown file
async function extractTitle(filePath) {
  try {
    const content = await fs.promises.readFile(filePath, 'utf8');
    
    // Try to extract title from frontmatter
    const frontmatterMatch = content.match(/^---\s*\n([\s\S]*?)\n---/);
    if (frontmatterMatch) {
      const frontmatter = frontmatterMatch[1];
      const titleMatch = frontmatter.match(/title:\s*(.+)$/m);
      if (titleMatch) {
        return titleMatch[1].trim().replace(/["']/g, '');
      }
    }
    
    // Try to extract first heading
    const headingMatch = content.match(/^#\s+(.+)$/m);
    if (headingMatch) {
      return headingMatch[1].trim();
    }
    
    // Fall back to filename
    return path.basename(filePath, '.md')
      .replace(/-/g, ' ')
      .replace(/\b\w/g, c => c.toUpperCase());
    
  } catch (err) {
    console.warn(`Warning: Could not extract title from ${filePath}:`, err.message);
    return path.basename(filePath, '.md')
      .replace(/-/g, ' ')
      .replace(/\b\w/g, c => c.toUpperCase());
  }
}

// Generate sidebar items for a directory
async function generateSidebarItems(dir) {
  const files = await getMarkdownFiles(dir);
  const items = [];
  
  for (const file of files) {
    const filePath = path.join(dir, file);
    const title = await extractTitle(filePath);
    const link = `/${path.relative(config.docsDir, dir)}/${path.basename(file, '.md')}`;
    
    items.push({
      text: title,
      link
    });
  }
  
  // Sort items alphabetically
  items.sort((a, b) => {
    // Special case: always put "introduction" first
    if (a.link.endsWith('/introduction')) return -1;
    if (b.link.endsWith('/introduction')) return 1;
    
    return a.text.localeCompare(b.text);
  });
  
  return items;
}

// Main function
async function main() {
  try {
    console.log('Generating sidebar configuration...');
    
    const sidebar = {};
    
    // Generate sidebar for each author
    for (const author of config.authors) {
      const authorDir = path.join(config.docsDir, author.id);
      const items = await generateSidebarItems(authorDir);
      
      if (items.length > 0) {
        sidebar[`/${author.id}/`] = [
          {
            text: author.title,
            items
          }
        ];
      }
    }
    
    // Generate sidebar for comparison pages
    const compareDir = path.join(config.docsDir, config.compareDir);
    const compareItems = await generateSidebarItems(compareDir);
    
    if (compareItems.length > 0) {
      sidebar[`/${config.compareDir}/`] = [
        {
          text: config.compareTitle,
          items: compareItems
        }
      ];
    }
    
    // Output the sidebar configuration
    const sidebarConfig = JSON.stringify(sidebar, null, 2);
    console.log('Sidebar configuration generated:');
    console.log(sidebarConfig);
    
    // Optionally, you could write this to a file or update the config.ts file
    
  } catch (err) {
    console.error('Error generating sidebar:', err);
    process.exit(1);
  }
}

main();
