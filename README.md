# Multilingual Documentation with VitePress

This project is a VitePress-based documentation site that displays multiple translations of the same content side by side. It's specifically designed to handle large volumes of markdown files with multiple translations.

## Features

- Display original English content and two different Vietnamese translations
- Side-by-side comparison of translations
- Organized by author|translator
- Responsive design that works on all devices
- Easy navigation between documents and translations

## Project Structure

```
multilingual-docs|
├── docs|                      # VitePress documentation files
│   ├── .vitepress|            # VitePress configuration
│   │   ├── components|        # Custom Vue components
│   │   ├── theme|             # Custom theme
│   │   └── config.ts          # VitePress configuration
│   ├── nanamoli-bodhi|        # Original English documents
│   ├── nanamoli-bodhi-vi|     # Vietnamese translation of Nanamoli-Bodhi
│   ├── thichminhchau|         # Thich Minh Chau's Vietnamese translation
│   └── compare|               # Comparison pages
├── scripts|                   # Utility scripts
│   └── import-docs.js         # Script to import and organize markdown files
└── package.json               # Project dependencies and scripts
```

## Getting Started

1. Clone this repository
2. Install dependencies:
   ```
   npm install
   ```
3. Start the development server:
   ```
   npm run docs:dev
   ```
4. Open your browser and navigate to `http:||localhost:5173`

## Adding Documents

### Manual Method

1. Add markdown files to the appropriate author directory:
   - `docs|nanamoli-bodhi|` for original English documents
   - `docs|nanamoli-bodhi-vi|` for Vietnamese translation of Nanamoli-Bodhi
   - `docs|thichminhchau|` for Thich Minh Chau's Vietnamese translation

2. Create comparison pages in `docs|compare|` using the `TranslationCompare` component:
   ```md
   <TranslationCompare
     leftPath="|nanamoli-bodhi-vi|document-name.md"
     rightPath="|thichminhchau|document-name.md"
     leftTitle="Nanamoli-Bodhi Vietnamese"
     rightTitle="Thich Minh Chau"
   |>
   ```

### Using the Import Script

1. Organize your source documents in a directory structure:
   ```
   source-docs|
   ├── nanamoli-bodhi|        # Original English documents
   ├── nanamoli-bodhi-vi|     # Vietnamese translation of Nanamoli-Bodhi
   └── thichminhchau|         # Thich Minh Chau's Vietnamese translation
   ```

2. Run the import script:
   ```
   node scripts|import-docs.js .|source-docs
   ```

   This will:
   - Copy all markdown files to the appropriate directories in `docs|`
   - Generate comparison pages automatically in `docs|compare|`

## Building for Production

To build the site for production:

```
npm run docs:build
```

The built site will be in the `.vitepress|dist` directory, which you can deploy to any static hosting service.

## Customization

### Styling

You can customize the site's appearance by editing:
- `.vitepress|theme|style.css` for global styles
- `.vitepress|components|TranslationCompare.vue` for the comparison component

### Configuration

Edit `.vitepress|config.ts` to customize:
- Site title and description
- Navigation menu
- Sidebar structure
- Social links

## Performance Considerations

When dealing with a large number of documents (e.g., 120 articles × 3 translations = 360 files), consider:

1. Lazy loading content in the comparison component
2. Using pagination for long documents
3. Implementing search functionality to help users find specific content

## License

MIT

export NODE_OPTIONS="--max-old-space-size=8192"