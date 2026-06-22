"""CommBank branding helpers — embeds the official logo as a data URI.

The logo lives in assets/commbank_logo.png and is base64-embedded so the
rendered HTML stays self-contained (works offline, no external requests).
"""
import base64
import os

ASSET_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

# CommBank palette
YELLOW = "#FFCC00"
YELLOW_HI = "#FFD84D"
BLACK = "#0A0A0A"
TEAL = "#0E9C94"


def _logo_path():
    for fn in ("commbank_logo.png", "commbank_logo.svg", "commbank_logo.jpg",
               "commbank_logo.jpeg", "commbank_logo.webp"):
        p = os.path.join(ASSET_DIR, fn)
        if os.path.exists(p):
            return p
    return None


def logo_data_uri():
    """Return a data: URI for the CommBank logo, or None if missing."""
    p = _logo_path()
    if not p:
        return None
    ext = p.rsplit(".", 1)[1].lower()
    mime = {"png": "image/png", "svg": "image/svg+xml", "jpg": "image/jpeg",
            "jpeg": "image/jpeg", "webp": "image/webp"}.get(ext, "image/png")
    with open(p, "rb") as fh:
        b64 = base64.b64encode(fh.read()).decode("ascii")
    return f"data:{mime};base64,{b64}"


def logo_img(size=24):
    """Return an <img> tag for the embedded logo (falls back to a yellow gem)."""
    uri = logo_data_uri()
    if uri:
        return (f'<img src="{uri}" width="{size}" height="{size}" alt="CommBank" '
                f'style="display:block;object-fit:contain" />')
    # Fallback diamond if the asset is ever missing.
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 100 100">'
            f'<polygon points="50,5 95,50 50,95 5,50" fill="{YELLOW}"/></svg>')
