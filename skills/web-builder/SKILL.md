---
name: web-builder
description: 🌐 [WebBuilder Suite] Framework pembuatan website otomatis modern berbasis dialog percakapan iteratif (sistem ⇄ pengguna). Mencakup eksplorasi niche & persona, 3 rekomendasi nama & tagline AI / input kustom, generator logo SVG & favicon suite, matriks 7 tipe tampilan, pemilihan database (NoSQL, SQLite, MySQL, PostgreSQL, Static), orkestrasi katalog 55 fitur & integrasi, serta perakitan kode HTML5/CSS/JS zero-slop standar Awwwards.
argument-hint: "[init|interview|scaffold|features] [options]"
metadata:
  author: skill-ai
  version: "1.0.0"
---

# 🌐 WebBuilder: Conversational Web Creation Framework

Framework otomasi pembuatan website modern melalui dialog percakapan kolaboratif (*Conversational Co-Creation*) antara sistem AI (Lead Web Architect) dan pengguna (Product Owner).

## 🚀 Kapan Menggunakan Skill Ini

Gunakan skill ini (`/web-builder` atau saat pengguna meminta membuat website baru) untuk:
- Membuat website dari nol dengan metode wawancara interaktif (bukan one-shot generation kasar).
- Menentukan persona, audiens target, dan menghasilkan 3 rekomendasi nama & deskripsi kreatif atau mengakomodasi input kustom brand.
- Menangani logo & favicon (menggunakan aset milik pengguna atau men-generate SVG logo vector & high-DPI favicon otomatis).
- Memilih arsitektur layout dari **7 Tipe Tampilan** standar industri.
- Memilih arsitektur database: **NoSQL**, **SQLite**, **MySQL/MariaDB**, **PostgreSQL**, atau **None/Static**.
- Memilih dan mengimplementasikan fitur dari **Master Katalog 55 Fitur & Integrasi**.
- Menghasilkan kode murni (HTML5, CSS Design Tokens, JavaScript ES Modules) berstandar Awwwards, zero-slop, cepat, responsif, dan aksesibel.
- Menyempurnakan dan merevisi tampilan secara percakapan (*conversational refinement loop*).

---

## 🧭 Alur Kerja 5 Tahapan (5-Phase Lifecycle)

Saat dipanggil dengan `/web-builder`, jalankan alur percakapan terpandu:

### 📍 Fase 1: Elicitation & Discovery (Wawancara Terarah)
Gunakan metode **Chunked Guided Inquiry** (3-4 pertanyaan per putaran agar pengguna tidak kewalahan):

#### Putaran 1: Niche, Persona, Brand Identity & Tipe Tampilan
1. **Niche & Tujuan**: Tanyakan jenis website yang ingin dibangun (contoh: Landing Page Pariwisata/Daerah, SaaS, Profil Bisnis, Portofolio Kreatif, Portal Media).
2. **Target Audiens & Persona**: Tanyakan siapa pengunjung utama (contoh: turis domestik & mancanegara, calon investor, pembeli produk, masyarakat umum).
3. **Rekomendasi Nama & Tagline (Brand Identity)**:
   Secara proaktif racik dan tawarkan **3 Alternatif Rekomendasi Nama & Deskripsi/Tagline** berdasarkan niche dan persona yang dipilih, atau berikan opsi bagi pengguna untuk mengisinya sendiri:
   - 💡 **Opsi A (Modern & Catchy)**: Ringkas, punchy, mudah diingat.
   - 🏛️ **Opsi B (Resmi & Kredibel)**: Formal, informatif, deskriptif.
   - 🌟 **Opsi C (Action & Story-Driven)**: Mengajak aksi emosional dan bercerita.
   - ✍️ **Opsi D (Input Kustom Pengguna)**: Pengguna memasukkan nama & tagline miliknya sendiri.
4. **Kepemilikan Logo & Favicon**:
   - 📁 **Opsi A (Milik Sendiri)**: Pengguna telah memiliki file logo (`logo.svg`/`logo.png`) dan favicon di foldernya.
   - ✨ **Opsi B (Sistem Bantu Buatkan Otomatis)**: Sistem akan men-generate **Modern Minimalist Vector Logo (SVG)** murni (responsif, tajam, dan selaras tema) serta paket **Favicon Suite** (`favicon.svg`, fallback PNG/ICO, apple-touch-icon) langsung ke `<head>`.
