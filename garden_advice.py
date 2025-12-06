"""Garden Advice Application

This application provides month-specific and season-specific gardening advice
based on the current date and supports both Northern and Southern hemispheres.
"""

import datetime


# Configuration dictionaries
MONTH_NAMES = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

MONTH_ADVICE = {
    1: "Plant bare-root trees and shrubs. Prune dormant trees. Plan your spring garden.",
    2: "Prune roses and fruit trees. Start seeds indoors. Prepare soil for spring planting.",
    3: "Plant cool-season vegetables like lettuce and peas. Divide perennials. Apply compost.",
    4: "Plant warm-season vegetables. Start annual flowers. Mulch garden beds.",
    5: "Plant summer vegetables and flowers. Water regularly as temperatures rise. Stake tall plants.",
    6: "Harvest early vegetables. Deadhead flowers. Monitor for pests and diseases.",
    7: "Water deeply during hot weather. Harvest vegetables regularly. Provide shade for sensitive plants.",
    8: "Continue harvesting. Plant fall vegetables. Prepare for autumn planting.",
    9: "Plant fall crops and bulbs. Divide perennials. Reduce watering as weather cools.",
    10: "Harvest remaining vegetables. Plant trees and shrubs. Clean up garden beds.",
    11: "Protect tender plants from frost. Plant spring bulbs. Mulch for winter protection.",
    12: "Plan next year's garden. Prune dormant trees. Maintain winter protection."
}

SEASON_ADVICE = {
    "Winter": "Focus on planning, pruning dormant plants, and protecting tender plants from frost.",
    "Spring": "Time for planting, soil preparation, and starting seeds. Watch for late frosts.",
    "Summer": "Maintain watering schedules, harvest regularly, and provide shade for heat-sensitive plants.",
    "Autumn": "Harvest crops, plant bulbs and trees, and prepare garden for winter."
}

NORTHERN_SEASONS = {
    "Winter": [12, 1, 2],
    "Spring": [3, 4, 5],
    "Summer": [6, 7, 8],
    "Autumn": [9, 10, 11]
}

SOUTHERN_SEASONS = {
    "Summer": [12, 1, 2],
    "Autumn": [3, 4, 5],
    "Winter": [6, 7, 8],
    "Spring": [9, 10, 11]
}


def get_current_month():
    """Get the current month from the system date.
    
    Returns:
        int: Current month as an integer (1-12)
    
    Example:
        >>> month = get_current_month()
        >>> print(month)
        12
    """
    try:
        return datetime.datetime.now().month
    except Exception as e:
        raise RuntimeError(f"Failed to get current month: {e}")


def validate_month(month):
    """Validate that month is within valid range.
    
    Args:
        month (int): Month to validate
        
    Raises:
        ValueError: If month is not between 1 and 12
        
    Example:
        >>> validate_month(6)
        >>> validate_month(13)
        Traceback (most recent call last):
        ...
        ValueError: Month must be between 1 and 12
    """
    if not isinstance(month, int):
        raise TypeError(f"Month must be an integer, got {type(month).__name__}")
    if not 1 <= month <= 12:
        raise ValueError(f"Month must be between 1 and 12, got {month}")


def validate_hemisphere(hemisphere):
    """Validate that hemisphere is either 'Northern' or 'Southern'.
    
    Args:
        hemisphere (str): Hemisphere to validate
        
    Raises:
        ValueError: If hemisphere is not 'Northern' or 'Southern'
        
    Example:
        >>> validate_hemisphere("Northern")
        >>> validate_hemisphere("Eastern")
        Traceback (most recent call last):
        ...
        ValueError: Hemisphere must be 'Northern' or 'Southern'
    """
    if not isinstance(hemisphere, str):
        raise TypeError(f"Hemisphere must be a string, got {type(hemisphere).__name__}")
    if hemisphere not in ["Northern", "Southern"]:
        raise ValueError(f"Hemisphere must be 'Northern' or 'Southern', got '{hemisphere}'")


