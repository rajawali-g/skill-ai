---
name: image-3d
description: 📸 [3D Image & PBR Suite] Pindai folder foto lokal, analisis peran 3D, kembangkan jadi tekstur PBR (Normal, Roughness, AO), seamless tiling, Power-of-Two GPU, dan konversi ke model 3D GLB via Trellis/Tripo.
---

# 📸 3D Image & PBR Suite (`/image-3d`)

Gunakan perintah `/image-3d` untuk membaca foto di folder yang ditentukan dan mengembangkannya menjadi aset 3D Web fotorealistis.

---

## ⚡ Kemampuan Utama

1. **Batch Folder Inspection & Auto-Development (`image-to-3d-web`)**:
   - Pindai semua foto dalam folder (`.jpg`, `.png`, `.webp`, `.tiff`, `.hdr`).
   - Deteksi otomatis peran 3D: *surface texture*, *panorama IBL*, *isolated prop*, *billboard*.
   - Hasilkan peta PBR otomatis: **Normal Map (+Y OpenGL Three.js)**, **Roughness**, **AO**, dan **Displacement**.
   - Jadikan tekstur berulang tanpa sambungan (*seamless tiling*).
   - Optimasi GPU Power-of-Two (POT 512, 1024, 2048) & kompresi WebP.
   - Buat file `threejs_materials.js` siap pakai.

2. **Image-to-3D Model Generation (`fal-3d`)**:
   - Ubah foto objek menjadi model 3D nyata (`.glb` / `.gltf`) menggunakan AI (Trellis / Hunyuan3D / Tripo).

---

## 🚀 Cara Memanggil di Chat

- `/image-3d public/textures/` ➔ Pindai dan kembangkan seluruh foto di folder tersebut menjadi PBR.
- `/image-3d assets/photos/batu.jpg` ➔ Buat tekstur batuan seamless PBR lengkap.
- `/image-3d --model trellis assets/monumen.png` ➔ Ubah foto monumen menjadi model 3D `.glb`.

---

## 🤝 Kolaborasi dengan Skill Lain

- **`/image-3d` + `/threejs`**: Hubungkan tekstur PBR dan model 3D yang dihasilkan langsung ke scene Three.js dengan pencahayaan IBL dan tone mapping ACES.
- **`/image-3d` + `/gsap`**: Animasikan pergerakan kamera atau rotasi objek 3D yang baru dibuat menggunakan GSAP ScrollTrigger.
