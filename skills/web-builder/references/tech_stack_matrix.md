# 🏛️ WebBuilder: Master Web Technology Stack & Framework Matrix (545 Teknologi)

Katalog referensi komprehensif 545 teknologi web, runtime, framework, library, CMS, dan platform DevOps untuk pemetaan arsitektur dan rekomendasi stack pada WebBuilder Suite.

---

## 📌 Panduan Evaluasi & Batas Cakupan

| Aspek | Penjelasan |
| :--- | :--- |
| **Tujuan** | Katalog referensi luas framework, library, CMS, platform, dan tools terkait pengembangan web. |
| **Batas cakupan** | Tidak mungkin menjamin semua proyek yang pernah dibuat; daftar mencakup ekosistem utama dan sejumlah alternatif niche/legacy. |
| **Status** | Label *'Aktif atau status perlu diperiksa'* bukan verifikasi langsung status rilis. Periksa dokumentasi resmi, aktivitas repositori, lisensi, dan kompatibilitas sebelum memilih. |
| **Tingkat penggunaan** | Menunjukkan perkiraan kompleksitas/konteks, bukan ranking popularitas atau jaminan kualitas. |
| **Arsitektur** | Framework backend, frontend, full-stack, CMS, platform, dan tools sengaja dibedakan. Jangan menganggap semuanya saling menggantikan. |
| **Sumber tren** | Stack Overflow Developer Survey 2026: https://survey.stackoverflow.co/2026/technology/data/web-framework |
| **Saran proyek pemerintah** | Evaluasi keamanan, pemeliharaan jangka panjang, dukungan bahasa, biaya hosting, kemampuan tim, audit trail, backup, aksesibilitas, dan interoperabilitas. |

---

## 🎯 Rekomendasi Stack Berdasarkan Kebutuhan Proyek

| Kebutuhan Proyek | Stack Rekomendasi | Pertimbangan & Sinergi Skill |
| :--- | :--- | :--- |
| **Portal Pemerintah / CMS** | **CodeIgniter 4** atau **Laravel** + **Bootstrap 5** / **Tailwind** + Editor WYSIWYG + Modul SEO + Backup & Audit Log | Sederhana, aman, mudah dikelola tim PHP lokal, biaya hosting ekonomis, integrasi langsung dengan `/ci4` & `/security`. |
| **Portal Modern dengan API** | **Laravel** / **FastAPI** + **Vue 3** (Composition API) + **TypeScript** + **PostgreSQL** / **MySQL** | Pemisahan tegas arsitektur frontend dan backend, reaktivitas tinggi, tipe data aman dengan `/vue` & `/nuxt`. |
| **AI Assistant / RAG Platform** | **FastAPI** + **Vue 3** / **Streamlit** + **PostgreSQL (pgvector)** atau Qdrant + Celery / Redis Queue | Pemisahan proses *ingestion* dokumen, retrieval RAG cepat, caching interaktif, dan antarmuka percakapan ramah pengguna. |
| **Enterprise .NET** | **ASP.NET Core** + **Angular** / **React** / **Blazor** + **SQL Server** / **PostgreSQL** | Standar korporat skala besar, ekosistem Microsoft, kontrol keamanan dan tata kelola enterprise yang ketat. |
| **Aplikasi Java Enterprise** | **Spring Boot** + **Angular** / **React** / **Vue** + **PostgreSQL** / **Oracle** | Stabilitas tinggi untuk transaksi finansial, ekosistem JVM matang, dan skalabilitas microservices. |
| **Situs Konten Statis / Dokumentasi** | **Astro** / **Hugo** / **Eleventy (11ty)** + Headless CMS (Decap / Strapi / Tina) jika diperlukan | Waktu muat ultra cepat (0ms JS by default), skor Core Web Vitals 100, hosting gratis di edge (Cloudflare Pages / Vercel). |
| **E-Commerce & Transaksional** | **WooCommerce**, **Medusa.js**, **Saleor**, **Shopware**, atau platform SaaS (Shopify) | Pertimbangan gateway pembayaran lokal (QRIS, VA), manajemen stok multi-gudang, kepatuhan pajak, dan audit keamanan transaksi. |

---

## 📋 Tabel Master 545 Teknologi Web

