# Personal Portfolio — Django

A single-page portfolio website for **Vendra Bhanu Prakash**, built with **Django**. It showcases projects, skills, resume links, and a contact section with a modern, responsive design.

---

## Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Main Features](#main-features)
- [How It Works](#how-it-works)
- [Customization Guide](#customization-guide)
- [Static Assets](#static-assets)
- [Future Improvements](#future-improvements)

---

## Overview

This is a **server-rendered** portfolio: Django receives a request, builds HTML from templates, and sends one full page to the browser. There is no separate frontend framework (no React/Vue). All sections (Home, About, Projects, Skills, Resume, Contact) live on a **single URL** (`/`) and are reached via anchor links (`#Projects`, `#Contact`, etc.).

| Detail | Value |
|--------|--------|
| Framework | Django 5.x |
| App name | `main` |
| Entry URL | `/` → `views.home` |
| Page type | Single-page (SPA-style navigation, multi-section HTML) |

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Django |
| Templates | Django Template Language (DTL) |
| Styling | Custom CSS (`theme.css`, `style.css`) |
| Layout / UI helpers | Bootstrap 5 |
| Icons | Font Awesome 6 |
| Fonts | Google Fonts (Outfit, DM Sans) |
| Database | SQLite (default Django setup; **not used** for page content yet) |

---

## Project Structure

```
portfolio/
├── manage.py                 # Django CLI (runserver, migrate, etc.)
├── README.md                 # This file
│
├── portfolio/                # Project settings package
│   ├── settings.py           # Installed apps, templates, static URL
│   ├── urls.py               # Root URLs → includes main.urls
│   ├── wsgi.py               # Production entry (WSGI)
│   └── asgi.py               # Async entry (ASGI)
│
└── main/                     # Portfolio app
    ├── views.py              # home() view + projects/skills data
    ├── urls.py               # Maps "" to home
    ├── templates/
    │   ├── index.html        # Main page shell + hero + includes
    │   ├── navbar.html       # Sticky navigation
    │   ├── about.html        # About section
    │   ├── projects.html     # Project cards (loop)
    │   ├── skills.html       # Skill categories (loop)
    │   ├── Resume.html       # View / Download resume
    │   ├── contact.html      # Contact info + form
    │   └── footer.html       # Footer + social links
    └── static/
        ├── theme.css         # CSS variables (colors, spacing)
        ├── style.css         # Layout, components, animations
        ├── default_pic.png   # Optional profile image
        └── bhn.png           # Optional image asset
```

---

## How to Run

### Prerequisites

- Python 3.10+ recommended
- pip

### Setup

```bash
# Navigate to project folder
cd portfolio

# Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# Install Django
pip install django

# Apply migrations (first time)
python manage.py migrate

# Start development server
python manage.py runserver
```

Open in browser: **http://127.0.0.1:8000/**

If styles look outdated, hard-refresh: **Ctrl + Shift + R**.

---

## Main Features

### 1. Hero section (Home)

**Where:** `main/templates/index.html` (inline, not a separate file)

**What it does:**

- Full-viewport intro with name, tagline, short bio, and CTA buttons
- Animated “VB” avatar (CSS ring + float animation)
- Links scroll to `#Projects` and `#Contact`

**How it’s done:**

- HTML structure in `index.html` with classes like `hero`, `hero-grid`, `profile-avatar`
- Styling in `style.css` (gradients, animations `fadeInDown`, `float`, `pulse-ring`)
- Colors/spacing from CSS variables in `theme.css`

---

### 2. Sticky navigation

**Where:** `main/templates/navbar.html`

**What it does:**

- Stays at top while scrolling
- Links to each section via hash anchors (`#home`, `#About`, `#Skills`, …)
- Collapsible menu on mobile (Bootstrap `navbar-toggler` + `collapse`)

**How it’s done:**

- Included in `index.html`: `{% include 'navbar.html' %}`
- Bootstrap JS handles toggle; `id="navbarNav"` must match `data-bs-target`
- `scroll-padding-top` in CSS offsets fixed navbar when jumping to sections

---

### 3. About section

**Where:** `main/templates/about.html`

**What it does:**

- Short bio, highlight bullets, stat cards (Python, Django, AI/ML)

**How it’s done:**

- Static HTML in the template (edit text directly in `about.html`)
- Grid layout: `.about-grid`, `.about-stats` in `style.css`

---

### 4. Projects section

**Where:** `main/templates/projects.html` + data in `main/views.py`

**What it does:**

- Displays a grid of project cards with icon, title, description, tech tags, and link

**How it’s done:**

1. **`views.py`** passes a `projects` list in the context:

   ```python
   context = {
       'projects': [
           {
               'title': '...',
               'description': '...',
               'icon': 'fas fa-laptop-code',  # Font Awesome class
               'tags': ['Django', 'Python'],
               'link': '#',
           },
           # ...
       ],
   }
   ```

2. **`projects.html`** loops with Django template tags:

   ```django
   {% for project in projects %}
     <article class="project-card">...</article>
   {% endfor %}
   ```

3. Icons use Font Awesome classes from the `icon` field; tags use a nested `{% for tag in project.tags %}` loop.

---

### 5. Skills section

**Where:** `main/templates/skills.html` + data in `main/views.py`

**What it does:**

- Groups skills into categories (Languages, Frameworks, AI & Data)
- Shows progress bars and optional badge chips

**How it’s done:**

1. **`views.py`** passes `skill_categories`:

   ```python
   'skill_categories': [
       {
           'name': 'Languages',
           'icon': 'fas fa-code',
           'skills': [{'name': 'Python', 'level': 90}, ...],
           'badges': ['JavaScript basics'],  # optional
       },
   ]
   ```

2. **`skills.html`** uses nested loops:

   - Outer: `{% for category in skill_categories %}`
   - Inner: `{% for skill in category.skills %}`
   - Progress width: `style="width: {{ skill.level }}%"`

3. Bootstrap `.progress` + custom `.progress-bar` gradient in CSS.

---

### 6. Resume (View & Download)

**Where:** `main/templates/Resume.html`

**What it does:**

- **View Resume** — opens PDF on Google Drive in a new tab
- **Download** — triggers Google Drive download export

**How it’s done:**

- Plain `<a href="...">` links (no backend file serving)
- View URL: `https://drive.google.com/file/d/FILE_ID/view?usp=sharing`
- Download URL: `https://drive.google.com/uc?export=download&id=FILE_ID`
- Separate button styles: `.btn-resume-view` (blue) and `.btn-resume-download` (teal) in `style.css`

To use your own resume, replace the Google Drive file ID in both links in `Resume.html`.

---

### 7. Contact section

**Where:** `main/templates/contact.html`

**What it does:**

- Left panel: email, location, role
- Right panel: name, email, message form

**How it’s done:**

- HTML `<form>` with styled inputs (`.contact-form-group`)
- **Note:** Form is **front-end only** — submitting does not send email or save to a database yet. Wiring it up would require a Django form view, email backend, or a third-party service.

---

### 8. Footer

**Where:** `main/templates/footer.html`

**What it does:**

- Name, tagline, social icons (Instagram, LinkedIn, GitHub), copyright

**How it’s done:**

- Static HTML; update `href="#"` with real profile URLs when ready.

---

## How It Works

### Request flow

```
Browser  →  GET /
              ↓
portfolio/urls.py  →  include('main.urls')
              ↓
main/urls.py  →  views.home
              ↓
views.home  →  builds context (projects, skill_categories)
              ↓
render('index.html', context)
              ↓
index.html  →  {% include %} partials
              ↓
HTML + static CSS  →  browser
```

### Template composition

`index.html` is the **only** template rendered by the view. Other files are **partials** pulled in with:

```django
{% include 'navbar.html' %}
{% include 'about.html' %}
...
```

This keeps each section in its own file without needing multiple URLs or views.

### Styling system

| File | Role |
|------|------|
| `theme.css` | Design tokens: colors, shadows, spacing, fonts, gradients |
| `style.css` | Components: navbar, hero, cards, buttons, responsive breakpoints |

Example: change accent color once in `theme.css` (`--accent-blue`) and many components update automatically.

### Static files in templates

At the top of `index.html`:

```django
{% load static %}
<link rel="stylesheet" href="{% static 'style.css' %}">
```

Django serves files from `main/static/` when `DEBUG = True` and `django.contrib.staticfiles` is installed.

---

## Customization Guide

| What to change | Where |
|----------------|--------|
| Projects list | `main/views.py` → `projects` |
| Skills & levels | `main/views.py` → `skill_categories` |
| Hero / page title | `main/templates/index.html` |
| About text | `main/templates/about.html` |
| Resume links | `main/templates/Resume.html` |
| Email / location | `main/templates/contact.html` |
| Social links | `main/templates/footer.html` |
| Colors & theme | `main/static/theme.css` |
| Layout & animations | `main/static/style.css` |
| Profile photo | Replace hero avatar in `index.html` with e.g. `<img src="{% static 'default_pic.png' %}" alt="Profile">` |

---

## Static Assets

| File | Purpose |
|------|---------|
| `theme.css` | CSS variables (design system) |
| `style.css` | All component and layout styles |
| `default_pic.png` | Profile image (optional; not wired in hero by default) |
| `bhn.png` | Additional image asset |

---

## Future Improvements

Ideas you can add later:

- [ ] Connect contact form to email (Django `EmailMessage` or service like Formspree)
- [ ] Store projects/skills in database + Django Admin
- [ ] Use `default_pic.png` or `bhn.png` in the hero
- [ ] Add `requirements.txt` with pinned Django version
- [ ] Deploy (PythonAnywhere, Render, Railway, etc.) with `ALLOWED_HOSTS` and `collectstatic`

---

## Author

**Vendra Bhanu Prakash**  
AI & ML Student · Python Developer · Django Enthusiast

---

## License

Personal portfolio project — use and modify as needed for your own portfolio.
