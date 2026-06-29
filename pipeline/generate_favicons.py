"""Generate multi-size favicon PNGs and an ICO from the source logo.

Usage:
    python pipeline/generate_favicons.py

This script prefers `media/favicon.png` and falls back to
`media/LTJ Fellowship Logo Work.png`.
"""
from pathlib import Path
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MEDIA = PROJECT_ROOT / "media"
FAV_DIR = MEDIA / "favicons"
FAV_DIR.mkdir(parents=True, exist_ok=True)

candidates = [MEDIA / "favicon.png", MEDIA / "LTJ Fellowship Logo Work.png"]
src = None
for c in candidates:
    if c.exists():
        src = c
        break

if src is None:
    print("No source image found. Place favicon.png or LTJ Fellowship Logo Work.png in media/")
    raise SystemExit(1)

print(f"Using source: {src}")

def make_square_and_resize(img: Image.Image, size: int) -> Image.Image:
    img = img.convert("RGBA")
    # Resize preserving aspect ratio
    img.thumbnail((size, size), Image.LANCZOS)
    # Paste onto transparent square
    out = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    out.paste(img, ((size - img.width) // 2, (size - img.height) // 2), img)
    return out

base = Image.open(src)
sizes = [512, 256, 192, 180, 48, 32, 16]
for s in sizes:
    out = make_square_and_resize(base, s)
    out_path = FAV_DIR / f"favicon-{s}.png"
    out.save(out_path)
    print("Wrote", out_path)

# Create ICO with multiple sizes (16,32,48,64)
ico_sizes = [16, 32, 48, 64]
icon_imgs = [make_square_and_resize(base, s) for s in ico_sizes]
# Pillow can save ICO with sizes parameter from a single image, so pass the largest
icon_imgs[-1].save(FAV_DIR / "favicon.ico", format="ICO", sizes=[(s, s) for s in ico_sizes])
print("Wrote", FAV_DIR / "favicon.ico")

print("Done. Favicons written to:", FAV_DIR)
