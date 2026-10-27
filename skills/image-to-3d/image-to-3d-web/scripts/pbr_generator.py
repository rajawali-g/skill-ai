#!/usr/bin/env python3
"""
PBR Texture Map Generator for Three.js & WebGPU
Generates Normal, Roughness, Ambient Occlusion (AO), and Displacement maps
from any raw diffuse/albedo image using NumPy and Pillow.
"""

from __future__ import annotations
import math
import numpy as np
from PIL import Image, ImageFilter, ImageOps


def to_grayscale_array(img: Image.Image) -> np.ndarray:
    """Convert PIL image to float32 grayscale array in range [0.0, 1.0]."""
    gray = img.convert("L")
    return np.array(gray, dtype=np.float32) / 255.0


def generate_normal_map(
    img: Image.Image,
    strength: float = 2.0,
    invert_y: bool = False
) -> Image.Image:
    """
    Generate an OpenGL-compliant (+Y Up) Normal Map for Three.js.
    Uses Sobel filter convolution on the height/luminance field.
    """
    h_arr = to_grayscale_array(img)
    rows, cols = h_arr.shape

    # Sobel kernels
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32)

    # Padding for boundary continuity (edge reflection)
    padded = np.pad(h_arr, pad_width=1, mode="reflect")

    # Vectorized convolution
    # Slice neighbors
    w00 = padded[:-2, :-2]
    w01 = padded[:-2, 1:-1]
    w02 = padded[:-2, 2:]
    w10 = padded[1:-1, :-2]
    w12 = padded[1:-1, 2:]
    w20 = padded[2:, :-2]
    w21 = padded[2:, 1:-1]
    w22 = padded[2:, 2:]

    # dx gradient
    dx = (w02 + 2.0 * w12 + w22) - (w00 + 2.0 * w10 + w20)
    # dy gradient
    dy = (w20 + 2.0 * w21 + w22) - (w00 + 2.0 * w01 + w02)

    # Scale gradients by bump strength
    dx = dx * strength
    dy = dy * strength

    # Three.js uses OpenGL format (+Y Up) by default
    # If invert_y is True, convert to DirectX (-Y)
    if invert_y:
        dy = -dy

    # Normal vector components: N = (-dx, dy, 1.0)
    nx = -dx
    ny = dy
    nz = np.ones_like(nx)

    # Normalize to unit length
    norm = np.sqrt(nx * nx + ny * ny + nz * nz)
    nx /= norm
    ny /= norm
    nz /= norm

    # Map from [-1.0, 1.0] to [0, 255] RGB
    r = np.clip((nx * 0.5 + 0.5) * 255.0, 0, 255).astype(np.uint8)
    g = np.clip((ny * 0.5 + 0.5) * 255.0, 0, 255).astype(np.uint8)
    b = np.clip((nz * 0.5 + 0.5) * 255.0, 0, 255).astype(np.uint8)

    normal_rgb = np.stack([r, g, b], axis=-1)
    return Image.fromarray(normal_rgb, mode="RGB")


def generate_roughness_map(
    img: Image.Image,
    invert: bool = False,
    contrast: float = 1.2,
    base_roughness: float = 0.5
) -> Image.Image:
    """
    Generate Roughness Map (0 = Mirror Smooth, 255 = Completely Rough).
    Derived from luminance distribution, frequency variance, and material contrast.
    """
    gray_arr = to_grayscale_array(img)

    # Contrast adjustment centered on mean
    mean = np.mean(gray_arr)
    adjusted = (gray_arr - mean) * contrast + mean + (base_roughness - 0.5)
    adjusted = np.clip(adjusted, 0.0, 1.0)

    if invert:
        adjusted = 1.0 - adjusted

    rough_uint8 = (adjusted * 255.0).astype(np.uint8)
    return Image.fromarray(rough_uint8, mode="L")


