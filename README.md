# 🧠 Antigravity AI Skills & Configuration Backup

Repositori ini berisi seluruh cadangan (*backup*) keahlian (*skills*), aturan penalaran desain (*design reasoning*), dan konfigurasi global untuk asisten koding **Google Antigravity**.

---

## 📦 Isi Backup

### 1. UI UX Pro Max Suite (`skills/ui-ux-pro-max/`)
- **Reasoning Rules:** 192 profil industri & aturan UX.
- **UI Styles:** 79 searchable styles (Glassmorphism, Minimalist, Bento Grid, Soft UI, Brutalism, dll.).
- **Palet Warna:** 192 palet terkurasi.
- **Tipografi:** 74 pairing Google Fonts dengan kode import.
- **UX Guidelines:** 119 aturan WCAG & usability.
- **Tech Stacks:** 22 stacks (React, Nuxt, Tailwind, Flutter, Svelte, dll.).
- **Search Engine:** Mesin pencari Python bawaan (`scripts/search.py`).
- **Pendukung:** `brand`, `banner-design`, `design`, `design-system`, `slides`, `ui-styling`.

### 2. Designer Skills Suite (`skills/designer-skills/`)
Koleksi lengkap 111 skills dan 9 plugin desain profesional dari Owl-Listener:
- **`ui-design` (19 skills):** *color-system, typography-scale, spacing-system, layout-grid, dark-mode-design, responsive-design, Gestalt laws, von-restorff-effect.*
- **`interaction-design` (22 skills):** *micro-interaction-spec, animation-principles, state-machine, form-design, navigation-patterns, loading-states, search-ux.*
- **`design-systems` (11 skills):** *design-token, component-spec, icon-system, theming-system, accessibility-audit, localization-design.*
- **`visual-critique` (7 skills):** *visual-hierarchy, typography-critique, color-critique, composition-critique, affordance-critique.*
- **`ux-strategy` (12 skills):** *information-architecture, journey-map, experience-mapping, competitive-audit, service-blueprint.*
- **`design-research` (14 skills):** *user-persona, empathy-map, jobs-to-be-done, usability-test-plan, card-sort-analysis.*
- **`prototyping-testing` (10 skills):** *heuristic-evaluation, usability-testing, a-b-experiment-spec.*
- **`design-ops` (9 skills):** *handoff-spec, design-qa-checklist, design-sprint-plan, design-debt-audit.*
- **`designer-toolkit` (7 skills):** *design-rationale, ux-writing, presentation-structure, case-study-structure.*

### 3. Taste Skill Suite (`skills/taste-skill/`)
- Anti-slop frontend art direction yang didistilasi dari 247 situs kurasi Awwwards & One Page Love.

### 4. Global Configurations (`.gemini-config/`)
- `skills.json`: Pendaftaran seluruh path repositori ke Antigravity.
- `mcp_config.json`: Konfigurasi integrasi Model Context Protocol.

---

## 🚀 Cara Restore / Pemulihan ke Komputer Baru

Jalankan perintah berikut di PowerShell (Run as Administrator jika diperlukan untuk pembuatan symlink/junction):

```powershell
.\restore.ps1
```

Script akan otomatis:
1. Menyalin aset ke direktori `~/.gemini/` dan `~/.agents/skills/`.
2. Menghubungkan seluruh junction ke `~/.gemini/config/skills/`.
3. Memperbarui file konfigurasi `~/.gemini/config/skills.json`.

---

## 🏷️ Release History
- **v1.0.0**: Initial full backup seluruh 140+ skill (UI/UX Pro Max, Designer Skills Pack 111 skills, Taste Skill, dan konfigurasi Antigravity global).
