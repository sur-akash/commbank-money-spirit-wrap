"""
Money Spirit — powered by Bankwest — Streamlit app.

A Spotify-Wrapped-style, year-end story that turns a customer's financial
behaviour into a celebratory "Money Spirit" identity, rendered inside a
Bankwest retail-app phone mockup (status bar, app header, story, bottom tab
bar) — styled to Bankwest's "just enough bank" design language.

Run locally:   streamlit run app.py
Deploy:        Streamlit Community Cloud (point it at app.py)

Synthetic demo data only — no real customer information, no balances or
transaction values are ever shown (privacy by design).
"""
import streamlit as st
import streamlit.components.v1 as components

from branding import FONT_IMPORT, FONT_STACK, INK, MUTED, logo_img
from engine import compute_wrap
from mock_data import SAMPLE_CUSTOMERS, generate_transactions
from phone_ui import render_story
from share_card import render_share_card

st.set_page_config(
    page_title="Money Spirit · Bankwest",
    page_icon="✨",
    layout="centered",
)

st.markdown(
    f"""
    <style>
      {FONT_IMPORT}
      html {{ scrollbar-gutter: stable both-edges; }}
      html, body, [class*="css"], .stApp, [data-testid="stSidebar"] {{ font-family:{FONT_STACK}; }}
      .stApp {{ background: radial-gradient(1000px 640px at 50% -8%, #FFF6EA 0%, #FFFFFF 55%); }}
      .block-container {{ padding-top: 2.4rem; padding-bottom: 1.4rem; max-width: 560px; }}
      header[data-testid="stHeader"] {{ background: rgba(0,0,0,0); }}
      [data-testid="stSidebar"] {{ background:#FFFBF4; border-right:1px solid #F0E7D9; }}
      .msw-h {{ text-align:center; color:{INK}; font-weight:800; font-size:1.5rem;
        letter-spacing:-.2px; margin-bottom:.1rem; }}
      .msw-sub {{ text-align:center; color:{MUTED}; margin-top:0; font-size:.95rem; }}
      div.stButton > button, .stDownloadButton > button {{ background:{INK}; color:#fff;
        border:none; border-radius:999px; font-weight:700;
        box-shadow:0 8px 20px rgba(0,0,0,.20); }}
      div.stButton > button:hover, .stDownloadButton > button:hover {{ background:#000; color:#fff; }}
    </style>
    """,
    unsafe_allow_html=True,
)

YEAR = 2026


def _share_download(persona):
    """Full standalone HTML document for the downloadable share card."""
    from branding import FONT_LINK, FONT_STACK
    card = render_share_card(persona, year=YEAR, standalone=True)
    return (
        "<!DOCTYPE html><html><head><meta charset='utf-8'/>"
        f"<title>My Money Spirit · {persona['name']}</title>{FONT_LINK}"
        f"<style>body{{margin:0;font-family:{FONT_STACK}}}</style>"
        f"</head><body>{card}</body></html>"
    )


@st.cache_data(show_spinner=False)
def all_wraps():
    out = {}
    for key, prof in SAMPLE_CUSTOMERS.items():
        wrap = compute_wrap(generate_transactions(key), year=YEAR)
        wrap["customer_name"] = prof["name"]
        out[key] = {"name": prof["name"], "wrap": wrap}
    return out


wraps = all_wraps()

# ---- sidebar: demo controls ----------------------------------------------
with st.sidebar:
    st.markdown(
        f"<div style='display:flex;align-items:center;gap:10px;margin-bottom:6px'>"
        f"{logo_img(32)}"
        f"<span style='font-weight:800;font-size:1.05rem;color:{INK}'>Money Spirit</span></div>",
        unsafe_allow_html=True,
    )
    st.caption(f"Bankwest app feature · {YEAR} · synthetic demo data only")
    st.divider()

    labels = {k: f"{v['name']} · {v['wrap']['persona']['name']}" for k, v in wraps.items()}
    choice = st.selectbox("Preview a customer", list(labels.keys()), format_func=lambda k: labels[k])

    st.caption(
        "Tap the right side of the phone (or **Next ›** / → key) to move through "
        "the story. Each Money Spirit is computed from a year of synthetic "
        "transactions."
    )
    st.divider()
    st.markdown("**Guardrails**")
    st.caption(
        "Positive-only framing · no balances or dollar values shown · "
        "percentile bands not precise figures · owner-shared only."
    )

selected = wraps[choice]
wrap = selected["wrap"]
persona = wrap["persona"]

# ---- header --------------------------------------------------------------
st.markdown(
    f"<div style='display:flex;justify-content:center;margin-bottom:.5rem'>{logo_img(46)}</div>",
    unsafe_allow_html=True,
)
st.markdown("<div class='msw-h'>Money Spirit</div>", unsafe_allow_html=True)
st.markdown(
    f"<p style='text-align:center;color:{INK};margin:0 0 .35rem;font-size:.8rem;"
    "font-weight:700;letter-spacing:.16em;text-transform:uppercase'>powered by Bankwest</p>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<p class='msw-sub'>{selected['name']} → <b style='color:{INK}'>{persona['name']}</b> · "
    f"{persona['title']} · {wrap['driver_label']} driver</p>",
    unsafe_allow_html=True,
)

# ---- the phone (single, centered) ----------------------------------------
components.html(render_story(wrap, full_document=True), height=930, scrolling=False)

# ---- download the social share card --------------------------------------
st.download_button(
    "⬇ Download social share card",
    data=_share_download(persona),
    file_name=f"money_spirit_{persona['driver']}_{YEAR}.html",
    mime="text/html",
    use_container_width=True,
)
