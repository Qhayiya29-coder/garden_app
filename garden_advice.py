"""Garden Advice Application"""
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
    """Get current month (1-12)"""
    return datetime.datetime.now().month


def get_season(month, hemisphere="Northern"):
    """Determine season from month and hemisphere"""
    if hemisphere == "Northern":
        season_map = NORTHERN_SEASONS
    else:
        season_map = SOUTHERN_SEASONS
    
    for season, months in season_map.items():
        if month in months:
            return season
    return "Unknown"


def get_month_advice(month):
    """Get advice for specific month"""
    month_name = MONTH_NAMES.get(month, "Unknown")
    advice = MONTH_ADVICE.get(month, "No advice available for this month.")
    return f"{month_name}: {advice}"


def get_season_advice(season):
    """Get advice for specific season"""
    return SEASON_ADVICE.get(season, "No advice available for this season.")


def display_advice(month, hemisphere="Northern"):
    """Display formatted gardening advice"""
    month_advice = get_month_advice(month)
    season = get_season(month, hemisphere)
    season_advice = get_season_advice(season)
    
    print(month_advice)
    print(f"{season}: {season_advice}")
    print(f"Current season ({hemisphere} hemisphere): {season}")


def main():
    """Main function to run the garden advice application"""
    month = get_current_month()
    display_advice(month)


if __name__ == "__main__":
    main()
