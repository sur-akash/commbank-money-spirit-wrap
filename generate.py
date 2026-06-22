"""
Static export for the Money Spirit Wrap.

Writes a self-contained HTML file per demo customer (and a default
money_spirit_wrap.html) using the same renderer as the Streamlit app
(phone_ui.render_story), so the offline export and the deployed app stay
perfectly in sync.

Usage:
    python3 generate.py              # writes money_spirit_wrap.html (+ per-customer)
    python3 generate.py --open       # also opens the default file in your browser
"""
import sys
import webbrowser
from pathlib import Path

from engine import compute_wrap
from mock_data import SAMPLE_CUSTOMERS, generate_transactions
from phone_ui import render_story

HERE = Path(__file__).parent
DEFAULT = HERE / "money_spirit_wrap.html"
YEAR = 2026


def main():
    written = []
    for key, prof in SAMPLE_CUSTOMERS.items():
        wrap = compute_wrap(generate_transactions(key), year=YEAR)
        wrap["customer_name"] = prof["name"]
        html = render_story(wrap, full_document=True)
        out = HERE / f"money_spirit_{key}.html"
        out.write_text(html, encoding="utf-8")
        written.append((key, wrap["persona"]["name"], len(html)))

    # Default file = first customer.
    first_key, first_prof = next(iter(SAMPLE_CUSTOMERS.items()))
    first_wrap = compute_wrap(generate_transactions(first_key), year=YEAR)
    first_wrap["customer_name"] = first_prof["name"]
    DEFAULT.write_text(render_story(first_wrap), encoding="utf-8")

    print(f"✓ Wrote {DEFAULT.name} + {len(written)} per-customer files:")
    for key, name, size in written:
        print(f"   • money_spirit_{key}.html  →  {name}  ({size // 1024} KB)")

    if "--open" in sys.argv:
        webbrowser.open(DEFAULT.as_uri())


if __name__ == "__main__":
    main()