5. **Aksi Utama (Primary CTA)**: Apa tindakan utama yang diinginkan (contoh: WhatsApp, Reservasi, Coba Gratis, Kontak).
6. **Pemilihan Tipe Tampilan (7 Layout Paradigms)**:
   Paparkan 7 tipe tampilan standar industri berikut:
   1. **Single-Page**: 1 halaman panjang, alur scroll berkesinambungan dengan sticky anchor navigation.
   2. **Multi-Page**: Terbagi beberapa halaman terpisah (Beranda, Profil/Layanan, Detail, Kontak).
   3. **Responsive Design**: Tata letak fleksibel yang adaptif di desktop, tablet, dan smartphone (standar wajib).
   4. **Card-Based (Bento Grid)**: Modul kartu terpisah berisi gambar, judul, dan data ringkas yang interaktif.
   5. **Grid-Heavy / Magazine Style**: Kolom berita padat berisi feed artikel mirip majalah/surat kabar digital.
   6. **Fullscreen / Immersive**: Visual penuh layar dengan canvas 3D, background video, atau grafis sinematik.
   7. **Dashboard / App-Like**: Shell aplikasi dengan sidebar navigasi tetap dan area kerja dinamis.

#### Putaran 2: Karakter Estetika & Emosi Visual
Tawarkan 3 rekomendasi gaya visual terkurasi (berkolaborasi dengan `/ui-ux`):
- **Gaya A: Dark Modern Luxury / Glassmorphism** (Deep dark, frosted glass cards, subtle neon glow).
- **Gaya B: Bento Grid Minimalist** (Clean white/soft gray, ultra-crisp typography, organized modules).
- **Gaya C: Immersive Nature / 3D Cinematic** (Vibrant organic colors, 3D interactive terrain, tangible textures).

---

### 📍 Fase 2: Architecture, Database & Feature Blueprint

#### 1. Penentuan Database
Paparkan 4 opsi database utama sesuai kebutuhan aplikasi:
- 🍃 **NoSQL** *(MongoDB / Firebase / KV)*: Schema-less, dokumen JSON, cocok untuk katalog dinamis & chat realtime.
- 🪶 **SQLite**: File lokal `.sqlite3`, zero-config, super cepat, ideal untuk MVP, dashboard personal, dan edge.
- 🐬 **MySQL / MariaDB**: Standar RDBMS terpopuler, ACID relasional ketat, hosting luas, sinergi dengan CodeIgniter 4 (`/ci4`).
- 🐘 **PostgreSQL**: RDBMS enterprise tingkat lanjut, JSONB indexing, geospasial (PostGIS), sinergi dengan Supabase / Prisma.
- ⚡ **None / Static Web**: Murni file HTML/CSS/JS tanpa backend database untuk web portofolio atau landing page.

#### 2. Pemilihan Fitur dari Katalog 55 Fitur
Tampilkan 6 klaster cerdas atau terima nomor pilihan pengguna:
- **Klaster A (UI/UX & Interaksi)**: #1 (Alert/Toast), #2 (Peta), #4 (Live Chat/WA), #7 (Medsos), #8 (Animasi Scroll), #9 (Search/Filter), #10 (Pagination), #16 (Dark/Light Mode), #51 (Banner Slider).
- **Klaster B (Data & Berkas)**: #5 (Grafik Data), #11 (Grafik Dinamis), #13 (Ekspor/Impor), #15 (Uploader/Cropper), #40 (Arsip Dokumen), #55 (Cloud Storage).
- **Klaster C (Autentikasi & Keamanan)**: #6 (Anti-Spam Form), #12 (MFA/OTP), #18 (RBAC Login), #23 (Proteksi XSS/CSRF), #25 (Audit Log), #35 (Cookie Consent), #39 (Manajemen Akun), #49 (SSO), #52 (Manajemen Sesi), #54 (Multi-Tenant).
- **Klaster D (Konten & Bahasa)**: #26 (CMS Halaman), #27 (Workflow Draf), #31 (Pengaturan Situs), #32 (Multi-Bahasa i18n), #43 (Menu Dinamis).
- **Klaster E (Komunikasi & AI)**: #3 (Payment Gateway), #14 (Push Notif), #34 (Email Transaksional), #47 (AI Chatbot), #48 (Knowledge Base), #50 (Status Layanan), #53 (Log Email).
- **Klaster F (DevOps & Backend)**: #17 (SEO OpenGraph), #19 (Sitemap/Robots), #20 (Schema JSON-LD), #21 (Web Vitals), #22 (Aksesibilitas WCAG), #24 (Backup), #28 (PWA), #29 (Analytics), #30 (Cache), #33 (Global Search), #36 (REST API), #37 (Error Pages), #38 (CI/CD), #41 (Cron Jobs), #42 (Queue Jobs), #44 (Swagger API), #45 (QA Testing), #46 (Staging/Env).

