---
name: threejs-gsap-integration
description: Master architecture and implementation patterns for animating Three.js with GSAP (GreenSock) and ScrollTrigger. Covers 3D property tweening (camera, mesh, materials, lighting), scroll-driven camera paths, zero-stutter render loop coordination with gsap.ticker, cursor/mouse inertia via quickTo, and framework lifecycle safety (Vue 3, Nuxt, React) using gsap.context() and ctx.revert(). Use when integrating GSAP with Three.js, building 3D scrollytelling websites, or animating WebGL/WebGPU scenes.
---

# Three.js + GSAP Integration Guide

This skill specifies the definitive patterns for combining **Three.js** (WebGL/WebGPU) and **GSAP (GreenSock Animation Platform v3)** to build smooth, cinematic, production-grade 3D web experiences without performance stutter or memory leaks.

---

## 1. Core Property Tweening in Three.js

Three.js objects use instances of `Vector3`, `Euler`, `Color`, and numerical scalar properties. Always target the actual numeric properties:

### A. Position and Scale (`Vector3`)
```javascript
import gsap from "gsap";

// Animate camera or mesh position
gsap.to(camera.position, {
  x: 0,
  y: 2.5,
  z: 6,
  duration: 1.8,
  ease: "power3.inOut"
});

// Uniform or individual scale
gsap.to(mesh.scale, {
  x: 1.5,
  y: 1.5,
  z: 1.5,
  duration: 1.2,
  ease: "back.out(1.7)"
});
```

### B. Rotation (`Euler`)
```javascript
// Rotate in Radians (Math.PI)
gsap.to(mesh.rotation, {
  x: Math.PI * 0.25,
  y: Math.PI * 2,
  duration: 2.5,
  ease: "expo.out"
});
```

### C. Materials and Colors
```javascript
// Transparent material fade
mesh.material.transparent = true;
gsap.to(mesh.material, {
  opacity: 0,
  duration: 1,
  ease: "power2.out"
});

// Color transition (interpolate hex or r, g, b)
const targetColor = new THREE.Color("#ff0077");
gsap.to(mesh.material.color, {
  r: targetColor.r,
  g: targetColor.g,
  b: targetColor.b,
  duration: 1.5,
  ease: "power2.inOut"
});
```

---

## 2. Render Loop & Ticker Coordination (Zero Stutter)

**The #1 mistake:** Running an independent `requestAnimationFrame` loop that conflicts with GSAP ScrollTrigger updates, causing micro-stuttering.

### Preferred Pattern: Let `gsap.ticker` drive the Three.js Render Loop
GSAP's internal ticker runs on `requestAnimationFrame` and coordinates all tweens and ScrollTriggers before rendering:

```javascript
import * as THREE from "three";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);

// Define the single render function
function onTick(time, deltaTime, frame) {
  // Optional: update controls or shaders
  // controls.update();
  
  renderer.render(scene, camera);
}

// Attach to GSAP Ticker
gsap.ticker.add(onTick);

// Set FPS priority if desired (defaults to 60/120Hz native refresh)
gsap.ticker.lagSmoothing(500, 33);
```

### If using Lenis Smooth Scroll
When combining **Lenis + GSAP + Three.js**:
```javascript
import Lenis from "lenis";

const lenis = new Lenis({ lerp: 0.1, smoothWheel: true });

// Synchronize Lenis with GSAP ScrollTrigger
lenis.on("scroll", ScrollTrigger.update);

gsap.ticker.add((time) => {
  lenis.raf(time * 1000);
});

// Disable GSAP lag smoothing to ensure synchronized momentum
gsap.ticker.lagSmoothing(0);
```

---

## 3. ScrollTrigger 3D Scrollytelling Architecture

To create an Awwwards-style persistent 3D world that travels through sections:

1. **Fixed Fullscreen Canvas**: Position the `<canvas>` fixed in the background (`position: fixed; inset: 0; z-index: 1; pointer-events: none`).
2. **DOM Story Chapters**: Regular HTML sections with content positioned in front (`position: relative; z-index: 2`).
3. **Master Scrub Timeline**:

