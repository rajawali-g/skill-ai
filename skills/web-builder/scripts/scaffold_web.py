#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WebBuilder Scaffolder Script (v1.7.1)
Generates starter web project files from
conversational specifications, selected layout display type, database choice, and the 55-feature catalog.

Features:
- Project presets (--preset); includes government, tourism, SaaS, portfolio, ecommerce, business, education, community, and events
- Real Multi-Page Linked Generation (--display multi-page)
- Interactive Terminal Wizard Mode (--interactive / -i)
- Design Tokens First (HSL CSS Variables)
- Starter output requires project-specific review; no WCAG/security certification is implied
- Simple SVG logo and favicon generation (no PNG/ICO suite)
"""

import os
import sys
import argparse
import json

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

THEMES = {
    "dark-luxury": {
        "name": "Dark Luxury & Glassmorphism",
        "bg": "hsl(222, 47%, 7%)",
        "surface": "hsla(222, 40%, 14%, 0.7)",
        "surface_card": "hsla(222, 35%, 18%, 0.8)",
        "primary": "hsl(210, 100%, 56%)",
        "primary_glow": "hsla(210, 100%, 56%, 0.35)",
        "accent": "hsl(160, 84%, 44%)",
        "text": "hsl(210, 40%, 98%)",
        "text_muted": "hsl(215, 20%, 65%)",
        "border": "hsla(215, 25%, 35%, 0.3)",
        "font_heading": "'Outfit', sans-serif",
        "font_body": "'Inter', sans-serif",
        "google_font_import": "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap"
    },
    "nature-cinematic": {
        "name": "Nature Cinematic & Volcanic Earth",
        "bg": "hsl(160, 25%, 7%)",
        "surface": "hsla(160, 25%, 13%, 0.75)",
        "surface_card": "hsla(160, 20%, 18%, 0.8)",
        "primary": "hsl(150, 75%, 42%)",
        "primary_glow": "hsla(150, 75%, 42%, 0.35)",
        "accent": "hsl(38, 92%, 52%)",
        "text": "hsl(150, 20%, 96%)",
        "text_muted": "hsl(150, 15%, 68%)",
        "border": "hsla(160, 20%, 30%, 0.3)",
        "font_heading": "'Plus Jakarta Sans', sans-serif",
        "font_body": "'Inter', sans-serif",
        "google_font_import": "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap"
    },
    "bento-minimal": {
        "name": "Bento Grid Minimalist",
        "bg": "hsl(210, 20%, 98%)",
        "surface": "hsl(0, 0%, 100%)",
        "surface_card": "hsl(210, 25%, 96%)",
        "primary": "hsl(225, 75%, 52%)",
        "primary_glow": "hsla(225, 75%, 52%, 0.2)",
        "accent": "hsl(260, 85%, 60%)",
        "text": "hsl(220, 25%, 10%)",
        "text_muted": "hsl(220, 15%, 45%)",
        "border": "hsl(220, 15%, 88%)",
        "font_heading": "'Plus Jakarta Sans', sans-serif",
        "font_body": "'Inter', sans-serif",
        "google_font_import": "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap"
    }
}

DISPLAY_TYPES = {
    "single-page": "Single-Page Scrollytelling",
    "multi-page": "Multi-Page Linked Structure",
    "responsive": "Responsive Modern Flex/Grid",
    "card-based": "Card-Based Bento Grid",
    "magazine": "Grid-Heavy Magazine Editorial",
    "fullscreen": "Fullscreen Immersive Experience",
    "dashboard": "Dashboard & App-Like Shell"
}

PRESETS = {
    "government": {
        "name": "Portal Pemda / Layanan Publik Resmi",
        "default_tagline": "Portal Resmi Informasi & Layanan Publik Terpadu",
        "display": "multi-page",
        "theme": "nature-cinematic",
        "db": "mysql",
        "features": "1,2,4,7,9,16,17,19,20,22,40,47"
    },
    "tourism": {
        "name": "Pesona Wisata & Budaya Daerah",
        "default_tagline": "The Living Landscape & Heritage Experience",
        "display": "single-page",
        "theme": "dark-luxury",
        "db": "postgresql",
        "features": "1,2,4,8,16,21,22,47,51"
    },
    "saas": {
        "name": "SaaS Platform & Digital Product",
        "default_tagline": "Accelerate Your Business with Modern Digital Intelligence",
        "display": "card-based",
        "theme": "bento-minimal",
        "db": "postgresql",
        "features": "1,4,5,6,8,16,21,22,28,47"
    },
    "portfolio": {
        "name": "Creative Agency & Developer Portfolio",
        "default_tagline": "Crafting High-End Immersive Digital Experiences",
        "display": "single-page",
        "theme": "dark-luxury",
        "db": "none",
        "features": "1,7,8,16,21,22,51"
    },
    "business": {
        "name": "Profil Bisnis & Jasa Profesional",
        "default_tagline": "Solusi yang Tepat untuk Kebutuhan Anda",
        "display": "multi-page",
        "theme": "bento-minimal",
        "db": "none",
        "features": "1,4,6,7,9,16,17,21,22"
    },
    "education": {
        "name": "Platform Pendidikan & Pembelajaran",
        "default_tagline": "Belajar dan Bertumbuh Bersama",
        "display": "multi-page",
        "theme": "bento-minimal",
        "db": "none",
        "features": "1,6,9,10,16,17,21,22,32"
    },
    "community": {
        "name": "Komunitas & Organisasi",
        "default_tagline": "Terhubung, Berbagi, dan Bergerak Bersama",
        "display": "single-page",
        "theme": "nature-cinematic",
        "db": "none",
        "features": "1,4,7,9,16,17,21,22,32"
    },
    "events": {
        "name": "Acara & Pengalaman",
        "default_tagline": "Temukan Pengalaman Berikutnya",
        "display": "single-page",
        "theme": "dark-luxury",
        "db": "none",
        "features": "1,4,7,9,16,17,21,22,51"
    },    "ecommerce": {
        "name": "Modern Store & E-Commerce",
        "default_tagline": "Curated Quality Products for Elevated Everyday Living",
        "display": "card-based",
        "theme": "bento-minimal",
        "db": "mysql",
        "features": "1,3,4,9,10,16,21,22,51"
    }
}

def generate_svg_logo(project_name, primary_color, accent_color):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%" fill="none">
  <defs>
    <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{primary_color}" />
      <stop offset="100%" stop-color="{accent_color}" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <rect x="8" y="8" width="84" height="84" rx="24" fill="url(#logoGrad)" filter="url(#glow)"/>
  <rect x="12" y="12" width="76" height="76" rx="20" fill="hsl(222, 47%, 8%)" fill-opacity="0.9" />
  <path d="M30 70 L50 26 L70 70 M38 54 L62 54" stroke="url(#logoGrad)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

def generate_svg_favicon(primary_color, accent_color):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none">
  <defs>
    <linearGradient id="favGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{primary_color}" />
      <stop offset="100%" stop-color="{accent_color}" />
    </linearGradient>
  </defs>
  <rect width="64" height="64" rx="16" fill="url(#favGrad)" />
  <circle cx="32" cy="32" r="14" fill="#ffffff" fill-opacity="0.95" />
  <circle cx="32" cy="32" r="7" fill="hsl(222, 47%, 8%)" />
</svg>"""

