# Money Spirit · powered by Bankwest

A Spotify-Wrapped-style, year-end story experience for **Bankwest** retail
banking customers. It turns a customer's financial activity into a positive,
personalised identity — their **Money Spirit** — across a sequence of animated,
swipeable story cards styled as a premium Bankwest app feature, finishing with
an Instagram-ready social share card.

Built with **Streamlit** so it can be deployed and shared with a single URL.

> Prototype. Uses synthetic mock data — no real customer information. No
> balances or transaction values are ever shown (privacy by design).

---

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open http://localhost:8501. Use the **sidebar** to preview any of the 8
demo customers; the phone plays their full story (tap the right side of the
phone or use ← / → keys), and the **social share card** renders beside it with
a download button.

## Deploy (Streamlit Community Cloud)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy?repository=sur-akash/bankwest-money-spirit&branch=main&mainModule=app.py)

The app needs **only Streamlit** at runtime — all assets (logo + mascot tiles)
are committed, so the build is fast and dependency-light.

1. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with
   GitHub (authorise access to this repo — private repos are supported on the
   free tier).
2. **Create app → Deploy a public app from GitHub**, then set:
   - Repository: `sur-akash/bankwest-money-spirit`
   - Branch: `main`
   - Main file path: `app.py`
3. (Optional) **Advanced settings → Python 3.12.**
4. **Deploy.** You'll get a public `https://<name>.streamlit.app` URL.

Community Cloud apps are **publicly viewable by default**, so the deployed app
is shareable even though the repo stays private. No secrets/env vars are
required.

---

## The experience (9 screens, per the product spec)

1. **Welcome** — animated orange particles, "Your 2026 Money Spirit is ready"
2. **Driver** — dominant behavioural theme (e.g. Travel)
3. **Peak** — most notable month, on a 12-month timeline
4. **Shine in the Crowd** — percentile badge (e.g. "Top 12%")
5. **Individually Rewarding** — a positive personal outcome
6. **Community Impact** — positive external contribution
7. **Money Spirit Reveal** — the emotional climax, with confetti
8. **Social Share Card** — the Instagram-ready share card
9. **Next-Year Action Plan** — helpful, non-salesy guidance

### The 8 Money Spirits

Each has a custom mascot drawn around its **spending behaviour** — props make
the behaviour legible at a glance:

| Spirit | Driver | Signature props |
|--------|--------|-----------------|
| Travel Kangaroo | Travel | sunglasses, boarding pass, backpack |
| Lifestyle Quokka | Lifestyle | phone (selfie) + coffee |
| Foodie Koala | Food | burger |
| Cinephile Possum | Entertainment | 3D glasses + popcorn |
| Fitness Emu | Fitness | sweatband + dumbbell |
| Saver Echidna | Saving | piggy bank + coin |
| Techie Platypus | Technology | laptop |
| Giver Kookaburra | Giving | gift box |

### The social share card

A light, feed-ready card with a black "Here's my 2026 Money Spirit" headline,
the mascot inside a soft orange gradient circle orbited by hand-drawn amber
doodle icons, the persona name, a "Big on …" descriptor, an orange Bankwest
CTA and the Bankwest logo. No balances, no transaction values.

---

## How it works

| File | Responsibility |
|------|----------------|
| `app.py` | Streamlit entry — sidebar picker, renders the phone + share card |
| `phone_ui.py` | Builds the 9-screen phone story (HTML/CSS/JS) for one customer |
| `share_card.py` | The Instagram-style social share card + doodle icons |
| `mascots.py` | The 8 behaviour-based mascot SVGs |
| `personas.py` | Persona library, copy, share descriptors, doodle sets |
| `engine.py` | Scores the 5 Wrap dimensions and resolves one persona |
| `mock_data.py` | Synthesises a year of transactions per demo customer |
| `branding.py` | Embeds the Bankwest logos as data URIs + light-theme palette/font |
| `generate.py` | Static export — writes self-contained HTML files (offline/share) |
| `assets/bankwest_logo.png` | Bankwest mark (orange "W" tile), shown in a circular frame |
| `assets/bankwest-logo-full.png` | Full Bankwest lockup, used on the social share card |

**Driver scoring** blends spend volume (60%) and frequency (40%) so a few
big-ticket purchases don't outweigh a consistent everyday habit. **Peak** is
the strongest month within the dominant driver. **Shine** maps relative driver
strength to a banded percentile (never a precise figure).

To plug in real data, replace `mock_data.generate_transactions()` with a feed
of `{month, category, driver, amount}` records (categories map to drivers via
`personas.CATEGORY_TO_DRIVER`). The engine, UI and share card need no changes.

### Static export (optional)

```bash
python3 generate.py          # writes money_spirit_<customer>.html (self-contained)
```

These single-file exports work fully offline and are handy for sharing a
specific customer's story without running the app.

---

## Design principles

- **Bankwest brand:** circular Bankwest logo + signature orange (`#FF961F`) on a
  light theme, with charcoal (`#26262B`) text, a green (`#43B02A`) app-icon accent
  (à la the Bankwest mobile app) and a Bankwest-style geometric sans (Poppins) —
  in line with Bankwest's "just enough bank" digital-first design language.
- **Emotion over analytics:** identity, storytelling and celebration — never a
  financial report. Copy is always positive; no guilt or judgement.
- **Mobile-first:** renders inside a phone frame, and goes edge-to-edge
  fullscreen on an actual phone.
- **Privacy by design:** no balances, no amounts, no precise figures — only
  themes, a month, a percentile band and positive copy.
