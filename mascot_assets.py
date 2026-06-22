"""
Mascot artwork loader.

Prefers a cropped, background-removed PNG in assets/mascots/<driver>.png
(produced by build_mascots.py from the supplied illustration grid). Falls
back to the built-in flat-vector SVG (mascots.py) when no PNG is present, so
the app always renders something.

Each mascot is embedded as a base64 data URI to keep the output
self-contained (works offline, no external requests).
"""
import base64
import os

ASSET_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "mascots")


def has_png(driver):
    return os.path.exists(os.path.join(ASSET_DIR, f"{driver}.png"))


def mascot_html(driver, svg_fallback, *, flip=False):
    """Return an <img> tag for the cropped PNG, or the SVG fallback.

    `flip=True` mirrors the artwork horizontally (used to vary orientation
    across pages while keeping the same icon).
    """
    p = os.path.join(ASSET_DIR, f"{driver}.png")
    if os.path.exists(p):
        with open(p, "rb") as fh:
            b64 = base64.b64encode(fh.read()).decode("ascii")
        style = "transform:scaleX(-1);" if flip else ""
        return (f'<img src="data:image/png;base64,{b64}" alt="{driver}" '
                f'style="{style}" />')
    return svg_fallback
