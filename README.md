# 🧠 Antigravity AI Skills & Configuration Backup

Repositori ini berisi seluruh cadangan (*backup*) keahlian (*skills*), aturan penalaran desain (*design reasoning*), pola arsitektur front-end (Vue 3/Nuxt), backend API (CodeIgniter 4), audit keamanan aplikasi (*bug hunter* / OWASP), pengolahan aset 3D Web & PBR, katalog master *Awesome Agent Skills*, dan konfigurasi global untuk asisten koding **Google Antigravity**.

---

## ⌨️ Panduan Pemanggilan Cepat dengan Slash (`/`) & Tooltips

Di dalam chat Antigravity IDE, Anda dapat langsung memanggil keahlian khusus hanya dengan mengetik garis miring (`/`). Saat Anda mengetik `/` atau mengarahkan kursor (*hover*) ke salah satu perintah slash, IDE akan memunculkan **Tooltip interaktif** yang menjelaskan kapabilitas skill tersebut.

### 📋 Tabel Master Slash Commands

| Slash Command | Tooltip / Keterangan Interaktif | Mengorkestrasi Sub-Skills |
| :--- | :--- | :--- |
| **`/image-3d`** | 📸 **[3D Image & PBR Suite]** Pindai folder foto lokal, analisis peran 3D, kembangkan jadi tekstur PBR (Normal, Roughness, AO), seamless tiling, Power-of-Two GPU, dan konversi ke model 3D GLB via Trellis/Tripo. | `image-to-3d-web`, `fal-3d` |
| **`/threejs`** | 🎮 **[Three.js & WebGPU Master]** Panduan lengkap grafis 3D web (r186), WebGPU TSL, tata pencahayaan IBL/HDR, material PBR, shader kustom, kamera, post-processing bloom, dan Rapier physics. | `threejs-core` (13 skills), `threejs-webgpu` (27 skills), `threejs-interactive` (3 skills) |
| **`/gsap`** | ✨ **[GSAP Animation Master]** Animasi web GreenSock v3, ScrollTrigger scrollytelling, koordinasi timeline, smooth scroll Lenis, integrasi Three.js ticker, dan koreografi web kelas Awwwards. | `gsap-official` (8 skills), `gsap-creative` (5 skills) |
| **`/motion`** | 🎭 **[Motion Choreography Suite]** Fondasi estetika gerak universal Disney, penentuan kurva easing, arketipe kepribadian UI, audit performa FPS, dan pembatasan stagger delay. | `motion-design`, `motion-director`, `web-motion-auditor` |
| **`/ui-ux`** | 🎨 **[UI/UX Pro Max Suite]** Sistem desain cerdas dengan 192 profil industri, 79 style visual (Bento, Glassmorphism, Minimalist), psikologi warna, tipografi, dan kepatuhan WCAG 2.2. | `ui-ux-pro-max`, `brand`, `designer-skills` (111 skills), `taste-skill` |
| **`/security`** | 🛡️ **[Security Master Suite]** Audit keamanan kode menyeluruh berbasis OWASP Top 10:2025, ASVS 5.0, celah PHP/API, CWE Top 25, pencegahan injection, IDOR, dan kalkulasi risiko CVSS. | `owasp-security`, `security-audit` |
| **`/ci4`** | 🐘 **[CodeIgniter 4 Suite]** Backend RESTful API, otentikasi Shield (Bearer Token/Session), Entity mapping, Model validation, dan arsitektur backend. | `ci4-api`, `ci4-shield`, `ci4`, `codeigniter` |
| **`/vue`** / **`/nuxt`** | 🟢 **[Vue 3 & Nuxt Suite]** Standar Vue 3 Composition API `<script setup lang="ts">`, Pinia state, NuxtHub, SSR, dan komponen antarmuka modern. | `vue-best-practices`, `pinia`, `nuxt`, `nuxt-ui` |

> 💡 **Sub-Skills Granular Tetap Tersedia:** Anda juga dapat memanggil sub-skill secara langsung untuk tugas ultra-spesifik, misalnya `/threejs-lighting`, `/threejs-materials`, `/gsap-scrolltrigger`, `/image-to-3d-web`, atau `/owasp-security`.

---

## 🤝 Resep Kolaborasi Lintas Skill (Sinergi Nyata)

