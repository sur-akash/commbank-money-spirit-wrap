"""
Instagram-style social share card for the Money Spirit Wrap.

Renders the highly shareable card described in the product spec, in the
**CommBank palette only** (black / white / yellow / golden — no other accent
colours):

  - clean white card (reads well in an Instagram feed/story)
  - black "Here's my <year> Money Spirit" headline
  - the persona mascot inside a soft golden gradient circle, orbited by
    hand-drawn gold doodle icons that hint at the spending behaviour
  - persona name + a "Big on …" descriptor
  - a yellow CommBank call-to-action pill + "Check your Money Wrapped" line
  - CommBank logo, no balances / no transaction values (per guardrails)

The card is always centred. Returns a self-contained HTML fragment (scoped
`igc-` classes) usable both as the in-phone Share screen and as a standalone
downloadable card.
"""
import math

INK = "#141414"          # black
MUTED = "#6B6B70"        # grey text
YELLOW = "#FFCC00"       # CBA yellow
GOLD = "#D9A300"         # golden (doodles / accents)
GOLD_DK = "#B8860B"      # deep golden

# Tiny 24x24 line-icon doodles (stroke-based) scattered around the mascot.
DOODLE_PATHS = {
    "plane": "M2 13l20-7-7 20-3-8-10-5z",
    "cloud": "M6 16a4 4 0 010-8 5 5 0 019-1 3.5 3.5 0 011 7H6z",
    "globe": "M12 3a9 9 0 100 18 9 9 0 000-18zM3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18",
    "pin": "M12 21s7-6 7-11a7 7 0 10-14 0c0 5 7 11 7 11zM12 10a1.5 1.5 0 100-3 1.5 1.5 0 000 3z",
    "sparkle": "M12 3l2 6 6 2-6 2-2 6-2-6-6-2 6-2z",
    "ticket": "M4 7h16v3a2 2 0 000 4v3H4v-3a2 2 0 000-4z M9 7v10",
    "coffee": "M5 9h12v4a4 4 0 01-4 4H9a4 4 0 01-4-4zM17 10h2a2 2 0 010 4h-2M8 4v2M11 4v2",
    "heart": "M12 20s-7-4.6-7-9.5A3.5 3.5 0 0112 7a3.5 3.5 0 017 3.5C19 15.4 12 20 12 20z",
    "chat": "M4 5h16v10H9l-4 4V5z",
    "bag": "M6 8h12l-1 12H7zM9 8a3 3 0 016 0",
    "music": "M9 18V6l10-2v12M9 18a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0zM19 16a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z",
    "fork": "M7 3v7a2 2 0 004 0V3M9 12v9M17 3c-2 0-3 3-3 6s1 4 3 4v8",
    "store": "M4 9l1-5h14l1 5M4 9v11h16V9M4 9h16M9 20v-6h6v6",
    "film": "M4 4h16v16H4zM4 9h16M4 14h16M8 4v16M16 4v16",
    "star": "M12 3l2.6 6.3 6.8.5-5.2 4.4 1.6 6.6L12 17l-5.8 3.3 1.6-6.6L2.6 9.8l6.8-.5z",
    "play": "M5 4l14 8-14 8z",
    "dumbbell": "M3 9v6M6 7v10M18 7v10M21 9v6M6 12h12",
    "bolt": "M13 2L4 14h7l-2 8 9-12h-7z",
    "drop": "M12 3s6 7 6 11a6 6 0 01-12 0c0-4 6-11 6-11z",
    "coin": "M12 3a9 9 0 100 18 9 9 0 000-18zM12 7v10M9.5 9.5h4a1.5 1.5 0 010 3h-3a1.5 1.5 0 000 3h4",
    "piggy": "M16 7a6 6 0 11-8 8v3H6v-3a6 6 0 01-2-3H2v-3h2a6 6 0 016-4h4l3-2v4zM15 10h.01",
    "chart": "M4 20V4M4 20h16M8 16v-5M12 16V8M16 16v-7",
    "shield": "M12 3l8 3v6c0 5-4 8-8 9-4-1-8-4-8-9V6z",
    "chip": "M7 7h10v10H7zM9 9h6v6H9M3 10v4M3 10h2M3 14h2M21 10v4M19 10h2M19 14h2M10 3h4M10 3v2M14 3v2M10 21h4M10 19v2M14 19v2",
    "wifi": "M5 12a10 10 0 0114 0M8 15a6 6 0 018 0M11 18a1.5 1.5 0 012 0",
    "gear": "M12 9a3 3 0 100 6 3 3 0 000-6zM12 2v3M12 19v3M5 5l2 2M17 17l2 2M2 12h3M19 12h3M5 19l2-2M17 7l2-2",
    "gift": "M4 11h16v9H4zM4 11V8h16v3M12 8v12M12 8C9 8 8 4 10 3s3 3 2 5M12 8c3 0 4-4 2-5s-3 3-2 5",
    "hands": "M7 13l3-3 2 2 3-4 3 3v6H7zM5 13v6M19 11v8",
}


def _doodle(name, x, y, size=26, color=GOLD):
    path = DOODLE_PATHS.get(name, DOODLE_PATHS["sparkle"])
    return (
        f'<svg class="igc-doodle" style="left:{x}%;top:{y}%;width:{size}px;height:{size}px" '
        f'viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.7" '
        f'stroke-linecap="round" stroke-linejoin="round"><path d="{path}"/></svg>'
    )


