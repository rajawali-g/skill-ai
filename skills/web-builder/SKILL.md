---
name: web-builder
description: Plans, scaffolds, builds, and improves websites in an existing or new project. Use for website creation, redesigns, or substantial web feature work; adapts its questions and implementation to the user's brief and the project's existing stack.
---

# WebBuilder

Bantu pengguna merancang dan membangun website secara kolaboratif. Gunakan pertimbangan teknis dan visual; jangan menganggap satu template atau stack cocok untuk semua proyek.

## Pilih jalur kerja

1. **Perubahan kecil atau brief sudah jelas:** langsung inspeksi proyek seperlunya, lalu kerjakan permintaan. Jangan memulai wawancara atau meminta persetujuan blueprint untuk perubahan terfokus.
2. **Website baru atau perubahan besar:** lakukan discovery adaptif, susun blueprint singkat, kemudian implementasikan. Minta konfirmasi blueprint hanya jika ada keputusan penting yang belum dipastikan pengguna atau jika tindakan yang akan dilakukan sulit dibalik.
3. **Pengguna meminta ide/rekomendasi saja:** berikan rekomendasi tanpa membuat atau mengubah berkas.

## Sebelum mengubah kode

- Periksa direktori kerja, berkas instruksi proyek (misalnya `AGENTS.md`, `GEMINI.md`, atau aturan lokal yang tersedia), struktur aplikasi, dan perubahan lokal yang relevan.
- Kenali framework, package manager, pola komponen, sistem styling, aset, dan perintah pemeriksaan yang sudah ada. Ikuti konvensi proyek; jangan mengganti stack atau menginisialisasi ulang proyek tanpa alasan yang diminta.
- Hindari menimpa berkas atau aset pengguna. Bila scaffold akan menulis ke direktori yang sudah berisi berkas, pilih output kosong yang aman atau adaptasikan implementasi ke proyek.
- Jangan mengasumsikan integrasi skill lain tersedia. Jika skill spesialis tidak tersedia, lanjutkan dengan kemampuan saat ini dan jelaskan batasnya bila berpengaruh.

## Discovery adaptif untuk proyek baru

Tanyakan hanya hal yang belum terjawab oleh brief atau proyek, dalam kelompok maksimal 3 pertanyaan. Izinkan pengguna menjawab bebas atau meminta rekomendasi. Jangan mengulang pertanyaan yang sudah dijawab.

Prioritaskan hal berikut, sesuai relevansi:

- Tujuan website dan tindakan utama yang diharapkan dari pengunjung.
- Audiens dan konten/halaman penting.
- Apakah situs statis/pasif atau dinamis (data berubah, akun, formulir yang diproses, atau integrasi backend). Tanyakan kebutuhan dashboard admin secara terpisah; situs dinamis tidak otomatis memerlukan dashboard.
- Identitas brand, logo/aset yang tersedia, dan gaya visual.
- Kebutuhan fungsi: autentikasi, data, formulir, pembayaran, pencarian, CMS, dan sebagainya.
- Stack, database, batasan hosting, atau preferensi teknologi.

Jika detail kecil belum diketahui, nyatakan asumsi yang masuk akal dan lanjutkan. Jangan memaksa pengguna memilih dari daftar panjang. Tawarkan maksimal tiga arah visual/teknis yang relevan jika pilihan memang diperlukan.

## Blueprint dan implementasi

Untuk proyek baru atau perubahan besar, rangkum secara ringkas sebelum implementasi: tujuan, audiens, halaman/section, arah visual, mode situs statis/dinamis, kebutuhan dashboard admin (ya/tidak/tidak relevan), stack yang dipilih atau diasumsikan, fitur lingkup kerja, serta asumsi/batasan. Jangan tampilkan seluruh katalog sebagai formulir. Blueprint berfungsi menyelaraskan lingkup; lanjutkan tanpa jeda ketika pengguna sudah memberi mandat jelas.

Implementasikan dalam irisan yang bisa ditinjau:

1. Bangun struktur dan alur utama dengan konten yang relevan, bukan placeholder generik.
2. Terapkan visual yang konsisten, responsif, dan sesuai brand/proyek. Gunakan token desain bila cocok dengan stack.
3. Lengkapi interaksi yang termasuk lingkup. Jangan mengklaim layanan backend, autentikasi, pembayaran, database, analytics, chatbot, atau integrasi eksternal aktif jika hanya membuat UI/mockup.
4. Perhatikan semantik HTML, label form, navigasi keyboard, focus state, kontras, reduced motion, dan layout layar kecil.
5. Pertahankan struktur dan konvensi proyek. Jangan menambah dependensi besar jika solusi yang sudah tersedia cukup.

## Gunakan scaffold dengan akurat

Scaffolder opsional dan ditujukan untuk membuat starter statis baru, bukan mengimplementasikan semua fitur katalog atau menyesuaikan proyek yang sudah berjalan.