def get_shared_css(name, theme, display_title):
    return f"""/* ==========================================================================
   Design Tokens & System Stylesheet: {name}
   Generated by WebBuilder Suite (v1.7.1)
   Architecture: {display_title}
   Theme: {theme['name']}
   ========================================================================== */

@import url('{theme['google_font_import']}');

:root {{
  /* Color Tokens */
  --color-bg: {theme['bg']};
  --color-surface: {theme['surface']};
  --color-surface-card: {theme['surface_card']};
  --color-primary: {theme['primary']};
  --color-primary-glow: {theme['primary_glow']};
  --color-accent: {theme['accent']};
  --color-text: {theme['text']};
  --color-text-muted: {theme['text_muted']};
  --color-border: {theme['border']};

  /* Typography Scale */
  --font-heading: {theme['font_heading']};
  --font-body: {theme['font_body']};
  --text-xs: clamp(0.75rem, 0.7rem + 0.25vw, 0.85rem);
  --text-sm: clamp(0.875rem, 0.8rem + 0.35vw, 1rem);
  --text-base: clamp(1rem, 0.95rem + 0.4vw, 1.125rem);
  --text-lg: clamp(1.2rem, 1.1rem + 0.6vw, 1.45rem);
  --text-xl: clamp(1.5rem, 1.35rem + 1vw, 2rem);
  --text-2xl: clamp(2rem, 1.7rem + 1.8vw, 2.75rem);
  --text-3xl: clamp(2.5rem, 2.1rem + 2.5vw, 3.8rem);

  /* Spacing Scale (8pt grid) */
  --space-2xs: 0.25rem;
  --space-xs: 0.5rem;
  --space-sm: 0.75rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;
  --space-xl: 2.25rem;
  --space-2xl: 3.5rem;
  --space-3xl: 5rem;

  /* Layout & Glassmorphism */
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --radius-pill: 9999px;
  --blur-glass: 16px;
  --shadow-card: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
  --shadow-glow: 0 0 35px var(--color-primary-glow);
  --transition-fast: 180ms cubic-bezier(0.16, 1, 0.3, 1);
  --transition-smooth: 350ms cubic-bezier(0.16, 1, 0.3, 1);
  --container-max: 1240px;
}}

/* Light Theme Overrides */
[data-theme="light"] {{
  --color-bg: hsl(210, 20%, 98%);
  --color-surface: hsla(0, 0%, 100%, 0.8);
  --color-surface-card: hsl(0, 0%, 100%);
  --color-text: hsl(222, 47%, 10%);
  --color-text-muted: hsl(215, 20%, 45%);
  --color-border: hsl(215, 25%, 88%);
  --shadow-card: 0 10px 30px -10px rgba(0, 0, 0, 0.08);
}}

/* CSS Reset & Base */
*, *::before, *::after {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}}

html {{
  scroll-behavior: smooth;
  font-size: 16px;
}}

body {{
  background-color: var(--color-bg);
  color: var(--color-text);
  font-family: var(--font-body);
  font-size: var(--text-base);
  line-height: 1.65;
  min-height: 100vh;
  overflow-x: hidden;
  transition: background-color var(--transition-smooth), color var(--transition-smooth);
}}

/* Typography */
h1, h2, h3, h4, h5, h6 {{
  font-family: var(--font-heading);
  line-height: 1.2;
  font-weight: 700;
  color: var(--color-text);
}}

h1 {{ font-size: var(--text-3xl); letter-spacing: -0.03em; }}
h2 {{ font-size: var(--text-2xl); letter-spacing: -0.02em; }}
h3 {{ font-size: var(--text-xl); }}

p {{
  color: var(--color-text-muted);
  max-width: 65ch;
}}

a {{
  color: inherit;
  text-decoration: none;
}}

.container {{
  width: 100%;
  max-width: var(--container-max);
  margin-left: auto;
  margin-right: auto;
  padding-left: var(--space-md);
  padding-right: var(--space-md);
}}

/* Header & Sticky Navbar */
.site-header {{
  position: sticky;
  top: 0;
  z-index: 100;
  background-color: var(--color-surface);
  backdrop-filter: blur(var(--blur-glass));
  -webkit-backdrop-filter: blur(var(--blur-glass));
  border-bottom: 1px solid var(--color-border);
  transition: all var(--transition-fast);
}}

.navbar {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 72px;
}}

.brand {{
  display: flex;
  align-items: center;
  gap: var(--space-sm);
  font-family: var(--font-heading);
  font-weight: 800;
  font-size: var(--text-lg);
  color: var(--color-text);
}}

.brand-logo {{
  width: 36px;
  height: 36px;
  display: block;
}}

.nav-links {{
  display: flex;
  align-items: center;
  gap: var(--space-lg);
  list-style: none;
}}

.nav-link {{
  font-size: var(--text-sm);
  font-weight: 500;
  color: var(--color-text-muted);
  transition: color var(--transition-fast);
  padding: var(--space-xs) 0;
  position: relative;
}}

.nav-link:hover, .nav-link.active {{
  color: var(--color-text);
  font-weight: 700;
}}

.nav-link::after {{
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0%;
  height: 2px;
  background-color: var(--color-primary);
  transition: width var(--transition-fast);
}}

.nav-link:hover::after, .nav-link.active::after {{
  width: 100%;
}}

.nav-actions {{
  display: flex;
  align-items: center;
  gap: var(--space-sm);
}}

/* Buttons */
.btn {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-xs);
  padding: 0.65rem 1.35rem;
  font-family: var(--font-heading);
  font-size: var(--text-sm);
  font-weight: 600;
  border-radius: var(--radius-pill);
  cursor: pointer;
  border: 1px solid transparent;
  transition: all var(--transition-fast);
  text-decoration: none;
}}

.btn-primary {{
  background: linear-gradient(135deg, var(--color-primary), var(--color-accent));
  color: #ffffff;
  box-shadow: 0 4px 18px var(--color-primary-glow);
}}

.btn-primary:hover {{
  transform: translateY(-2px);
  box-shadow: 0 6px 24px var(--color-primary-glow);
}}

.btn-ghost {{
  background-color: transparent;
  color: var(--color-text);
  border-color: var(--color-border);
}}

.btn-ghost:hover {{
  background-color: var(--color-surface-card);
}}

.theme-toggle {{
  background: transparent;
  border: 1px solid var(--color-border);
  color: var(--color-text);
  width: 40px;
  height: 40px;
  border-radius: var(--radius-pill);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 1.1rem;
  transition: all var(--transition-fast);
}}

.theme-toggle:hover {{
  background-color: var(--color-surface-card);
}}

/* Hero Section */
.hero {{
  position: relative;
  padding: var(--space-3xl) 0 var(--space-2xl);
  overflow: hidden;
}}

.hero-content {{
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-xl);
  text-align: center;
  align-items: center;
}}

.badge {{
  display: inline-flex;
  align-items: center;
  gap: var(--space-xs);
  padding: 0.35rem 0.9rem;
  background-color: var(--color-surface-card);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-pill);
  font-size: var(--text-xs);
  font-weight: 600;
  color: var(--color-primary);
  margin-bottom: var(--space-sm);
}}

.hero-title {{
  margin-bottom: var(--space-md);
}}

.hero-title span {{
  background: linear-gradient(135deg, var(--color-primary), var(--color-accent));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

.hero-desc {{
  font-size: var(--text-lg);
  margin: 0 auto var(--space-xl);
}}

.hero-cta-group {{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-md);
  flex-wrap: wrap;
}}

/* Bento Grid System */
.section-title-wrap {{
  text-align: center;
  margin-bottom: var(--space-2xl);
}}

.section-title-wrap p {{
  margin: var(--space-xs) auto 0;
}}

.bento-grid {{
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--space-md);
  margin-bottom: var(--space-3xl);
}}

.bento-card {{
  background-color: var(--color-surface-card);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-xl);
  backdrop-filter: blur(10px);
  transition: transform var(--transition-smooth), border-color var(--transition-smooth), box-shadow var(--transition-smooth);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: var(--shadow-card);
}}

.bento-card:hover {{
  transform: translateY(-4px);
  border-color: var(--color-primary);
  box-shadow: 0 12px 36px -10px var(--color-primary-glow);
}}

.card-span-12 {{ grid-column: span 12; }}
.card-span-8  {{ grid-column: span 8; }}
.card-span-6  {{ grid-column: span 6; }}
.card-span-4  {{ grid-column: span 4; }}

.card-icon {{
  width: 48px;
  height: 48px;
  border-radius: var(--radius-md);
  background: linear-gradient(135deg, var(--color-primary-glow), transparent);
  border: 1px solid var(--color-border);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  margin-bottom: var(--space-md);
}}

/* Toast Container (Feature #1) */
.toast-container {{
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 1000;
  display: flex;
  flex-direction: column;
  gap: 10px;
}}

.toast {{
  background-color: var(--color-surface-card);
  color: var(--color-text);
  border: 1px solid var(--color-primary);
  padding: 0.85rem 1.25rem;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-card);
  display: flex;
  align-items: center;
  gap: var(--space-sm);
  font-size: var(--text-sm);
  animation: slideInUp 0.3s ease forwards;
}}

.toast-fadeout {{
  opacity: 0;
  transform: translateY(10px);
  transition: opacity 0.3s, transform 0.3s;
}}

@keyframes slideInUp {{
  from {{ opacity: 0; transform: translateY(20px); }}
  to   {{ opacity: 1; transform: translateY(0); }}
}}

/* Floating Action WhatsApp (Feature #4) */
.floating-chat-btn {{
  position: fixed;
  bottom: 28px;
  left: 28px;
  width: 52px;
  height: 52px;
  border-radius: var(--radius-pill);
  background-color: #25D366;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.75rem;
  box-shadow: 0 6px 20px rgba(37, 211, 102, 0.4);
  z-index: 90;
  transition: transform var(--transition-fast);
}}

.floating-chat-btn:hover {{
  transform: scale(1.1);
}}

/* Footer */
.site-footer {{
  background-color: var(--color-surface);
  border-top: 1px solid var(--color-border);
  padding: var(--space-2xl) 0 var(--space-lg);
  margin-top: var(--space-3xl);
}}

.footer-bottom {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: var(--space-md);
  padding-top: var(--space-lg);
  border-top: 1px solid var(--color-border);
  font-size: var(--text-xs);
  color: var(--color-text-muted);
}}

/* Responsive Breakpoints */
@media (max-width: 992px) {{
  .card-span-8, .card-span-4, .card-span-6 {{ grid-column: span 12; }}
}}

@media (max-width: 768px) {{
  .navbar {{ height: 64px; }}
  .nav-links {{ display: none; }}
  .hero-cta-group {{ flex-direction: column; width: 100%; }}
  .hero-cta-group .btn {{ width: 100%; }}
}}
"""