#### 3. Penerbitan Project Blueprint
Tampilkan ringkasan blueprint ke pengguna dan minta konfirmasi sebelum menulis kode:
```markdown
### 📐 Project Blueprint: [Nama Website]
- Niche & Persona: ...
- Nama & Tagline: ...
- Status Logo & Favicon: ...
- Tipe Tampilan: ...
- Database: ...
- Fitur Terpilih: [Daftar nomor & nama fitur]
- Palet HSL & Tipografi Google Fonts: ...
- Rencana Section: [Navbar, Hero, Bento Grid, Showcase, CTA, Footer]
```

---

### 📍 Fase 3: Foundation & Design Tokens
1. Tulis `style.css` dengan token HSL murni:
   - `--color-bg`, `--color-surface`, `--color-surface-glass`
   - `--color-primary`, `--color-accent`, `--color-text`, `--color-text-muted`
   - Skala spasi modular: `--space-xs`, `--space-sm`, `--space-md`, `--space-lg`, `--space-xl`
   - Radius & shadow: `--radius-md`, `--radius-lg`, `--shadow-glow`
2. Reset CSS modern & tipografi dari Google Fonts (`Inter`, `Outfit`, `Plus Jakarta Sans`).

---

### 📍 Fase 4: Progressive Assembly (Perakitan Bertahap)
1. **HTML Struktur Semantik**:
   - `<header>` dengan sticky navbar dan drawer responsif.
   - `<main>` dengan `<section>` beridentitas jelas (`hero`, `features`, `showcase`, `map`, `faq`, `contact`).
   - SVG logo vector tajam & terintegrasi.
   - Favicon links lengkap (`<link rel="icon" type="image/svg+xml" href="...">`).
   - Aksesibilitas: tag ARIA, kontras warna WCAG AA, focus outline ramah keyboard.
2. **JavaScript Modular (`main.js`)**:
   - Toast notifications untuk fitur #1.
   - Dark/Light mode switcher untuk fitur #16.
   - Smooth anchor scrolling & drawer navigation.
   - Opsional: integrasi Leaflet untuk fitur #2, Chart.js untuk fitur #5, atau GSAP ScrollTrigger untuk fitur #8.

---

### 📍 Fase 5: Conversational Refinement (Loop Revisi Percakapan)
Setelah kode dibuat, buka dialog revisi interaktif:
- Tanyakan apakah ada aspek visual, warna, teks hero, atau tata letak kartu yang ingin disesuaikan.
- Terima instruksi bahasa alami (contoh: *"Buat tombol CTA lebih mencolok dan ubah kartu ke-3 jadi testimonial"*).
- Lakukan pembaruan terfokus pada CSS/JS tanpa merusak struktur dasar.

---

## 🛠️ CLI Helper Script: `scaffold_web.py`

Untuk men-generate fondasi instan, gunakan script scaffolding bawaan:
```bash
python skills/web-builder/scripts/scaffold_web.py --name "MinselScape" --display "single-page" --theme "dark-luxury" --db "postgresql" --features "1,2,4,8,16,21,22,47" --output "./output-site"
```

Argumen yang didukung:
- `--name`: Nama website.
- `--tagline`: Tagline / subjudul website.
- `--display`: Salah satu dari 7 tipe (`single-page`, `multi-page`, `responsive`, `card-based`, `magazine`, `fullscreen`, `dashboard`).
- `--theme`: Tema visual (`dark-luxury`, `bento-minimal`, `nature-cinematic`).
- `--db`: Database (`nosql`, `sqlite`, `mysql`, `postgresql`, `none`).
- `--features`: Nomor fitur dipisah koma (contoh: `1,2,4,8,16,21,22,47`).
- `--output`: Direktori output tempat kode dibuat.

---

## 🎼 Orkestrasi Kolaborasi Skill Lain

WebBuilder bertindak sebagai **Konduktor Utama** yang memanggil spesialisasi lain:
- Gaya & Warna: `/ui-ux`
- Foto & Tekstur PBR: `/image-3d`
- Animasi 3D Canvas: `/threejs`
- Scrollytelling: `/gsap`
- Koreografi Easing: `/motion`
- Form Audit & Keamanan: `/security`
- Backend MVC & Auth: `/ci4`
- Frontend Komponen Reaktif: `/vue`

---

## 📚 Dokumen Referensi Tambahan

- **[README.md](file:///e:/project/htdocs/skill-ai/skills/web-builder/README.md)**: Gambaran arsitektur lengkap dan filosofi WebBuilder.
- **[Interview Playbook](file:///e:/project/htdocs/skill-ai/skills/web-builder/references/interview_playbook.md)**: Panduan naskah dialog percakapan terperinci langkah demi langkah.
- **[Master Feature Catalog](file:///e:/project/htdocs/skill-ai/skills/web-builder/references/feature_catalog.md)**: Panduan teknis & pola kode untuk 55 fitur & integrasi.
