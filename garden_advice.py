"""
Garden Advice Application

This application provides gardening advice based on the month/season.
Users can input a month name, and the application will determine the 
corresponding season and provide relevant gardening tips.

Usage:
    Run the script and enter a month when prompted:
    $ python garden_advice.py
    Which month is it? march
    
    Season detected: Spring
    Tip: Start seeds indoors, prep beds, and feed the soil with compost.

The application supports all 12 months and maps them to four seasons:
- Spring: March, April, May
- Summer: June, July, August  
- Autumn: September, October, November
- Winter: December, January, February
"""

# TODO: Replace these hardcoded tasks with constants or a config structure.

# Dictionary mapping seasons to gardening advice
# Each season has specific tasks that are most appropriate for that time of year
SEASON_TASKS = {
    "spring": "Start seeds indoors, prep beds, and feed the soil with compost.",
    "summer": "Keep up with watering, mulch to retain moisture, and watch for pests.",
    "autumn": "Plant cover crops, divide perennials, and gather leaves for mulch.",
    "winter": "Plan next year's garden, prune dormant shrubs, and clean your tools.",
}

# Dictionary mapping month names (lowercase) to their corresponding seasons
# Used to determine which season a given month belongs to
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
    """
    Determine the season for a given month.
    
    Args:
        month (str): The name of the month (case-insensitive, any format)
    
    Returns:
        str: The season name ("spring", "summer", "autumn", or "winter")
             Returns "summer" as default if month is not recognized
    
    Example:
        >>> get_season("March")
        'spring'
        >>> get_season("  JULY  ")
        'summer'
    """
    # Normalize input: remove whitespace and convert to lowercase for matching
    cleaned = month.strip().lower()
    # Look up the season, defaulting to "summer" if month not found
    return MONTH_TO_SEASON.get(cleaned, "summer")


def get_user_input() -> str:
    """
    Prompt the user to enter a month name.
    
    Returns:
        str: The user's input with leading/trailing whitespace removed
    
    Example:
        If user enters "  March  ", returns "March"
    """
    return input("Which month is it? ").strip()


def get_advice(season: str) -> str:
    """
    Retrieve gardening advice for a specific season.
    
    Args:
        season (str): The season name ("spring", "summer", "autumn", or "winter")
    
    Returns:
        str: Gardening advice for the season, or a default message if season not found
    
    Example:
        >>> get_advice("spring")
        'Start seeds indoors, prep beds, and feed the soil with compost.'
    """
    # Look up advice in SEASON_TASKS dictionary, with fallback message
    return SEASON_TASKS.get(season, "Keep an eye on your plants today.")


def display_advice(season: str, advice: str) -> None:
    """
    Display the detected season and corresponding gardening advice to the user.
    
    Args:
        season (str): The season name (will be capitalized for display)
        advice (str): The gardening advice to display
    
    Example:
        >>> display_advice("spring", "Start seeds indoors...")
        (prints formatted output to console)
    """
    # Capitalize season name for better readability (e.g., "spring" -> "Spring")
    print(f"\nSeason detected: {season.title()}")
    print(f"Tip: {advice}")


def main() -> None:
    """
    Main entry point for the garden advice application.
    
    Orchestrates the flow:
    1. Get month input from user
    2. Determine the season for that month
    3. Retrieve appropriate gardening advice
    4. Display the results to the user
    """
    # Step 1: Get user input
    user_month = get_user_input()
    # Step 2: Convert month to season
    season = get_season(user_month)
    # Step 3: Get advice for the season
    advice = get_advice(season)
    # Step 4: Display results
    display_advice(season, advice)


if __name__ == "__main__":
    main()
