# Neurochirurgie Fischer — Medical Practice Website

> A multilingual, fully responsive medical website built for a neurosurgery & spinal surgery practice in NRW, Germany.

**🌐 Live Site:** [my-bandscheibe.de](https://my-bandscheibe.de)

---

## 📋 Project Overview

A complete, production-ready static website for a multi-location neurosurgical practice. The site serves patients in **5 languages** and features an interactive video-modal system for medical education content.

### Key Features

- **5 language versions** — German (DE), English (EN), Russian (RU), Turkish (TR), Arabic (AR) with RTL support
- **Responsive design** — Optimized for mobile, MacBook, 1080p and ultra-wide (2560px) monitors
- **Interactive video modals** — 11+ medical explainer videos per language with auto-play/stop
- **Multi-location** — 3 clinic locations in NRW (Mönchengladbach, Viersen, Düsseldorf)
- **Doctolib integration** — Direct appointment booking widget
- **SEO optimized** — hreflang tags, structured data (JSON-LD), sitemap, meta tags per language
- **Cookie consent** — GDPR-compliant banner for German medical context

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Structure | HTML5 (Semantic) |
| Styling | Vanilla CSS3 (No frameworks) |
| Logic | Vanilla JavaScript (ES6) |
| Fonts | Google Fonts (Plus Jakarta Sans, Inter) |
| Icons | Inline SVG |
| Video | Local MP4 with dubbed versions per language |

---

## 📁 Project Structure

```
/
├── index.html                  # Main landing page (DE)
├── praxis-schwerpunkte.html    # Diseases & conditions page
├── behandlungen.html           # Treatments & surgeries page
├── diagnostik.html             # Diagnostics page
├── sprechzeiten.html           # Appointment / contact page
├── unser-team.html             # Our team page
├── zweitmeinung.html           # Second opinion page
├── patienten.html              # Patient info page
├── presseschau.html            # Press page
├── impressum.html              # Legal notice (Impressum)
├── datenschutz.html            # Privacy policy (Datenschutz)
│
├── en/                         # English language versions
├── ru/                         # Russian language versions
├── tr/                         # Turkish language versions
├── ar/                         # Arabic language versions (RTL)
│
├── video/                      # Medical explainer videos (MP4)
│   ├── *_en-US_dubbed.mp4      # English dubbed versions
│   └── *_ru_dubbed.mp4         # Russian dubbed versions
│
├── img/                        # Optimized WebP images
├── fonts/                      # Self-hosted font files
├── pdfs/                       # Patient brochures (PDF)
│
├── index-styles.css            # Styles for the main landing page
├── style.css                   # Shared styles for all other pages
├── sitemap.xml                 # SEO sitemap
└── robots.txt                  # SEO robots config
```

---

## 🌍 Multilingual Architecture

Each language lives in its own subdirectory and shares the same CSS, video and image assets via relative paths. Proper `hreflang` alternate link tags connect all language variants for Google.

---

## 📱 Responsive Breakpoints

| Breakpoint | Target |
|---|---|
| `min-width: 769px` (default) | Desktop / 1080p |
| `min-height: 1200px + min-width: 769px` | Ultra-wide / 2560px |
| `max-height: 980px + min-width: 769px` | MacBook / Laptop |
| `max-width: 768px` | Mobile / Tablet |

---

## 🎬 Video System

Each medical topic has up to 3 language versions of its explainer video. Videos open in a split-panel modal (video left, text content right) with auto-play on open and auto-stop on close.

---

*Built by Arkadii Redozubov*
