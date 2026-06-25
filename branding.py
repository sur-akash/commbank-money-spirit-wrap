"""Bankwest branding helpers — embeds the official logos as data URIs.

The mark (assets/bankwest_logo.png) is the orange "W" tile; it is rendered
inside a circular frame to match Bankwest's circular logo lockup. The full
lockup (assets/bankwest-logo-full.png) is used on the social share card.

Everything is base64-embedded so the rendered HTML stays self-contained
(works offline, no external requests).
"""
import base64
import os

ASSET_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

# ---------------------------------------------------------------------------
# Bankwest palette (sampled from the official logo + mobile-app branding)
# ---------------------------------------------------------------------------
ORANGE = "#FF961F"        # primary brand orange
ORANGE_HI = "#FFB259"     # light orange (hovers / highlights)
ORANGE_DK = "#E0780F"     # deep orange (accents / gradients)
GREEN = "#43B02A"         # Bankwest app green (icon accents)
GREEN_DK = "#2E8B1E"      # deep green
INK = "#26262B"           # charcoal (the logo "W" colour) — text/headlines
MUTED = "#6B6B70"         # secondary grey text
CREAM = "#FFF6EA"         # warm light surface
LINE = "#ECECEF"          # hairlines / borders

# Bankwest's brand type is a friendly geometric sans; Poppins is the closest
# freely-hosted match, with a robust system fallback so it still looks right
# offline.
FONT_STACK = ("'Poppins',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,"
              "Helvetica,Arial,sans-serif")
FONT_LINK = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?'
    'family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">'
)
FONT_IMPORT = ("@import url('https://fonts.googleapis.com/css2?"
               "family=Poppins:wght@400;500;600;700;800;900&display=swap');")


def _asset_uri(*filenames):
    """Return a data: URI for the first existing asset, or None."""
    for fn in filenames:
        p = os.path.join(ASSET_DIR, fn)
        if os.path.exists(p):
            ext = fn.rsplit(".", 1)[1].lower()
            mime = {"png": "image/png", "svg": "image/svg+xml", "jpg": "image/jpeg",
                    "jpeg": "image/jpeg", "webp": "image/webp"}.get(ext, "image/png")
            with open(p, "rb") as fh:
                b64 = base64.b64encode(fh.read()).decode("ascii")
            return f"data:{mime};base64,{b64}"
    return None


def logo_data_uri():
    """Return a data: URI for the Bankwest mark (orange 'W' tile)."""
    return _asset_uri("bankwest_logo.png", "bwa_logo.png", "bwa_logo.svg",
                      "bwa_logo.jpg", "bwa_logo.jpeg", "bwa_logo.webp")


def logo_full_data_uri():
    """Return a data: URI for the full Bankwest lockup (mark + wordmark)."""
    return _asset_uri("bankwest-logo-full.png", "bankwest_logo_full.png")


def logo_img(size=24):
    """Return the Bankwest mark enclosed in a circular frame.

    The source tile is square; clipping it to a circle yields Bankwest's
    circular logo lockup (orange disc with the charcoal 'W').
    """
    uri = logo_data_uri()
    if uri:
        return (
            f'<span style="display:inline-flex;width:{size}px;height:{size}px;'
            f'border-radius:50%;overflow:hidden;flex:0 0 auto;'
            f'box-shadow:0 0 0 1px rgba(0,0,0,.10),0 2px 6px rgba(0,0,0,.12)">'
            f'<img src="{uri}" width="{size}" height="{size}" alt="Bankwest" '
            f'style="display:block;width:100%;height:100%;object-fit:cover"/></span>'
        )
    # Fallback orange disc with a diamond if the asset is ever missing.
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 100 100">'
            f'<circle cx="50" cy="50" r="50" fill="{ORANGE}"/>'
            f'<polygon points="50,22 78,50 50,78 22,50" fill="{INK}"/></svg>')


def logo_full_img(height=26):
    """Return an <img> tag for the full Bankwest lockup (used on the share card)."""
    uri = logo_full_data_uri()
    if uri:
        return (f'<img src="{uri}" alt="Bankwest" '
                f'style="height:{height}px;width:auto;display:block;object-fit:contain"/>')
    # Fallback: circular mark + wordmark.
    return (f'<span style="display:inline-flex;align-items:center;gap:8px">'
            f'{logo_img(height)}<span style="font-weight:800;color:{INK};'
            f'font-size:{int(height * 0.7)}px;letter-spacing:.2px">bankwest</span></span>')
