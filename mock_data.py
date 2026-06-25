"""
Mock Bankwest customer transaction data for the Money Spirit prototype.

In production this layer would be replaced by de-identified, aggregated
behavioural signals from the bank's data platform. Here we synthesise a
year of transactions per sample customer so the engine has something real
to score. No real customer data is used.
"""
import random

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

# Each sample customer has a "lean" (their true dominant driver) plus some
# secondary noise, so the engine has to actually discriminate.
SAMPLE_CUSTOMERS = {
    "alex": {
        "name": "Alex",
        "lean": "travel",
        "peak_month": "December",
        "secondary": ["food", "lifestyle"],
    },
    "sam": {
        "name": "Sam",
        "lean": "saving",
        "peak_month": "June",
        "secondary": ["technology", "fitness"],
    },
    "jordan": {
        "name": "Jordan",
        "lean": "food",
        "peak_month": "March",
        "secondary": ["lifestyle", "entertainment"],
    },
    "riley": {
        "name": "Riley",
        "lean": "fitness",
        "peak_month": "September",
        "secondary": ["food", "saving"],
    },
    "morgan": {
        "name": "Morgan",
        "lean": "giving",
        "peak_month": "November",
        "secondary": ["lifestyle", "saving"],
    },
    "taylor": {
        "name": "Taylor",
        "lean": "technology",
        "peak_month": "August",
        "secondary": ["entertainment", "lifestyle"],
    },
    "casey": {
        "name": "Casey",
        "lean": "lifestyle",
        "peak_month": "October",
        "secondary": ["food", "travel"],
    },
    "devon": {
        "name": "Devon",
        "lean": "entertainment",
        "peak_month": "May",
        "secondary": ["technology", "food"],
    },
}

# Representative merchant categories per driver, used to synthesise spend.
DRIVER_CATEGORIES = {
    "travel": ["airlines", "hotels", "transport", "travel_booking", "car_rental"],
    "lifestyle": ["shopping", "fashion", "events", "experiences"],
    "food": ["restaurants", "cafes", "food_delivery"],
    "entertainment": ["cinema", "streaming", "media", "gaming"],
    "fitness": ["gyms", "fitness", "sports", "wellness"],
    "saving": ["savings_transfer", "goal_contribution", "investment"],
    "technology": ["technology", "digital_services", "subscriptions"],
    "giving": ["charity", "community", "fundraising"],
}


def generate_transactions(customer_key, seed=None):
    """Return a list of synthetic transactions for a sample customer.

    Each transaction: {month, category, driver, amount}. Amounts are kept
    internal — the experience never surfaces precise values.
    """
    profile = SAMPLE_CUSTOMERS[customer_key]
    rng = random.Random(seed if seed is not None else customer_key)
    txns = []

    lean = profile["lean"]
    peak = profile["peak_month"]

    for month in MONTHS:
        # Dominant driver: heavy presence, amplified in the peak month.
        base_count = rng.randint(6, 10)
        if month == peak:
            base_count = int(base_count * 2.2)
        for _ in range(base_count):
            cat = rng.choice(DRIVER_CATEGORIES[lean])
            txns.append({
                "month": month,
                "category": cat,
                "driver": lean,
                "amount": round(rng.uniform(25, 650), 2),
            })

        # Secondary drivers: moderate presence.
        for sec in profile["secondary"]:
            for _ in range(rng.randint(2, 5)):
                cat = rng.choice(DRIVER_CATEGORIES[sec])
                txns.append({
                    "month": month,
                    "category": cat,
                    "driver": sec,
                    "amount": round(rng.uniform(15, 300), 2),
                })

        # Background noise across all other drivers.
        for other in DRIVER_CATEGORIES:
            if rng.random() < 0.4:
                cat = rng.choice(DRIVER_CATEGORIES[other])
                txns.append({
                    "month": month,
                    "category": cat,
                    "driver": other,
                    "amount": round(rng.uniform(10, 120), 2),
                })

    rng.shuffle(txns)
    return txns
