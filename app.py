"""
CommBank · Money Spirit Wrap — Streamlit app.

A Spotify-Wrapped-style, year-end story that turns a customer's financial
behaviour into a celebratory "Money Spirit" identity, rendered inside a
CommBank retail-app phone mockup (status bar, app header, story, bottom tab
bar) — consistent with the CommBiz "Business Spirit Wrap" layout.

Run locally:   streamlit run app.py
Deploy:        Streamlit Community Cloud (point it at app.py)

Synthetic demo data only — no real customer information, no balances or
transaction values are ever shown (privacy by design).
"""
import streamlit as st
import streamlit.components.v1 as components

from branding import logo_data_uri
from engine import compute_wrap
from mock_data import SAMPLE_CUSTOMERS, generate_transactions
from phone_ui import render_story
from share_card import render_share_card

st.set_page_config(
    page_title="CommBank · Money Spirit Wrap",
    page_icon="✨",
    layout="centered",
)

st.markdown(
    """
    <style>
      html { scrollbar-gutter: stable both-edges; }
      .stApp { background: radial-gradient(900px 600px at 50% -5%, #1c1c1c 0%, #0a0a0a 55%); }
      .block-container { padding-top: 2.6rem; padding-bottom: 1.4rem; max-width: 560px; }
      header[data-testid="stHeader"] { background: rgba(0,0,0,0); }
      [data-testid="stSidebar"] { background:#141414; }
      .msw-h { text-align:center; color:#FFCC00; font-weight:800; font-size:1.45rem;
        letter-spacing:.4px; margin-bottom:.1rem; }
      .msw-sub { text-align:center; color:#B9B9B9; margin-top:0; font-size:.95rem; }
      div.stButton > button, .stDownloadButton > button { background:#FFCC00; color:#000;
        border:none; border-radius:999px; font-weight:700; }
      div.stButton > button:hover, .stDownloadButton > button:hover { background:#FFD740; color:#000; }
    </style>
    """,
    unsafe_allow_html=True,
)

YEAR = 2026


def _share_download(persona, logo_uri):
    """Full standalone HTML document for the downloadable share card."""
    logo_tag = f"<img src='{logo_uri}' width='20' style='border-radius:5px'/>" if logo_uri else ""
    card = render_share_card(persona, year=YEAR, logo_html=logo_tag, standalone=True)
    return (
        "<!DOCTYPE html><html><head><meta charset='utf-8'/>"
        f"<title>My Money Spirit · {persona['name']}</title>"
        "<style>body{margin:0;font-family:-apple-system,'Segoe UI',Roboto,sans-serif}</style>"
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
logo = logo_data_uri()

# ---- sidebar: demo controls ----------------------------------------------
with st.sidebar:
    if logo:
        st.markdown(
            f"<div style='display:flex;align-items:center;gap:10px;margin-bottom:6px'>"
            f"<img src='{logo}' width='30' style='border-radius:7px'/>"
            f"<span style='font-weight:800;font-size:1.05rem;color:#fff'>Money Spirit Wrap</span></div>",
            unsafe_allow_html=True,
        )
    st.caption(f"CommBank app feature · {YEAR} · synthetic demo data only")
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
st.markdown("<div class='msw-h'>CommBank · Money Spirit Wrap</div>", unsafe_allow_html=True)
st.markdown(
    f"<p class='msw-sub'>{selected['name']} → <b style='color:#fff'>{persona['name']}</b> · "
    f"{persona['title']} · {wrap['driver_label']} driver</p>",
    unsafe_allow_html=True,
)

# ---- the phone (single, centered) ----------------------------------------
components.html(render_story(wrap, full_document=True), height=900, scrolling=False)

# ---- download the social share card --------------------------------------
st.download_button(
    "⬇ Download social share card",
    data=_share_download(persona, logo),
    file_name=f"money_spirit_{persona['driver']}_{YEAR}.html",
    mime="text/html",
    use_container_width=True,
)