| No. | Kategori | Jenis | Tingkat Penggunaan | Bahasa / Runtime | Framework / Teknologi | Status / Catatan | Keterangan |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Native / Platform Web | Fondasi | Dasar | HTML | HTML5 | Aktif | Standar markup web |
| 2 | Native / Platform Web | Fondasi | Dasar | CSS | CSS3 | Aktif | Standar styling web |
| 3 | Native / Platform Web | Fondasi | Dasar | JavaScript | JavaScript (ES Modules) | Aktif | Bahasa utama browser |
| 4 | Native / Platform Web | Fondasi | Dasar | TypeScript | TypeScript | Aktif | Superset JavaScript |
| 5 | Native / Platform Web | Fondasi | Dasar | JavaScript / Web Platform | Web Components | Aktif | Standar komponen native |
| 6 | Native / Platform Web | Fondasi | Dasar | Web API | Fetch API | Aktif | API HTTP browser |
| 7 | Native / Platform Web | Fondasi | Dasar | JavaScript / Node.js | Node.js HTTP module | Aktif | HTTP server native |
| 8 | Native / Platform Web | Fondasi | Dasar | TypeScript / Deno | Deno standard HTTP APIs | Aktif | Runtime dan API native |
| 9 | Native / Platform Web | Fondasi | Dasar | Python | Python http.server | Aktif | Server sederhana; bukan untuk produksi umum |
| 10 | Native / Platform Web | Fondasi | Dasar | Go | Go net/http | Aktif | HTTP server standard library |
| 11 | Native / Platform Web | Fondasi | Dasar | PHP | PHP Native | Aktif | Tanpa framework |
| 12 | Native / Platform Web | Fondasi | Dasar | Java / JVM | Java Servlet API | Aktif | Fondasi aplikasi Java web |
| 13 | Native / Platform Web | Fondasi | Dasar | C# / .NET | ASP.NET Core Minimal APIs | Aktif | Model endpoint minimal |
| 14 | Native / Platform Web | Fondasi | Dasar | Rust | Rust std / hyper ecosystem | Aktif | Hyper merupakan library HTTP, bukan framework penuh |
| 15 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Bootstrap | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 16 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Tailwind CSS | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 17 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Bulma | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 18 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Foundation | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 19 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | UIkit | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 20 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Pico CSS | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 21 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Pure.css | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 22 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Skeleton | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 23 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Semantic UI (legacy status perlu diperiksa) | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 24 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Open Props | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 25 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Materialize CSS | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 26 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Material Design Components Web | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 27 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Shoelace | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 28 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | DaisyUI | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 29 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Flowbite | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 30 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Preline UI | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 31 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Chakra UI | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 32 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | MUI (Material UI) | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 33 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Ant Design | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 34 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Mantine | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 35 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | shadcn/ui | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 36 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Radix UI | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 37 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Headless UI | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 38 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | PrimeVue | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 39 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Vuetify | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 40 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Quasar UI | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 41 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Element Plus | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 42 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Naive UI | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 43 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Arco Design | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 44 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Fluent UI | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 45 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Carbon Design System | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 46 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Kendo UI | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 47 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Syncfusion UI | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 48 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | DevExtreme | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 49 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Wijmo | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 50 | CSS Framework / UI Component | Frontend / UI | Dasar–Enterprise | CSS / JavaScript / TypeScript | Ext JS | Aktif atau status perlu diperiksa | UI toolkit/library; bukan semuanya framework aplikasi |
| 51 | DOM / Progressive Enhancement | Frontend Library | Dasar–Menengah | JavaScript | jQuery | Aktif atau legacy | Library atau pendekatan frontend |
| 52 | DOM / Progressive Enhancement | Frontend Library | Dasar–Menengah | JavaScript | Alpine.js | Aktif atau legacy | Library atau pendekatan frontend |
| 53 | DOM / Progressive Enhancement | Frontend Library | Dasar–Menengah | JavaScript / HTML | htmx | Aktif atau legacy | Library atau pendekatan frontend |
| 54 | DOM / Progressive Enhancement | Frontend Library | Dasar–Menengah | JavaScript | Stimulus | Aktif atau legacy | Library atau pendekatan frontend |
| 55 | DOM / Progressive Enhancement | Frontend Library | Dasar–Menengah | JavaScript / HTML | Turbo / Hotwire | Aktif atau legacy | Library atau pendekatan frontend |
| 56 | DOM / Progressive Enhancement | Frontend Library | Dasar–Menengah | JavaScript | Lodash | Aktif atau legacy | Library atau pendekatan frontend |
| 57 | DOM / Progressive Enhancement | Frontend Library | Dasar–Menengah | JavaScript | Underscore.js | Aktif atau legacy | Library atau pendekatan frontend |
| 58 | DOM / Progressive Enhancement | Frontend Library | Dasar–Menengah | JavaScript | MooTools | Aktif atau legacy | Library atau pendekatan frontend |
| 59 | DOM / Progressive Enhancement | Frontend Library | Dasar–Menengah | JavaScript | Prototype.js | Aktif atau legacy | Library atau pendekatan frontend |
| 60 | DOM / Progressive Enhancement | Frontend Library | Dasar–Menengah | JavaScript | Petite Vue | Aktif atau legacy | Library atau pendekatan frontend |
| 61 | DOM / Progressive Enhancement | Frontend Library | Dasar–Menengah | JavaScript / HTML | Unpoly | Aktif atau legacy | Library atau pendekatan frontend |
| 62 | DOM / Progressive Enhancement | Frontend Library | Dasar–Menengah | JavaScript | Swup | Aktif atau legacy | Library atau pendekatan frontend |
| 63 | DOM / Progressive Enhancement | Frontend Library | Dasar–Menengah | JavaScript | Barba.js | Aktif atau legacy | Library atau pendekatan frontend |
| 64 | PHP Backend / MVC | Backend / Monolith | Menengah–Profesional | PHP | Laravel | Aktif | MVC/full-stack PHP |
| 65 | PHP Backend / MVC | Backend / Monolith | Menengah–Profesional | PHP | CodeIgniter 4 | Aktif | MVC PHP ringan |
| 66 | PHP Backend / MVC | Backend / Monolith | Profesional–Enterprise | PHP | Symfony | Aktif | Komponen dan full-stack PHP |
| 67 | PHP Backend / MVC | Backend / Monolith | Menengah–Profesional | PHP | CakePHP | Aktif | MVC PHP |
| 68 | PHP Backend / MVC | Backend / Monolith | Menengah–Profesional | PHP | Yii 2 | Aktif | MVC PHP; periksa dukungan versi |
| 69 | PHP Backend / MVC | Backend / Monolith | Profesional | PHP | Yii 3 | Status versi perlu diperiksa | Generasi Yii berikutnya |
| 70 | PHP Backend / MVC | Backend / Monolith | Profesional–Enterprise | PHP | Laminas MVC / Mezzio | Aktif; ekosistem Zend berevolusi | PHP |
| 71 | PHP Backend / MVC | Backend / Monolith | Menengah–Profesional | PHP | Nette | Aktif | PHP |
| 72 | PHP Backend / MVC | Backend / Monolith | Profesional | PHP | Phalcon | Aktif; periksa kompatibilitas versi | PHP extension-based |
| 73 | PHP Backend / MVC | Backend / Monolith | Profesional | PHP | Spiral Framework | Aktif | PHP |
| 74 | PHP Backend / MVC | Backend / Monolith | Dasar–Menengah | PHP | Flight PHP | Aktif | Microframework |
| 75 | PHP Backend / MVC | Backend / Monolith | Menengah | PHP | Slim | Aktif | Microframework |
| 76 | PHP Backend / MVC | Backend / Monolith | Menengah | PHP | Fat-Free Framework (F3) | Status pemeliharaan perlu diperiksa | PHP microframework |
| 77 | PHP Backend / MVC | Backend / Monolith | Legacy | PHP | Silex | Tidak direkomendasikan untuk proyek baru | Symfony microframework lama |
| 78 | PHP Backend / MVC | Backend / Monolith | Legacy / maintenance | PHP | Lumen | Periksa status resmi | Laravel microframework lama |
| 79 | PHP Backend / MVC | Backend / Monolith | Profesional–Enterprise | PHP | Drupal module ecosystem | Aktif | CMS framework ecosystem |
| 80 | Python Backend / API | Backend | Menengah–Enterprise | Python | Django | Aktif | Full-stack MVC |
| 81 | Python Backend / API | Backend | Dasar–Profesional | Python | Flask | Aktif | Microframework |
| 82 | Python Backend / API | Backend | Menengah–Profesional | Python | FastAPI | Aktif | API-first, async support |
| 83 | Python Backend / API | Backend | Profesional | Python | Starlette | Aktif | ASGI toolkit |
| 84 | Python Backend / API | Backend | Profesional | Python | Litestar | Aktif | ASGI framework |
| 85 | Python Backend / API | Backend | Profesional | Python | Falcon | Aktif | API framework |
| 86 | Python Backend / API | Backend | Profesional | Python | Sanic | Aktif | Async web framework |
| 87 | Python Backend / API | Backend | Profesional | Python | aiohttp | Aktif | Async HTTP client/server |
| 88 | Python Backend / API | Backend | Profesional | Python | Tornado | Aktif | Async networking/web |
| 89 | Python Backend / API | Backend | Dasar–Menengah | Python | Bottle | Aktif | Microframework |
| 90 | Python Backend / API | Backend | Menengah–Profesional | Python | Pyramid | Aktif | Flexible web framework |
| 91 | Python Backend / API | Backend | Menengah | Python | CherryPy | Aktif; periksa status rilis | Python web framework |
| 92 | Python Backend / API | Backend | Menengah | Python | Web2py | Status pemeliharaan perlu diperiksa | Full-stack Python |
| 93 | Python Backend / API | Backend | Menengah–Profesional | Python | TurboGears | Aktif; periksa versi | Python full-stack |
| 94 | Python Backend / API | Backend | Menengah | Python | Masonite | Periksa status proyek | Python MVC |
| 95 | Python Backend / API | Backend | Menengah–Enterprise | Python | Frappe Framework | Aktif | Metadata-driven full-stack Python |
| 96 | Python Backend / API | Backend | Profesional | Python | Robyn | Periksa kematangan dan status | Async Python framework |
| 97 | Python Backend / API | Backend | Spesialis / legacy | Python | Hug | Status perlu diperiksa | API framework lama |
| 98 | JavaScript / TypeScript Backend | Backend / API | Dasar–Enterprise | JavaScript / TypeScript / Node.js / Bun / Deno | Node.js | Aktif | Runtime, bukan framework |
| 99 | JavaScript / TypeScript Backend | Backend / API | Dasar–Profesional | JavaScript / TypeScript / Node.js / Bun / Deno | Express.js | Aktif | Minimal web framework |
| 100 | JavaScript / TypeScript Backend | Backend / API | Menengah–Profesional | JavaScript / TypeScript / Node.js / Bun / Deno | Fastify | Aktif | Performance-focused |
| 101 | JavaScript / TypeScript Backend | Backend / API | Menengah | JavaScript / TypeScript / Node.js / Bun / Deno | Koa | Aktif; ekosistem lebih kecil | Node.js |
| 102 | JavaScript / TypeScript Backend | Backend / API | Menengah–Profesional | JavaScript / TypeScript / Node.js / Bun / Deno | Hapi | Aktif | Configuration-centric |
| 103 | JavaScript / TypeScript Backend | Backend / API | Profesional–Enterprise | JavaScript / TypeScript / Node.js / Bun / Deno | NestJS | Aktif | TypeScript architecture |
| 104 | JavaScript / TypeScript Backend | Backend / API | Menengah–Profesional | JavaScript / TypeScript / Node.js / Bun / Deno | AdonisJS | Aktif | Full-stack Node.js |
| 105 | JavaScript / TypeScript Backend | Backend / API | Menengah | JavaScript / TypeScript / Node.js / Bun / Deno | Sails.js | Aktif; periksa versi | MVC/realtime |
| 106 | JavaScript / TypeScript Backend | Backend / API | Menengah–Profesional | JavaScript / TypeScript / Node.js / Bun / Deno | Feathers | Aktif | Service-oriented |
| 107 | JavaScript / TypeScript Backend | Backend / API | Profesional–Enterprise | JavaScript / TypeScript / Node.js / Bun / Deno | LoopBack | Aktif | API framework |
| 108 | JavaScript / TypeScript Backend | Backend / API | Menengah–Profesional | JavaScript / TypeScript / Node.js / Bun / Deno | Hono | Aktif | Multi-runtime/edge |
| 109 | JavaScript / TypeScript Backend | Backend / API | Menengah–Profesional | JavaScript / TypeScript / Node.js / Bun / Deno | Elysia | Aktif | Bun-oriented; compatibility varies |
| 110 | JavaScript / TypeScript Backend | Backend / API | Profesional | JavaScript / TypeScript / Node.js / Bun / Deno | Nitro | Aktif | Server engine used by Nuxt and others |
| 111 | JavaScript / TypeScript Backend | Backend / API | Profesional | JavaScript / TypeScript / Node.js / Bun / Deno | Encore.ts | Aktif; vendor/platform model | Backend framework |
| 112 | JavaScript / TypeScript Backend | Backend / API | Profesional | JavaScript / TypeScript / Node.js / Bun / Deno | Ts.ED | Status perlu diperiksa | TypeScript backend |
| 113 | JavaScript / TypeScript Backend | Backend / API | Menengah–Profesional | JavaScript / TypeScript / Node.js / Bun / Deno | FoalTS | Status perlu diperiksa | TypeScript framework |
| 114 | JavaScript / TypeScript Backend | Backend / API | Menengah–Profesional | JavaScript / TypeScript / Node.js / Bun / Deno | Meteor | Aktif; specialized ecosystem | Full-stack JS |
| 115 | JavaScript / TypeScript Backend | Backend / API | Menengah–Profesional | JavaScript / TypeScript / Node.js / Bun / Deno | Total.js | Status versi perlu diperiksa | Node.js framework |
| 116 | JavaScript / TypeScript Backend | Backend / API | Legacy / niche | JavaScript / TypeScript / Node.js / Bun / Deno | DerbyJS | Status perlu diperiksa | Realtime MVC |
| 117 | JavaScript / TypeScript Backend | Backend / API | Menengah | JavaScript / TypeScript / Node.js / Bun / Deno | Restify | Aktif; API-focused | Node.js API |
| 118 | JavaScript / TypeScript Backend | Backend / API | Dasar–Menengah | JavaScript / TypeScript / Node.js / Bun / Deno | Polka | Aktif/niche | Minimal Node.js |
| 119 | JavaScript / TypeScript Backend | Backend / API | Niche / legacy | JavaScript / TypeScript / Node.js / Bun / Deno | Micro | Status perlu diperiksa | Serverless microframework |
| 120 | Go Backend | Backend | Menengah–Profesional | Go | Gin | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 121 | Go Backend | Backend | Menengah–Profesional | Go | Fiber | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 122 | Go Backend | Backend | Menengah–Profesional | Go | Echo | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 123 | Go Backend | Backend | Menengah–Profesional | Go | Chi | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 124 | Go Backend | Backend | Menengah–Profesional | Go | Beego | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 125 | Go Backend | Backend | Menengah–Profesional | Go | Buffalo | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 126 | Go Backend | Backend | Menengah–Profesional | Go | Revel | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 127 | Go Backend | Backend | Menengah–Profesional | Go | Iris | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 128 | Go Backend | Backend | Menengah | Go | Gorilla Mux | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 129 | Go Backend | Backend | Profesional | Go | Goa | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 130 | Go Backend | Backend | Profesional–Enterprise | Go | Kratos | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 131 | Go Backend | Backend | Profesional | Go | Hertz | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 132 | Rust Backend | Backend | Profesional | Rust | Axum | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 133 | Rust Backend | Backend | Profesional | Rust | Actix Web | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 134 | Rust Backend | Backend | Profesional | Rust | Rocket | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 135 | Rust Backend | Backend | Profesional | Rust | Poem | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 136 | Rust Backend | Backend | Profesional | Rust | Warp | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 137 | Rust Backend | Backend | Profesional | Rust | Salvo | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 138 | Rust Backend | Backend | Niche / status perlu diperiksa | Rust | Tide | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 139 | Java / JVM Backend | Backend | Profesional–Enterprise | Java / JVM | Spring Boot | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 140 | Java / JVM Backend | Backend | Profesional–Enterprise | Java / JVM | Spring MVC | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 141 | Java / JVM Backend | Backend | Enterprise | Java / JVM | Jakarta EE | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 142 | Java / JVM Backend | Backend | Profesional–Enterprise | Java / JVM | Quarkus | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 143 | Java / JVM Backend | Backend | Profesional–Enterprise | Java / JVM | Micronaut | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 144 | Java / JVM Backend | Backend | Profesional–Enterprise | Java / JVM | Helidon | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 145 | Java / JVM Backend | Backend | Profesional–Enterprise | Java / JVM | Vert.x | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 146 | Java / JVM Backend | Backend | Profesional | Java / JVM | Dropwizard | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 147 | Java / JVM Backend | Backend | Menengah–Profesional | Java / JVM | Javalin | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 148 | Java / JVM Backend | Backend | Menengah | Java / JVM | Spark Java | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 149 | Java / JVM Backend | Backend | Profesional | Java / JVM | Play Framework | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 150 | Java / JVM Backend | Backend | Menengah–Profesional | Java / JVM | Ktor | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 151 | Java / JVM Backend | Backend | Profesional–Enterprise | Java / JVM | Vaadin | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 152 | Java / JVM Backend | Backend | Profesional | Java / JVM | Grails | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 153 | Java / JVM Backend | Backend | Menengah–Profesional | Java / JVM | Jooby | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 154 | .NET / C# Backend | Backend | Profesional–Enterprise | C# / .NET | ASP.NET Core MVC | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 155 | .NET / C# Backend | Backend | Profesional–Enterprise | C# / .NET | ASP.NET Core Web API | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 156 | .NET / C# Backend | Backend | Menengah–Enterprise | C# / .NET | Minimal APIs | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 157 | .NET / C# Backend | Backend | Profesional | C# / .NET | Blazor Server | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 158 | .NET / C# Backend | Backend | Profesional | C# / .NET | Blazor WebAssembly | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 159 | .NET / C# Backend | Backend | Profesional | C# / .NET | ServiceStack | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 160 | .NET / C# Backend | Backend | Legacy | C# / .NET | NancyFX | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 161 | .NET / C# Backend | Backend | Legacy | C# / .NET | ASP.NET MVC 5 | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 162 | .NET / C# Backend | Backend | Legacy | C# / .NET | ASP.NET Web Forms | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 163 | Ruby Backend | Backend | Menengah–Enterprise | Ruby | Ruby on Rails | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 164 | Ruby Backend | Backend | Dasar–Menengah | Ruby | Sinatra | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 165 | Ruby Backend | Backend | Menengah–Profesional | Ruby | Hanami | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 166 | Ruby Backend | Backend | Menengah–Profesional | Ruby | Roda | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 167 | Ruby Backend | Backend | API framework | Ruby | Grape | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 168 | Ruby Backend | Backend | Niche / status perlu diperiksa | Ruby | Padrino | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 169 | Elixir Backend | Backend | Profesional–Enterprise | Elixir | Phoenix | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 170 | Elixir Backend | Backend | Menengah–Profesional | Elixir | Plug | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 171 | Elixir Backend | Backend | Profesional | Elixir | Ash Framework | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 172 | Elixir Backend | Backend | Embedded; bukan web umum | Elixir | Nerves | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 173 | Scala Backend | Backend | Profesional | Scala | Play Framework | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 174 | Scala Backend | Backend | Profesional | Scala | http4s | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 175 | Scala Backend | Backend | Profesional; lisensi/status perlu diperiksa | Scala | Akka HTTP | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 176 | Scala Backend | Backend | Profesional | Scala | Pekko HTTP | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 177 | Scala Backend | Backend | Niche | Scala | Lift | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 178 | Scala Backend | Backend | Profesional | Scala | Finatra | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 179 | Clojure Backend | Backend | Menengah–Profesional | Clojure | Ring | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 180 | Clojure Backend | Backend | Menengah–Profesional | Clojure | Luminus | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 181 | Clojure Backend | Backend | Menengah | Clojure | Compojure | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 182 | Clojure Backend | Backend | Profesional | Clojure | Pedestal | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 183 | Clojure Backend | Backend | Routing library | Clojure | Reitit | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 184 | Erlang Backend | Backend | Profesional | Erlang | Cowboy | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 185 | Erlang Backend | Backend | Niche | Erlang | Yaws | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 186 | Erlang Backend | Backend | Legacy / status perlu diperiksa | Erlang | ChicagoBoss | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 187 | Functional / Other Backend | Backend | Spesialis | Beragam | Haskell Yesod | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 188 | Functional / Other Backend | Backend | Spesialis | Beragam | Servant | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 189 | Functional / Other Backend | Backend | Spesialis | Beragam | Scotty | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 190 | Functional / Other Backend | Backend | Spesialis | Beragam | F# Giraffe | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 191 | Functional / Other Backend | Backend | Spesialis | Beragam | F# Saturn | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 192 | Functional / Other Backend | Backend | Spesialis | Beragam | OCaml Dream | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 193 | Functional / Other Backend | Backend | Spesialis | Beragam | Crystal Kemal | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 194 | Functional / Other Backend | Backend | Spesialis | Beragam | Crystal Lucky | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 195 | Functional / Other Backend | Backend | Menengah–Profesional | Beragam | Perl Mojolicious | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 196 | Functional / Other Backend | Backend | Menengah | Beragam | Perl Dancer | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 197 | Functional / Other Backend | Backend | Menengah | Beragam | Perl Catalyst | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 198 | Functional / Other Backend | Backend | Spesialis | Beragam | Raku Cro | Aktif atau status perlu diperiksa | Kategori khusus; periksa rilis, dukungan, dan lisensi |
| 199 | Frontend Component Framework | Frontend | Menengah–Profesional | JavaScript / TypeScript | React | Aktif | UI library |
| 200 | Frontend Component Framework | Frontend | Menengah–Profesional | JavaScript / TypeScript | Vue 3 | Aktif | Progressive framework |
| 201 | Frontend Component Framework | Frontend | Profesional–Enterprise | TypeScript | Angular | Aktif | Full frontend framework |
| 202 | Frontend Component Framework | Frontend | Menengah–Profesional | JavaScript / TypeScript | Svelte | Aktif | Compiler-based UI framework |
| 203 | Frontend Component Framework | Frontend | Menengah | JavaScript | Preact | Aktif | React-like lightweight library |
| 204 | Frontend Component Framework | Frontend | Menengah–Profesional | JavaScript / TypeScript | SolidJS | Aktif | Fine-grained reactive UI |
| 205 | Frontend Component Framework | Frontend | Profesional | TypeScript | Qwik | Aktif | Resumability-focused |
| 206 | Frontend Component Framework | Frontend | Profesional | JavaScript | Marko | Aktif | UI framework |
| 207 | Frontend Component Framework | Frontend | Menengah | JavaScript | Mithril | Aktif | Small SPA framework |
| 208 | Frontend Component Framework | Frontend | Menengah–Profesional | JavaScript / TypeScript | Lit | Aktif | Web Components |
| 209 | Frontend Component Framework | Frontend | Profesional | TypeScript | Stencil | Aktif | Web component compiler |
| 210 | Frontend Component Framework | Frontend | Menengah | JavaScript | Riot.js | Status perlu diperiksa | Small UI library |
| 211 | Frontend Component Framework | Frontend | Menengah | JavaScript | Inferno | Status perlu diperiksa | React-like library |
| 212 | Frontend Component Framework | Frontend | Profesional | JavaScript | Ember.js | Aktif | Convention-based SPA framework |
| 213 | Frontend Component Framework | Frontend | Profesional | JavaScript / TypeScript | Aurelia | Aktif; periksa generasi versi | Frontend framework |
| 214 | Frontend Component Framework | Frontend | Enterprise / legacy | JavaScript | Dojo Toolkit | Status versi perlu diperiksa | Legacy enterprise toolkit |
| 215 | Frontend Component Framework | Frontend | Legacy | JavaScript | AngularJS | EOL; hindari proyek baru | Generasi Angular lama |
| 216 | Frontend Component Framework | Frontend | Legacy / maintenance | JavaScript | Backbone.js | Status perlu diperiksa | Legacy MVC library |
| 217 | Frontend Component Framework | Frontend | Legacy / maintenance | JavaScript | Knockout.js | Status perlu diperiksa | MVVM library |
| 218 | Frontend Component Framework | Frontend | Niche / status perlu diperiksa | JavaScript | Ractive.js | Status perlu diperiksa | UI framework |
| 219 | Frontend Component Framework | Frontend | Niche | JavaScript | Hyperapp | Status perlu diperiksa | Minimal UI framework |
| 220 | Frontend Component Framework | Frontend | Spesialis | Elm | Elm | Aktif/niche | Functional frontend |
| 221 | Frontend Component Framework | Frontend | Spesialis | Gleam | Lustre | Aktif/niche | Frontend framework |
| 222 | Frontend Component Framework | Frontend | Spesialis | Rust / WebAssembly | Leptos | Aktif | Reactive web framework |
| 223 | Frontend Component Framework | Frontend | Spesialis | Rust / WebAssembly | Yew | Aktif | Frontend framework |
| 224 | Frontend Component Framework | Frontend | Spesialis | Rust | Dioxus | Aktif | Cross-platform UI |
| 225 | Frontend Component Framework | Frontend | Spesialis | Rust | Sycamore | Status perlu diperiksa | Reactive UI |
| 226 | Frontend Component Framework | Frontend | Cross-platform | Dart | Flutter Web | Aktif | Web target; tradeoffs SEO/accessibility |
| 227 | Frontend Component Framework | Frontend | Enterprise | C# | Blazor WebAssembly | Aktif | WebAssembly UI |
| 228 | React SSR / Meta-framework | Full-Stack / SSR / Bridge | Profesional–Modern | React / TypeScript | Next.js | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 229 | React SSR / Meta-framework | Full-Stack / SSR / Bridge | Profesional–Modern | React / TypeScript | React Router Framework Mode | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 230 | React SSR / Meta-framework | Full-Stack / SSR / Bridge | Profesional–Modern | React / TypeScript | TanStack Start | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 231 | React SSR / Meta-framework | Full-Stack / SSR / Bridge | Profesional | React / TypeScript | RedwoodJS | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 232 | React SSR / Meta-framework | Full-Stack / SSR / Bridge | Niche | React / TypeScript | Waku | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 233 | React SSR / Meta-framework | Full-Stack / SSR / Bridge | Menengah–Profesional | React / TypeScript | Gatsby | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 234 | React SSR / Meta-framework | Full-Stack / SSR / Bridge | Niche / status perlu diperiksa | React / TypeScript | Razzle | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 235 | Vue SSR / Meta-framework | Full-Stack / SSR / Bridge | Profesional–Modern | Vue / JavaScript | Nuxt | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 236 | Vue SSR / Meta-framework | Full-Stack / SSR / Bridge | Menengah–Profesional | Vue / JavaScript | Quasar | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 237 | Vue SSR / Meta-framework | Full-Stack / SSR / Bridge | Profesional | Vue / JavaScript | Vite SSR | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 238 | Vue SSR / Meta-framework | Full-Stack / SSR / Bridge | Profesional | Vue / JavaScript | Vike | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 239 | Vue SSR / Meta-framework | Full-Stack / SSR / Bridge | Legacy / status perlu diperiksa | Vue / JavaScript | Gridsome | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 240 | Svelte / Other Meta-framework | Full-Stack / SSR / Bridge | Profesional–Modern | JavaScript / TypeScript | SvelteKit | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 241 | Svelte / Other Meta-framework | Full-Stack / SSR / Bridge | Menengah–Profesional | JavaScript / TypeScript | Astro | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 242 | Svelte / Other Meta-framework | Full-Stack / SSR / Bridge | Menengah–Profesional | JavaScript / TypeScript | Fresh | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 243 | Svelte / Other Meta-framework | Full-Stack / SSR / Bridge | Profesional–Modern | JavaScript / TypeScript | RedwoodSDK | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 244 | Svelte / Other Meta-framework | Full-Stack / SSR / Bridge | Profesional | JavaScript / TypeScript | SolidStart | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 245 | Svelte / Other Meta-framework | Full-Stack / SSR / Bridge | Profesional | JavaScript / TypeScript | Analog | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 246 | Svelte / Other Meta-framework | Full-Stack / SSR / Bridge | Profesional | JavaScript / TypeScript | Marko | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 247 | HTML-over-the-Wire / Bridge | Full-Stack / SSR / Bridge | Menengah–Profesional | Beragam | Laravel Livewire | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 248 | HTML-over-the-Wire / Bridge | Full-Stack / SSR / Bridge | Menengah–Profesional | Beragam | Inertia.js | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 249 | HTML-over-the-Wire / Bridge | Full-Stack / SSR / Bridge | Profesional | Beragam | Phoenix LiveView | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 250 | HTML-over-the-Wire / Bridge | Full-Stack / SSR / Bridge | Menengah–Profesional | Beragam | Hotwire | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 251 | HTML-over-the-Wire / Bridge | Full-Stack / SSR / Bridge | Menengah–Profesional | Beragam | Django + HTMX | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 252 | HTML-over-the-Wire / Bridge | Full-Stack / SSR / Bridge | Menengah–Profesional | Beragam | Symfony UX | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 253 | HTML-over-the-Wire / Bridge | Full-Stack / SSR / Bridge | Menengah–Profesional | Beragam | Turbo Rails | Aktif atau status perlu diperiksa | Periksa versi dan strategi rendering |
| 254 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | PHP | WordPress | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 255 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | PHP | Drupal | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 256 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | PHP | Joomla | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 257 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | PHP | TYPO3 | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 258 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | Node.js | Ghost | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 259 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | PHP | Craft CMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 260 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | PHP / Laravel | Statamic | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 261 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | PHP / Laravel | October CMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 262 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | PHP / Laravel | Winter CMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 263 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | PHP | ProcessWire | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 264 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | PHP | Grav | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 265 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | PHP | Concrete CMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 266 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | PHP | Silverstripe CMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 267 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | C# / .NET | Umbraco | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 268 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | C# / .NET | Orchard Core | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 269 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | C# / .NET | DNN Platform | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 270 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | C# / .NET | Kentico Xperience | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 271 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | C# / .NET | Sitecore | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 272 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | PHP | ExpressionEngine | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 273 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | PHP | Kirby CMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 274 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | PHP | Pico CMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 275 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | PHP | Bludit | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 276 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | PHP | WonderCMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 277 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | PHP | Backdrop CMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 278 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | PHP | MODX | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 279 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | PHP | eZ Platform / Ibexa | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 280 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | Python | Plone | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 281 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | Python / Django | Wagtail | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 282 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | Python / Django | django CMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 283 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | Python / Django | Mezzanine | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 284 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | Python | Lektor | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 285 | CMS Monolitik | CMS / Content Platform | Menengah–Enterprise | Desktop static CMS | Publii | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 286 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | Node.js | Strapi | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 287 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | Node.js / TypeScript | Directus | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 288 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | TypeScript | Payload CMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 289 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | Node.js | KeystoneJS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 290 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | Hosted / JavaScript | Sanity | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 291 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | SaaS | Contentful | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 292 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | SaaS | Storyblok | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 293 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | SaaS | Prismic | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 294 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | SaaS | DatoCMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 295 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | SaaS | Hygraph | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 296 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | SaaS | Kontent.ai | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 297 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | SaaS | ButterCMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 298 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | SaaS | Builder.io | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 299 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | SaaS | Agility CMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 300 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | React / Git-based | TinaCMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 301 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | Git-based | Decap CMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 302 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | Git-based / SaaS | CloudCannon | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 303 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | Node.js | ApostropheCMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 304 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | SaaS | Cosmic | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 305 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | PHP | Cockpit CMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 306 | Headless CMS | CMS / Content Platform | Menengah–Enterprise | PHP | Grav with API plugins | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 307 | Enterprise / Java CMS | CMS / Content Platform | Menengah–Enterprise | Java | Liferay DXP | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 308 | Enterprise / Java CMS | CMS / Content Platform | Menengah–Enterprise | Java | Magnolia CMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 309 | Enterprise / Java CMS | CMS / Content Platform | Menengah–Enterprise | Java / SaaS | Bloomreach Experience Manager | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 310 | Enterprise / Java CMS | CMS / Content Platform | Menengah–Enterprise | Java ecosystem | Adobe Experience Manager | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 311 | Enterprise / Java CMS | CMS / Content Platform | Menengah–Enterprise | Java | OpenCms | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 312 | Enterprise / Java CMS | CMS / Content Platform | Menengah–Enterprise | Java | Jahia | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 313 | Enterprise / Java CMS | CMS / Content Platform | Menengah–Enterprise | Java | CrafterCMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 314 | Enterprise / Java CMS | CMS / Content Platform | Menengah–Enterprise | Java | dotCMS | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 315 | Enterprise / Java CMS | CMS / Content Platform | Menengah–Enterprise | Java | CoreMedia | Aktif atau status perlu diperiksa | CMS; bukan framework aplikasi umum |
| 316 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | WordPress / PHP | WooCommerce | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 317 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | PHP | Magento Open Source | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 318 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | PHP | Adobe Commerce | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 319 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | PHP | Shopware | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 320 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | PHP / Symfony | Sylius | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 321 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | PHP | PrestaShop | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 322 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | PHP | OpenCart | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 323 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | PHP / Laravel | Bagisto | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 324 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | PHP | Aimeos | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 325 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | Python / Django | Saleor | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 326 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | Node.js / TypeScript | Medusa.js | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 327 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | Node.js / TypeScript | Vendure | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 328 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | Ruby on Rails | Spree Commerce | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 329 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | Ruby on Rails | Solidus | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 330 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | React / Shopify | Shopify Hydrogen | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 331 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | Liquid | Shopify Liquid themes | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 332 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | React / Next.js | BigCommerce Catalyst | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 333 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | Node.js; status perlu diperiksa | Reaction Commerce | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 334 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | C# / .NET | nopCommerce | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 335 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | C# / .NET | Virto Commerce | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 336 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | SaaS / API | CommerceTools | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 337 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | SaaS / API | Elastic Path | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 338 | E-Commerce | E-Commerce Platform | Menengah–Enterprise | PHP / Symfony | Sylius Plus | Aktif atau status perlu diperiksa | Periksa biaya, lisensi, integrasi pembayaran, dan dukungan |
| 339 | Static Site Generator | Static / Jamstack | Dasar–Profesional | Go | Hugo | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 340 | Static Site Generator | Static / Jamstack | Dasar–Profesional | Ruby | Jekyll | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 341 | Static Site Generator | Static / Jamstack | Dasar–Profesional | JavaScript | Eleventy (11ty) | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 342 | Static Site Generator | Static / Jamstack | Dasar–Profesional | JavaScript / TypeScript | Astro | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 343 | Static Site Generator | Static / Jamstack | Dasar–Profesional | Vue / TypeScript | VitePress | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 344 | Static Site Generator | Static / Jamstack | Dasar–Profesional | Vue / JavaScript | VuePress | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 345 | Static Site Generator | Static / Jamstack | Dasar–Profesional | React / TypeScript | Docusaurus | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 346 | Static Site Generator | Static / Jamstack | Dasar–Profesional | Rust | Zola | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 347 | Static Site Generator | Static / Jamstack | Dasar–Profesional | Node.js | Hexo | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 348 | Static Site Generator | Static / Jamstack | Dasar–Profesional | Python | Pelican | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 349 | Static Site Generator | Static / Jamstack | Dasar–Profesional | Python | MkDocs | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 350 | Static Site Generator | Static / Jamstack | Dasar–Profesional | Python | Material for MkDocs | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 351 | Static Site Generator | Static / Jamstack | Dasar–Profesional | Python | Sphinx | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 352 | Static Site Generator | Static / Jamstack | Dasar–Profesional | Python / web stack | Zensical | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 353 | Static Site Generator | Static / Jamstack | Dasar–Profesional | React | Gatsby | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 354 | Static Site Generator | Static / Jamstack | Dasar–Profesional | Vue | Gridsome | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 355 | Static Site Generator | Static / Jamstack | Dasar–Profesional | Deno | Lume | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 356 | Static Site Generator | Static / Jamstack | Dasar–Profesional | Ruby | Bridgetown | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 357 | Static Site Generator | Static / Jamstack | Dasar–Profesional | Ruby | Middleman | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 358 | Static Site Generator | Static / Jamstack | Dasar–Profesional | Ruby | Nanoc | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 359 | Static Site Generator | Static / Jamstack | Dasar–Profesional | Desktop application | Publii | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 360 | Static Site Generator | Static / Jamstack | Dasar–Profesional | JavaScript / Git CMS | 11ty + Decap CMS | Aktif atau status perlu diperiksa | Untuk situs konten, dokumentasi, landing page |
| 361 | Real-Time / WebSocket | Infrastructure / API / Platform | Menengah–Enterprise | Node.js | Socket.IO | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 362 | Real-Time / WebSocket | Infrastructure / API / Platform | Menengah–Enterprise | Node.js | ws | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 363 | Real-Time / WebSocket | Infrastructure / API / Platform | Menengah–Enterprise | Node.js / C++ | uWebSockets.js | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 364 | Real-Time / WebSocket | Infrastructure / API / Platform | Menengah–Enterprise | C# / .NET | SignalR | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 365 | Real-Time / WebSocket | Infrastructure / API / Platform | Menengah–Enterprise | PHP / Laravel | Laravel Reverb | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 366 | Real-Time / WebSocket | Infrastructure / API / Platform | Menengah–Enterprise | Ruby on Rails | Action Cable | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 367 | Real-Time / WebSocket | Infrastructure / API / Platform | Menengah–Enterprise | Elixir | Phoenix Channels | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 368 | Real-Time / WebSocket | Infrastructure / API / Platform | Menengah–Enterprise | Go | Centrifugo | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 369 | Real-Time / WebSocket | Infrastructure / API / Platform | Menengah–Enterprise | SaaS | Pusher Channels | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 370 | Real-Time / WebSocket | Infrastructure / API / Platform | Menengah–Enterprise | SaaS | Ably | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 371 | Real-Time / WebSocket | Infrastructure / API / Platform | Menengah–Enterprise | SaaS | PubNub | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 372 | RPC / API Protocol | Infrastructure / API / Platform | Menengah–Enterprise | Multi-language | gRPC | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 373 | RPC / API Protocol | Infrastructure / API / Platform | Menengah–Enterprise | Multi-language | Connect RPC | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 374 | RPC / API Protocol | Infrastructure / API / Platform | Menengah–Enterprise | TypeScript | tRPC | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 375 | RPC / API Protocol | Infrastructure / API / Platform | Menengah–Enterprise | Multi-language | Apache Thrift | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 376 | RPC / API Protocol | Infrastructure / API / Platform | Menengah–Enterprise | Query language / ecosystem | GraphQL | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 377 | RPC / API Protocol | Infrastructure / API / Platform | Menengah–Enterprise | Node.js / GraphQL | Apollo Server | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 378 | RPC / API Protocol | Infrastructure / API / Platform | Menengah–Enterprise | Node.js / GraphQL | Yoga GraphQL | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 379 | RPC / API Protocol | Infrastructure / API / Platform | Menengah–Enterprise | GraphQL / platform | Hasura | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 380 | RPC / API Protocol | Infrastructure / API / Platform | Menengah–Enterprise | Node.js / PostgreSQL | PostGraphile | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 381 | RPC / API Protocol | Infrastructure / API / Platform | Menengah–Enterprise | Python | Strawberry GraphQL | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 382 | RPC / API Protocol | Infrastructure / API / Platform | Menengah–Enterprise | Python | Ariadne | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 383 | RPC / API Protocol | Infrastructure / API / Platform | Menengah–Enterprise | C# / .NET | Hot Chocolate | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 384 | RPC / API Protocol | Infrastructure / API / Platform | Menengah–Enterprise | Node.js / Fastify | Mercurius | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 385 | RPC / API Protocol | Infrastructure / API / Platform | Menengah–Enterprise | Frontend GraphQL client | urql | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 386 | API Gateway / Service Mesh | Infrastructure / API / Platform | Menengah–Enterprise | Gateway | Kong Gateway | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 387 | API Gateway / Service Mesh | Infrastructure / API / Platform | Menengah–Enterprise | Gateway | Tyk | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 388 | API Gateway / Service Mesh | Infrastructure / API / Platform | Menengah–Enterprise | Gateway | Apache APISIX | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 389 | API Gateway / Service Mesh | Infrastructure / API / Platform | Menengah–Enterprise | Gateway | Gravitee | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 390 | API Gateway / Service Mesh | Infrastructure / API / Platform | Menengah–Enterprise | Gateway | KrakenD | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 391 | API Gateway / Service Mesh | Infrastructure / API / Platform | Menengah–Enterprise | Proxy / gateway | Traefik | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 392 | API Gateway / Service Mesh | Infrastructure / API / Platform | Menengah–Enterprise | Proxy | Envoy Proxy | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 393 | API Gateway / Service Mesh | Infrastructure / API / Platform | Menengah–Enterprise | Web server / proxy | NGINX | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 394 | API Gateway / Service Mesh | Infrastructure / API / Platform | Menengah–Enterprise | Load balancer | HAProxy | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 395 | API Gateway / Service Mesh | Infrastructure / API / Platform | Menengah–Enterprise | Service mesh | Istio | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 396 | API Gateway / Service Mesh | Infrastructure / API / Platform | Menengah–Enterprise | Service mesh | Linkerd | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 397 | API Gateway / Service Mesh | Infrastructure / API / Platform | Menengah–Enterprise | Distributed app runtime | Dapr | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 398 | Serverless / Edge | Infrastructure / API / Platform | Menengah–Enterprise | JavaScript / TypeScript / WASM | Cloudflare Workers | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 399 | Serverless / Edge | Infrastructure / API / Platform | Menengah–Enterprise | Deno | Deno Deploy | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 400 | Serverless / Edge | Infrastructure / API / Platform | Menengah–Enterprise | Multi-language | AWS Lambda | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 401 | Serverless / Edge | Infrastructure / API / Platform | Menengah–Enterprise | Multi-language | Azure Functions | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 402 | Serverless / Edge | Infrastructure / API / Platform | Menengah–Enterprise | Multi-language | Google Cloud Functions / Cloud Run | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 403 | Serverless / Edge | Infrastructure / API / Platform | Menengah–Enterprise | Node.js / edge | Vercel Functions | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 404 | Serverless / Edge | Infrastructure / API / Platform | Menengah–Enterprise | Multi-language | Netlify Functions | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 405 | Serverless / Edge | Infrastructure / API / Platform | Menengah–Enterprise | WASM / multi-language | Fastly Compute | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 406 | Serverless / Edge | Infrastructure / API / Platform | Menengah–Enterprise | Multi-language | Nitric | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 407 | Serverless / Edge | Infrastructure / API / Platform | Menengah–Enterprise | Multi-language | OpenFaaS | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 408 | Authentication / Identity | Infrastructure / API / Platform | Menengah–Enterprise | Java | Keycloak | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 409 | Authentication / Identity | Infrastructure / API / Platform | Menengah–Enterprise | Python | Authentik | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 410 | Authentication / Identity | Infrastructure / API / Platform | Menengah–Enterprise | Go | Zitadel | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 411 | Authentication / Identity | Infrastructure / API / Platform | Menengah–Enterprise | Go | Ory Kratos / Hydra | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 412 | Authentication / Identity | Infrastructure / API / Platform | Menengah–Enterprise | SaaS | Auth0 | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 413 | Authentication / Identity | Infrastructure / API / Platform | Menengah–Enterprise | SaaS | Okta | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 414 | Authentication / Identity | Infrastructure / API / Platform | Menengah–Enterprise | SaaS | Firebase Authentication | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 415 | Authentication / Identity | Infrastructure / API / Platform | Menengah–Enterprise | SaaS | Amazon Cognito | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 416 | Authentication / Identity | Infrastructure / API / Platform | Menengah–Enterprise | SaaS | Microsoft Entra ID | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 417 | Authentication / Identity | Infrastructure / API / Platform | Menengah–Enterprise | Multi-language | SuperTokens | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 418 | Authentication / Identity | Infrastructure / API / Platform | Menengah–Enterprise | TypeScript | Logto | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 419 | Authentication / Identity | Infrastructure / API / Platform | Menengah–Enterprise | TypeScript; status/version perlu diperiksa | Lucia Auth | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 420 | Authentication / Identity | Infrastructure / API / Platform | Menengah–Enterprise | TypeScript | Better Auth | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 421 | Authentication / Identity | Infrastructure / API / Platform | Menengah–Enterprise | Node.js | Passport.js | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 422 | Authentication / Identity | Infrastructure / API / Platform | Menengah–Enterprise | Ruby on Rails | Devise | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 423 | Authentication / Identity | Infrastructure / API / Platform | Menengah–Enterprise | PHP / Laravel | Laravel Sanctum | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 424 | Authentication / Identity | Infrastructure / API / Platform | Menengah–Enterprise | PHP / Laravel | Laravel Passport | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 425 | Authentication / Identity | Infrastructure / API / Platform | Menengah–Enterprise | PHP / CodeIgniter | CodeIgniter Shield | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 426 | Backend as a Service / Database Platform | Infrastructure / API / Platform | Menengah–Enterprise | PostgreSQL / platform | Supabase | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 427 | Backend as a Service / Database Platform | Infrastructure / API / Platform | Menengah–Enterprise | Google platform | Firebase | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 428 | Backend as a Service / Database Platform | Infrastructure / API / Platform | Menengah–Enterprise | Multi-language / platform | Appwrite | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 429 | Backend as a Service / Database Platform | Infrastructure / API / Platform | Menengah–Enterprise | Go / platform | PocketBase | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 430 | Backend as a Service / Database Platform | Infrastructure / API / Platform | Menengah–Enterprise | PostgreSQL / GraphQL | Nhost | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 431 | Backend as a Service / Database Platform | Infrastructure / API / Platform | Menengah–Enterprise | TypeScript / platform | Convex | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 432 | Backend as a Service / Database Platform | Infrastructure / API / Platform | Menengah–Enterprise | Multi-language | Parse Platform | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 433 | Backend as a Service / Database Platform | Infrastructure / API / Platform | Menengah–Enterprise | GraphQL / PostgreSQL | Hasura | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 434 | Backend as a Service / Database Platform | Infrastructure / API / Platform | Menengah–Enterprise | Node.js / database platform | Directus | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 435 | Backend as a Service / Database Platform | Infrastructure / API / Platform | Menengah–Enterprise | Platform | Backendless | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 436 | Backend as a Service / Database Platform | Infrastructure / API / Platform | Menengah–Enterprise | No-code backend | Xano | Aktif atau status perlu diperiksa | Tidak semuanya framework; sebagian platform atau infrastruktur |
| 437 | AI / Data Application UI | AI / Data / Dashboard | Menengah–Profesional | Python | Gradio | Aktif atau status perlu diperiksa | Untuk prototipe AI, dashboard, dan aplikasi data |
| 438 | AI / Data Application UI | AI / Data / Dashboard | Menengah–Profesional | Python | Streamlit | Aktif atau status perlu diperiksa | Untuk prototipe AI, dashboard, dan aplikasi data |
| 439 | AI / Data Application UI | AI / Data / Dashboard | Menengah–Profesional | Python | Chainlit | Aktif atau status perlu diperiksa | Untuk prototipe AI, dashboard, dan aplikasi data |
| 440 | AI / Data Application UI | AI / Data / Dashboard | Menengah–Profesional | Python | NiceGUI | Aktif atau status perlu diperiksa | Untuk prototipe AI, dashboard, dan aplikasi data |
| 441 | AI / Data Application UI | AI / Data / Dashboard | Menengah–Profesional | Python | Dash | Aktif atau status perlu diperiksa | Untuk prototipe AI, dashboard, dan aplikasi data |
| 442 | AI / Data Application UI | AI / Data / Dashboard | Menengah–Profesional | Python | Panel | Aktif atau status perlu diperiksa | Untuk prototipe AI, dashboard, dan aplikasi data |
| 443 | AI / Data Application UI | AI / Data / Dashboard | Menengah–Profesional | R / Python | Shiny | Aktif atau status perlu diperiksa | Untuk prototipe AI, dashboard, dan aplikasi data |
| 444 | AI / Data Application UI | AI / Data / Dashboard | Menengah–Profesional | Python | Reflex | Aktif atau status perlu diperiksa | Untuk prototipe AI, dashboard, dan aplikasi data |
| 445 | AI / Data Application UI | AI / Data / Dashboard | Menengah–Profesional | Python | Mesop | Aktif atau status perlu diperiksa | Untuk prototipe AI, dashboard, dan aplikasi data |
| 446 | AI / Data Application UI | AI / Data / Dashboard | Menengah–Profesional | Python | Taipy | Aktif atau status perlu diperiksa | Untuk prototipe AI, dashboard, dan aplikasi data |
| 447 | AI / Data Application UI | AI / Data / Dashboard | Menengah–Profesional | Python | Voilà | Aktif atau status perlu diperiksa | Untuk prototipe AI, dashboard, dan aplikasi data |
| 448 | AI / Data Application UI | AI / Data / Dashboard | Menengah–Profesional | Python | Bokeh Server | Aktif atau status perlu diperiksa | Untuk prototipe AI, dashboard, dan aplikasi data |
| 449 | AI / Data Application UI | AI / Data / Dashboard | Menengah–Profesional | Python | Solara | Aktif atau status perlu diperiksa | Untuk prototipe AI, dashboard, dan aplikasi data |
| 450 | AI / Data Application UI | AI / Data / Dashboard | Menengah–Profesional | Python | FastHTML | Aktif atau status perlu diperiksa | Untuk prototipe AI, dashboard, dan aplikasi data |
| 451 | AI / Data Application UI | AI / Data / Dashboard | Menengah–Profesional | Python | Marimo | Aktif atau status perlu diperiksa | Untuk prototipe AI, dashboard, dan aplikasi data |
| 452 | AI / Data Application UI | AI / Data / Dashboard | Menengah–Profesional | Python | Shiny for Python | Aktif atau status perlu diperiksa | Untuk prototipe AI, dashboard, dan aplikasi data |
| 453 | AI / Data Application UI | AI / Data / Dashboard | Menengah–Profesional | Python | Gradio Blocks | Aktif atau status perlu diperiksa | Untuk prototipe AI, dashboard, dan aplikasi data |
| 454 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | PHP | PHPUnit | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 455 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | PHP | Pest | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 456 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | PHP | Codeception | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 457 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | PHP | Behat | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 458 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | Python | Pytest | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 459 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | Python | unittest | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 460 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | JavaScript | Jest | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 461 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | JavaScript / TypeScript | Vitest | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 462 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | JavaScript | Mocha | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 463 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | JavaScript | Jasmine | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 464 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | Multi-browser | Playwright | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 465 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | JavaScript | Cypress | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 466 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | Multi-language | Selenium | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 467 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | JavaScript | WebdriverIO | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 468 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | JavaScript | Puppeteer | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 469 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | Frontend | Testing Library | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 470 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | UI development | Storybook | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 471 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | Visual testing SaaS | Chromatic | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 472 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | Load testing | k6 | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 473 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | Python load testing | Locust | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 474 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | Java load testing | JMeter | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 475 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | Scala load testing | Gatling | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 476 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | Security testing | OWASP ZAP | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 477 | Testing / QA | Tool / Library / Platform | Dasar–Enterprise | Security testing | Burp Suite | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 478 | Documentation / API Tools | Tool / Library / Platform | Dasar–Enterprise | API specification | OpenAPI | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 479 | Documentation / API Tools | Tool / Library / Platform | Dasar–Enterprise | API docs | Swagger UI | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 480 | Documentation / API Tools | Tool / Library / Platform | Dasar–Enterprise | API docs | Scalar | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 481 | Documentation / API Tools | Tool / Library / Platform | Dasar–Enterprise | API docs | Redoc | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 482 | Documentation / API Tools | Tool / Library / Platform | Dasar–Enterprise | API design platform | Stoplight | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 483 | Documentation / API Tools | Tool / Library / Platform | Dasar–Enterprise | React | Docusaurus | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 484 | Documentation / API Tools | Tool / Library / Platform | Dasar–Enterprise | Vue | VitePress | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 485 | Documentation / API Tools | Tool / Library / Platform | Dasar–Enterprise | Python | MkDocs | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 486 | Documentation / API Tools | Tool / Library / Platform | Dasar–Enterprise | Python | Sphinx | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 487 | Documentation / API Tools | Tool / Library / Platform | Dasar–Enterprise | SaaS | GitBook | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 488 | Documentation / API Tools | Tool / Library / Platform | Dasar–Enterprise | SaaS | Mintlify | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 489 | Documentation / API Tools | Tool / Library / Platform | Dasar–Enterprise | API documentation | Fern | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 490 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Build tool | Vite | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 491 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Bundler | Webpack | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 492 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Bundler | Rollup | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 493 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Bundler | esbuild | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 494 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Bundler | Rspack | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 495 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Bundler | Parcel | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 496 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Bundler | Turbopack | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 497 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Compiler | Babel | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 498 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Compiler | SWC | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 499 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Compiler | TypeScript compiler | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 500 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Package manager | npm | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 501 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Package manager | pnpm | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 502 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Package manager | Yarn | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 503 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Runtime / package manager | Bun | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 504 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Runtime / package manager | Deno | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 505 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | PHP package manager | Composer | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 506 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Python package manager | pip | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 507 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Python package manager | uv | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 508 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Python dependency manager | Poetry | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 509 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Rust package manager | Cargo | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 510 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Java build tool | Maven | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 511 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | Java build tool | Gradle | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 512 | Build / Package / Tooling | Tool / Library / Platform | Dasar–Enterprise | C# package manager | NuGet | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 513 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | Container platform | Docker | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 514 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | Container platform | Podman | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 515 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | Container orchestration | Docker Compose | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 516 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | Orchestration | Kubernetes | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 517 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | Kubernetes package manager | Helm | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 518 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | Infrastructure as code | Terraform | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 519 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | Infrastructure as code | OpenTofu | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 520 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | Configuration management | Ansible | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 521 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | Infrastructure as code | Pulumi | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 522 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | CI/CD | GitHub Actions | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 523 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | CI/CD | GitLab CI/CD | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 524 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | CI/CD | Jenkins | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 525 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | GitOps | Argo CD | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 526 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | GitOps | Flux CD | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 527 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | Monitoring | Prometheus | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 528 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | Observability | Grafana | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 529 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | Telemetry | OpenTelemetry | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 530 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | Error monitoring | Sentry | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 531 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | Uptime monitoring | Uptime Kuma | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 532 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | Log aggregation | Loki | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 533 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | Log/search platform | ELK / Elastic Stack | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 534 | DevOps / Deployment | Tool / Library / Platform | Dasar–Enterprise | Search/observability | OpenSearch | Aktif atau status perlu diperiksa | Bukan semuanya framework aplikasi |
| 535 | Cross-Platform / Hybrid | Cross-Platform | Menengah–Profesional | TypeScript / Web | Ionic | Aktif atau status perlu diperiksa | Tidak semua ditujukan untuk website publik |
| 536 | Cross-Platform / Hybrid | Cross-Platform | Menengah–Profesional | Web / native bridge | Capacitor | Aktif atau status perlu diperiksa | Tidak semua ditujukan untuk website publik |
| 537 | Cross-Platform / Hybrid | Cross-Platform | Menengah–Profesional | JavaScript | Framework7 | Aktif atau status perlu diperiksa | Tidak semua ditujukan untuk website publik |
| 538 | Cross-Platform / Hybrid | Cross-Platform | Menengah–Profesional | JavaScript / TypeScript | NativeScript | Aktif atau status perlu diperiksa | Tidak semua ditujukan untuk website publik |
| 539 | Cross-Platform / Hybrid | Cross-Platform | Menengah–Profesional | JavaScript | Onsen UI | Aktif atau status perlu diperiksa | Tidak semua ditujukan untuk website publik |
| 540 | Cross-Platform / Hybrid | Cross-Platform | Menengah–Profesional | Vue | Quasar | Aktif atau status perlu diperiksa | Tidak semua ditujukan untuk website publik |
| 541 | Cross-Platform / Hybrid | Cross-Platform | Menengah–Profesional | Dart | Flutter | Aktif atau status perlu diperiksa | Tidak semua ditujukan untuk website publik |
| 542 | Cross-Platform / Hybrid | Cross-Platform | Menengah–Profesional | JavaScript / TypeScript | React Native | Aktif atau status perlu diperiksa | Tidak semua ditujukan untuk website publik |
| 543 | Cross-Platform / Hybrid | Cross-Platform | Menengah–Profesional | React Native platform | Expo | Aktif atau status perlu diperiksa | Tidak semua ditujukan untuk website publik |
| 544 | Cross-Platform / Hybrid | Cross-Platform | Menengah–Profesional | Rust + web frontend | Tauri | Aktif atau status perlu diperiksa | Tidak semua ditujukan untuk website publik |
| 545 | Cross-Platform / Hybrid | Cross-Platform | Menengah–Profesional | Node.js + web frontend | Electron | Aktif atau status perlu diperiksa | Tidak semua ditujukan untuk website publik |