def generate_displacement_map(
    img: Image.Image,
    blur_radius: float = 1.0
) -> Image.Image:
    """
    Generate Height / Displacement Map for 3D geometric vertex displacement.
    Lightly smoothed to prevent jagged mesh tearing under tessellation.
    """
    gray = img.convert("L")
    if blur_radius > 0:
        gray = gray.filter(ImageFilter.GaussianBlur(radius=blur_radius))
    # Normalize contrast to maximize displacement depth
    return ImageOps.autocontrast(gray, cutoff=1)


def generate_ao_map(
    img: Image.Image,
    intensity: float = 1.0,
    cavity_blur: float = 4.0
) -> Image.Image:
    """
    Generate Ambient Occlusion (AO) / Cavity Map.
    Detects crevasses and micro-shadows by comparing fine detail against local average.
    """
    h_arr = to_grayscale_array(img)
    # Blur image to get local average height
    blurred = img.convert("L").filter(ImageFilter.GaussianBlur(radius=cavity_blur))
    b_arr = np.array(blurred, dtype=np.float32) / 255.0

    # Cavity: where local height is lower than neighborhood average
    diff = b_arr - h_arr
    cavity = np.clip(diff * 2.5 * intensity, 0.0, 1.0)

    # AO map: 1.0 is unoccluded (white), lower is occluded (dark)
    ao = 1.0 - cavity
    ao = np.clip(ao, 0.0, 1.0)

    ao_uint8 = (ao * 255.0).astype(np.uint8)
    return Image.fromarray(ao_uint8, mode="L")


def make_seamless(
    img: Image.Image,
    blend_ratio: float = 0.15
) -> Image.Image:
    """
    Create a seamless repeating / tileable texture by offsetting and alpha blending
    the cross seams.
    """
    w, h = img.size
    offset_x = w // 2
    offset_y = h // 2

    # Offset image
    shifted = Image.new(img.mode, (w, h))
    # 4 quadrants
    q1 = img.crop((0, 0, offset_x, offset_y))
    q2 = img.crop((offset_x, 0, w, offset_y))
    q3 = img.crop((0, offset_y, offset_x, h))
    q4 = img.crop((offset_x, offset_y, w, h))

    shifted.paste(q4, (0, 0))
    shifted.paste(q3, (w - offset_x, 0))
    shifted.paste(q2, (0, h - offset_y))
    shifted.paste(q1, (w - offset_x, h - offset_y))

    # Linear cross blend along center seam
    blend_w = max(4, int(w * blend_ratio))
    blend_h = max(4, int(h * blend_ratio))

    orig_arr = np.array(img, dtype=np.float32)
    shift_arr = np.array(shifted, dtype=np.float32)

    # Create 2D smooth blend mask (1 at edges, 0 at center)
    x = np.linspace(0, np.pi, w)
    y = np.linspace(0, np.pi, h)
    xx, yy = np.meshgrid(np.sin(x), np.sin(y))
    mask = (xx * yy) ** 0.5
    if len(orig_arr.shape) == 3:
        mask = np.expand_dims(mask, axis=-1)

    blended = shift_arr * (1.0 - mask) + orig_arr * mask
    blended = np.clip(blended, 0, 255).astype(np.uint8)
    return Image.fromarray(blended, mode=img.mode)


def get_nearest_pot(val: int, max_val: int = 4096) -> int:
    """Return the nearest Power of Two (POT) integer <= max_val."""
    pot = 2 ** round(math.log2(val))
    return min(max_val, max(128, pot))


def resize_to_pot(
    img: Image.Image,
    target_size: tuple[int, int] | None = None,
    square: bool = True,
    max_dim: int = 2048
) -> Image.Image:
    """
    Resize image to Power-of-Two dimensions for optimal WebGL/WebGPU texture mipmapping.
    """
    w, h = img.size
    if target_size:
        tw, th = target_size
    elif square:
        dim = get_nearest_pot(max(w, h), max_val=max_dim)
        tw, th = dim, dim
    else:
        tw = get_nearest_pot(w, max_val=max_dim)
        th = get_nearest_pot(h, max_val=max_dim)

    if (w, h) == (tw, th):
        return img

    return img.resize((tw, th), Image.Resampling.LANCZOS)
