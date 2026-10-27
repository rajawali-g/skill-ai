# 🧩 WebBuilder: Component Snippets Library

Pustaka snippet komponen antarmuka siap pakai (*Zero-Slop Production Snippets*) untuk WebBuilder Suite. Seluruh snippet dirancang menggunakan **CSS Design Tokens**, semantik HTML5, aksesibel (WCAG AA), dan tanpa ketergantungan library luar yang berlebihan (*dependency-free* atau minimal).

---

## 📑 Daftar Snippet

1. [Accordion FAQ Interaktif](#1-accordion-faq-interaktif)
2. [Peta Lokasi Interaktif Leaflet.js](#2-peta-lokasi-interaktif-leafletjs)
3. [Card Visualisasi Data Chart.js](#3-card-visualisasi-data-chartjs)
4. [Modal Dialog / Lightbox Gambar](#4-modal-dialog--lightbox-gambar)
5. [Formulir Kontak Anti-Spam (Honeypot Protected)](#5-formulir-kontak-anti-spam-honeypot-protected)
6. [Timeline / Jejak Sejarah Vertikal](#6-timeline--jejak-sejarah-vertikal)
7. [Banner Slider / Carousel Ringan](#7-banner-slider--carousel-ringan)
8. [Statistik Angka Berjalan (Counter Stats)](#8-statistik-angka-berjalan-counter-stats)

---

## 1. Accordion FAQ Interaktif

Komponen FAQ yang mulus dengan tag HTML semantik `<details>` dan `<summary>` atau tombol ramah keyboard ARIA.

### HTML Markup:
```html
<section class="faq-section" id="faq">
  <div class="container">
    <div class="section-title-wrap">
      <h2>Pertanyaan yang Sering Diajukan</h2>
      <p>Jawaban cepat untuk pertanyaan umum pengunjung website kami.</p>
    </div>

    <div class="accordion-group">
      <details class="accordion-item" open>
        <summary class="accordion-header">
          <span>Bagaimana cara menghubungi tim pengelola?</span>
          <span class="accordion-icon" aria-hidden="true">+</span>
        </summary>
        <div class="accordion-content">
          <p>Anda dapat menghubungi kami melalui widget WhatsApp di pojok kanan bawah, formulir kontak, atau email resmi yang tertera di bagian footer.</p>
        </div>
      </details>

      <details class="accordion-item">
        <summary class="accordion-header">
          <span>Apakah website ini mendukung akses ramah disabilitas?</span>
          <span class="accordion-icon" aria-hidden="true">+</span>
        </summary>
        <div class="accordion-content">
          <p>Ya, website ini dibangun mematuhi standar aksesibilitas WCAG AA dengan navigasi keyboard penuh, rasio kontras tinggi, dan struktur semantik yang ramah screen reader.</p>
        </div>
      </details>

      <details class="accordion-item">
        <summary class="accordion-header">
          <span>Bagaimana keamanan data yang saya masukkan?</span>
          <span class="accordion-icon" aria-hidden="true">+</span>
        </summary>
        <div class="accordion-content">
          <p>Seluruh transmisi data dienkripsi dengan HTTPS TLS modern, dilindungi token anti-CSRF, dan diaudit secara berkala dari celah keamanan OWASP.</p>
        </div>
      </details>
    </div>
  </div>
</section>
```

### CSS Styling:
```css
.accordion-group {
  max-width: 800px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: var(--space-sm);
}

.accordion-item {
  background-color: var(--color-surface-card);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  overflow: hidden;
  transition: border-color var(--transition-fast);
}

.accordion-item[open] {
  border-color: var(--color-primary);
}

.accordion-header {
  list-style: none;
  cursor: pointer;
  padding: var(--space-md) var(--space-lg);
  font-family: var(--font-heading);
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: space-between;
  user-select: none;
}

.accordion-header::-webkit-details-marker {
  display: none;
}

.accordion-icon {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--color-primary);
  transition: transform var(--transition-fast);
}

.accordion-item[open] .accordion-icon {
  transform: rotate(45deg);
}

.accordion-content {
  padding: 0 var(--space-lg) var(--space-md);
  color: var(--color-text-muted);
  font-size: var(--text-sm);
  line-height: 1.6;
}
```

---

## 2. Peta Lokasi Interaktif Leaflet.js

Wadah peta ringan (Leaflet.js) tanpa API key berbayar dengan dark-mode tile layer yang elegan.

### HTML Markup:
```html
<!-- Load Leaflet in <head> -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<section class="map-section" id="location">
  <div class="container">
    <div class="section-title-wrap">
      <h2>Lokasi & Destinasi</h2>
      <p>Jelajahi titik lokasi langsung pada peta interaktif berikut.</p>
    </div>
    <div id="interactiveMap" class="map-container" role="region" aria-label="Peta Interaktif"></div>
  </div>
</section>
```

### CSS Styling:
```css
.map-container {
  width: 100%;
  height: 480px;
  border-radius: var(--radius-lg);
  border: 1px solid var(--color-border);
  box-shadow: var(--shadow-card);
  overflow: hidden;
}
```

### JavaScript Initialization:
```javascript
function initInteractiveMap(lat = 1.2185, lng = 124.7836, zoom = 11, label = "Minahasa Selatan") {
  const mapEl = document.getElementById('interactiveMap');
  if (!mapEl || typeof L === 'undefined') return;

  const map = L.map('interactiveMap').setView([lat, lng], zoom);

  // CartoDB Dark Matter / Positron tiles for high-end look
  const isDark = document.documentElement.getAttribute('data-theme') !== 'light';
  const tileLayerUrl = isDark
    ? 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png'
    : 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png';

  L.tileLayer(tileLayerUrl, {
    attribution: '&copy; <a href="https://carto.com/">CARTO</a>',
    maxZoom: 19
  }).addTo(map);

  const marker = L.marker([lat, lng]).addTo(map);
  marker.bindPopup(`<b>${label}</b><br>Pusat Destinasi`).openPopup();
}
```

---

## 3. Card Visualisasi Data Chart.js

### HTML Markup:
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<div class="bento-card card-span-8">
  <div class="card-header">
    <h3>Statistik Tren Pengunjung</h3>
    <span class="badge">Live 2026</span>
  </div>
  <div class="chart-wrapper">
    <canvas id="trafficChart"></canvas>
  </div>
</div>
```

### CSS Styling:
```css
.chart-wrapper {
  position: relative;
  width: 100%;
  height: 300px;
  margin-top: var(--space-md);
}
```

### JavaScript:
```javascript
function initTrafficChart() {
  const ctx = document.getElementById('trafficChart');
  if (!ctx || typeof Chart === 'undefined') return;

  new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul'],
      datasets: [{
        label: 'Kunjungan (Ribu)',
        data: [12, 19, 15, 27, 34, 42, 58],
        borderColor: '#38bdf8',
        backgroundColor: 'rgba(56, 189, 248, 0.15)',
        tension: 0.4,
        fill: true
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { labels: { color: '#94a3b8' } }
      },
      scales: {
        x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#94a3b8' } },
        y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#94a3b8' } }
      }
    }
  });
}
```

---

## 4. Modal Dialog / Lightbox Gambar

### HTML Markup:
```html
<div id="siteModal" class="modal-backdrop" aria-hidden="true" role="dialog" aria-modal="true">
  <div class="modal-card">
    <div class="modal-header">
      <h3 id="modalTitle">Detail Informasi</h3>
      <button class="modal-close-btn" id="modalCloseBtn" aria-label="Tutup Dialog">&times;</button>
    </div>
    <div class="modal-body" id="modalBody">
      <p>Konten detail modal akan dimuat di sini secara dinamis.</p>
    </div>
  </div>
</div>
```

### CSS Styling:
```css
.modal-backdrop {
  position: fixed;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(8px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-md);
  opacity: 0;
  pointer-events: none;
  transition: opacity var(--transition-fast);
}

.modal-backdrop.active {
  opacity: 1;
  pointer-events: auto;
}

.modal-card {
  background-color: var(--color-surface-card);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  max-width: 560px;
  width: 100%;
  box-shadow: var(--shadow-card);
  overflow: hidden;
  transform: scale(0.95);
  transition: transform var(--transition-fast);
}

.modal-backdrop.active .modal-card {
  transform: scale(1);
}

.modal-header {
  padding: var(--space-md) var(--space-lg);
  border-bottom: 1px solid var(--color-border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.modal-close-btn {
  background: transparent;
  border: none;
  font-size: 1.5rem;
  color: var(--color-text-muted);
  cursor: pointer;
}

.modal-body {
  padding: var(--space-lg);
}
```

### JavaScript:
```javascript
function openModal(title, content) {
  const modal = document.getElementById('siteModal');
  if (!modal) return;
  document.getElementById('modalTitle').textContent = title;
  document.getElementById('modalBody').innerHTML = content;
  modal.classList.add('active');
  modal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  const modal = document.getElementById('siteModal');
  if (!modal) return;
  modal.classList.remove('active');
  modal.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
}

// Close on ESC and backdrop click
document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeModal(); });
document.getElementById('siteModal')?.addEventListener('click', (e) => {
  if (e.target.id === 'siteModal') closeModal();
});
document.getElementById('modalCloseBtn')?.addEventListener('click', closeModal);
```

---

## 5. Formulir Kontak Anti-Spam (Honeypot Protected)

Formulir dengan kolom jebakan bot tersembunyi (*honeypot*) dan validasi interaktif.

### HTML Markup:
```html
<form class="contact-form" id="contactForm" novalidate>
  <!-- Honeypot Field (Bot trap) -->
  <div style="display: none !important; opacity: 0; position: absolute;" aria-hidden="true">
    <label for="website_url">Jangan diisi:</label>
    <input type="text" id="website_url" name="website_url" tabindex="-1" autocomplete="off" />
  </div>

  <div class="form-group">
    <label for="senderName" class="form-label">Nama Lengkap *</label>
    <input type="text" id="senderName" class="form-control" placeholder="Nama Anda" required />
  </div>

  <div class="form-group">
    <label for="senderEmail" class="form-label">Alamat Email *</label>
    <input type="email" id="senderEmail" class="form-control" placeholder="nama@domain.com" required />
  </div>

  <div class="form-group">
    <label for="senderMessage" class="form-label">Pesan / Keterangan *</label>
    <textarea id="senderMessage" class="form-control" rows="4" placeholder="Tuliskan pesan Anda..." required></textarea>
  </div>

  <button type="submit" class="btn btn-primary" style="width: 100%;">
    <span>Kirim Pesan Sekarang</span>
  </button>
</form>
```

### CSS Styling:
```css
.contact-form {
  background-color: var(--color-surface-card);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-xl);
  max-width: 600px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: var(--space-md);
  text-align: left;
}

.form-label {
  display: block;
  font-size: var(--text-xs);
  font-weight: 600;
  margin-bottom: var(--space-2xs);
  color: var(--color-text);
}

.form-control {
  width: 100%;
  padding: 0.75rem 1rem;
  background-color: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  color: var(--color-text);
  font-family: inherit;
  font-size: var(--text-sm);
  transition: border-color var(--transition-fast), box-shadow var(--transition-fast);
}

.form-control:focus {
  outline: none;
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px var(--color-primary-glow);
}
```

### JavaScript:
```javascript
document.getElementById('contactForm')?.addEventListener('submit', function(e) {
  e.preventDefault();

  // Honeypot check: If bot filled the hidden field, silently reject
  const honeypot = document.getElementById('website_url')?.value;
  if (honeypot) {
    console.warn('Bot submission blocked.');
    return;
  }

  const name = document.getElementById('senderName').value.trim();
  const email = document.getElementById('senderEmail').value.trim();
  const msg = document.getElementById('senderMessage').value.trim();

  if (!name || !email || !msg) {
    showToast('Mohon lengkapi seluruh kolom formulir!', 'error');
    return;
  }

  showToast('Terima kasih! Pesan Anda telah terkirim.', 'success');
  this.reset();
});
```

---

## 6. Timeline / Jejak Sejarah Vertikal

### HTML Markup:
```html
<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-dot"></div>
    <div class="timeline-content">
      <span class="timeline-date">Tahun 1820</span>
      <h4>Awal Mula Warisan Budaya</h4>
      <p>Pencatatan pertama peninggalan situs megalitikum dan tradisi lokal.</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-dot"></div>
    <div class="timeline-content">
      <span class="timeline-date">Tahun 2003</span>
      <h4>Pemekaran Wilayah</h4>
      <p>Pembentukan resmi kabupaten otonom yang mandiri dan berdaya saing.</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-dot"></div>
    <div class="timeline-content">
      <span class="timeline-date">Tahun 2026</span>
      <h4>Transformasi Digital Hijau</h4>
      <p>Peluncuran portal terpadu dan pariwisata berkelanjutan kelas dunia.</p>
    </div>
  </div>
</div>
```

### CSS Styling:
```css
.timeline {
  position: relative;
  max-width: 680px;
  margin: var(--space-2xl) auto;
  padding-left: var(--space-xl);
  border-left: 2px solid var(--color-border);
}

.timeline-item {
  position: relative;
  margin-bottom: var(--space-xl);
}

.timeline-dot {
  position: absolute;
  left: calc(-1 * var(--space-xl) - 6px);
  top: 4px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background-color: var(--color-primary);
  box-shadow: 0 0 10px var(--color-primary);
}

.timeline-date {
  font-size: var(--text-xs);
  font-weight: 700;
  color: var(--color-primary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.timeline-content h4 {
  margin: var(--space-2xs) 0;
}
```

---

## 7. Banner Slider / Carousel Ringan

### HTML Markup:
```html
<div class="slider-container" role="region" aria-label="Banner Promo">
  <div class="slider-track" id="sliderTrack">
    <div class="slide">
      <div class="slide-content">
        <h3>Eksplorasi Keajaiban Alam</h3>
        <p>Panorama danau vulkanik dan perbukitan hijau mempesona.</p>
      </div>
    </div>
    <div class="slide">
      <div class="slide-content">
        <h3>Warisan Leluhur Malesung</h3>
        <p>Mengenal situs cagar budaya Waruga yang bersejarah.</p>
      </div>
    </div>
  </div>
  <div class="slider-controls">
    <button id="slidePrev" aria-label="Slide Sebelumnya">&larr;</button>
    <button id="slideNext" aria-label="Slide Berikutnya">&rarr;</button>
  </div>
</div>
```

### CSS Styling:
```css
.slider-container {
  position: relative;
  overflow: hidden;
  border-radius: var(--radius-lg);
  border: 1px solid var(--color-border);
  background-color: var(--color-surface-card);
}

.slider-track {
  display: flex;
  transition: transform var(--transition-smooth);
}

.slide {
  min-width: 100%;
  padding: var(--space-3xl) var(--space-xl);
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.slider-controls {
  position: absolute;
  bottom: var(--space-md);
  right: var(--space-md);
  display: flex;
  gap: var(--space-xs);
}

.slider-controls button {
  width: 36px;
  height: 36px;
  border-radius: var(--radius-pill);
  border: 1px solid var(--color-border);
  background: var(--color-surface);
  color: var(--color-text);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}
```

---

## 8. Statistik Angka Berjalan (Counter Stats)

### HTML Markup:
```html
<div class="bento-grid">
  <div class="bento-card card-span-4" style="text-align: center;">
    <div class="stat-number" data-target="150">0</div>
    <div class="stat-label">Destinasi Terverifikasi</div>
  </div>
  <div class="bento-card card-span-4" style="text-align: center;">
    <div class="stat-number" data-target="48">0</div>
    <div class="stat-label">Desa Wisata Aktif</div>
  </div>
  <div class="bento-card card-span-4" style="text-align: center;">
    <div class="stat-number" data-target="98">0</div>
    <div class="stat-label">% Kepuasan Pengunjung</div>
  </div>
</div>
```

### JavaScript:
```javascript
function initCounterStats() {
  const counters = document.querySelectorAll('.stat-number');
  counters.forEach(counter => {
    const target = +counter.getAttribute('data-target');
    let count = 0;
    const increment = target / 60;

    const updateCount = () => {
      count += increment;
      if (count < target) {
        counter.textContent = Math.ceil(count);
        requestAnimationFrame(updateCount);
      } else {
        counter.textContent = target + (counter.getAttribute('data-target') === '98' ? '%' : '+');
      }
    };
    updateCount();
  });
}
```
