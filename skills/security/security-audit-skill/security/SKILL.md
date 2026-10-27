---
name: security
description: 🛡️ [Security Master Suite] Audit keamanan kode menyeluruh berbasis OWASP Top 10:2025, ASVS 5.0, celah PHP/API, CWE Top 25, pencegahan injection, IDOR, dan kalkulasi risiko CVSS.
---

# 🛡️ Security Master Suite (`/security`)

Gunakan perintah `/security` untuk memicu audit kelayakan keamanan aplikasi secara komprehensif, baik pada kode backend (PHP/CodeIgniter/Node), API endpoints, maupun frontend.

---

## ⚡ Kemampuan Utama

1. **Audit OWASP Top 10:2025 & ASVS 5.0 (`owasp-security`)**:
   - *Broken Access Control* (IDOR, role bypass, rute tanpa filter autentikasi).
   - *Cryptographic Failures* (API key/JWT secrets bocor di kode, hashing lemah).
   - *Injection Vulnerabilities* (SQLi, Command Injection, SSRF).
   - *XSS & CSRF* (Input tanpa sanitasi, output tanpa escaping).

2. **Audit Mendalam Arsitektur & PHP (`security-audit`)**:
   - 80+ PHP security checkpoints.
   - Klasifikasi celah dengan **CWE Top 25** dan kalkulasi skor risiko **CVSS v3.1 / v4.0**.
   - Menghasilkan rekomendasi kode remediasi (*drop-in fix*) siap pasang.

---

## 🚀 Cara Memanggil di Chat

Ketik `/security` diikuti target atau instruksi spesifik:
- `/security` ➔ Audit seluruh repository saat ini.
- `/security controllers/` ➔ Audit keamanan rute dan controller.
- `/security api` ➔ Audit autentikasi token, CORS, dan envelope API.

---

## 🤝 Kolaborasi dengan Skill Lain

- **`/security` + `/ci4`**: Audit khusus sistem autentikasi CodeIgniter Shield, proteksi query builder terhadap SQL injection, dan CSRF filter.
- **`/security` + `/vue`**: Memeriksa kebocoran environment variable (`VITE_*`) di frontend bundle dan sanitasi `v-html` terhadap serangan XSS.
