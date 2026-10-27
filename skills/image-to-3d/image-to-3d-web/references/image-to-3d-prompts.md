# AI Prompting Framework for 3D Web Textures & Assets

When creating 3D Web experiences, raw photos from smartphones often suffer from three major issues:
1. **Baked harsh shadows** (sunlight or flash creates directional shadows that conflict with Three.js scene lights).
2. **Perspective distortion** (angling causes non-uniform texture scaling).
3. **Lens distortion & chromatic aberration**.

Use these prompt templates with **Flux 1.1 Pro**, **Midjourney v6.1**, or **Stable Diffusion 3.5** to generate clean, shadow-free source images.

---

## 1. Seamless Surface Textures (Floors, Walls, Grounds)

### Key Keywords:
`seamless texture`, `flat lay`, `orthographic top-down projection`, `neutral diffuse lighting`, `overcast sky`, `zero cast shadows`, `photorealistic 8k`, `PBR texture map`.

### Example Prompts:
- **Stone / Pavement**:
  > *"Seamless top-down texture of weathered basalt volcanic paving stones, damp surface, micro-crevices, moss between cracks, flat diffuse overcast lighting, zero shadows, orthographic, ultra-detailed 8k, raw texture map."*
- **Wood Flooring**:
  > *"Seamless flat top-down photo of natural aged teak wood planks with subtle wood grain, matte finish, soft diffused studio lighting, no reflections, zero shadows, 8k resolution, raw albedo map."*
- **Terrain / Soil / Grass**:
  > *"Seamless orthographic top-down texture of tropical rich soil with scattered volcanic pebbles and tiny green sprouts, diffuse lighting, flat plane, 8k photorealistic."*

---

## 2. Isolated 3D Props & Objects (For Image-to-3D)

When preparing an image to feed into **Trellis**, **Tripo3D**, or `threejs-object-sculptor`:

### Key Keywords:
`isolated on plain neutral gray background`, `centered`, `full object in frame`, `soft studio light box`, `neutral 50% gray background`, `no occlusion`.

### Example Prompts:
- **Cultural Artifact / Monument**:
  > *"A single ancient Minahasa Waruga stone sarcophagus with carved traditional relief, centered, full view from slight three-quarter front angle, isolated on solid 50% neutral gray background, soft box diffuse studio lighting, zero cast shadows, photorealistic, 8k."*
- **Product Model**:
  > *"A modern ceramic coffee cup, minimalist design, centered, isolated on white background, studio product photography, clean silhouette, sharp focus, 8k."*

---

## 3. 360° Equirectangular Panoramas (For Three.js IBL Environment)

### Key Keywords:
`360 equirectangular panorama`, `equirectangular projection`, `2:1 aspect ratio`, `seamless spherical horizon`, `HDRI lighting`.

### Example Prompts:
- **Scenic Landscape**:
  > *"360 equirectangular panorama of Minahasa mountain ridge overlooking volcanic lake Linow, sunrise with soft golden ambient light, crystal clear atmosphere, 2:1 aspect ratio, seamless 360x180 spherical view, 8k resolution, photorealistic HDRI."*
- **Modern Interior Showroom**:
  > *"360 equirectangular spherical panorama of luxury minimalist architectural gallery, polished concrete floors, floor-to-ceiling glass windows, soft ambient daylight, 2:1 ratio, 8k HDRI environment."*
