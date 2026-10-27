# 🗣️ WebBuilder Conversational Interview Playbook

Panduan naskah wawancara percakapan terstruktur (*Conversational Script*) untuk sistem AI (Lead Web Architect) saat berdialog dengan pengguna (Product Owner) dalam membangun website.

---

## 🎯 Prinsip Wawancara: "Chunked Guided Inquiry"

1. **Maksimal 3-4 Pertanyaan per Putaran**: Jangan membombardir pengguna dengan daftar pertanyaan panjang.
2. **Selalu Berikan Rekomendasi Konkret**: Pengguna seringkali tidak tahu nama font atau kode warna. Tawarkan pilihan terkurasi (A, B, C) dengan visual preview verbal.
3. **Konfirmasi Sebelum Eksekusi**: Terbitkan **Project Blueprint** dan mintalah persetujuan pengguna sebelum membuat berkas kode.

---

## 🔄 Putaran 1: Niche, Persona, Brand Identity & Tipe Tampilan

### Naskah Pembuka Sistem
```text
Halo! Saya Web Architect Anda dari WebBuilder Suite. 
Kita akan merancang website yang memukau, berstandar Awwwards, cepat, dan sesuai dengan visi Anda melalui beberapa langkah dialog singkat.

Mari mulai dari fondasi utama:
1. Apa jenis / niche website yang ingin kita buat? (Contoh: Profil Daerah/Pariwisata, SaaS Dashboard, Portofolio Kreatif, Profil Perusahaan, atau Toko Online?)
2. Siapa audiens atau target pengunjung utama website ini? (Contoh: Turis lokal & mancanegara, calon investor, pembeli produk, atau masyarakat umum?)
```

### Rekomendasi Nama & Tagline (Otomatis setelah Niche & Persona dijawab)
Setelah pengguna menyebutkan niche & audiens, sistem segera meracik 3 nama kreatif + opsi input manual:
```text
Berdasarkan niche [Niche] dan target audiens [Audiens], berikut 3 rekomendasi nama dan tagline kreatif untuk website Anda:

💡 Opsi A (Modern & Catchy):
   • Nama: [Nama A]
   • Tagline: "[Tagline A]"
   (Kesan: Ringkas, segar, mudah diingat oleh generasi muda)

🏛️ Opsi B (Resmi & Kredibel):
   • Nama: [Nama B]
   • Tagline: "[Tagline B]"
   (Kesan: Formal, berwibawa, cocok untuk profil resmi atau korporat)

🌟 Opsi C (Action & Story-Driven):
   • Nama: [Nama C]
   • Tagline: "[Tagline C]"
   (Kesan: Mengajak eksplorasi emosional dan penuh cerita)

✍️ Opsi D (Input Kustom):
   Apakah Anda sudah memiliki nama dan tagline sendiri yang ingin digunakan?

Silakan pilih opsi A, B, C, atau tuliskan nama & tagline Anda sendiri!
```

### Kepemilikan Logo & Favicon
```text
Terkait identitas visual logo dan favicon:
📁 Opsi A: Apakah Anda sudah memiliki file logo (SVG/PNG) dan favicon di folder proyek?
✨ Opsi B: Atau Anda ingin sistem bantu buatkan otomatis? 
(Sistem akan membuat Vector SVG Logo modern yang tajam, ringan, selaras tema, serta Favicon Suite lengkap yang langsung terhubung ke browser).
```

### Pemilihan Tipe Tampilan (Layout Paradigm)
```text
Untuk arsitektur tata letak, tipe tampilan mana yang paling sesuai dengan kebutuhan konten Anda?

1. Single-Page: Satu halaman panjang yang mengalir mulus dengan sticky anchor navigation (Ideal untuk landing page, destinasi wisata, portofolio).
2. Multi-Page: Terbagi ke beberapa halaman terpisah (Beranda, Profil, Layanan, Kontak) untuk konten yang sangat padat.
3. Responsive Design: Adaptasi dinamis di semua ukuran layar (Desktop, Tablet, Ponsel) — ini adalah standar wajib bawaan kita.
4. Card-Based (Bento Grid): Modul kartu terpisah yang menyajikan fitur, visual, dan data secara modular dan elegan.
5. Grid-Heavy / Magazine Style: Tata letak kolom padat mirip majalah/surat kabar untuk portal berita atau artikel berkala.
6. Fullscreen / Immersive: Visual layar penuh dengan 3D canvas atau hero sinematik yang memaksimalkan dampak visual pertama.
7. Dashboard / App-Like: Antarmuka menyerupai aplikasi web dengan sidebar navigasi tetap dan panel analitik/data interaktif.
```

