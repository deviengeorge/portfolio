# Portfolio — deviengeorge.me

## Tech Stack
- Astro 6 (static site generator)
- Tailwind CSS v4 (utility-first, `class` strategy dark mode)
- MDX for content collections
- TypeScript (strict mode)

## Conventions
- Components in `src/components/` as `.astro` files
- Content collections in `src/content/` with schemas in `src/content.config.ts`
- Layouts in `src/layouts/`
- Use semantic HTML elements (`<article>`, `<section>`, `<nav>`, `<main>`)
- Dark mode: toggle `.dark` class on `<html>`, use Tailwind `dark:` prefix
- Fonts: Instrument Serif (headings), DM Sans (body)
- Design: minimal, editorial, typography-driven. No animations.
- Colors: warm stone palette with amber accent

## Commands
- `npm run dev` — Start dev server (port 4321)
- `npm run build` — Build static site to `dist/`
- `npm run preview` — Preview production build
- `docker build -t portfolio .` — Build Docker image

## Deployment
- Hosted on Contabo VPS via Coolify
- Docker: multi-stage build (node → nginx)
- Site URL: https://deviengeorge.me
