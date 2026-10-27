---
name: threejs
description: 🎮 [Three.js & WebGPU Master] Panduan lengkap grafis 3D web (r186), WebGPU TSL, tata pencahayaan IBL/HDR, material PBR, shader kustom, kamera, post-processing bloom, dan Rapier physics.
---

# 🎮 Three.js & WebGPU Master Suite (`/threejs`)

Gunakan perintah `/threejs` untuk merancang, membangun, dan mengoptimalkan pengalaman grafis 3D interaktif pada browser menggunakan WebGL r186 maupun WebGPU modern.

---

## ⚡ Kemampuan Utama

1. **Core WebGL & PBR Standard**:
   - `threejs-fundamentals`, `threejs-geometry`, `threejs-materials`, `threejs-lighting`, `threejs-textures`.
   - Pencegahan halusinasi API lama: gunakan `Timer` (bukan `Clock`), `HDRLoader` (bukan `RGBELoader`), dan `SRGBColorSpace`.
2. **WebGPU & TSL Procedural Worlds**:
   - Pencahayaan global IBL, GTAO ambient contact shading, bloom sinematik, kabut volumetrik, dan simulasi air spektral.
3. **Fisika & Interaktivitas**:
   - Integrasi engine fisika modern (Rapier WASM & Cannon-es), raycasting, dan kontrol kamera halus.

---

## 🚀 Cara Memanggil di Chat

- `/threejs buatkan canvas 3D produk interaktif dengan material emas PBR dan bayangan lembut`
- `/threejs setup scene WebGPU dengan pencahayaan HDR environment`
- `/threejs optimasi performa 60 FPS untuk render 10.000 partikel`

---

## 🤝 Kolaborasi dengan Skill Lain

- **`/threejs` + `/image-3d`**: Gunakan tekstur PBR (Normal, Roughness, AO) hasil olahan folder foto untuk material permukaan yang realistis.
- **`/threejs` + `/gsap`**: Sinkronkan perputaran objek atau pergerakan kamera sinematik dengan scroll halaman menggunakan GSAP `ScrollTrigger` dan `quickTo`.
- **`/threejs` + `/ui-ux`**: Padukan canvas 3D dengan antarmuka UI Glassmorphism atau Bento Grid modern.
