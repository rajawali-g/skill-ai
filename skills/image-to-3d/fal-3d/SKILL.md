---
name: fal-3d
description: Generate 3D models (GLB, OBJ) from text or 2D reference images using state-of-the-art AI endpoints (Trellis, Hunyuan3D, Tripo3D).
---

# fal-3d: AI Image-to-3D Model Generator

Convert 2D images or text prompts into high-quality 3D assets (`.glb` / `.gltf`) with geometric meshes and PBR texture maps using serverless AI inference.

---

## 🚀 Capabilities

1. **Image to 3D**:
   - Converts single-view or multi-view photos of objects into clean 3D meshes.
   - Recommended Models:
     - `fal-ai/trellis`: State-of-the-art (Microsoft) structured 3D geometry + PBR texture maps from a single image.
     - `fal-ai/hunyuan3d-v2/image-to-3d`: High-fidelity asset generation with dense vertex detail.
     - `fal-ai/triposr`: Lightning-fast sub-second mesh extraction for quick previews.

2. **Text to 3D**:
   - Generates textured 3D models directly from detailed natural language descriptions.

---

## 🛠️ Usage

### Generate 3D Model from Image:
```bash
python "<skill-dir>/scripts/generate_3d.py" --image "path/to/object.png" --model trellis --output "assets/models/"
```

### Parameters:
- `--image`: Path to input photo (isolated object on plain background yields the best geometry).
- `--prompt`: (Optional) Text description guiding the 3D generation.
- `--model`: `trellis` (default), `hunyuan3d`, or `tripo`.
- `--texture-size`: `1024` or `2048`.
- `--api-key`: FAL_KEY environment variable or direct argument.
