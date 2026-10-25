# 🧠 Antigravity AI Skills & Configuration Backup

Repositori ini berisi seluruh cadangan (*backup*) keahlian (*skills*), aturan penalaran desain (*design reasoning*), pola arsitektur front-end (Vue 3/Nuxt), backend API (CodeIgniter 4), audit keamanan aplikasi (*bug hunter* / OWASP), katalog master *Awesome Agent Skills*, dan konfigurasi global untuk asisten koding **Google Antigravity**.

---

## 📦 Isi Lengkap Backup (179+ Skills)

### 1. 🛡️ Security Audit & Bug Hunter Suite (`skills/security/`)
Koleksi lengkap audit kelayakan keamanan aplikasi berbasis standar global:
- **`owasp-security`**: Standar **OWASP Top 10:2025** dan **ASVS 5.0**. Memeriksa kerentanan kode di 20+ bahasa (termasuk PHP dan TypeScript/JavaScript), meliputi:
  - *Broken Access Control (IDOR, role bypass)*
  - *Cryptographic Failures (kebocoran API key, hardcoded JWT secrets)*
  - *Injection (SQL Injection, Command Injection, SSRF)*
  - *Cross-Site Scripting (XSS) & CSRF*
  - *Insecure Design & Supply Chain Checks*
- **`security-audit`**: Audit keamanan komprehensif dari Netresearch DTT:
  - Analisis mendalam celah arsitektur web & PHP (80+ PHP security checkpoints).
  - Klasifikasi kerentanan menggunakan **CWE Top 25** dan kalkulasi skor risiko **CVSS v3.1 / v4.0**.
  - Rekomendasi kode remediasi (*drop-in fix*) langsung.

### 2. 📚 Awesome Agent Skills Master Catalog (`skills/awesome-agent-skills/`)
- Katalog resmi dari **VoltAgent** yang merangkum **1.497+ Official Agent Skills** dari tim rekayasa terkemuka dunia (Vercel, Supabase, Cloudflare, Stripe, Anthropic, Sentry, Better Auth, GSAP, TestMu AI, dll.).
- Terintegrasi sebagai skill lokal (`awesome-agent-skills`) sehingga Antigravity dapat mencari rekomendasi tools resmi kapan saja melalui file referensi `directory.md`.

### 3. 🐘 Backend: CodeIgniter 4 Suite (`skills/codeigniter4/`)
- **`ci4-api`**: Pembuatan RESTful controller (`ResourceController`), standardisasi envelope JSON response, CORS handling, dan webhook.
- **`ci4-shield`**: Otentikasi API CodeIgniter Shield (Bearer tokens, Personal Access Tokens, Session auth, role-based permissions).
- **`ci4` & `ci4-advanced`**: Pola Entity mapping, Model validation rules, isolated migrations, dan module auto-discovery.
- **`codeigniter`**: Panduan pengujian unit test PHPUnit (`CIUnitTestCase`, `FeatureTestTrait`) dan filter keamanan.

### 4. 🟢 Frontend: Vue 3 & Nuxt Ecosystem (`skills/vue-ecosystem/`)
- **`vue-best-practices`**: Standar Vue 3 Composition API `<script setup lang="ts">`, reaktivitas (`ref`, `computed`, `watchEffect`), dan composables modular.
- **`vue-pinia-best-practices` & `pinia`**: State management Pinia terpusat, setup stores, dan pencegahan error reaktivitas.
- **`vue-router-best-practices`**: Dynamic routing, route meta, dan navigation auth guards.
- **`vueuse-functions`**: Pemanfaatan utilitas VueUse untuk interaksi browser, sensor, dan animasi.
- **`nuxt` & `nuxt-ui`**: Server-Side Rendering (SSR), composables `useFetch` / `$fetch`, Nuxt UI components, dan NuxtHub.
- **`nuxt-seo`**: Metadata otomatis, sitemap, OpenGraph tags, dan optimasi Core Web Vitals.
- **`vite` & `vitest`**: Konfigurasi build tool Vite dan unit testing Vitest.

### 5. 🎨 UI UX Pro Max Suite (`skills/ui-ux-pro-max/`)
- **Reasoning Rules:** 192 profil industri & aturan UX.
- **UI Styles:** 79 searchable styles (Glassmorphism, Minimalist, Bento Grid, Soft UI, Brutalism, dll.).
- **Palet Warna:** 192 palet terkurasi sesuai psikologi industri.
- **Tipografi:** 74 pairing Google Fonts dengan kode import siap pakai.
- **UX Guidelines:** 119 aturan WCAG & usability.
- **Tech Stacks:** 22 stacks (HTML/Tailwind, Vue, Nuxt, React, Flutter, dll.).
- **Search Engine:** Mesin pencari Python lokal (`scripts/search.py`).
- **Komponen Pendukung:** `brand`, `banner-design`, `design`, `design-system`, `slides`, `ui-styling`.

### 6. 🏛️ Designer Skills Suite (`skills/designer-skills/`)
Koleksi 111 skills dan 9 plugin desain profesional dari Owl-Listener:
- `ui-design` (19 skills), `interaction-design` (22 skills), `design-systems` (11 skills), `visual-critique` (7 skills), `ux-strategy` (12 skills), `design-research` (14 skills), `prototyping-testing` (10 skills), `design-ops` (9 skills), `designer-toolkit` (7 skills).

### 7. 🤌 Taste Skill Suite (`skills/taste-skill/`)
- Anti-slop frontend art direction yang didistilasi dari 247 situs kurasi Awwwards & One Page Love.

### 8. ⚙️ Global Configurations (`.gemini-config/`)
- `skills.json`: Pendaftaran seluruh path repositori ke Antigravity.
- `mcp_config.json`: Konfigurasi Model Context Protocol.

---

## 🚀 Cara Restore / Pemulihan ke Komputer Baru

Jalankan perintah berikut di PowerShell:

```powershell
.\restore.ps1
```

Script akan otomatis:
1. Menyalin seluruh aset ke `~/.gemini/` dan `~/.agents/skills/`.
2. Menghubungkan seluruh junction ke `~/.gemini/config/skills/`.
3. Memperbarui file konfigurasi `~/.gemini/config/skills.json`.

---

## 🏷️ Release History
- **v1.2.0**: Penambahan modul **Security Audit & Bug Hunter Suite** (`owasp-security`, `security-audit`) dan master katalog **Awesome Agent Skills** (1,497+ skills terkurasi). Total 179 skills terpasang global.
- **v1.1.0**: Penambahan keahlian backend CodeIgniter 4 API Suite dan frontend Vue 3 / Nuxt Ecosystem Suite.
- **v1.0.0**: Initial full backup seluruh skill dasar (UI/UX Pro Max, Designer Skills Pack 111 skills, Taste Skill, dan konfigurasi Antigravity global).
