"""
Crop the supplied mascot illustration grid into 8 rounded-square icon tiles.

Input  : assets/mascots_source.png  (a 4-column x 2-row grid of mascot tiles)
Output : assets/mascots/<driver>.png  (one per persona)

The original artwork already presents each mascot inside a rounded-square tile
with its own dark or cream background (alternating across the grid). Rather
than removing those backgrounds, we keep them: each cell is tight-cropped to
its tile and a rounded-rectangle mask trims the outer white gap/corners, giving
a clean app-icon-style tile that preserves the illustration exactly.

Run:  python3 build_mascots.py
Tune: CORNER_RADIUS if the rounded corners show white or clip the art.
"""
import os

from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "mascots_source.png")
OUT_DIR = os.path.join(HERE, "assets", "mascots")

# Grid position (row, col) -> persona driver. Matches the supplied artwork:
#   row 0: Kangaroo · Echidna · Koala · Emu
#   row 1: Kookaburra · Platypus · Quokka · Possum
LAYOUT = {
    (0, 0): "travel",  (0, 1): "saving",     (0, 2): "food",      (0, 3): "fitness",
    (1, 0): "giving",  (1, 1): "technology", (1, 2): "lifestyle", (1, 3): "entertainment",
}

COLS, ROWS = 4, 2
GRID_MARGIN = 0.015     # trim a sliver off each cell before tile detection
WHITE = (252, 252, 252, 255)
WHITE_TOL = 30          # how close to pure white counts as the outer gap
CORNER_RADIUS = 0.14    # rounded-corner radius as a fraction of the tile side
SUPERSAMPLE = 4         # mask anti-aliasing quality


def _close(a, b, tol):
    return abs(a[0] - b[0]) <= tol and abs(a[1] - b[1]) <= tol and abs(a[2] - b[2]) <= tol


def _tile_bbox(px, w, h):
    """Bounding box of the non-white region = the rounded tile within the cell."""
    minx, miny, maxx, maxy, found = w, h, 0, 0, False
    for y in range(0, h, 2):
        for x in range(0, w, 2):
            if not _close(px[x, y], WHITE, WHITE_TOL):
                found = True
                minx, maxx = min(minx, x), max(maxx, x)
                miny, maxy = min(miny, y), max(maxy, y)
    if not found:
        return (0, 0, w, h)
    return (max(0, minx), max(0, miny), min(w, maxx + 1), min(h, maxy + 1))


def _rounded_square(tile):
    """Centre the tile on a square canvas and apply a rounded-rect alpha mask."""
    tw, th = tile.size
    side = max(tw, th)
    canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    canvas.paste(tile, ((side - tw) // 2, (side - th) // 2))

    big = side * SUPERSAMPLE
    mask = Image.new("L", (big, big), 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        [0, 0, big - 1, big - 1], radius=int(big * CORNER_RADIUS), fill=255
    )
    mask = mask.resize((side, side), Image.LANCZOS)

    out = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    out.paste(canvas, (0, 0), mask)
    return out


def main():
    if not os.path.exists(SRC):
        raise SystemExit(
            f"Source not found: {SRC}\n"
            "Save the mascot grid image there first (assets/mascots_source.png)."
        )
    os.makedirs(OUT_DIR, exist_ok=True)
    img = Image.open(SRC).convert("RGBA")
    W, H = img.size
    cw, ch = W / COLS, H / ROWS
    mx, my = cw * GRID_MARGIN, ch * GRID_MARGIN

    for (row, col), driver in LAYOUT.items():
        cell = img.crop((int(col * cw + mx), int(row * ch + my),
                         int((col + 1) * cw - mx), int((row + 1) * ch - my)))
        px = cell.load()
        cell = cell.crop(_tile_bbox(px, cell.width, cell.height))
        out_img = _rounded_square(cell)
        out = os.path.join(OUT_DIR, f"{driver}.png")
        out_img.save(out)
        print(f"  ✓ {driver:13s} {out_img.size}  ->  {os.path.relpath(out, HERE)}")

    print("Done. Re-run generate.py (and restart the app) to use the new tiles.")


if __name__ == "__main__":
    main()