### 🌟 1. The 3D Creative Web Quad (Landing Page Sinematik / Scrollytelling)
Sinergi: **`/image-3d` ➔ `/threejs` ➔ `/gsap` ➔ `/ui-ux`**

```text
Contoh Prompt:
/image-3d kembangkan foto di folder public/textures/alam/ menjadi PBR maps dan tekstur seamless
lalu /threejs buatkan canvas 3D dengan pencahayaan IBL alam dan material MeshPhysicalMaterial
lalu /gsap sinkronkan rotasi kamera dan pergantian chapter pemandangan dengan native scroll halaman
dan /ui-ux rancang overlay kartu informasi transparan (glassmorphism) dengan tipografi modern
```

- **Langkah 1 (`/image-3d`)**: Mengolah foto smartphone/kamera menjadi PBR maps tajam (`Normal +Y OpenGL`, `Roughness`, `AO`, `Displacement`) serta Power-of-Two (POT) GPU.
- **Langkah 2 (`/threejs`)**: Memasang scene 3D dengan ACES Filmic Tone Mapping, IBL HDR environment, dan material fisik realistis.
- **Langkah 3 (`/gsap`)**: Menghubungkan scroll halaman ke timeline animasi 3D tanpa frame drop (60 FPS).
- **Langkah 4 (`/ui-ux`)**: Menata elemen teks dan tombol interaktif di atas canvas agar memiliki kontras tinggi dan estetika kelas Awwwards.

### 🛡️ 2. Full-Stack Web Application (Aman, Modular, Cepat)
Sinergi: **`/ui-ux` ➔ `/vue` ➔ `/ci4` ➔ `/security`**

```text
Contoh Prompt:
/ui-ux rancang antarmuka dashboard admin bento grid dengan dark mode elegan
lalu /vue buatkan komponen interaktifnya menggunakan Composition API dan Pinia
lalu /ci4 siapkan RESTful controller backend dengan otentikasi CodeIgniter Shield Bearer Token
dan /security lakukan audit komprehensif terhadap celah SQL Injection, IDOR, dan CSRF
```

### ⚡ 3. High-Performance Motion & Micro-Interaction
Sinergi: **`/motion` ➔ `/gsap`**

```text
Contoh Prompt:
/motion tentukan kurva easing dan token durasi transisi modal agar terasa mewah tanpa lag
lalu /gsap implementasikan animasinya dengan gsap.timeline dan pembersihan siklus hidup di onUnmounted
```

---

## 📦 Isi Lengkap Backup (247+ Skills)

### 1. 🛡️ Security Audit & Bug Hunter Suite (`skills/security/`)
Koleksi lengkap audit kelayakan keamanan aplikasi berbasis standar global:
- **`security`** *(Master Slash)*: Pemicu cepat audit keamanan menyeluruh via `/security`.
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

### 2. 📸 3D Web Image & PBR Suite (`skills/image-to-3d/`) - *2 Skills*
Suite khusus untuk memproses dan mengembangkan foto 2D menjadi aset 3D Web fotorealistis:
- **`image-3d`** *(Master Slash)*: Pemicu cepat inspeksi folder & konversi 3D via `/image-3d`.
- **`image-to-3d-web`**:
  - **Batch Inspection:** Memindai seluruh foto di folder yang ditentukan, mengklasifikasikan perannya (*surface texture*, *environment IBL*, *isolated prop*, *billboard 2.5D*), dan memverifikasi kepatuhan Power-of-Two (POT).
  - **PBR Generator Engine (`scripts/pbr_generator.py`):** Otomatis membuat peta **Normal Map (+Y OpenGL Three.js)** via filter gradien Sobel, **Roughness Map**, **Ambient Occlusion (AO)**, dan **Displacement/Height Map**.
  - **Seamless Tiling:** Mengubah foto biasa menjadi tekstur berulang tanpa sambungan (*tileable*) untuk lantai/dinding/terrain 3D.
  - **GPU POT Resizer:** Mengubah ukuran foto ke 512, 1024, atau 2048 dengan kompresi WebP & PNG agar Three.js mipmapping tajam tanpa lag.
  - **Three.js Code Generator:** Otomatis menghasilkan file `threejs_materials.js` dengan konfigurasi color space yang benar (`SRGBColorSpace` vs `NoColorSpace`).