def get_shared_js(name):
    return f"""/**
 * Main Application Logic: {name}
 * Generated by WebBuilder Suite (v1.7.1)
 */

document.addEventListener('DOMContentLoaded', () => {{
  initThemeToggle();
  initToastNotification();
  initSmoothScroll();
}});

function initThemeToggle() {{
  const toggleBtn = document.getElementById('themeToggle');
  const root = document.documentElement;

  const savedTheme = localStorage.getItem('theme') || 
    (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
  
  root.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);

  if (toggleBtn) {{
    toggleBtn.addEventListener('click', () => {{
      const current = root.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
      updateThemeIcon(next);
      showToast(`Tema beralih ke mode ${{next === 'dark' ? 'Gelap 🌙' : 'Terang ☀️'}}`);
    }});
  }}
}}

function updateThemeIcon(theme) {{
  const toggleBtn = document.getElementById('themeToggle');
  if (toggleBtn) {{
    toggleBtn.textContent = theme === 'dark' ? '☀️' : '🌙';
  }}
}}

function initToastNotification() {{
  const btn = document.getElementById('btnTestToast');
  if (btn) {{
    btn.addEventListener('click', () => {{
      showToast('Aksi berhasil dicatat! Notifikasi responsif WebBuilder.');
    }});
  }}
}}

window.showToast = function(message, type = 'success') {{
  const container = document.getElementById('toastContainer');
  if (!container) return;

  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.innerHTML = `<span>✓</span><span>${{message}}</span>`;
  container.appendChild(toast);

  setTimeout(() => {{
    toast.classList.add('toast-fadeout');
    setTimeout(() => toast.remove(), 300);
  }}, 3500);
}};

function initSmoothScroll() {{
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
    anchor.addEventListener('click', function(e) {{
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      const targetEl = document.querySelector(targetId);
      if (targetEl) {{
        e.preventDefault();
        targetEl.scrollIntoView({{ behavior: 'smooth' }});
      }}
    }});
  }});
}}
"""