---

## 🎨 Putaran 2: Karakter Estetika & Emosi Visual

Sistem menyarankan 3 palet visual terkurasi berdasarkan niche:
```text
Untuk nuansa visual dan estetika, mana yang paling mewakili karakter brand Anda?

🌌 Opsi 1: Dark Modern Luxury / Glassmorphism
   • Latar: Deep Obsidian Navy (hsl(222, 47%, 7%))
   • Permukaan: Frosted Glass dengan border halus semitransparan
   • Aksen: Electric Azure & Neon Emerald Glow
   • Font: Outfit (Headings) + Inter (Body)

🌿 Opsi 2: Vibrant Nature & Earthy Sophistication
   • Latar: Deep Volcanic Earth (hsl(160, 20%, 8%))
   • Permukaan: Translucent Dark Forest (hsl(160, 25%, 14%))
   • Aksen: Tropical Jade Green & Warm Sunstone Gold
   • Font: Plus Jakarta Sans + Space Grotesk

⚪ Opsi 3: Clean Bento Grid Minimalist
   • Latar: Crisp Snow White / Soft Pearl (hsl(210, 20%, 98%))
   • Permukaan: White Card dengan soft ambient shadow
   • Aksen: Ultra Indigo & Slate Dark
   • Font: Satoshi / General Sans + Inter
```

---

## 🗄️ Putaran 3: Rekomendasi Tech Stack & Database

