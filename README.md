# deviengeorge.me

Personal portfolio website for Devien George, a Full-Stack Software Engineer.

Built with Astro, Tailwind CSS v4, and MDX. Minimal editorial design with typography-driven aesthetics.

## Tech Stack

- **Astro 6** — Static site generator
- **Tailwind CSS v4** — Utility-first styling
- **MDX** — Blog posts and project case studies
- **TypeScript** — Type safety

## Development

```sh
npm install
npm run dev        # http://localhost:4321
npm run build      # Static build → dist/
npm run preview    # Preview production build
```

## Deployment

Deployed on Contabo VPS via Coolify using Docker:

```sh
docker build -t portfolio .
```

## Structure

```
src/
  layouts/       Base HTML layout with meta tags and fonts
  components/    Astro components (Nav, Hero, Stats, etc.)
  pages/         Route pages (index, blog, projects)
  content/       MDX content collections (projects, blog)
  styles/        Tailwind CSS with theme configuration
public/          Static assets (favicon, robots.txt, llms.txt)
```
