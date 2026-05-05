// CV - Devien George Francis

#set document(
  title: "Full-Stack Software Engineer - Devien George's CV",
  author: "Devien George",
)

#set page(
  paper: "a4",
  margin: (top: 2cm, bottom: 2cm, left: 2cm, right: 2cm),
  numbering: none,
)

#set text(font: "Charis SIL", size: 10pt, fill: black, lang: "en")
#set par(justify: false, leading: 0.55em, spacing: 0.55em)
#set list(indent: 0.4cm, body-indent: 0.15cm, spacing: 0.45em, marker: [•])

// --- Reusable Components ---

#let section-title(title) = {
  v(0.3cm)
  text(weight: "bold", size: 12.5pt, title)
  v(1pt)
  line(length: 100%, stroke: 0.5pt + black)
  v(0.2cm)
}

#let two-col-entry(left-content, date) = {
  grid(
    columns: (1fr, auto),
    column-gutter: 10pt,
    left-content,
    align(right, text(style: "italic", date)),
  )
}

#let separator = box(inset: (x: 4pt), "|")

// --- Header ---

#align(center)[
  #text(size: 25pt)[Devien George Francis]
  #v(-2pt)
  #text(size: 15pt)[Full-Stack Software Engineer]
  #v(5pt)
  #text(size: 10pt)[
    Cairo, Egypt#separator#link("mailto:deviengeorge99@gmail.com")[deviengeorge99\@gmail.com]#separator#link("tel:+201281089983")[+20 0128 108 9983]#separator#link("https://linkedin.com/in/deviengeorge")[linkedin.com/in/deviengeorge]
    #linebreak()
    #link("https://github.com/deviengeorge")[github.com/deviengeorge]#separator#link("https://x.com/devien_george")[twitter.com/devien\_george]
  ]
]

// --- Professional Summary ---

#section-title("Professional Summary")

Full-Stack Software Engineer with 4+ years of experience building and scaling production web platforms, complemented by a strong teaching background across 5+ institutions. Built systems serving *1,000+ daily users* across *24 organizations*, led cross-functional teams, and mentored *70+ students* in full-stack and microservices development. Proven track record in performance optimization (up to 45% SEO gains, 35% faster load times), *CI/CD* pipeline design, multi-server deployment and infrastructure management, and delivering scalable software from architecture to deployment. Leverages AI-assisted development tools (*Claude Code*, *OpenCode* with Qwen 3.7 Coder) to accelerate engineering workflows.

// --- Technologies ---

#section-title("Technologies")

*Backend:* Laravel, Node.js (Express, NestJS, AdonisJS), Java (Spring Boot), C\#, .NET 8
#v(0.15cm)
*Database:* PostgreSQL, MySQL, MongoDB, Redis, Elasticsearch, Database Indexing, Caching, Replication, Sharding
#v(0.15cm)
*Frontend:* React, Next.js, Vue.js, Nuxt.js, Angular, TypeScript, JavaScript (ES6+), jQuery, Pug/Jade, Sass/SCSS, TailwindCSS, Bootstrap, Framer Motion, Storybook, Cypress, Testing Library, Puppeteer, Electron
#v(0.15cm)
*DevOps & Cloud:* Docker, Jenkins, GitHub Actions, Kubernetes, AWS (EC2, S3, RDS), Nginx, Linux, Bash, CI/CD Pipelines, Podman, Ansible, Multi-Server Deployment & Infrastructure Management
#v(0.15cm)
*Architecture:* Software Architecture, Microservices, Event-Driven Systems, OOP, SOLID Principles, Design Patterns, UML, Monorepo Architecture, Distributed Systems, Queues
#v(0.15cm)
*Testing:* JUnit, Mockito, Cypress, Testing Library, Postman, Newman, Integration Testing, Unit Testing, E2E Testing
#v(0.15cm)
*Tools:* Git, GitHub, GitLab, IntelliJ IDEA, VS Code, Figma, Agile / Scrum, Jira, Claude Code, OpenCode (Qwen 3.7 Coder)

// --- Experience ---

#section-title("Experience")

#two-col-entry(
  [*Full Stack Software Engineer (Contract)*, ALReserve -- Remote],
  [Apr. 2026 – Present],
)
#v(0.10cm)
- Building a membership-based luxury accommodation booking platform for GCC travelers visiting the UK, USA, and Europe.
- Developing the full-stack application using *React 19*, *Hono*, *Bun*, and *Supabase* within a *TypeScript monorepo* architecture.
- Integrating third-party booking APIs (*HyperGuest*, *Amadeus*) for real-time hotel search, availability, and reservation management.
- Implementing *RTL-first* internationalization (Arabic/English) with react-i18next and Tailwind logical properties.
- Designing the database schema with *Drizzle ORM* and *PostgreSQL*, including background job processing with *pg-boss* and *Redis* caching.
- Setting up *Docker*-based deployments and CI workflows with *Biome* linting and *Playwright* E2E testing.

#v(0.2cm)

#two-col-entry(
  [*Senior Software Engineer (Full-Time)*, StemEC -- Remote],
  [Aug. 2025 – Apr. 2026],
)
#v(0.10cm)
- Led the development of an education SaaS platform (inspired by Skool.com) using *Laravel*, *React*, and *Docker*.
- Managed a cross-functional team of developers to deliver high-quality, scalable features.
- Built *CI/CD* pipelines with *Jenkins*, *Docker*, and *Kubernetes* for automated deployments.
- Architected microservices and mentored junior engineers on clean code and *Git* best practices.

#v(0.2cm)