- **`fal-3d`**:
  - Mengubah foto 2D atau prompt menjadi model 3D nyata (`.glb` / `.gltf`) menggunakan model AI terdepan (Microsoft Trellis, Tencent Hunyuan3D v2, Tripo3D).

### 3. 🎮 Three.js 3D Graphics & WebGPU Suite (`skills/threejs/`) - *43 Skills*
Paket keahlian grafis 3D terlengkap untuk WebGL, WebGPU, TSL (*Three.js Shading Language*), Physics, dan WebXR:
- **`threejs`** *(Master Slash)*: Pemicu cepat rancang bangun 3D Web via `/threejs`.
- **Core WebGL & R3F r186 (CloudAI-X - 13 Skills)**:
  - `threejs-fundamentals`, `threejs-geometry`, `threejs-materials`, `threejs-lighting`, `threejs-textures`
  - `threejs-animation`, `threejs-shaders`, `threejs-postprocessing`, `threejs-performance`
  - `threejs-loaders` (GLTF, Draco, HDR), `threejs-interaction`, `threejs-asset-pipeline`, `threejs-react-three-fiber`
  - *Menghilangkan halusinasi AI terhadap API lama (`Clock` ➔ `Timer`, `RGBELoader` ➔ `HDRLoader`, dll.)*.
- **WebGPU & TSL Procedural Engine (Linegel - 27 Skills)**:
  - *Routing & QA*: `threejs-choose-skills`, `threejs-debugging`, `threejs-visual-validation`, `threejs-compatibility-fallbacks`
  - *Lighting & Camera*: `threejs-camera-controls-and-rigs`, `threejs-scalable-real-time-shadows` (CSM), `threejs-ambient-contact-shading` (GTAO), `threejs-bloom`, `threejs-exposure-color-grading`, `threejs-image-pipeline`
  - *Worlds & Nature*: `threejs-sky-atmosphere-and-haze`, `threejs-volumetric-clouds`, `threejs-spectral-ocean` (FFT ocean waves), `threejs-water-optics`, `threejs-rain-snow-and-wet-surfaces`
  - *Procedural Content*: `threejs-procedural-fields`, `threejs-procedural-geometry`, `threejs-procedural-materials`, `threejs-procedural-motion-systems`, `threejs-procedural-planets`, `threejs-procedural-vegetation`, `threejs-procedural-buildings-and-cities`, `threejs-procedural-creatures`, `threejs-dynamic-surface-effects`, `threejs-particles-trails-and-effects`, `threejs-black-holes-and-space-effects`, `threejs-object-sculptor`
- **Interactive, Physics & WebXR (Alton47 - 3 Skills)**:
  - `threejs-physics`: Integrasi physics engine modern (Rapier WASM & Cannon-es), rigid bodies, colliders, constraints.
  - `threejs-audio`: Spatial & positional audio listener 3D.
  - `threejs-xr`: WebXR, VR controllers, AR hit-testing, dan interaksi spasial.

### 4. ✨ GSAP Animation & Creative 3D Web Suite (`skills/gsap/`) - *13 Skills*
Integrasi resmi animasi GreenSock dan arsitektur penghubung ke visual Three.js:
- **`gsap`** *(Master Slash)*: Pemicu cepat animasi & scrollytelling via `/gsap`.
- **Official GreenSock Skills (`gsap-official-skills` - 8 Skills)**:
  - `gsap-core`: Syntax dasar v3, tweens, targetting properti numeric Three.js.
  - `gsap-timeline`: Sequencing animasi kompleks, orchestration label.
  - `gsap-scrolltrigger`: Scroll-driven animation, scrubbing, pinning, trigger bounds.
  - `gsap-frameworks`: Penggunaan `gsap.context()` & `ctx.revert()` di Vue 3, Nuxt, Svelte, React untuk pencegahan memory leak.
  - `gsap-react`: Integrasi hook `@gsap/react` dan `useGSAP`.
  - `gsap-plugins`: Flip, Draggable, MotionPath, Observer, TextPlugin, SplitText.
  - `gsap-performance`: Optimasi frame rate, koordinasi render ticker, GPU compositing.
  - `gsap-utils`: Math helpers (`clamp`, `mapRange`, `interpolate`, `pipe`, `wrap`).
