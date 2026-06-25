"""
Crop the supplied mascot illustration grid into 8 rounded-square icon tiles.

Input  : assets/mascot.png  (a 4-column x 2-row grid of white, bordered tiles)
Output : assets/mascots/<driver>.png  (one per persona)

The artwork presents each mascot inside a white rounded-square tile with a thin
border, on a white page. We keep those tiles exactly as drawn: each cell is
tight-cropped to its tile (via the border), then the four outer corners — the
white page showing through outside the rounded border — are flood-filled to
transparency. The white fill and border inside the tile are left untouched, so
the icon keeps its original look on any background.

Run:  python3 build_mascots.py
"""
import os
from collections import deque

from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "mascot.png")
OUT_DIR = os.path.join(HERE, "assets", "mascots")

# Grid position (row, col) -> persona driver. Matches the supplied artwork:
#   row 0: Kangaroo · Echidna · Koala · Emu
#   row 1: Kookaburra · Platypus · Quokka · Possum
LAYOUT = {
    (0, 0): "travel",  (0, 1): "saving",     (0, 2): "food",      (0, 3): "fitness",
    (1, 0): "giving",  (1, 1): "technology", (1, 2): "lifestyle", (1, 3): "entertainment",
}

COLS, ROWS = 4, 2
GRID_MARGIN = 0.01      # trim a sliver off each cell before tile detection
BORDER_LEVEL = 232      # pixels darker than this (any channel) count as foreground
CORNER_WHITE = 236      # corner-flood clears pixels lighter than this

# White rounded-tile output (consistent app-icon style, with a subtle border)
TILE = 360              # output tile size (px)
MASCOT_MARGIN = 0.12    # white margin around the mascot inside the tile
RADIUS = 0.18           # corner radius as a fraction of the tile size
TILE_FILL = (255, 255, 255, 255)
BORDER_COLOR = (214, 214, 217, 255)
BORDER_W = 4
SS = 4                  # supersampling for smooth mask/border


def _is_white(c, level):
    return c[0] >= level and c[1] >= level and c[2] >= level


def _tile_bbox(px, w, h):
    """Bounding box of the tile (its border is the outermost non-white ring)."""
    minx, miny, maxx, maxy, found = w, h, 0, 0, False
    for y in range(0, h, 2):
        for x in range(0, w, 2):
            if not _is_white(px[x, y], BORDER_LEVEL):
                found = True
                minx, maxx = min(minx, x), max(maxx, x)
                miny, maxy = min(miny, y), max(maxy, y)
    if not found:
        return (0, 0, w, h)
    return (max(0, minx - 1), max(0, miny - 1), min(w, maxx + 2), min(h, maxy + 2))


def _clear_corners(tile):
    """Flood from the four corners, clearing the white page outside the rounded
    border to transparency (stops at the border, so the tile fill is kept)."""
    tile = tile.convert("RGBA")
    px = tile.load()
    w, h = tile.size
    seen = [[False] * w for _ in range(h)]
    q = deque([(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)])
    while q:
        x, y = q.popleft()
        if not (0 <= x < w and 0 <= y < h) or seen[y][x]:
            continue
        seen[y][x] = True
        c = px[x, y]
        if c[3] == 0 or _is_white(c, CORNER_WHITE):
            px[x, y] = (0, 0, 0, 0)
            q.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])
    return tile


def _white_tile(mascot):
    """Centre the isolated mascot on a uniform white rounded tile with a thin
    border — keeping the consistent boxed icon style on any background."""
    bbox = mascot.getbbox()
    if bbox:
        mascot = mascot.crop(bbox)
    inner = int(TILE * (1 - 2 * MASCOT_MARGIN))
    scale = min(inner / mascot.width, inner / mascot.height)
    mascot = mascot.resize(
        (max(1, int(mascot.width * scale)), max(1, int(mascot.height * scale))),
        Image.LANCZOS,
    )

    # rounded-rect alpha mask (supersampled)
    big = TILE * SS
    mask = Image.new("L", (big, big), 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        [0, 0, big - 1, big - 1], radius=int(big * RADIUS), fill=255
    )
    mask = mask.resize((TILE, TILE), Image.LANCZOS)

    tile = Image.new("RGBA", (TILE, TILE), TILE_FILL)
    tile.paste(mascot, ((TILE - mascot.width) // 2, (TILE - mascot.height) // 2), mascot)
    tile.putalpha(mask)

    # subtle border, drawn just inside the rounded edge
    bd = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    off = BORDER_W * SS // 2
    ImageDraw.Draw(bd).rounded_rectangle(
        [off, off, big - 1 - off, big - 1 - off],
        radius=int(big * RADIUS) - off, outline=BORDER_COLOR, width=BORDER_W * SS,
    )
    tile.alpha_composite(bd.resize((TILE, TILE), Image.LANCZOS))
    return tile


def main():
    if not os.path.exists(SRC):
        raise SystemExit(f"Source not found: {SRC}\nSave the mascot grid there first.")
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
        out_img = _white_tile(_clear_corners(cell))
        out = os.path.join(OUT_DIR, f"{driver}.png")
        out_img.save(out)
        print(f"  ✓ {driver:13s} {out_img.size}  ->  {os.path.relpath(out, HERE)}")

    print("Done. Re-run generate.py (and restart the app) to use the new tiles.")


if __name__ == "__main__":
    main()
