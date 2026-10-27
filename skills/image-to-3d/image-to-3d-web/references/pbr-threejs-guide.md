# Three.js & WebGPU PBR Realism Reference Guide

Achieving photorealism in WebGL and WebGPU relies on four pillars:
1. **PBR Texture Quality (Albedo, Normal, Roughness, AO, Displacement)**
2. **Correct Color Spaces & Linear Pipeline**
3. **Image-Based Lighting (IBL / HDRI Environment)**
4. **Tone Mapping & Exposure**

---

## 1. Complete Three.js PBR Setup Example

```javascript
import * as THREE from 'three';
import { HDRLoader } from 'three/examples/jsm/loaders/HDRLoader.js'; // or RGBELoader

// 1. Renderer Setup with Tone Mapping
const renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: 'high-performance' });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

// Tone mapping is CRITICAL for realistic light falloff
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;
renderer.outputColorSpace = THREE.SRGBColorSpace;
document.body.appendChild(renderer.domElement);

// 2. Texture Loading with Correct Color Spaces
const textureLoader = new THREE.TextureLoader();

function loadPBRTexture(url, isColor = false) {
  const tex = textureLoader.load(url);
  tex.wrapS = THREE.RepeatWrapping;
  tex.wrapT = THREE.RepeatWrapping;
  tex.colorSpace = isColor ? THREE.SRGBColorSpace : THREE.NoColorSpace;
  return tex;
}

const albedoMap = loadPBRTexture('./textures/wood_diffuse.webp', true);
const normalMap = loadPBRTexture('./textures/wood_normal.png', false);
const roughnessMap = loadPBRTexture('./textures/wood_roughness.png', false);
const aoMap = loadPBRTexture('./textures/wood_ao.png', false);
const displacementMap = loadPBRTexture('./textures/wood_displacement.png', false);

// 3. Realistic MeshPhysicalMaterial
const pbrMaterial = new THREE.MeshPhysicalMaterial({
  map: albedoMap,
  normalMap: normalMap,
  normalScale: new THREE.Vector2(1.2, 1.2),
  roughnessMap: roughnessMap,
  roughness: 0.85,
  aoMap: aoMap,
  aoMapIntensity: 1.2,
  metalness: 0.05,
  displacementMap: displacementMap,
  displacementScale: 0.05, // Subtle geometric relief
  displacementBias: -0.025,
  clearcoat: 0.08,
  clearcoatRoughness: 0.1,
});

// 4. Geometry (Requires Second UV Set for AO Map!)
const geometry = new THREE.PlaneGeometry(10, 10, 128, 128); // Tessellated for displacement
// In Three.js, aoMap requires uv2:
geometry.setAttribute('uv2', geometry.attributes.uv);

const mesh = new THREE.Mesh(geometry, pbrMaterial);
scene.add(mesh);

// 5. Image-Based Lighting (IBL)
new HDRLoader().load('./textures/studio_env.hdr', (envTexture) => {
  envTexture.mapping = THREE.EquirectangularReflectionMapping;
  scene.environment = envTexture; // Lights all PBR materials automatically
});
```

---

## 2. Common Realism Pitfalls

| Mistake | Visual Symptom | Solution |
| :--- | :--- | :--- |
| Normal map set to `SRGBColorSpace` | Weird blotchy highlights, wrong bumps | Set `normalMap.colorSpace = THREE.NoColorSpace` |
| Missing `uv2` attribute | AO map has no visible effect | `geometry.setAttribute('uv2', geometry.attributes.uv)` |
| Missing Tone Mapping | Blown-out white highlights or flat colors | `renderer.toneMapping = THREE.ACESFilmicToneMapping` |
| Non-Power-of-Two (NPOT) textures | Stutter during upload, blurry mipmaps | Resize to 512, 1024, or 2048 with `process_folder.py --action pot` |
| Hardcoded pure black (0,0,0) or pure white (255,255,255) | Unnatural void or radioactive glow | Real-world albedo ranges between ~30 and ~230 |
