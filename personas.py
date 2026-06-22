"""
Money Spirit persona definitions.

Each persona maps a dominant behavioural driver to a celebratory
"Money Spirit" identity. Spending categories feed the engine (engine.py),
which scores drivers and resolves a single persona for the reveal.

Brand anchor: CommBank yellow (#FFCC00) + black, with a per-persona
accent gradient for the story cards.
"""

# ---------------------------------------------------------------------------
# Spend categories -> driver themes
# ---------------------------------------------------------------------------
# Merchant categories observed in transactions are grouped into the eight
# behavioural drivers the experience celebrates.
CATEGORY_TO_DRIVER = {
    # Travel
    "airlines": "travel",
    "hotels": "travel",
    "transport": "travel",
    "travel_booking": "travel",
    "car_rental": "travel",
    # Lifestyle
    "shopping": "lifestyle",
    "fashion": "lifestyle",
    "events": "lifestyle",
    "experiences": "lifestyle",
    # Food
    "restaurants": "food",
    "cafes": "food",
    "food_delivery": "food",
    "groceries_premium": "food",
    # Entertainment
    "cinema": "entertainment",
    "streaming": "entertainment",
    "media": "entertainment",
    "gaming": "entertainment",
    # Fitness
    "gyms": "fitness",
    "fitness": "fitness",
    "sports": "fitness",
    "wellness": "fitness",
    # Saving
    "savings_transfer": "saving",
    "goal_contribution": "saving",
    "investment": "saving",
    # Technology
    "technology": "technology",
    "digital_services": "technology",
    "subscriptions": "technology",
    # Giving
    "charity": "giving",
    "community": "giving",
    "fundraising": "giving",
}