```javascript
const tl = gsap.timeline({
  scrollTrigger: {
    trigger: "#scroll-container",
    start: "top top",
    end: "bottom bottom",
    scrub: 1.2, // Smooth interpolation delay (0.8 - 1.5s for cinematic feel)
  }
});

// Chapter 1 -> Chapter 2
tl.addLabel("chapter-hero")
  .to(camera.position, { x: 3, y: 1.5, z: 8, ease: "power1.inOut" }, "step1")
  .to(mesh.rotation, { y: Math.PI * 0.5, ease: "none" }, "step1")
  .to("#hero-text", { opacity: 0, y: -50, ease: "power2.in" }, "step1");

// Chapter 2 -> Chapter 3
tl.addLabel("chapter-details")
  .to(camera.position, { x: -2, y: 0.5, z: 4, ease: "power1.inOut" }, "step2")
  .to(mesh.rotation, { y: Math.PI, ease: "none" }, "step2")
  .fromTo("#details-text", { opacity: 0, y: 50 }, { opacity: 1, y: 0, ease: "power2.out" }, "step2");
```

---

## 4. Mouse Inertia Parallax (`quickTo`)

For smooth, non-laggy cursor-following 3D tilts:

```javascript
// Pre-calculate setters for maximum performance
const xTo = gsap.quickTo(camera.position, "x", { duration: 0.8, ease: "power3.out" });
const yTo = gsap.quickTo(camera.position, "y", { duration: 0.8, ease: "power3.out" });

window.addEventListener("pointermove", (e) => {
  const normX = (e.clientX / window.innerWidth - 0.5) * 2;
  const normY = -(e.clientY / window.innerHeight - 0.5) * 2;
  
  // Parallax offset (e.g. ±0.5 units)
  xTo(normX * 0.5);
  yTo(normY * 0.3);
});
```

---

## 5. Framework Lifecycle (Vue 3 / Nuxt / React)

Prevent memory leaks, orphaned ScrollTriggers, and duplicate WebGL contexts:

### Vue 3 / Nuxt 3 Pattern
```vue
<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";
import * as THREE from "three";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

const canvasRef = ref<HTMLCanvasElement | null>(null);
let ctx: gsap.Context | null = null;
let renderer: THREE.WebGLRenderer | null = null;

onMounted(() => {
  if (!canvasRef.value) return;

  // 1. Initialize Three.js
  renderer = new THREE.WebGLRenderer({ canvas: canvasRef.value, antialias: true, alpha: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 100);

  // 2. Wrap all GSAP in gsap.context for easy cleanup
  ctx = gsap.context(() => {
    gsap.to(camera.position, {
      z: 5,
      scrollTrigger: {
        trigger: ".story-section",
        start: "top top",
        end: "bottom bottom",
        scrub: true,
      }
    });

    // Drive render loop inside ticker
    gsap.ticker.add(() => {
      renderer?.render(scene, camera);
    });
  });
});

onUnmounted(() => {
  // 3. Clean up GSAP context (kills all animations, scrolltriggers, and ticker listeners)
  ctx?.revert();
  
  // 4. Clean up Three.js WebGL context
  renderer?.dispose();
  renderer?.forceContextLoss();
});
</script>
```

---

## 6. Checklist & Anti-Patterns

- [x] **DO** use `gsap.context()` in any component lifecycle.
- [x] **DO** drive `renderer.render()` via `gsap.ticker.add()` or sync with `ScrollTrigger.update()`.
- [x] **DO** use numeric properties (`pos.x`, `color.r`, `material.opacity`).
- [ ] **DON'T** manually set `mesh.rotation.y += 0.01` in RAF while GSAP is also tweening `mesh.rotation.y` (they fight each other).
- [ ] **DON'T** forget to call `ScrollTrigger.refresh()` after 3D models or asynchronous fonts have loaded.
