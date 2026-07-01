# CommBank · Money Spirit Wrap

A Spotify-Wrapped-style, year-end story experience for **CommBank** retail
banking customers. It turns a customer's financial activity into a positive,
personalised identity — their **Money Spirit** — across a sequence of animated,
swipeable story cards styled as a premium CommBank app feature, finishing with
an Instagram-ready social share card.

Built with **Streamlit** so it can be deployed and shared with a single URL.

> Prototype. Uses synthetic mock data — no real customer information. No
> balances or transaction values are ever shown (privacy by design).

---

**Streamlit Link:** https://commbank-money-spirit-wrap.streamlit.app/

---

## The experience (9 screens, per the product spec)

1. **Welcome** — animated gold particles, "Your 2026 Money Spirit is ready"
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

Matches the supplied reference creative: a light, feed-ready card with a teal
"Here's my 2026 Money Spirit" headline, the mascot inside a green→yellow
gradient circle orbited by hand-drawn doodle icons, the persona name, a
"Big on …" descriptor, a yellow CommBank CTA and the CommBank logo. No
balances, no transaction values.

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
| `branding.py` | Embeds the official CommBank logo as a data URI |
| `generate.py` | Static export — writes self-contained HTML files (offline/share) |
| `assets/commbank_logo.png` | Official CommBank logo, embedded everywhere |

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

- **CommBank brand:** official logo + signature yellow (`#FFCC00`) and black,
  per-persona accent gradients, a teal accent on the share card.
- **Emotion over analytics:** identity, storytelling and celebration — never a
  financial report. Copy is always positive; no guilt or judgement.
- **Mobile-first:** renders inside a phone frame, and goes edge-to-edge
  fullscreen on an actual phone.
- **Privacy by design:** no balances, no amounts, no precise figures — only
  themes, a month, a percentile band and positive copy.
