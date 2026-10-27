#!/usr/bin/env python3
"""
CLI Helper for fal.ai 3D Model Generation (Trellis / Hunyuan3D / Tripo)
Converts 2D images or prompts into 3D .glb models.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Generate 3D GLB models from images or prompts.")
    parser.add_argument("--image", type=str, help="Path or URL to input image")
    parser.add_argument("--prompt", type=str, help="Text prompt for text-to-3d")
    parser.add_argument("--model", type=str, default="trellis", choices=["trellis", "hunyuan3d", "tripo"])
    parser.add_argument("--output", type=str, default="output_model.glb", help="Destination path for .glb file")
    parser.add_argument("--api-key", type=str, default=None, help="fal.ai API Key (or set FAL_KEY env var)")

    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("FAL_KEY")

    if not args.image and not args.prompt:
        print("[ERROR] Please provide either --image or --prompt.", file=sys.stderr)
        sys.exit(1)

    print(f"🎮 Initializing 3D generation with model: {args.model.upper()}")

    if not api_key:
        print("\n[NOTE] No FAL_KEY detected.")
        print("To run live cloud inference with Microsoft Trellis or Tencent Hunyuan3D:")
        print("  1. Get an API key from https://fal.ai")
        print("  2. Set environment variable: $env:FAL_KEY='your_key' or pass --api-key")
        print(f"\nCommand prepared:")
        print(f"  Model: fal-ai/{args.model}")
        print(f"  Input: {args.image or args.prompt}")
        print(f"  Target output: {args.output}")
        sys.exit(0)

    try:
        import fal_client
        print(f"Connecting to fal.ai endpoint...")
        # Endpoint mapping
        endpoints = {
            "trellis": "fal-ai/trellis",
            "hunyuan3d": "fal-ai/hunyuan3d-v2/image-to-3d",
            "tripo": "fal-ai/triposr"
        }
        endpoint = endpoints.get(args.model, "fal-ai/trellis")
        
        arguments = {}
        if args.image:
            image_path = Path(args.image)
            if image_path.exists():
                print(f"Uploading reference image: {image_path.name}...")
                image_url = fal_client.upload_file(str(image_path))
                arguments["image_url"] = image_url
            else:
                arguments["image_url"] = args.image
        if args.prompt:
            arguments["prompt"] = args.prompt

        print(f"Generating 3D model (this may take 15-40 seconds)...")
        handler = fal_client.submit(endpoint, arguments=arguments)
        result = handler.get()

        model_url = result.get("model_mesh", {}).get("url") or result.get("glb_url")
        if model_url:
            print(f"Downloading generated 3D GLB asset from: {model_url}")
            out_file = Path(args.output)
            out_file.parent.mkdir(parents=True, exist_ok=True)
            urllib.request.urlretrieve(model_url, str(out_file))
            print(f"✅ 3D model saved to: {out_file.resolve()}")
        else:
            print(f"Result received: {json.dumps(result, indent=2)}")

    except ImportError:
        print("[ERROR] 'fal-client' package not installed. Run: pip install fal-client", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Failed during 3D generation: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
