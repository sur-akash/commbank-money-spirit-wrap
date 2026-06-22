"""
Crop the supplied mascot illustration grid into 8 isolated, transparent PNGs.

Input  : assets/mascots_source.png  (a 4-column x 2-row grid of mascot tiles)
Output : assets/mascots/<driver>.png  (one per persona, background removed)

Pipeline per tile:
  1. split the grid into 8 equal cells;
  2. tight-crop to the rounded tile (drop the wide white gap);
  3. isolate the centred animal from the solid tile fill, branching on whether
     the tile is light (cream) or dark (navy) — they need different handling:
       * light tiles: flood away pixels close to the cream/white fill;
       * dark tiles: luminance-capped region-grow so the dark fill is removed
         but light-coloured animals (and their interiors) survive;
  4. keep only sizeable components that don't touch the border (drops the gap,
     the anti-aliased ring and small floating tile decorations);
  5. auto-crop + pad onto a square canvas.

Run:  python3 build_mascots.py
"""
import os
from collections import Counter, deque

from PIL import Image

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
GRID_MARGIN = 0.02   # fraction of each cell trimmed before tile detection
PAD = 18             # transparent padding around the cropped subject
WHITE = (252, 252, 252, 255)


def _close(a, b, tol):
    return abs(a[0] - b[0]) <= tol and abs(a[1] - b[1]) <= tol and abs(a[2] - b[2]) <= tol


def _lum(c):
    return 0.299 * c[0] + 0.587 * c[1] + 0.114 * c[2]


def _tile_bbox(px, w, h):
    """Bounding box of non-white pixels = the rounded tile within the cell."""
    minx, miny, maxx, maxy, found = w, h, 0, 0, False
    for y in range(0, h, 2):
        for x in range(0, w, 2):
            if not _close(px[x, y], WHITE, 34):
                found = True
                minx, maxx = min(minx, x), max(maxx, x)
                miny, maxy = min(miny, y), max(maxy, y)
    if not found:
        return (0, 0, w, h)
    return (max(0, minx - 2), max(0, miny - 2), min(w, maxx + 3), min(h, maxy + 3))


def _sample_fill(px, w, h):
    """Most common colour in a frame ring just inside the tile edges."""
    cnt = Counter()
    for fr in (0.06, 0.1, 0.14):
        yt, yb = int(h * fr), int(h * (1 - fr))
        for x in range(int(w * 0.06), int(w * 0.94), 4):
            cnt[px[x, yt][:3]] += 1
            cnt[px[x, yb][:3]] += 1
        xl, xr = int(w * fr), int(w * (1 - fr))
        for y in range(int(h * 0.06), int(h * 0.94), 4):
            cnt[px[xl, y][:3]] += 1
            cnt[px[xr, y][:3]] += 1
    return cnt.most_common(1)[0][0]


def _flood_light(px, w, h, colors, tol):
    """Flood from the border, clearing pixels close to any of `colors`
    (cream / white fill) and passing through already-transparent pixels."""
    targets = [c if len(c) == 4 else c + (255,) for c in colors]
    seen = [[False] * w for _ in range(h)]
    q = deque((x, 0) for x in range(w))
    q.extend((x, h - 1) for x in range(w))
    q.extend((0, y) for y in range(h))
    q.extend((w - 1, y) for y in range(h))
    while q:
        x, y = q.popleft()
        if not (0 <= x < w and 0 <= y < h) or seen[y][x]:
            continue
        seen[y][x] = True
        c = px[x, y]
        if c[3] == 0 or any(_close(c, t, tol) for t in targets):
            px[x, y] = (0, 0, 0, 0)
            q.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])


def _flood_dark(px, w, h, tol, lumcap):
    """Region-grow from the border across the dark fill (and its gradient),
    stopping at brighter pixels so light-coloured animals survive.

    Passes through already-transparent pixels (the stripped white gap) with
    `prev=None`, then adopts the first dark opaque pixel it meets as the new
    frontier colour — so it still reaches the navy fill behind a white border.
    """
    seen = [[False] * w for _ in range(h)]
    q = deque((x, 0, None) for x in range(w))
    q.extend((x, h - 1, None) for x in range(w))
    q.extend((0, y, None) for y in range(h))
    q.extend((w - 1, y, None) for y in range(h))
    while q:
        x, y, prev = q.popleft()
        if not (0 <= x < w and 0 <= y < h) or seen[y][x]:
            continue
        c = px[x, y]
        if c[3] == 0:
            seen[y][x] = True
            nxt = prev
        elif _lum(c) < lumcap and (prev is None or _close(c, prev, tol)):
            seen[y][x] = True
            px[x, y] = (0, 0, 0, 0)
            nxt = c[:3]
        else:
            continue
        q.extend([(x + 1, y, nxt), (x - 1, y, nxt), (x, y + 1, nxt), (x, y - 1, nxt)])


def _keep_central(px, w, h):
    """Drop opaque components that touch the border or are tiny (ring/specks)."""
    seen = [[False] * w for _ in range(h)]
    keep = [[False] * w for _ in range(h)]
    min_area = w * h * 0.012
    for sy in range(h):
        for sx in range(w):
            if seen[sy][sx] or px[sx, sy][3] == 0:
                continue
            comp, touches, stack = [], False, [(sx, sy)]
            seen[sy][sx] = True
            while stack:
                x, y = stack.pop()
                comp.append((x, y))
                if x == 0 or y == 0 or x == w - 1 or y == h - 1:
                    touches = True
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= nx < w and 0 <= ny < h and not seen[ny][nx] and px[nx, ny][3] > 0:
                        seen[ny][nx] = True
                        stack.append((nx, ny))
            if not touches and len(comp) >= min_area:
                for x, y in comp:
                    keep[y][x] = True
    for y in range(h):
        for x in range(w):
            if not keep[y][x]:
                px[x, y] = (0, 0, 0, 0)


def _autocrop(tile, pad):
    bbox = tile.getbbox()
    if not bbox:
        return tile
    l, t, r, b = bbox
    sub = tile.crop((max(0, l - pad), max(0, t - pad),
                     min(tile.width, r + pad), min(tile.height, b + pad)))
    side = max(sub.width, sub.height)
    canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    canvas.paste(sub, ((side - sub.width) // 2, (side - sub.height) // 2), sub)
    return canvas


def _process_tile(cell):
    cell = cell.convert("RGBA")
    px = cell.load()
    w, h = cell.size
    cell = cell.crop(_tile_bbox(px, w, h))   # tight-crop to the tile
    px = cell.load()
    w, h = cell.size

    fill = _sample_fill(px, w, h)
    if _lum(fill) > 150:                      # light (cream) tile
        _flood_light(px, w, h, [fill, WHITE], 30)
    else:                                     # dark (navy) tile
        _flood_light(px, w, h, [WHITE], 30)   # strip the white gap first
        _flood_dark(px, w, h, 14, 120)        # then remove the (uniform) navy fill
    _keep_central(px, w, h)
    return _autocrop(cell, PAD)


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
        box = (int(col * cw + mx), int(row * ch + my),
               int((col + 1) * cw - mx), int((row + 1) * ch - my))
        out_img = _process_tile(img.crop(box))
        out = os.path.join(OUT_DIR, f"{driver}.png")
        out_img.save(out)
        print(f"  ✓ {driver:13s} {out_img.size}  ->  {os.path.relpath(out, HERE)}")

    print("Done. Re-run generate.py (and restart the app) to use the new mascots.")


if __name__ == "__main__":
    main()