def get_season(month, hemisphere="Northern"):
    """Determine the season based on month and hemisphere.
    
    Args:
        month (int): Month number (1-12)
        hemisphere (str, optional): Hemisphere, either 'Northern' or 'Southern'.
                                   Defaults to 'Northern'.
    
    Returns:
        str: Season name ('Winter', 'Spring', 'Summer', or 'Autumn')
    
    Raises:
        ValueError: If month is not between 1 and 12
        ValueError: If hemisphere is not 'Northern' or 'Southern'
    
    Example:
        >>> get_season(1, "Northern")
        'Winter'
        >>> get_season(1, "Southern")
        'Summer'
    """
    validate_month(month)
    validate_hemisphere(hemisphere)
    
    # Select appropriate season mapping based on hemisphere
    if hemisphere == "Northern":
        season_map = NORTHERN_SEASONS
    else:
        season_map = SOUTHERN_SEASONS
    
    # Find season that contains the given month
    for season, months in season_map.items():
        if month in months:
            return season
    
    # This should never happen if validation passes, but included for safety
    return "Unknown"


def get_month_advice(month):
    """Get gardening advice for a specific month.
    
    Args:
        month (int): Month number (1-12)
    
    Returns:
        str: Formatted advice string with month name and advice
    
    Raises:
        ValueError: If month is not between 1 and 12
    
    Example:
        >>> advice = get_month_advice(3)
        >>> print(advice)
        March: Plant cool-season vegetables like lettuce and peas...
    """
    validate_month(month)
    
    month_name = MONTH_NAMES.get(month, "Unknown")
    advice = MONTH_ADVICE.get(month, "No advice available for this month.")
    return f"{month_name}: {advice}"


def get_season_advice(season):
    """Get gardening advice for a specific season.
    
    Args:
        season (str): Season name ('Winter', 'Spring', 'Summer', or 'Autumn')
    
    Returns:
        str: Advice string for the given season
    
    Example:
        >>> advice = get_season_advice("Spring")
        >>> print(advice)
        Time for planting, soil preparation, and starting seeds...
    """
    return SEASON_ADVICE.get(season, "No advice available for this season.")


def display_advice(month=None, hemisphere="Northern"):
    """Display formatted gardening advice for the given month and hemisphere.
    
    Args:
        month (int, optional): Month number (1-12). If None, uses current month.
                              Defaults to None.
        hemisphere (str, optional): Hemisphere, either 'Northern' or 'Southern'.
                                   Defaults to 'Northern'.
    
    Raises:
        ValueError: If month is not between 1 and 12
        ValueError: If hemisphere is not 'Northern' or 'Southern'
        RuntimeError: If unable to get current month
    
    Example:
        >>> display_advice(6, "Northern")
        June: Harvest early vegetables...
        Summer: Maintain watering schedules...
        Current season (Northern hemisphere): Summer
    """
    try:
        # Use current month if not provided
        if month is None:
            month = get_current_month()
        
        # Validate inputs
        validate_month(month)
        validate_hemisphere(hemisphere)
        
        # Get advice
        month_advice = get_month_advice(month)
        season = get_season(month, hemisphere)
        season_advice = get_season_advice(season)
        
        # Format output with borders and emojis for better readability
        print("=" * 60)
        print("🌱 GARDENING ADVICE 🌱")
        print("=" * 60)
        print(f"\n📅 {month_advice}")
        print(f"\n🍂 {season}: {season_advice}")
        print(f"\n🌍 Current season ({hemisphere} hemisphere): {season}")
        print("=" * 60)
        
    except (ValueError, TypeError) as e:
        print(f"❌ Error: {e}")
    except RuntimeError as e:
        print(f"❌ Runtime Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


def main():
    """Main function to run the garden advice application.
    
    This function gets the current month and displays gardening advice
    for the Northern hemisphere by default.
    
    Example:
        >>> main()
        ============================================================
        🌱 GARDENING ADVICE 🌱
        ============================================================
        ...
    """
    try:
        month = get_current_month()
        display_advice(month)
    except Exception as e:
        print(f"❌ Failed to run application: {e}")


if __name__ == "__main__":
    main()