- Temukan lokasi folder skill dari `SKILL.md` yang sedang digunakan. Jalankan `scripts/scaffold_web.py --help` menggunakan Python 3 sebelum memilih opsi. Gunakan path absolut hasil inspeksi atau working directory yang terverifikasi; jangan gunakan placeholder path.
- Berikan `--output` ke lokasi proyek yang dimaksud pengguna. Jangan menulis output ke dalam direktori instalasi skill.
- Periksa target output terlebih dahulu. Script membuat direktori jika belum ada dan menulis/mengganti `index.html`, `style.css`, `main.js`, `blueprint.json`, serta SVG logo/favicon di `assets/icons/`; jangan arahkan ke direktori berisi berkas penting.
- Scaffold menerima pilihan nama, tagline, tipe tampilan, tema, database, nomor fitur, mode situs (`--site-mode static|dynamic`), dan rencana dashboard admin (`--dashboard yes|no`). Nilai mode/dashboard dan database/fitur adalah metadata rencana; scaffold tidak membuat database, backend, atau dashboard admin.
- Bedakan `--display dashboard` (archetype tata letak bergaya aplikasi) dari `--dashboard yes` (rencana panel administrasi). Dashboard admin memerlukan situs dinamis; dynamic site tetap bisa tidak memiliki dashboard.
- Script menghasilkan SVG logo dan `favicon.svg`; ia tidak menghasilkan fallback PNG/ICO atau apple-touch icon terpisah. Bila pengguna memerlukan aset tersebut, buat/konversi secara eksplisit dan pastikan hasilnya benar-benar tersedia.
- Script mendukung preset, mode interaktif, dan multi-page; periksa `--help` agar memakai opsi yang tersedia saat ini. Target output dapat berisi berkas yang akan ditimpa.
- Preset seperti government, tourism, SaaS, portfolio, ecommerce, business, education, community, dan events adalah titik awal. Jangan menganggap preset government sebagai default atau membawa bahasa, jam operasional, lokasi, aturan, maupun klaim domain tertentu ke preset lain. Sesuaikan semua halaman dan CTA dengan konteks pengguna.
- Setelah scaffold, inspeksi berkas keluaran, hapus atau ganti konten contoh yang tidak relevan, dan sesuaikan dengan brief. Jangan berhenti pada template jika pengguna meminta website yang berfungsi penuh.
- Jangan menyebut hasil scaffold atau skor auditor sebagai siap produksi. Status produksi baru dapat dinilai setelah konten, integrasi nyata, konfigurasi rahasia, privasi/hukum, deployment, dan pemeriksaan di lingkungan target ditangani sesuai kebutuhan proyek.

## Referensi

Baca hanya referensi yang diperlukan untuk keputusan saat ini:

- `references/interview_playbook.md` untuk contoh pertanyaan discovery.
- `references/feature_catalog.md` untuk merinci fitur atau integrasi tertentu. Katalog adalah daftar ide/ruang lingkup, bukan bukti fitur tersedia.
- `references/tech_stack_matrix.md` untuk membandingkan stack. Verifikasi rekomendasi terhadap kebutuhan proyek dan dokumentasi terkini bila versi/dukungan berpengaruh.
- `references/component_snippets.md` hanya untuk pola komponen yang relevan; tinjau dan adaptasikan, jangan menyalin semua snippet tanpa konteks.
- `scripts/audit_site.py` adalah pemeriksa heuristik berbasiskan pola, bukan audit WCAG, keamanan, kualitas produksi, atau browser. Jalankan hanya jika pemeriksaan diminta; jelaskan batasannya.
- `README.md` untuk gambaran konsep skill.

Gunakan path relatif dari folder skill. Jangan mengandalkan path komputer tertentu atau menyatakan angka katalog sebagai fakta jika belum memeriksa dokumennya.

## Verifikasi dan laporan

- Ikuti instruksi pengguna tentang verifikasi. Jangan menjalankan rangkaian tes yang tidak diminta; bila tidak ada permintaan, lakukan hanya pemeriksaan minimal yang diperlukan untuk memastikan perubahan aman, seperti membaca diff atau memvalidasi konfigurasi yang diubah.
- Jangan mengklaim sudah menjalankan server, tes, build, aksesibilitas audit, atau pemeriksaan browser kecuali benar-benar dilakukan.
- Ringkas apa yang berubah, keputusan/asumsi penting, pemeriksaan yang dilakukan, dan batasan yang masih ada. Jika ada langkah lanjutan yang jelas, sebutkan secara singkat.

## Prinsip desain

Hasil harus terasa dibuat untuk kebutuhan proyek, bukan keluaran template generik. Hindari efek dekoratif yang tidak mendukung konten, placeholder kosong, animasi berlebihan, dan klaim kualitas absolut seperti “Awwwards-ready”. Prioritaskan hirarki yang jelas, tipografi terbaca, komposisi konsisten, aset yang relevan, performa, dan aksesibilitas.