#two-col-entry(
  [*Full Stack Instructor (Contract)*, Konecta -- Cairo, On-site],
  [May 2025 – Oct. 2025],
)
#v(0.10cm)
- Designed and delivered a 7-week internship curriculum covering advanced Full Stack and Microservices topics.
- Taught Java, Spring Boot, C\#, .NET 10, Eureka, API Gateway, Software Architecture, and Microservices design patterns.
- Led 2 internship batches (40+ students) to deliver production-ready microservice projects.
- Authored detailed PRDs with in-depth technical and architectural requirements.
- Guided students on best practices for teamwork, version control, and CI / CD integration.

#v(0.2cm)

#two-col-entry(
  [*Full Stack Web Instructor (Contract)*, AMIT Learning -- Cairo, On-site],
  [Jun. 2024 – Sep. 2025],
)
#v(0.10cm)
- Taught the Full-Stack Web Development track covering HTML, CSS, JavaScript, PHP, Laravel, React, Node.js, NPM, Composer, and MySQL.
- Supervised and evaluated over 30 student projects, ensuring best practices in front-end and back-end architecture.
- Conducted in-depth sessions on advanced topics including Next.js, FilamentPHP, Tailwind CSS, Figma, and PWA development.
- Mentored students on version control, deployment strategies, and career development in web engineering.

#v(0.2cm)

#two-col-entry(
  [*Additional Teaching Experience*],
  [2022 – 2025],
)
#v(0.10cm)
- *StemEC (Remote, 2025):* Delivered a 2-week front-end internship covering HTML, CSS, JavaScript, and Bootstrap.
- *RiskRice (Remote, 2025):* Taught a 2-week full-stack internship covering Node.js, Express.js, and SQL.
- *ITI (Cairo, 2022):* Guest session on MongoDB, NoSQL indexing, replication, and sharding for the Data Engineering Track.

#v(0.2cm)

#two-col-entry(
  [*Mid-Level Frontend Engineer (Full-Time)*, Stallion AI -- Remote],
  [Jun. 2022 – May 2023],
)
#v(0.10cm)
- Migrated the company's main website from Vue 3 to Nuxt 3, enhancing SSR and SEO capabilities.
- Collaborated closely with UI/UX designers in Figma to design futuristic, high-fidelity interfaces.
- Integrated REST APIs and optimized front-end rendering performance across multiple modules.
- Improved component reusability and state management consistency throughout the app.
- Implemented image lazy loading and route-based code splitting to improve performance by 35%.

#v(0.2cm)

#two-col-entry(
  [*Web Instructor (Contract)*, Senior Steps -- Cairo, Hybrid],
  [Oct. 2021 – May 2022],
)
#v(0.10cm)
- Delivered courses on Vue 3, NuxtJs, React (Redux, RTK Query), and Python Django.
- Focused on building problem-solving and real-world project skills in students.

#v(0.2cm)

#two-col-entry(
  [*Junior Frontend Engineer (Full-Time)*, Etolv -- Cairo, Hybrid],
  [May. 2021 – Oct. 2022],
)
#v(0.10cm)
- Migrated a legacy React e-commerce platform to Next.js, improving SEO performance by 45% and reducing page load time by 32% through server-side rendering and optimized asset delivery.
- Enhanced a large-scale Angular 8 Travel Management System, boosting overall system responsiveness by 40% with virtualized lists, pagination, and PWA architecture for offline usability.
- Diagnosed and resolved 100+ critical UI/UX bugs across 60+ pages, improving user satisfaction scores and reducing customer-reported issues by 30%.
- Collaborated with backend teams to integrate APIs and ensure consistent UI behavior across devices and browsers.

// --- Education ---

#section-title("Education")

#two-col-entry(
  [*University of Helwan*, BS in Computer Science & Statistics],
  [Sep. 2020 – May 2026],
)
#v(0.10cm)
- *Coursework:* Computer Architecture, Data Structures, Algorithms, Computational Theory, Computer Vision, GUI, Databases, UML, OOP, Networks, Compiler Design.

// --- Projects ---

#section-title("Projects")

#two-col-entry(
  [*Regional Church System* _( Community & Data Management Platform )_],
  [2023 - Present],
)
#v(0.10cm)

A system designed for regional church administration to manage congregational data, family information, attendance, and communication across multiple churches. The system streamlines data collection, report generation, and event management. Designed and developed a church management system using *Laravel, Filament, and MySQL*, now used by *24 churches* with over *1,000 active daily users*.

#v(0.10cm)

Key Contributions:
- Architected a modular system with *Laravel* and *React*.
- Built role-based access control for different levels: bishop, priests, managers, administrators and servants.
- Implemented data analytics and reporting dashboards using Filament widgets and PostgreSQL queries.
- Containerized the application with Docker and configured *Nginx* reverse proxy for production deployment.
- Enhanced data integrity and scalability through *Redis* caching and database indexing strategies.

Tools used: Laravel, Filamentphp, MySQL, Docker, Redis, Nginx, Livewire, Tailwind CSS

#v(0.2cm)

#two-col-entry(
  [*Hessah System Education Management SaaS Platform (EdTech System)*],
  [2024 - 2025],
)
#v(0.10cm)

A full-featured SaaS platform built for private tutors in Egypt to manage student attendance, finances, and exam performance. The system empowers educators to organize multiple classes, upload materials, and share detailed performance reports with parents.
- Architected and developed the platform using Laravel and FilamentPHP, with a modular, scalable backend.
- Implemented attendance tracking, payment management, and exam performance analytics dashboards.
- Integrated a real-time notification system for tutors and parents via Laravel Queues & Events.
- Designed a customizable dashboard per tutor, supporting branding, icons, and multi-role access control.
- Optimized backend performance and caching, improving overall system speed by 40%.
- Gained hands-on experience in business strategy, marketing, and SaaS product management, driving growth and user engagement.

// --- Languages ---

#section-title("Languages")

- *English* — Professional Working Proficiency
- *Arabic* — Native Speaker