- **Creative & Three.js Bridging Skills (`gsap-creative-skills` - 5 Skills)**:
  - `threejs-gsap-integration`: Standar arsitektur penghubung Three.js + GSAP (animasi kamera, sinkronisasi `gsap.ticker` tanpa stutter, mouse parallax `quickTo`, pembersihan siklus hidup Vue/React).
  - `build-threejs-scroll-worlds`: Membangun dunia 3D persisten yang dikendalikan oleh native scroll melalui authored chapters.
  - `cinematic-gsap-lenis-motion-system`: Sistem gerak sinematik mewah kelas editorial Awwwards dengan GSAP + Lenis smooth scroll.
  - `gsap-scrolltrigger-storytelling`: Storytelling produk sticky bertahap dan progressive UI reveals.
  - `build-awwwards-quality-sites`: Panduan koreografi visual standar Awwwards Site of the Day.

### 5. 🎭 Motion Design & Choreography Suite (`skills/motion/`) - *4 Skills*
Fondasi estetika, prinsip gerak universal, dan tata kelola ritme animasi web:
- **`motion`** *(Master Slash)*: Pemicu cepat desain gerak via `/motion`.
- **`motion-design`** *(LottieFiles Universal)*: Prinsip animasi Disney yang diadaptasi untuk antarmuka web (antisipasi, overshoot, follow-through), durasi mikro-interaksi (100–300ms vs scene 800ms+), larangan linear easing untuk pergerakan spasial, dan arketipe kepribadian gerak (*Playful*, *Premium*, *Corporate*, *Energetic*).
- **`motion-director`** *(FrankX)*: Desain konsep gerak, pemilihan stack optimal (CSS vs GSAP vs Rive vs Three.js), dan token waktu.
- **`site-motion-excellence-director`** *(FrankX)*: Koreografi situs sinematik, *still-frame gate* (dilarang menganimasi frame statis yang buruk), dan kepatuhan `prefers-reduced-motion`.
- **`web-motion-auditor`** *(FrankX)*: Evaluasi audit kualitas animasi web, pembatasan *stagger delay* agar pengguna tidak menunggu konten, dan pengujian performa FPS.

### 6. 🎨 UI UX Pro Max Suite (`skills/ui-ux-pro-max/`)
- **`ui-ux`** *(Master Slash)*: Pemicu cepat sistem desain via `/ui-ux`.
- **Reasoning Rules:** 192 profil industri & aturan UX.
- **UI Styles:** 79 searchable styles (Glassmorphism, Minimalist, Bento Grid, Soft UI, Brutalism, dll.).
- **Palet Warna:** 192 palet terkurasi sesuai psikologi industri.
- **Tipografi:** 74 pairing Google Fonts dengan kode import siap pakai.
- **UX Guidelines:** 119 aturan WCAG & usability.
- **Tech Stacks:** 22 stacks (HTML/Tailwind, Vue, Nuxt, React, Flutter, dll.).
- **Search Engine:** Mesin pencari Python lokal (`scripts/search.py`).
- **Komponen Pendukung:** `brand`, `banner-design`, `design`, `design-system`, `slides`, `ui-styling`.

### 7. 🏛️ Designer Skills Suite (`skills/designer-skills/`)
Koleksi 111 skills dan 9 plugin desain profesional dari Owl-Listener:
- `ui-design` (19 skills), `interaction-design` (22 skills), `design-systems` (11 skills), `visual-critique` (7 skills), `ux-strategy` (12 skills), `design-research` (14 skills), `prototyping-testing` (10 skills), `design-ops` (9 skills), `designer-toolkit` (7 skills).

### 8. 🤌 Taste Skill Suite (`skills/taste-skill/`)
- Anti-slop frontend art direction yang didistilasi dari 247 situs kurasi Awwwards & One Page Love.

