import datetime

month = datetime.datetime.now().month

# TODO: Refactor into separate functions
# TODO: Add documentation (docstrings)
# TODO: Replace hardcoded values with config data
# TODO: Add error handling and validation

# Hardcoded if-elif chain for months
if month == 1:
    print("January: Plant bare-root trees and shrubs. Prune dormant trees. Plan your spring garden.")
elif month == 2:
    print("February: Prune roses and fruit trees. Start seeds indoors. Prepare soil for spring planting.")
elif month == 3:
    print("March: Plant cool-season vegetables like lettuce and peas. Divide perennials. Apply compost.")
elif month == 4:
    print("April: Plant warm-season vegetables. Start annual flowers. Mulch garden beds.")
elif month == 5:
    print("May: Plant summer vegetables and flowers. Water regularly as temperatures rise. Stake tall plants.")
elif month == 6:
    print("June: Harvest early vegetables. Deadhead flowers. Monitor for pests and diseases.")
elif month == 7:
    print("July: Water deeply during hot weather. Harvest vegetables regularly. Provide shade for sensitive plants.")
elif month == 8:
    print("August: Continue harvesting. Plant fall vegetables. Prepare for autumn planting.")
elif month == 9:
    print("September: Plant fall crops and bulbs. Divide perennials. Reduce watering as weather cools.")
elif month == 10:
    print("October: Harvest remaining vegetables. Plant trees and shrubs. Clean up garden beds.")
elif month == 11:
    print("November: Protect tender plants from frost. Plant spring bulbs. Mulch for winter protection.")
elif month == 12:
    print("December: Plan next year's garden. Prune dormant trees. Maintain winter protection.")

# Hardcoded season advice
if month in [12, 1, 2]:
    print("Winter: Focus on planning, pruning dormant plants, and protecting tender plants from frost.")
elif month in [3, 4, 5]:
    print("Spring: Time for planting, soil preparation, and starting seeds. Watch for late frosts.")
elif month in [6, 7, 8]:
    print("Summer: Maintain watering schedules, harvest regularly, and provide shade for heat-sensitive plants.")
elif month in [9, 10, 11]:
    print("Autumn: Harvest crops, plant bulbs and trees, and prepare garden for winter.")

# Hemisphere support (hardcoded to Northern - TODO: make configurable)
hemisphere = "Northern"
if hemisphere == "Northern":
    if month in [12, 1, 2]:
        season = "Winter"
    elif month in [3, 4, 5]:
        season = "Spring"
    elif month in [6, 7, 8]:
        season = "Summer"
    else:
        season = "Autumn"
else:  # Southern hemisphere
    if month in [12, 1, 2]:
        season = "Summer"
    elif month in [3, 4, 5]:
        season = "Autumn"
    elif month in [6, 7, 8]:
        season = "Winter"
    else:
        season = "Spring"

print(f"Current season ({hemisphere} hemisphere): {season}")
