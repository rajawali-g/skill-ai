# 🧠 Antigravity AI Skills & Configuration Backup

Repositori ini berisi seluruh cadangan (*backup*) keahlian (*skills*), aturan penalaran desain (*design reasoning*), pola arsitektur front-end (Vue 3/Nuxt), backend API (CodeIgniter 4), dan konfigurasi global untuk asisten koding **Google Antigravity**.

---

## 📦 Isi Lengkap Backup (170+ Skills)

### 1. Backend: CodeIgniter 4 Suite (`skills/codeigniter4/`)
Koleksi lengkap standar arsitektur REST API & aplikasi CodeIgniter 4:
- **`ci4-api`**: Pembuatan RESTful controller (`ResourceController`), standardisasi envelope JSON response, pagination, CORS handling, dan webhook.
- **`ci4-shield`**: Sistem otentikasi CodeIgniter Shield (Bearer tokens, Personal Access Tokens, Session auth, role-based permissions).
- **`ci4` & `ci4-advanced`**: Pola Entity mapping, Model validation rules, isolated migrations, dan module auto-discovery.
- **`codeigniter`**: Panduan pengujian unit test PHPUnit (`CIUnitTestCase`, `FeatureTestTrait`) dan filter keamanan.

### 2. Frontend: Vue 3 & Nuxt Ecosystem (`skills/vue-ecosystem/`)
Koleksi keahlian lengkap untuk pengembangan antarmuka modern:
- **`vue-best-practices`**: Standar Vue 3 Composition API `<script setup lang="ts">`, reaktivitas (`ref`, `computed`, `watchEffect`), dan composables modular.
- **`vue-pinia-best-practices` & `pinia`**: State management Pinia terpusat, setup stores, dan pencegahan error reaktivitas.
- **`vue-router-best-practices`**: Dynamic routing, route meta, dan navigation auth guards.
- **`vueuse-functions`**: Koleksi utilitas VueUse siap pakai untuk interaksi browser, sensor, dan animasi.
- **`nuxt` & `nuxt-ui`**: Server-Side Rendering (SSR), composables `useFetch` / `$fetch`, Nuxt UI components, dan NuxtHub.
- **`nuxt-seo`**: Metadata otomatis, sitemap, OpenGraph tags, dan optimasi Core Web Vitals.
- **`vite` & `vitest`**: Konfigurasi build tool Vite dan unit testing Vitest.

### 3. UI UX Pro Max Suite (`skills/ui-ux-pro-max/`)
- **Reasoning Rules:** 192 profil industri & aturan UX.
- **UI Styles:** 79 searchable styles (Glassmorphism, Minimalist, Bento Grid, Soft UI, Brutalism, dll.).
- **Palet Warna:** 192 palet terkurasi sesuai psikologi industri.
- **Tipografi:** 74 pairing Google Fonts dengan kode import siap pakai.
- **UX Guidelines:** 119 aturan WCAG & usability.
- **Tech Stacks:** 22 stacks (HTML/Tailwind, Vue, Nuxt, React, Flutter, dll.).
- **Search Engine:** Mesin pencari Python lokal (`scripts/search.py`).
- **Komponen Grafis Pendukung:** `brand`, `banner-design`, `design`, `design-system`, `slides`, `ui-styling`.

### 4. Designer Skills Suite (`skills/designer-skills/`)
Koleksi 111 skills dan 9 plugin desain profesional dari Owl-Listener:
- **`ui-design` (19 skills):** *color-system, typography-scale, spacing-system, layout-grid, dark-mode-design, responsive-design, Gestalt laws, von-restorff-effect.*
- **`interaction-design` (22 skills):** *micro-interaction-spec, animation-principles, state-machine, form-design, navigation-patterns, loading-states, search-ux.*
- **`design-systems` (11 skills):** *design-token, component-spec, icon-system, theming-system, accessibility-audit, localization-design.*
- **`visual-critique` (7 skills):** *visual-hierarchy, typography-critique, color-critique, composition-critique, affordance-critique.*
- **`ux-strategy` (12 skills):** *information-architecture, journey-map, experience-mapping, competitive-audit, service-blueprint.*
- **`design-research` (14 skills):** *user-persona, empathy-map, jobs-to-be-done, usability-test-plan, card-sort-analysis.*
- **`prototyping-testing` (10 skills):** *heuristic-evaluation, usability-testing, a-b-experiment-spec.*
- **`design-ops` (9 skills):** *handoff-spec, design-qa-checklist, design-sprint-plan, design-debt-audit.*
- **`designer-toolkit` (7 skills):** *design-rationale, ux-writing, presentation-structure, case-study-structure.*

### 5. Taste Skill Suite (`skills/taste-skill/`)
- Anti-slop frontend art direction yang didistilasi dari 247 situs kurasi Awwwards & One Page Love.

### 6. Global Configurations (`.gemini-config/`)
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
- **v1.1.0**: Penambahan keahlian backend **CodeIgniter 4 API Suite** (`ci4-api`, `ci4-shield`, `ci4-advanced`, dll.) dan frontend **Vue 3 / Nuxt Ecosystem Suite** (`vue-best-practices`, `pinia`, `vueuse-functions`, `nuxt-ui`, dll.). Total 176 skills terpasang global.
- **v1.0.0**: Initial full backup seluruh skill dasar (UI/UX Pro Max, Designer Skills Pack 111 skills, Taste Skill, dan konfigurasi Antigravity global).