### 9. 🟢 Frontend: Vue 3 & Nuxt Ecosystem (`skills/vue-ecosystem/`)
- **`vue-best-practices` & `vue`**: Standar Vue 3 Composition API `<script setup lang="ts">`, reaktivitas (`ref`, `computed`, `watchEffect`), dan composables modular.
- **`vue-pinia-best-practices` & `pinia`**: State management Pinia terpusat, setup stores, dan pencegahan error reaktivitas.
- **`vue-router-best-practices`**: Dynamic routing, route meta, dan navigation auth guards.
- **`vueuse-functions`**: Pemanfaatan utilitas VueUse untuk interaksi browser, sensor, dan animasi.
- **`nuxt` & `nuxt-ui`**: Server-Side Rendering (SSR), composables `useFetch` / `$fetch`, Nuxt UI components, dan NuxtHub.
- **`nuxt-seo`**: Metadata otomatis, sitemap, OpenGraph tags, dan optimasi Core Web Vitals.
- **`vite` & `vitest`**: Konfigurasi build tool Vite dan unit testing Vitest.

### 10. 🐘 Backend: CodeIgniter 4 Suite (`skills/codeigniter4/`)
- **`ci4` & `ci4-api`**: Pembuatan RESTful controller (`ResourceController`), standardisasi envelope JSON response, CORS handling, dan webhook.
- **`ci4-shield`**: Otentikasi API CodeIgniter Shield (Bearer tokens, Personal Access Tokens, Session auth, role-based permissions).
- **`ci4` & `ci4-advanced`**: Pola Entity mapping, Model validation rules, isolated migrations, dan module auto-discovery.
- **`codeigniter`**: Panduan pengujian unit test PHPUnit (`CIUnitTestCase`, `FeatureTestTrait`) dan filter keamanan.

### 11. 📚 Awesome Agent Skills Master Catalog (`skills/awesome-agent-skills/`)
- Katalog resmi dari **VoltAgent** yang merangkum **1.497+ Official Agent Skills** dari tim rekayasa terkemuka dunia (Vercel, Supabase, Cloudflare, Stripe, Anthropic, Sentry, Better Auth, GSAP, TestMu AI, dll.).
- Terintegrasi sebagai skill lokal (`awesome-agent-skills`) sehingga Antigravity dapat mencari rekomendasi tools resmi kapan saja melalui file referensi `directory.md`.

### 12. ⚙️ Global Configurations (`.gemini-config/`)
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
- **v1.6.1**: Penambahan **Master Slash Commands Hub** (`/security`, `/image-3d`, `/threejs`, `/gsap`, `/motion`, `/ui-ux`) dengan integrasi tooltip interaktif, panduan pemanggilan cepat slash `/`, dan resep kolaborasi lintas suite di README. Total **247 skills** terpasang global.
- **v1.6.0**: Penambahan **3D Web Image & PBR Suite** (`image-to-3d-web`, `fal-3d`). Kemampuan memindai folder foto lokal mana pun, menganalisis properti visual, dan mengembangkannya menjadi peta PBR lengkap (Normal, Roughness, AO, Displacement), tekstur seamless, Power-of-Two GPU optimization, dan generasi mesh 3D / Three.js code.
- **v1.5.0**: Penambahan **Motion Design & Choreography Suite** (4 skills: LottieFiles Universal Animation Principles + FrankX Motion Director, Site Choreography, dan Web Motion Auditor). Melengkapi *The Trinity of Motion* (Motion Design + GSAP + Three.js). Total 239 skills terpasang global.
- **v1.4.0**: Penambahan **GSAP Animation & Creative 3D Web Suite** (13 skills: 8 skills resmi GreenSock + 5 skills bridging Three.js scrollytelling & Awwwards motion). Total 235 skills terpasang global.
- **v1.3.0**: Penambahan **Three.js 3D Graphics & WebGPU Suite** (43 skills lengkap: WebGL r186, WebGPU / TSL procedural simulation, Rapier/Cannon physics, spatial audio, dan WebXR). Total 222 skills terpasang global.
- **v1.2.0**: Penambahan modul **Security Audit & Bug Hunter Suite** (`owasp-security`, `security-audit`) dan master katalog **Awesome Agent Skills** (1,497+ skills terkurasi). Total 179 skills terpasang global.
- **v1.1.0**: Penambahan keahlian backend CodeIgniter 4 API Suite dan frontend Vue 3 / Nuxt Ecosystem Suite.
- **v1.0.0**: Initial full backup seluruh skill dasar (UI/UX Pro Max, Designer Skills Pack 111 skills, Taste Skill, dan konfigurasi Antigravity global).
