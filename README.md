# Neurochirurgie Fischer — Medical Practice Website

> A multilingual, fully responsive medical website and custom CMS built for a neurosurgery & spinal surgery practice in NRW, Germany.

**Live Site:** [my-bandscheibe.de](https://my-bandscheibe.de)

---

## Project Overview

A complete, production-ready web platform for a multi-location neurosurgical practice. The site serves patients in **6 languages**, features an interactive video-modal system for medical education content, and includes an administrative CMS with automated deployment.

### Key Features

- **6 language versions** — German (DE), English (EN), Russian (RU), Turkish (TR), Arabic (AR) with RTL support, and Uzbek (UZ)
- **Interactive video modals** — Medical explainer videos per language with split-panel layout, procedure steps, and auto-play/stop
- **Custom CMS & Admin Panel** — Firebase-backed dashboard for managing doctors, treatments, clinical focus areas, reviews, and office hours
- **Automated CI/CD** — GitHub Actions workflow synchronizing CMS updates into static HTML and deploying via FTP to the production server
- **Multi-location** — 3 clinic locations in NRW (Mönchengladbach, Viersen, Düsseldorf)
- **Responsive design** — Optimized for mobile, MacBook, 1080p and ultra-wide (2560px) monitors
- **Doctolib integration** — Direct appointment booking widget alongside contact forms
- **SEO & GDPR compliant** — Localized hreflang tags, structured data (JSON-LD), sitemap, and cookie consent

---

## Tech Stack

| Layer | Technology |
|---|---|
| Structure | Semantic HTML5 |
| Styling | Vanilla CSS3 (Custom design, no frameworks) |
| Logic | Vanilla JavaScript (ES6+) |
| Backend & CMS | Google Firebase (Firestore, Authentication) |
| CI/CD & Hosting | GitHub Actions, FTP Deploy, Apache (ALL-INKL) |
| Typography | Google Fonts (Plus Jakarta Sans, Inter) |
| Media | Localized MP4 video explainers, optimized WebP images |

---

## Multilingual Architecture

Each language lives in its own subdirectory (`/en/`, `/ru/`, `/tr/`, `/ar/`, `/uz/`) and shares the same styling and media assets via relative paths. Arabic includes dedicated RTL styles. Proper `hreflang` alternate tags connect all language variants for search engines.

---

## Responsive Breakpoints

| Breakpoint | Target |
|---|---|
| `min-width: 769px` (default) | Desktop / 1080p |
| `min-height: 1200px + min-width: 769px` | Ultra-wide / 2560px |
| `max-height: 980px + min-width: 769px` | MacBook / Laptop |
| `max-width: 768px` | Mobile / Tablet |

---

## Video System

Medical topics feature localized explainer videos. Each video opens in a split-panel modal (video on the left, structured clinical text and procedure steps on the right) with auto-play on open and auto-stop on close.

---

*Built by Arkadii Redozubov*
