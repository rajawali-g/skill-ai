---
name: image-to-3d-web
description: Inspect, scan, and transform photos from any local folder into realistic 3D web assets — including automatic PBR map generation (Normal, Roughness, AO, Displacement), seamless tiling, Power-of-Two GPU optimization, Image-to-3D mesh pipelines (Trellis/Tripo/GLTF), and ready-to-use Three.js/WebGPU material code.
---

# Image to 3D Web & PBR Suite

Transform raw photos and image directories into production-ready, hyper-realistic 3D web assets. This skill handles the complete pipeline from inspecting source images in any folder to generating physically based rendering (PBR) maps, seamless textures, GPU-friendly Power-of-Two (POT) resolutions, and ready-to-paste Three.js (WebGL / WebGPU TSL) code.

---

## ⚡ When to Activate This Skill

Activate this skill when:
- The user specifies a folder of photos (e.g., `assets/images/`, `public/photos/`, `textures/`) and wants to use them in a 3D web project.
- You need to generate realistic textures, depth, or bumpiness from a 2D flat photo.
- You need PBR maps: **Normal Map (+Y OpenGL for Three.js)**, **Roughness Map**, **Ambient Occlusion (AO) Map**, and **Displacement Map**.
- You need seamless tiling so textures repeat across 3D planes without visible seams.
- You want to convert an object photo into a 3D model (`.glb` / `.gltf`) or procedural Three.js mesh.
- You want to setup realistic Image-Based Lighting (IBL) from a 360° panorama photo.

---

## 🛠️ CLI Tool: `process_folder.py`

This skill provides a high-performance Python script powered by `numpy` and `Pillow`.

### 1. Inspect Image Folder
Inspect all images in any specified directory:
```bash
python "<skill-dir>/scripts/process_folder.py" "<path/to/folder>" --action inspect
```
Outputs a technical report:
- Resolution, aspect ratio, color channels.
- Power-of-Two (POT) compliance check (e.g. 512, 1024, 2048) for GPU mipmapping.
- 3D Role Classification:
  - `texture_surface`: Ideal for ground, wall, wood, stone, fabric PBR materials.
  - `environment_ibl`: 360° equirectangular panoramas (2:1 ratio or HDR/EXR).
  - `billboard_cutout`: Transparent PNGs for 2.5D interactive cards or sprites.
  - `object_or_prop`: Isolated objects for 3D model reconstruction.

### 2. Full PBR & 3D Development (`--action all` or `--action pbr`)
Automatically process every photo in the folder:
```bash
python "<skill-dir>/scripts/process_folder.py" "<path/to/folder>" --action all --pot-size 1024 --strength 2.0
```
What this generates in `<folder>/developed_3d_assets/`:
1. `[name]_diffuse.webp` / `[name]_diffuse.png`: Resized to Power-of-Two with high-quality Lanczos filtering.
2. `[name]_normal.png`: OpenGL-standard (+Y Up) Normal Map computed via Sobel spatial gradients.
3. `[name]_roughness.png`: Roughness map calibrated for realistic micro-facet light scattering.
4. `[name]_ao.png`: Cavity and Ambient Occlusion map highlighting deep crevices and joints.
5. `[name]_displacement.png`: Smooth height field for 3D vertex displacement.
6. `threejs_materials.js`: Ready-to-import Three.js & WebGPU material setup module.
7. `asset_manifest.json`: JSON metadata for programmatic loading.

### 3. Make Seamless Repeating Textures (`--seamless`)
If photos are surfaces that need to tile infinitely on 3D floors, terrains, or walls:
```bash
python "<skill-dir>/scripts/process_folder.py" "<path/to/folder>" --action pbr --seamless --pot-size 1024
```

### 4. Generate Three.js Code Only (`--action code`)
Print the complete Three.js code without modifying files:
```bash
python "<skill-dir>/scripts/process_folder.py" "<path/to/folder>" --action code
```

---

## 🎨 Three.js PBR Standards & Critical Rules

### 1. Color Space Rules (Do Not Skip!)
Failure to set the correct color space will make 3D scenes look washed out or plasticky:
```javascript
// Color maps (albedo, diffuse, background) MUST use SRGB:
albedoTexture.colorSpace = THREE.SRGBColorSpace;

// Mathematical data maps (normal, roughness, metalness, AO, height) MUST use NoColorSpace:
normalTexture.colorSpace = THREE.NoColorSpace;
roughnessTexture.colorSpace = THREE.NoColorSpace;
aoTexture.colorSpace = THREE.NoColorSpace;
displacementTexture.colorSpace = THREE.NoColorSpace;
```

### 2. Normal Map Coordinates
- **Three.js uses OpenGL Normal Maps (+Y Up)**.
- `process_folder.py` generates OpenGL format by default (green channel points up).
- If using DirectX normal maps (-Y), invert the green scale in Three.js:
  `material.normalScale.set(1.0, -1.0);`

### 3. MeshPhysicalMaterial Best Practices
For ultra-realism, prefer `THREE.MeshPhysicalMaterial` over basic `MeshStandardMaterial`:
```javascript
const material = new THREE.MeshPhysicalMaterial({
  map: diffuseTexture,
  normalMap: normalTexture,
  normalScale: new THREE.Vector2(1.0, 1.0),
  roughnessMap: roughnessTexture,
  roughness: 0.8,
  aoMap: aoTexture,
  aoMapIntensity: 1.2,
  metalness: 0.05,
  // Subtle real-world physical reflections:
  clearcoat: 0.1,
  clearcoatRoughness: 0.1,
  reflectivity: 0.5,
});
```

---

## 🚀 Image-to-3D Model Pipeline (Turning Photos into 3D Meshes)

When a photo contains an object (e.g. a product, souvenir, building, monument):
1. **Procedural Reconstruction**:
   - Use `threejs-object-sculptor` to extract silhouettes, massing, and construct procedural Three.js geometry.
2. **AI Image-to-3D Generation (`fal-3d`)**:
   - Use fal.ai's **Trellis (Microsoft)** or **Hunyuan3D** endpoints:
     - Input: Single clean photo.
     - Output: `.glb` with high-poly geometric mesh and extracted PBR textures.
   - Command:
     ```bash
     python "<skill-dir>/scripts/generate_3d.py" --image "<path/to/image.jpg>" --model trellis
     ```

---

## 💡 AI Prompting for Realism (Flux / Midjourney)

If the user's photos are blurry, unevenly lit, or have harsh baked shadows, use these prompting formulas to recreate or enhance them before generating PBR maps:

### Formula for PBR Texture Albedo:
> *"Seamless flat top-down photo of [material, e.g., ancient volcanic stone wall, Minahasa teak wood planks], neutral overcast studio lighting, zero cast shadows, ultra-detailed micro-texture, 8k resolution, raw photorealistic texture map, orthographic projection."*

### Formula for Isolated 3D Prop:
> *"A single [object, e.g., Minahasa Waruga traditional stone sarcophagus], centered, full object visible, isolated on plain solid neutral gray background, diffuse soft box lighting, zero harsh shadows, studio product photography, photorealistic, 8k."*

### Formula for 360° Environment IBL:
> *"360 equirectangular spherical panorama, [environment, e.g., lush tropical mountain overlook at sunrise, Minahasa highlands], high dynamic range, photorealistic, 8k, full 360x180 view, seamless horizon."*