def generate_page_html(name, tagline, current_page, is_multi_page, display_title, db_choice, features_list):
    # Navigation items
    if is_multi_page:
        nav_items = [
            ("index.html", "Beranda", current_page == "index"),
            ("about.html", "Tentang", current_page == "about"),
            ("services.html", "Produk & Layanan", current_page == "services"),
            ("contact.html", "Kontak", current_page == "contact"),
        ]
        cta_href = "contact.html"
    else:
        nav_items = [
            ("#hero", "Beranda", True),
            ("#features", "Sorotan", False),
            ("#contact", "Kontak", False),
        ]
        cta_href = "#contact"

    nav_links_html = "".join([
        f'<li><a href="{href}" class="nav-link{" active" if is_act else ""}">{lbl}</a></li>\n          '
        for href, lbl, is_act in nav_items
    ])

    features_meta = ""

    # Body Content based on Page
    if current_page == "about":
        main_body = f"""
    <section class="hero" style="padding-top: var(--space-2xl);">
      <div class="container hero-content">
        <div>
          <div class="badge">Profil {name}</div>
          <h1 class="hero-title">Tentang <span>{name}</span></h1>
          <p class="hero-desc">
            Ceritakan latar belakang {name}, siapa yang Anda layani, dan alasan proyek ini hadir. Sesuaikan teks ini dengan brand atau organisasi Anda.
          </p>
        </div>
      </div>
    </section>

    <section class="container" style="margin-bottom: var(--space-3xl);">
      <div class="bento-grid">
        <div class="bento-card card-span-6">
          <div class="card-icon">🎯</div>
          <div>
            <h3>Tujuan Kami</h3>
            <p>Tuliskan visi atau tujuan utama organisasi, bisnis, produk, atau karya Anda di sini.</p>
          </div>
        </div>
        <div class="bento-card card-span-6">
          <div class="card-icon">🚀</div>
          <div>
            <h3>Yang Kami Tawarkan</h3>
            <p>Jelaskan pendekatan, nilai, atau manfaat yang membedakan produk dan layanan Anda.</p>
          </div>
        </div>
      </div>
    </section>
"""
    elif current_page == "services":
        main_body = f"""
    <section class="hero" style="padding-top: var(--space-2xl);">
      <div class="container hero-content">
        <div>
          <div class="badge">⚙️ Modul & Fitur Layanan</div>
          <h1 class="hero-title">Produk & Layanan <span>{name}</span></h1>
          <p class="hero-desc">
            Perkenalkan produk, layanan, program, atau karya utama. Sesuaikan kartu-kartu berikut dengan penawaran Anda.
          </p>
        </div>
      </div>
    </section>

    <section class="container" style="margin-bottom: var(--space-3xl);">
      <div class="bento-grid">
        <div class="bento-card card-span-4">
          <div class="card-icon">📊</div>
          <h3>Penawaran Utama</h3>
          <p>Jelaskan manfaat utama yang diterima pelanggan atau pengunjung.</p>
        </div>
        <div class="bento-card card-span-4">
          <div class="card-icon">🛡️</div>
          <h3>Cara Kami Bekerja</h3>
          <p>Jelaskan proses, bahan, metode, atau komitmen yang benar-benar Anda sediakan.</p>
        </div>
        <div class="bento-card card-span-4">
          <div class="card-icon">🤖</div>
          <h3>Sorotan Lainnya</h3>
          <p>Tambahkan produk, layanan, proyek, atau informasi lain yang relevan. Hapus kartu ini jika tidak diperlukan.</p>
        </div>
      </div>
    </section>
"""
    elif current_page == "contact":
        main_body = f"""
    <section class="hero" style="padding-top: var(--space-2xl);">
      <div class="container hero-content">
        <div>
          <div class="badge">📍 Hubungi Kami</div>
          <h1 class="hero-title">Hubungi <span>{name}</span></h1>
          <p class="hero-desc">
            Tambahkan cara kontak, lokasi, atau jam layanan yang benar-benar berlaku untuk bisnis atau organisasi Anda.
          </p>
        </div>
      </div>
    </section>

    <section class="container" style="margin-bottom: var(--space-3xl);">
      <div class="bento-grid">
        <div class="bento-card card-span-6">
          <div class="card-icon">💬</div>
          <h3>Kirim Pesan</h3>
          <form style="display:flex; flex-direction:column; gap: var(--space-sm); margin-top: var(--space-md);">
            <input type="text" placeholder="Nama Anda" style="padding:0.75rem; border-radius:var(--radius-md); border:1px solid var(--color-border); background:var(--color-bg); color:var(--color-text);" required />
            <input type="email" placeholder="Email Anda" style="padding:0.75rem; border-radius:var(--radius-md); border:1px solid var(--color-border); background:var(--color-bg); color:var(--color-text);" required />
            <textarea placeholder="Pesan Anda..." rows="4" style="padding:0.75rem; border-radius:var(--radius-md); border:1px solid var(--color-border); background:var(--color-bg); color:var(--color-text);" required></textarea>
            <button type="button" class="btn btn-primary" onclick="showToast('Form contoh: hubungkan backend sebelum pesan dapat dikirim.', 'warning')">Kirim Pesan</button>
          </form>
        </div>

        <div class="bento-card card-span-6">
          <div class="card-icon">🗺️</div>
          <h3>Lokasi atau Informasi Kontak</h3>
          <p style="margin-bottom: var(--space-md);">Tambahkan alamat atau detail kontak yang telah diverifikasi; hapus blok ini bila tidak relevan.</p>
          <div style="background:var(--color-bg); border:1px solid var(--color-border); border-radius:var(--radius-md); height:200px; display:flex; align-items:center; justify-content:center; color:var(--color-text-muted);">
            Area contoh peta; integrasi peta belum dibuat oleh scaffold.
          </div>
        </div>
      </div>
    </section>
"""
    else: # Index / Home Page
        main_body = f"""
    <!-- Hero Section -->
    <section class="hero" id="hero">
      <div class="container hero-content">
        <div>
          <div class="badge">✨ Starter WebBuilder</div>
          <h1 class="hero-title">{name}: <span>{tagline}</span></h1>
          <p class="hero-desc">
            Starter website ini dibuat oleh WebBuilder. Sesuaikan konten, aset, dan interaksi untuk kebutuhan proyek Anda.
          </p>
          <div class="hero-cta-group">
            <button class="btn btn-primary" id="btnTestToast">Coba Notifikasi Real-time</button>
            <a href="{cta_href}" class="btn btn-ghost">Pelajari Struktur Fitur</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Bento Grid Section -->
    <section class="features" id="features">
      <div class="container">
        <div class="section-title-wrap">
          <h2>Struktur Starter</h2>
          <p>Dirakit dengan modularitas tinggi dan siap dikembangkan sesuai skala kebutuhan Anda.</p>
        </div>

        <div class="bento-grid">
          <!-- Card 1: Utama -->
          <div class="bento-card card-span-8">
            <div class="card-icon">💎</div>
            <div>
              <h3>Arsitektur Tampilan: {display_title}</h3>
              <p>Menggunakan sistem CSS Grid 12-kolom responsif, token desain HSL adaptif, dan tipografi proporsional yang tajam di berbagai resolusi layar.</p>
            </div>
            <div style="margin-top: var(--space-md); font-size: var(--text-xs); color: var(--color-primary);">
              Layout pilihan: <strong>{display_title.upper()}</strong>
            </div>
          </div>

          <!-- Card 2: Database -->
          <div class="bento-card card-span-4">
            <div class="card-icon">🗄️</div>
            <div>
              <h3>Pilihan Database</h3>
              <p>Rencana pilihan: <strong>{db_choice.upper()}</strong>. Scaffold ini belum menghubungkan database atau membuat backend.</p>
            </div>
          </div>

          <!-- Card 3: 55 Fitur -->
          <div class="bento-card card-span-4">
            <div class="card-icon">⚙️</div>
            <div>
              <h3>Katalog Fitur</h3>
              <p>{len(features_list)} pilihan fitur tercatat di blueprint; implementasi tiap fitur perlu dibuat terpisah.</p>
            </div>
          </div>

          <!-- Card 4: Keamanan & Kecepatan -->
          <div class="bento-card card-span-4">
            <div class="card-icon">🛡️</div>
            <div>
              <h3>Keamanan & Aksesibilitas</h3>
              <p>Starter ini belum diaudit terhadap WCAG, keamanan, atau Core Web Vitals. Tinjau dan verifikasi sebelum rilis.</p>
            </div>
          </div>

          <!-- Card 5: AI & Ekosistem -->
          <div class="bento-card card-span-4">
            <div class="card-icon">🤖</div>
            <div>
              <h3>Interaksi Starter</h3>
              <p>Berisi interaksi sisi klien dasar. Form kontak dan integrasi layanan eksternal perlu dikonfigurasi sebelum digunakan.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact & Action Section -->
    <section class="contact" id="contact" style="padding: var(--space-3xl) 0;">
      <div class="container" style="text-align: center;">
        <h2>Siap Memulai Perjalanan Bersama {name}?</h2>
        <p style="margin: var(--space-sm) auto var(--space-xl);">Ganti teks dan tombol ini dengan ajakan bertindak yang sesuai dengan tujuan website.</p>
        <a href="contact.html" class="btn btn-primary">
          Lihat Informasi Kontak
        </a>
      </div>
    </section>
"""

    return f"""<!DOCTYPE html>
<html lang="id" data-theme="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{name} — {tagline}</title>
  <meta name="description" content="{name} — {tagline}. Dibuat menggunakan WebBuilder Suite." />
  
  <!-- OpenGraph Metadata (Feature #17) -->
  <meta property="og:title" content="{name} — {tagline}" />
  <meta property="og:description" content="{name} — {tagline}" />
  <meta property="og:type" content="website" />

  <!-- SVG favicon -->
  <link rel="icon" type="image/svg+xml" href="assets/icons/favicon.svg" />

  <!-- Stylesheet & Google Fonts -->
  <link rel="stylesheet" href="style.css" />{features_meta}
</head>
<body>

  <!-- Sticky Glassmorphic Navbar -->
  <header class="site-header" id="header">
    <div class="container">
      <nav class="navbar" aria-label="Main Navigation">
        <a href="index.html" class="brand" aria-label="{name} Homepage">
          <img src="assets/icons/logo.svg" alt="{name} Logo" class="brand-logo" />
          <span>{name}</span>
        </a>

        <ul class="nav-links">
          {nav_links_html}
        </ul>

        <div class="nav-actions">
          <button id="themeToggle" class="theme-toggle" aria-label="Ganti Tema Tampilan">🌓</button>
          <a href="{cta_href}" class="btn btn-primary" id="primaryCtaNav">Pelajari Lebih Lanjut</a>
        </div>
      </nav>
    </div>
  </header>

  <!-- Main Content -->
  <main>
{main_body}
  </main>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-bottom">
        <div>&copy; 2026 {name}. All rights reserved. Powered by <strong>WebBuilder Suite</strong>.</div>
        <div>Tipe Tampilan: {display_title} | Database: {db_choice.upper()}</div>
      </div>
    </div>
  </footer>

  <!-- Toast Container (Feature #1) -->
  <div class="toast-container" id="toastContainer" aria-live="polite"></div>


  <!-- JavaScript ES Module -->
  <script src="main.js"></script>
</body>
</html>
"""