def _doodle_ring(names, color=GOLD):
    """Scatter doodles evenly around the mascot circle."""
    out = []
    n = len(names)
    sizes = [28, 22, 26, 23, 27, 22]
    for i, name in enumerate(names):
        ang = -90 + (360 / n) * i + (12 if i % 2 else -8)
        rad = 47 + (4 if i % 2 else 0)
        x = 50 + rad * math.cos(math.radians(ang))
        y = 50 + rad * math.sin(math.radians(ang))
        out.append(_doodle(name, x - 4, y - 4, sizes[i % len(sizes)], color))
    return "".join(out)


def render_share_card(persona, year=2026, logo_html="", *, standalone=False):
    """Return the Instagram-style share card as an HTML fragment.

    `persona` is a persona dict (from personas.PERSONAS). `logo_html` is the
    embedded CommBank logo (img tag). When `standalone=True` the card includes
    its own outer padding/background for download/preview use.
    """
    name = persona["name"]
    desc = persona.get("share_descriptor", persona.get("theme", ""))
    art = persona["art"]
    doodles = _doodle_ring(persona.get("doodles", ["sparkle"] * 6))

    wrapper_open = '<div class="igc-stage">' if standalone else ""
    wrapper_close = "</div>" if standalone else ""

    return f"""{wrapper_open}
<div class="igc-card">
  <div class="igc-top">
    <div class="igc-logo">{logo_html}<span>CommBank</span></div>
  </div>
  <div class="igc-head">Here's my {year}<br/>Money Spirit</div>

  <div class="igc-orbit">
    <div class="igc-circle">
      <div class="igc-mascot">{art}</div>
    </div>
    {doodles}
  </div>

  <div class="igc-name">{name}</div>
  <div class="igc-desc">{desc}</div>

  <div class="igc-cta">What's YOUR {year} Money spend?</div>
  <div class="igc-foot">Check your Money Wrapped in the app</div>
</div>
{wrapper_close}
<style>
  .igc-stage {{ display:flex; align-items:center; justify-content:center;
    padding:18px; min-height:100%; background:radial-gradient(700px 500px at 50% 0%, #1a1a1a, #000); }}
  .igc-card {{
    width:340px; margin:0 auto; background:#FFFFFF;
    border-radius:30px; padding:30px 26px 26px; text-align:center;
    box-shadow:0 24px 60px rgba(0,0,0,.45); position:relative; overflow:hidden;
    border:1px solid rgba(255,204,0,.35);
    font-family:-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
  }}
  .igc-card::before {{ content:""; position:absolute; left:0; right:0; top:0; height:6px;
    background:linear-gradient(90deg,#FFCC00,#E0AC00); }}
  .igc-card::after {{ content:""; position:absolute; inset:0;
    background:radial-gradient(120% 55% at 50% 118%, rgba(255,204,0,.12), transparent 60%); }}
  .igc-top {{ display:flex; justify-content:center; position:relative; z-index:2; }}
  .igc-logo {{ display:flex; align-items:center; gap:7px; color:{INK};
    font-weight:800; font-size:13px; letter-spacing:.2px; }}
  .igc-logo img {{ width:20px; height:20px; display:block; border-radius:5px; }}
  .igc-head {{ position:relative; z-index:2; color:{INK}; font-weight:800;
    font-size:27px; line-height:1.12; letter-spacing:-.3px; margin:14px 0 6px; }}

  .igc-orbit {{ position:relative; width:230px; height:230px; margin:6px auto 4px; z-index:2; }}
  .igc-circle {{ position:absolute; left:50%; top:50%; transform:translate(-50%,-50%);
    width:160px; height:160px; border-radius:50%;
    background:radial-gradient(circle at 50% 36%, #FFF4CC 0%, #FFE07A 52%, #FFCC00 100%);
    box-shadow:inset 0 0 0 6px rgba(255,255,255,.65), 0 8px 22px rgba(255,204,0,.35);
    display:flex; align-items:center; justify-content:center; }}
  .igc-mascot {{ width:132px; height:132px; display:flex; align-items:center; justify-content:center; }}
  .igc-mascot svg {{ width:100%; height:100%; display:block;
    filter:drop-shadow(0 6px 10px rgba(0,0,0,.18)); }}
  .igc-mascot img {{ width:100%; height:100%; object-fit:contain;
    filter:drop-shadow(0 6px 10px rgba(0,0,0,.2)); }}
  .igc-doodle {{ position:absolute; opacity:.9; }}

  .igc-name {{ position:relative; z-index:2; color:{INK}; font-weight:900;
    font-size:25px; letter-spacing:-.3px; margin-top:6px; }}
  .igc-desc {{ position:relative; z-index:2; color:{MUTED}; font-size:15px; margin-top:5px; }}

  .igc-cta {{ position:relative; z-index:2; margin:20px auto 0; max-width:280px;
    background:{YELLOW}; color:#1a1a1a; font-weight:800; font-size:15px;
    padding:14px 18px; border-radius:999px; box-shadow:0 8px 20px rgba(255,204,0,.4); }}
  .igc-foot {{ position:relative; z-index:2; color:{MUTED}; font-size:13px; margin-top:12px; }}
</style>"""
