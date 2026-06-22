"""
Money Spirit engine.

Turns a year of transactions into the five-dimension Wrap structure:
  1. Driver               - dominant behavioural theme
  2. Peak                 - most notable month
  3. Shine in the Crowd   - relative percentile vs. similar customers
  4. Individually Rewarding - positive personal outcome
  5. Community Impact     - positive external impact

...then resolves a single Money Spirit persona for the reveal.

Privacy-by-design: outputs carry no precise dollar values or balances —
only themes, months, percentile bands and qualitative copy.
"""
from collections import defaultdict

from personas import PERSONAS, DRIVER_COHORT, DRIVER_LABEL


def _driver_totals(transactions):
    """Aggregate spend weight per driver (internal only)."""
    totals = defaultdict(float)
    counts = defaultdict(int)
    for t in transactions:
        totals[t["driver"]] += t["amount"]
        counts[t["driver"]] += 1
    return totals, counts


def _percentile_band(strength):
    """Map a dominant-driver strength (~0.3..0.7) to a friendly 'top X%' band.

    Centred so a typical strong driver (~0.60) lands around the top 12%, with
    a steep enough slope that customers spread across distinct bands. Higher
    strength -> smaller (better) top-percentage. Banded so we never imply
    false precision.
    """
    top = round(12 - (strength - 0.60) * 120)
    top = max(5, min(25, top))
    # Snap to clean marketing bands.
    for band in (5, 8, 10, 12, 15, 20, 25):
        if top <= band:
            return band
    return 25


def compute_wrap(transactions, year=2026):
    """Compute the full Wrap payload for one customer."""
    totals, counts = _driver_totals(transactions)
    if not totals:
        raise ValueError("No transactions to score.")

    # --- 1. Driver -------------------------------------------------------
    # Weight by a blend of spend volume and frequency so a few big-ticket
    # items don't dominate a consistent everyday habit.
    grand_total = sum(totals.values())
    total_count = sum(counts.values())
    blended = {
        d: 0.6 * (totals[d] / grand_total) + 0.4 * (counts[d] / total_count)
        for d in totals
    }
    driver = max(blended, key=blended.get)
    driver_strength = blended[driver]  # 0..1

    # Runner-up drivers for richer secondary copy / share.
    ranked = sorted(blended.items(), key=lambda kv: kv[1], reverse=True)

    # --- 2. Peak ---------------------------------------------------------
    # Most notable month within the dominant driver.
    by_month = defaultdict(float)
    for t in transactions:
        if t["driver"] == driver:
            by_month[t["month"]] += t["amount"]
    peak_month = max(by_month, key=by_month.get) if by_month else "December"

    # --- 3. Shine in the Crowd ------------------------------------------
    # Convert relative strength into a percentile band vs. similar customers.
    band = _percentile_band(driver_strength)

    persona = PERSONAS[driver]
    cohort = DRIVER_COHORT[driver]

    return {
        "year": year,
        "driver": driver,
        "driver_label": DRIVER_LABEL[driver],
        "driver_copy": persona["driver_copy"],
        "peak_month": peak_month,
        "shine_band": band,
        "shine_copy": f"You ranked among the top {band}% of {cohort} this year.",
        "rewarding_copy": persona["rewarding_copy"],
        "community_copy": persona["community_copy"],
        "persona": persona,
        "secondary_drivers": [DRIVER_LABEL[d] for d, _ in ranked[1:3]],
        # Lightweight 12-month shape for the Peak timeline (normalised 0..1,
        # no dollar values exposed).
        "timeline": _monthly_shape(transactions, driver),
    }


def _monthly_shape(transactions, driver):
    from mock_data import MONTHS
    by_month = defaultdict(float)
    for t in transactions:
        if t["driver"] == driver:
            by_month[t["month"]] += t["amount"]
    peak_val = max(by_month.values()) if by_month else 1.0
    return [
        {"month": m[:3], "value": round((by_month.get(m, 0.0) / peak_val), 3)}
        for m in MONTHS
    ]