# ---------------------------------------------------------------------------
# Persona library
# ---------------------------------------------------------------------------
# Order matters only for stable tie-breaks. Copy is positive-only and never
# references precise balances or transaction values (per product spec).
PERSONAS = {
    "travel": {
        "driver": "travel",
        "name": "Travel Kangaroo",
        "emoji": "🦘",
        "title": "The Explorer",
        "theme": "Travel & exploration",
        "traits": ["Adventurous", "Curious", "Purposeful"],
        "description": (
            "You spent the year exploring new horizons and embracing "
            "meaningful journeys. You move with purpose, curiosity and "
            "confidence."
        ),
        "tagline": "Exploring with heart, not haste.",
        "driver_copy": (
            "You consistently explored new places this year, making travel "
            "one of the strongest themes in your financial journey."
        ),
        "rewarding_copy": "You maximised rewards and benefits from your travel spending.",
        "community_copy": "Travellers like you help support hospitality and tourism communities across Australia.",
        "action_title": "Make next year's adventures go further",
        "action_copy": "Explore travel rewards, fee-free overseas spending and trip budgeting tools.",
        "accent": "#FF8A3D",
        "accent_2": "#FFC400",
        "gradient": ["#1C2B4A", "#3A4D7A", "#FF8A3D"],
    },
    "lifestyle": {
        "driver": "lifestyle",
        "name": "Lifestyle Quokka",
        "emoji": "🐨",
        "title": "The Joy-Seeker",
        "theme": "Lifestyle & experiences",
        "traits": ["Social", "Balanced", "Spirited"],
        "description": (
            "You know how to enjoy life's moments while keeping things "
            "balanced and intentional."
        ),
        "tagline": "Finding joy in everyday moments.",
        "driver_copy": (
            "You leaned into experiences and the things you love, making "
            "lifestyle a defining theme of your year."
        ),
        "rewarding_copy": "You balanced enjoying the moment with staying intentional about your money.",
        "community_copy": "Customers like you help local retailers, makers and venues thrive.",
        "action_title": "Keep the good times balanced",
        "action_copy": "Set a flexible 'fun' budget and track everyday spending with smart insights.",
        "accent": "#FF5FA2",
        "accent_2": "#FFC400",
        "gradient": ["#3A1340", "#7A2A6B", "#FF5FA2"],
    },
    "food": {
        "driver": "food",
        "name": "Foodie Koala",
        "emoji": "🐨",
        "title": "The Tastemaker",
        "theme": "Food & dining",
        "traits": ["Curious", "Community-minded", "Experiential"],
        "description": (
            "You explored flavours, supported local food communities and "
            "made dining part of your story."
        ),
        "tagline": "Savouring every moment.",
        "driver_copy": (
            "From cafes to restaurants, food and dining became one of the "
            "richest themes of your year."
        ),
        "rewarding_copy": "You turned everyday dining into moments worth savouring.",
        "community_copy": "Your dining choices helped support local restaurants and food businesses.",
        "action_title": "Savour more, spend smarter",
        "action_copy": "Review your dining patterns and discover easy ways to save on the side.",
        "accent": "#FF7A59",
        "accent_2": "#FFC400",
        "gradient": ["#3A2410", "#7A4A22", "#FF7A59"],
    },
    "entertainment": {
        "driver": "entertainment",
        "name": "Cinephile Possum",
        "emoji": "🎬",
        "title": "The Storyteller",
        "theme": "Entertainment & culture",
        "traits": ["Creative", "Curious", "Story-driven"],
        "description": "You found inspiration through stories, culture and entertainment.",
        "tagline": "Living through stories.",
        "driver_copy": (
            "Cinema, streaming and culture lit up your year, making "
            "entertainment a leading theme."
        ),
        "rewarding_copy": "You filled your year with stories, culture and inspiration.",
        "community_copy": "Audiences like you help sustain creators, venues and the arts.",
        "action_title": "Curate your subscriptions",
        "action_copy": "See your recurring streaming and media spend, and trim what you no longer use.",
        "accent": "#9B6BFF",
        "accent_2": "#FFC400",
        "gradient": ["#1A1340", "#3E2A7A", "#9B6BFF"],
    },
    "fitness": {
        "driver": "fitness",
        "name": "Fitness Emu",
        "emoji": "🏃",
        "title": "The Mover",
        "theme": "Health & wellbeing",
        "traits": ["Disciplined", "Energetic", "Growth-minded"],
        "description": (
            "You invested in your wellbeing and built momentum through "
            "healthy habits."
        ),
        "tagline": "Strong strides forward.",
        "driver_copy": (
            "Gyms, sport and wellness shaped your routine, making fitness a "
            "standout theme of your year."
        ),
        "rewarding_copy": "You consistently invested in your wellbeing.",
        "community_copy": "Health-focused customers help sustain local fitness and wellbeing ecosystems.",
        "action_title": "Keep your momentum going",
        "action_copy": "Track recurring health and fitness spending and set a wellbeing goal.",
        "accent": "#34D39A",
        "accent_2": "#FFC400",
        "gradient": ["#0E3326", "#1C7A57", "#34D39A"],
    },
    "saving": {
        "driver": "saving",
        "name": "Saver Echidna",
        "emoji": "🦔",
        "title": "The Planner",
        "theme": "Saving & planning",
        "traits": ["Prepared", "Steady", "Future-focused"],
        "description": (
            "You built security one step at a time and prepared for the "
            "future with patience and consistency."
        ),
        "tagline": "Small actions, lasting impact.",
        "driver_copy": (
            "Steady saving and planning were the quiet superpower behind "
            "your year."
        ),
        "rewarding_copy": "You grew your savings habit steadily throughout the year.",
        "community_copy": "Future-focused customers help build stronger, more resilient communities.",
        "action_title": "Set your next milestone",
        "action_copy": "Create a Savings Goal for next year and let automatic transfers do the work.",
        "accent": "#FFC400",
        "accent_2": "#FFE680",
        "gradient": ["#2E2A0E", "#7A6E1C", "#FFC400"],
    },
    "technology": {
        "driver": "technology",
        "name": "Techie Platypus",
        "emoji": "🦫",
        "title": "The Innovator",
        "theme": "Technology & innovation",
        "traits": ["Curious", "Adaptive", "Forward-thinking"],
        "description": "You embraced innovation and explored the tools shaping tomorrow.",
        "tagline": "Always exploring what's next.",
        "driver_copy": (
            "New tech and digital services defined your year, making "
            "innovation a leading theme."
        ),
        "rewarding_copy": "You stayed ahead of the curve with the tools that work for you.",
        "community_copy": "Early adopters like you help drive innovation across the economy.",
        "action_title": "Master your subscriptions",
        "action_copy": "Get a clear view of digital services and subscriptions in one place.",
        "accent": "#3DD6FF",
        "accent_2": "#FFC400",
        "gradient": ["#0E2A33", "#1C5A7A", "#3DD6FF"],
    },
    "giving": {
        "driver": "giving",
        "name": "Giver Kookaburra",
        "emoji": "🦅",
        "title": "The Changemaker",
        "theme": "Generosity & contribution",
        "traits": ["Compassionate", "Community-minded", "Supportive"],
        "description": (
            "You created impact through generosity and helped support "
            "causes beyond yourself."
        ),
        "tagline": "Sharing positivity wherever you go.",
        "driver_copy": (
            "Generosity and contribution ran through your year, making "
            "giving one of your strongest themes."
        ),
        "rewarding_copy": "You supported causes and communities that mattered to you.",
        "community_copy": "Your generosity contributed to community impact and charitable activity.",
        "action_title": "Give with even more impact",
        "action_copy": "Track your giving and discover causes aligned with what matters to you.",
        "accent": "#5BC8FF",
        "accent_2": "#FFC400",
        "gradient": ["#10283A", "#235A7A", "#5BC8FF"],
    },
}