def scaffold_project(name, tagline, display_type, theme_key, db_choice, features_str, output_dir):
    theme = THEMES.get(theme_key, THEMES["dark-luxury"])
    display_title = DISPLAY_TYPES.get(display_type, "Single-Page Scrollytelling")
    is_multi_page = (display_type == "multi-page")
    features_list = [f.strip() for f in features_str.split(",") if f.strip().isdigit()]
    
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, "assets", "icons"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "assets", "images"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "assets", "models"), exist_ok=True)

    # 1. Assets
    logo_svg = generate_svg_logo(name, theme["primary"], theme["accent"])
    favicon_svg = generate_svg_favicon(theme["primary"], theme["accent"])
    
    with open(os.path.join(output_dir, "assets", "icons", "logo.svg"), "w", encoding="utf-8") as f:
        f.write(logo_svg)
    with open(os.path.join(output_dir, "assets", "icons", "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(favicon_svg)

    # 2. CSS & JS
    css_content = get_shared_css(name, theme, display_title)
    js_content = get_shared_js(name)
    with open(os.path.join(output_dir, "style.css"), "w", encoding="utf-8") as f:
        f.write(css_content)
    with open(os.path.join(output_dir, "main.js"), "w", encoding="utf-8") as f:
        f.write(js_content)

    # 3. HTML Pages Generation
    generated_pages = []
    if is_multi_page:
        pages_to_generate = [
            ("index.html", "index"),
            ("about.html", "about"),
            ("services.html", "services"),
            ("contact.html", "contact"),
        ]
        for filename, page_key in pages_to_generate:
            html = generate_page_html(name, tagline, page_key, True, display_title, db_choice, features_list)
            with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
                f.write(html)
            generated_pages.append(filename)
    else:
        index_html = generate_page_html(name, tagline, "index", False, display_title, db_choice, features_list)
        with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(index_html)
        generated_pages.append("index.html")

    # 4. Project Blueprint File
    blueprint_data = {
        "project_name": name,
        "tagline": tagline,
        "display_type": display_type,
        "display_title": display_title,
        "theme": theme["name"],
        "database": db_choice,
        "features": features_list,
        "generated_files": generated_pages + [
            "style.css",
            "main.js",
            "assets/icons/logo.svg",
            "assets/icons/favicon.svg"
        ]
    }

    with open(os.path.join(output_dir, "blueprint.json"), "w", encoding="utf-8") as f:
        json.dump(blueprint_data, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Proyek web '{name}' berhasil dirakit di: {output_dir}")
    print(f"   • Tipe Tampilan : {display_title} ({'Multi-Page (' + ', '.join(generated_pages) + ')' if is_multi_page else 'Single-Page'})")
    print(f"   • Tema Desain   : {theme['name']}")
    print(f"   • Database      : {db_choice.upper()}")
    print(f"   • Pilihan Fitur : {len(features_list)} fitur ({', '.join(features_list)})")
    print(f"   • Logo & Favicon: Vector SVG generated di assets/icons/\n")

def run_interactive_wizard():
    print("\n" + "=" * 55)
    print(" 🌐 WebBuilder Interactive CLI Wizard (v1.7.1)")
    print("=" * 55)

    print("\nPilih Arketipe Proyek / Preset:")
    print("Pilih tipe proyek sebagai titik awal; semua preset dapat disesuaikan.")
    preset_keys = list(PRESETS.keys())
    for idx, key in enumerate(preset_keys, 1):
        print(f"  {idx}. {key} — {PRESETS[key]['name']}")
    custom_choice = len(preset_keys) + 1
    print(f"  {custom_choice}. custom — Tentukan sendiri / proyek umum")

    p_choice = input(f"Pilihan (1-{custom_choice}) [default: {custom_choice}]: ").strip() or str(custom_choice)
    try:
        selected_idx = int(p_choice)
    except ValueError:
        selected_idx = custom_choice
    preset_key = preset_keys[selected_idx - 1] if 1 <= selected_idx <= len(preset_keys) else None
    if preset_key:
        p_cfg = PRESETS[preset_key]
        name = input(f"Nama Website [default: {p_cfg['name']}]: ").strip() or p_cfg['name']
        tagline = input(f"Tagline Website [default: {p_cfg['default_tagline']}]: ").strip() or p_cfg['default_tagline']
        display = p_cfg['display']
        theme = p_cfg['theme']
        db = p_cfg['db']
        features = p_cfg['features']
    else:
        name = input("Nama Website [default: WebProject]: ").strip() or "WebProject"
        tagline = input("Tagline Website [default: Modern Web Experience]: ").strip() or "Modern Web Experience"
        
        print("\nPilih Tipe Tampilan (1-7):")
        d_keys = list(DISPLAY_TYPES.keys())
        for idx, k in enumerate(d_keys, 1):
            print(f"  {idx}. {DISPLAY_TYPES[k]} ({k})")
        d_idx = input("Pilihan (1-7) [default: 1]: ").strip() or "1"
        try:
            display = d_keys[int(d_idx) - 1]
        except Exception:
            display = "single-page"

        print("\nPilih Tema Visual (1-3):")
        t_keys = list(THEMES.keys())
        for idx, k in enumerate(t_keys, 1):
            print(f"  {idx}. {THEMES[k]['name']} ({k})")
        t_idx = input("Pilihan (1-3) [default: 1]: ").strip() or "1"
        try:
            theme = t_keys[int(t_idx) - 1]
        except Exception:
            theme = "dark-luxury"

        print("\nPilih Database:")
        print("  1. nosql | 2. sqlite | 3. mysql | 4. postgresql | 5. none")
        db_map = {"1": "nosql", "2": "sqlite", "3": "mysql", "4": "postgresql", "5": "none"}
        db_idx = input("Pilihan (1-5) [default: 5]: ").strip() or "5"
        db = db_map.get(db_idx, "none")

        features = input("Nomor fitur yang diinginkan (dipisah koma) [default: 1,2,4,8,16,21,22]: ").strip() or "1,2,4,8,16,21,22"

    out_dir = input("Direktori output [default: ./output-site]: ").strip() or "./output-site"

    scaffold_project(
        name=name,
        tagline=tagline,
        display_type=display,
        theme_key=theme,
        db_choice=db,
        features_str=features,
        output_dir=out_dir
    )

def main():
    parser = argparse.ArgumentParser(description="WebBuilder Project Scaffolder")
    parser.add_argument("-i", "--interactive", action="store_true", help="Launch interactive terminal wizard")
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Project starting preset; customize generated content for the actual project")
    parser.add_argument("--name", default=None, help="Website project name")
    parser.add_argument("--tagline", default=None, help="Tagline / Meta description")
    parser.add_argument("--display", choices=list(DISPLAY_TYPES.keys()), help="Display layout architecture")
    parser.add_argument("--theme", choices=list(THEMES.keys()), help="Visual theme")
    parser.add_argument("--db", choices=["nosql", "sqlite", "mysql", "postgresql", "none"], help="Database architecture")
    parser.add_argument("--features", default=None, help="Comma-separated feature numbers (1-55)")
    parser.add_argument("--output", default="./output-site", help="Destination directory")

    args = parser.parse_args()

    if args.interactive:
        run_interactive_wizard()
        return

    # Apply Preset if specified
    if args.preset:
        p = PRESETS[args.preset]
        name = args.name or p["name"]
        tagline = args.tagline or p["default_tagline"]
        display = args.display or p["display"]
        theme = args.theme or p["theme"]
        db = args.db or p["db"]
        features = args.features or p["features"]
    else:
        name = args.name or "WebProject"
        tagline = args.tagline or "Modern Web Experience"
        display = args.display or "single-page"
        theme = args.theme or "dark-luxury"
        db = args.db or "none"
        features = args.features or "1,2,4,8,16,21,22"

    scaffold_project(
        name=name,
        tagline=tagline,
        display_type=display,
        theme_key=theme,
        db_choice=db,
        features_str=features,
        output_dir=args.output
    )

if __name__ == "__main__":
    main()
