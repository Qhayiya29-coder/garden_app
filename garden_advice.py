"""
Simple gardening advice helper.

Asks for a month and prints a basic task suggestion. The data is tiny
on purpose so it's easy to extend during the Git workflow exercises.
"""

# TODO: Turn the ad-hoc logic into small functions so it's easier to test.
# TODO: Replace these hardcoded tasks with constants or a config structure.
# TODO: Add clearer inline comments or a README section describing how to use this script.

SEASON_TASKS = {
    "spring": "Start seeds indoors, prep beds, and feed the soil with compost.",
    "summer": "Keep up with watering, mulch to retain moisture, and watch for pests.",
    "autumn": "Plant cover crops, divide perennials, and gather leaves for mulch.",
    "winter": "Plan next year's garden, prune dormant shrubs, and clean your tools.",
}

MONTH_TO_SEASON = {
    "december": "winter",
    "january": "winter",
    "february": "winter",
    "march": "spring",
    "april": "spring",
    "may": "spring",
    "june": "summer",
    "july": "summer",
    "august": "summer",
    "september": "autumn",
    "october": "autumn",
    "november": "autumn",
}


def get_season(month: str) -> str:
    """Return season name for a month string; defaults to 'summer' for unknown."""
    cleaned = month.strip().lower()
    return MONTH_TO_SEASON.get(cleaned, "summer")


def main() -> None:
    user_month = input("Which month is it? ").strip()
    season = get_season(user_month)
    advice = SEASON_TASKS.get(season, "Keep an eye on your plants today.")

    print(f"\nSeason detected: {season.title()}")
    print(f"Tip: {advice}")


if __name__ == "__main__":
    main()