# Friendly labels for "Shine in the Crowd" cohorts.
DRIVER_COHORT = {
    "travel": "travel-oriented customers",
    "lifestyle": "lifestyle-loving customers",
    "food": "food-loving customers",
    "entertainment": "culture-and-entertainment fans",
    "fitness": "health-focused customers",
    "saving": "savers",
    "technology": "tech-forward customers",
    "giving": "givers",
}

DRIVER_LABEL = {
    "travel": "Travel",
    "lifestyle": "Lifestyle",
    "food": "Food",
    "entertainment": "Entertainment",
    "fitness": "Fitness",
    "saving": "Saving",
    "technology": "Technology",
    "giving": "Giving",
}

# Short "Big on …" descriptor for the Instagram-style social share card.
SHARE_DESCRIPTOR = {
    "travel": "Big on trips, flights and getaways",
    "lifestyle": "Big on experiences, shopping and good times",
    "food": "Big on cafes, dining and food adventures",
    "entertainment": "Big on movies, streaming and culture",
    "fitness": "Big on gyms, sport and wellbeing",
    "saving": "Big on saving, planning and reaching goals",
    "technology": "Big on gadgets, apps and what's next",
    "giving": "Big on giving, causes and community",
}

# Hand-drawn doodle icons that orbit the mascot on the share card. Each is a
# tiny path drawn in a 24x24 box; the renderer scatters them in a ring.
DOODLES = {
    "travel": ["plane", "cloud", "globe", "pin", "sparkle", "ticket"],
    "lifestyle": ["coffee", "heart", "chat", "bag", "music", "sparkle"],
    "food": ["coffee", "fork", "heart", "chat", "store", "sparkle"],
    "entertainment": ["film", "music", "star", "play", "sparkle", "chat"],
    "fitness": ["dumbbell", "heart", "bolt", "drop", "sparkle", "pin"],
    "saving": ["coin", "piggy", "chart", "star", "sparkle", "shield"],
    "technology": ["bolt", "chip", "wifi", "sparkle", "star", "gear"],
    "giving": ["heart", "gift", "hands", "star", "sparkle", "globe"],
}

# Three relevant, non-salesy actionables per persona for the final
# "Next-Year Action Plan" card. Framed as helpful in-app next steps.
ACTIONS = {
    "travel": [
        "Set up a Travel Money goal for your next trip",
        "Explore a Travel card with no international transaction fees",
        "Turn on travel notifications to track holiday spending",
    ],
    "lifestyle": [
        "Create a flexible 'fun money' budget in the app",
        "Use Spend Tracker to see your top lifestyle categories",
        "Set a weekly limit for dining and going out",
    ],
    "food": [
        "Set a monthly cafe & dining budget in the app",
        "Review your food spend in Spend Tracker",
        "Round up purchases into savings as you dine",
    ],
    "entertainment": [
        "See all your streaming subscriptions in one place",
        "Cancel or pause subscriptions you no longer use",
        "Set a monthly entertainment budget",
    ],
    "fitness": [
        "Track recurring gym and fitness payments",
        "Set a wellbeing savings goal",
        "Spot duplicate or unused health subscriptions",
    ],
    "saving": [
        "Set a 2027 Savings Goal with automatic transfers",
        "Turn on Round-ups to grow your savings effortlessly",
        "Earn bonus interest with a GoalSaver account",
    ],
    "technology": [
        "View all your digital subscriptions in one place",
        "Set alerts for free-trial renewals",
        "Start a goal for your next big tech purchase",
    ],
    "giving": [
        "Track your charitable giving in Spend Tracker",
        "Set a monthly giving budget",
        "Round up purchases to donate your spare change",
    ],
}

# Attach the custom flat-vector mascot SVG + share copy to each persona so it
# flows through the engine payload to the UI (reveal, share card, action plan).
from mascots import MASCOTS  # noqa: E402
from mascot_assets import mascot_html  # noqa: E402

for _driver, _persona in PERSONAS.items():
    # Prefer the supplied illustration (assets/mascots/<driver>.png); fall
    # back to the built-in SVG until those assets are generated.
    _persona["art"] = mascot_html(_driver, MASCOTS[_driver])
    _persona["share_descriptor"] = SHARE_DESCRIPTOR[_driver]
    _persona["doodles"] = DOODLES[_driver]
    _persona["actions"] = ACTIONS[_driver]
