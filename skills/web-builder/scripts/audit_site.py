#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WebBuilder Heuristic Site Checker
Audits generated web projects for:
- Zero-Slop CSS Design Tokens compliance
- HTML5 Semantics & Structure
- Accessibility (WCAG 2.1 AA) landmarks, img alt, aria labels
- Mobile Viewport & SEO OpenGraph tags
- Favicon & Vector SVG Logo assets
"""

import os
import sys
import re
import argparse

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

class SiteAuditor:
    def __init__(self, target_dir):
        self.target_dir = os.path.abspath(target_dir)
        self.passed = []
        self.warnings = []
        self.failures = []
        self.score = 100

    def run(self):
        print("\n" + "=" * 55)
        print(f" 🌐 WebBuilder Heuristic Site Checks")
        print(f" Target: {self.target_dir}")
        print("=" * 55)

        self.audit_files()
        self.audit_html()
        self.audit_css()
        self.print_report()
        return 0 if self.score >= 80 else 1

    def audit_files(self):
        # 1. Essential files
        for fname in ["index.html", "style.css", "main.js"]:
            fpath = os.path.join(self.target_dir, fname)
            if os.path.exists(fpath):
                self.passed.append(f"Berkas inti '{fname}' ditemukan.")
            else:
                self.failures.append(f"Berkas inti '{fname}' TIDAK ditemukan.")
                self.score -= 20

        # 2. Asset files
        logo_path = os.path.join(self.target_dir, "assets", "icons", "logo.svg")
        fav_path = os.path.join(self.target_dir, "assets", "icons", "favicon.svg")
        
        if os.path.exists(logo_path):
            self.passed.append("Aset logo vector 'assets/icons/logo.svg' tersedia.")
        else:
            self.warnings.append("Aset logo 'logo.svg' tidak ditemukan di assets/icons/.")
            self.score -= 5

        if os.path.exists(fav_path):
            self.passed.append("Aset favicon 'assets/icons/favicon.svg' tersedia.")
        else:
            self.warnings.append("Aset favicon 'favicon.svg' tidak ditemukan di assets/icons/.")
            self.score -= 5

    def audit_html(self):
        html_path = os.path.join(self.target_dir, "index.html")
        if not os.path.exists(html_path):
            return

        with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # Viewport
        if '<meta name="viewport"' in content:
            self.passed.append("Meta viewport responsif terpasang.")
        else:
            self.failures.append("Meta viewport responsif TIDAK terpasang!")
            self.score -= 10

        # Title & Meta Description
        if "<title>" in content and "</title>" in content:
            self.passed.append("Tag <title> halaman terpasang.")
        else:
            self.failures.append("Tag <title> tidak ditemukan!")
            self.score -= 10

        if '<meta name="description"' in content:
            self.passed.append("Meta deskripsi SEO terpasang.")
        else:
            self.warnings.append("Meta deskripsi SEO tidak ditemukan.")
            self.score -= 5

        # OpenGraph
        if 'property="og:title"' in content and 'property="og:description"' in content:
            self.passed.append("Tag OpenGraph media sosial lengkap.")
        else:
            self.warnings.append("Tag OpenGraph (og:title/og:description) belum lengkap.")
            self.score -= 5

        # Semantics Landmarks
        landmarks = ["<header", "<nav", "<main", "<footer"]
        found_landmarks = [lm for lm in landmarks if lm in content]
        if len(found_landmarks) == len(landmarks):
            self.passed.append("Landmark semantik HTML5 lengkap (<header>, <nav>, <main>, <footer>).")
        else:
            self.warnings.append(f"Sebagian landmark semantik tidak ditemukan ({len(found_landmarks)}/{len(landmarks)}).")
            self.score -= 5

        # H1 Check
        h1_matches = re.findall(r"<h1[^>]*>(.*?)<\/h1>", content, re.IGNORECASE | re.DOTALL)
        if len(h1_matches) == 1:
            self.passed.append("Struktur heading memiliki tepat 1 <h1> utama.")
        elif len(h1_matches) > 1:
            self.warnings.append(f"Ditemukan {len(h1_matches)} tag <h1> (Direkomendasikan hanya 1 per halaman).")
            self.score -= 3
        else:
            self.failures.append("Tidak ditemukan tag <h1> utama pada halaman!")
            self.score -= 10

        # Images without alt
        img_tags = re.findall(r"<img\s+([^>]*?)/?>", content, re.IGNORECASE)
        missing_alt = 0
        for tag in img_tags:
            if 'alt="' not in tag and "alt='" not in tag:
                missing_alt += 1

        if img_tags and missing_alt == 0:
            self.passed.append(f"Seluruh gambar ({len(img_tags)}) memiliki atribut 'alt' aksesibel.")
        elif missing_alt > 0:
            self.failures.append(f"Terdapat {missing_alt} gambar tanpa atribut 'alt' (perlu tinjauan aksesibilitas).")
            self.score -= (missing_alt * 5)

        # Placeholder detection
        if "placeholder.com" in content or "via.placeholder" in content:
            self.failures.append("Terdeteksi link placeholder kasar (placeholder.com). Hapus slop!")
            self.score -= 15

    def audit_css(self):
        css_path = os.path.join(self.target_dir, "style.css")
        if not os.path.exists(css_path):
            return

        with open(css_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # Design Tokens check
        if ":root" in content and "--color-" in content:
            self.passed.append("CSS Design Tokens (:root CSS Variables) terdefinisi.")
        else:
            self.failures.append("Design Tokens tidak ditemukan! Dilarang menggunakan styling ad-hoc.")
            self.score -= 20

        # Theme toggle support
        if '[data-theme="light"]' in content or '[data-theme="dark"]' in content:
            self.passed.append("Dukungan tema Dark / Light Mode terpasang.")
        else:
            self.warnings.append("Dukungan variabel Dark/Light mode tidak ditemukan.")
            self.score -= 5

        # Responsive media queries
        if "@media" in content and "max-width" in content:
            self.passed.append("Media query responsif ditemukan di stylesheet.")
        else:
            self.warnings.append("Tidak ditemukan breakpoint @media query responsif.")
            self.score -= 10

    def print_report(self):
        self.score = max(0, min(100, self.score))

        print("\n📋 HASIL PEMERIKSAAN:")
        for p in self.passed:
            print(f"  ✅ [PASS] {p}")
        for w in self.warnings:
            print(f"  ⚠️  [WARN] {w}")
        for f in self.failures:
            print(f"  ❌ [FAIL] {f}")

        print("\n" + "-" * 55)
        grade = "A (Lolos pemeriksaan heuristik)" if self.score >= 90 else (
                "B (Perlu tinjauan lanjutan)" if self.score >= 80 else (
                "C (Perlu Perbaikan)" if self.score >= 60 else "D (Banyak Pelanggaran)"))

        print(f" Skor pemeriksaan heuristik: {self.score}/100 — Predikat: {grade}")
        print("-" * 55 + "\n")

def main():
    parser = argparse.ArgumentParser(description="WebBuilder Heuristic Site Checker")
    parser.add_argument("--dir", default="./", help="Directory of the generated web project")
    args = parser.parse_args()

    auditor = SiteAuditor(args.dir)
    sys.exit(auditor.run())

if __name__ == "__main__":
    main()