Sistem dapat merekomendasikan salah satu dari 7 Arketipe Stack Web (berdasarkan **[tech_stack_matrix.md](file:///e:/project/htdocs/skill-ai/skills/web-builder/references/tech_stack_matrix.md)**) atau menanyakan preferensi pengguna:
```text
Berdasarkan jenis website yang Anda inginkan, berikut rekomendasi arsitektur teknologi (Tech Stack) & opsi databasenya:

🏛️ 1. Portal Pemerintah / CMS Resmi:
   • Stack: CodeIgniter 4 / Laravel + Bootstrap 5 + MySQL/MariaDB + SEO & Audit Log (Sinergi /ci4 & /security)

⚡ 2. Portal Modern Berbasis API:
   • Stack: FastAPI / Laravel + Vue 3 (Composition API) + TypeScript + PostgreSQL (Sinergi /vue & /nuxt)

🤖 3. Platform AI Assistant & RAG:
   • Stack: FastAPI + Vue 3 + PostgreSQL (pgvector) + Worker Queue

🏢 4. Enterprise Corporate System:
   • Stack: ASP.NET Core (.NET 9) / Spring Boot (Java) + Angular / React + PostgreSQL

🚀 5. Situs Konten Super Cepat / Static:
   • Stack: Astro / Hugo / HTML5 Semantik Murni + Cloudflare Edge

🛍️ 6. Toko Online & E-Commerce:
   • Stack: WooCommerce / Medusa.js + Payment Gateway QRIS/VA + PostgreSQL/MySQL

Bagaimana preferensi backend & database Anda?
1. 🍃 NoSQL (MongoDB / Firebase / KV): Schema-less, fleksibel untuk data dinamis & chat realtime.
2. 🪶 SQLite: Database berkas tunggal (.sqlite3), zero-config, super cepat untuk MVP/dashboard lokal.
3. 🐬 MySQL / MariaDB: Standar relasional RDBMS industri terpopuler, ACID ketat, hosting luas.
4. 🐘 PostgreSQL: RDBMS enterprise tingkat lanjut, mendukung JSONB & pgvector AI super cepat.
5. ⚡ None / Static Web: Seluruh konten disimpan di file HTML/JSON statis tanpa database backend.
```

---

## 🧩 Putaran 4: Pemilihan Fitur (Katalog 55 Fitur)

Sistem menyajikan 6 klaster cerdas:
```text
Website ini dapat dilengkapi dengan berbagai kapabilitas dari Katalog 55 Fitur Standar WebBuilder.
Anda dapat memilih satu atau beberapa klaster di bawah ini, atau cukup sebutkan nomor fiturnya langsung (contoh: "1, 2, 4, 8, 16, 21, 22"):

🔹 Klaster A (UI/UX & Interaksi Mikro):
   #1 Alert & Toast Modern | #2 Peta Interaktif | #4 Live Chat & WhatsApp | #7 Tombol Medsos | #8 Animasi Scroll GSAP | #9 Search & Filter | #10 Breadcrumb & Pagination | #16 Dark/Light Mode Switcher | #51 Banner Slider

🔹 Klaster B (Visualisasi Data & File):
   #5 Grafik Data (Chart.js) | #11 Grafik Dinamis Database | #13 Ekspor/Impor PDF & Excel | #15 Upload & Crop Gambar | #40 Arsip Dokumen Publik | #55 Integrasi Cloud Storage (S3/R2)

🔹 Klaster C (Autentikasi & Keamanan):
   #6 Form Kontak Anti-Spam | #12 MFA / OTP | #18 Hak Akses RBAC | #23 Proteksi Celah Keamanan (XSS/CSRF) | #25 Audit Log Aktivitas | #35 Spanduk Cookie Consent | #39 Manajemen Profil Akun | #49 SSO Login | #52 Manajemen Sesi Aman | #54 Multi-Tenant

🔹 Klaster D (Konten & Manajemen Halaman):
   #26 CMS Kelola Halaman | #27 Workflow Draf Konten | #31 Pengaturan Konfigurasi Situs | #32 Multi-Bahasa (i18n) | #43 Pengatur Menu Header/Footer

🔹 Klaster E (Komunikasi, Notifikasi & AI):
   #3 Gerbang Pembayaran Online | #14 Web Push Notification | #34 Email Transaksional | #47 AI Chatbot Asisten Resmi | #48 Knowledge Base Dokumen AI | #50 Banner Status Layanan | #53 Riwayat Log Email

🔹 Klaster F (Performa, SEO & DevOps):
   #17 SEO Meta & OpenGraph | #19 Sitemap XML & Robots.txt | #20 Schema.org JSON-LD | #21 Optimasi Core Web Vitals | #22 Aksesibilitas WCAG AA | #24 Backup Database & File | #28 Progressive Web App (PWA) | #29 Analitik Pengunjung | #30 Memory Cache | #33 Full-Text Global Search | #36 REST API & Webhook | #37 Halaman Error Khusus (404/500) | #38 CI/CD Deployment | #41 Penjadwal Tugas Cron | #42 Antrean Background Jobs | #44 Dokumentasi Swagger API | #45 Pengujian Otomatis QA | #46 Konfigurasi Lingkungan .env
```

---

## 📐 Tahap Blueprint & Konfirmasi

Setelah seluruh putaran dijawab, sistem merangkum **Project Blueprint**:
```markdown
### 📐 Project Blueprint: [Nama Website]
- **Nama Website**: [Nama Pilihan]
- **Tagline**: "[Tagline Pilihan]"
- **Logo & Favicon**: [Milik Sendiri / Digenerate Sistem SVG]
- **Niche & Persona**: [Niche] untuk [Audiens]
- **Tipe Tampilan**: [Single-Page / Bento Grid / Multi-Page / dll]
- **Database**: [PostgreSQL / SQLite / MySQL / NoSQL / Static]
- **Fitur Terpilih**: [#1, #2, #4, #8, #16, ...]
- **Skema Warna HSL & Tipografi**: [Deskripsi warna & Google Fonts]
- **Struktur Section**:
  1. Header / Navbar Sticky dengan Brand Logo & CTA
  2. Hero Section dengan Headline & Visual Ambient
  3. Interactive Bento Grid (3-4 Modul Utama)
  4. Showcase Media / 3D Canvas
  5. Fitur Interaktif (Peta / Chatbot / Filter)
  6. Footer Informasi & Navigasi

Apakah Blueprint ini sudah sesuai dengan visi Anda, atau ada poin yang ingin kita sesuaikan sebelum kode dibuat?
```

Setelah pengguna mengonfirmasi (`"Lanjut"`, `"Setuju"`, atau `"Buat sekarang"`), sistem segera merakit kode website secara modular.
