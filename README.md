# 🌱 Garden Advice Application

A Python application that provides month-specific and season-specific gardening advice based on the current date, with support for both Northern and Southern hemispheres.

## Features

- 📅 **Month-specific advice**: Get tailored gardening tips for all 12 months
- 🍂 **Season-specific tips**: Receive advice based on the current season
- 🌍 **Hemisphere support**: Works for both Northern and Southern hemispheres
- ✅ **Error handling**: Comprehensive validation and error handling
- 📚 **Well documented**: Full docstrings and inline comments
- 🎨 **Formatted output**: Beautiful console output with emojis and borders

## Requirements

- Python 3.6 or higher
- Standard library only (no external dependencies)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Qhayiya29-coder/garden_app.git
cd garden_app
```

2. Run the application:
```bash
python garden_advice.py
```

## Usage

### Basic Usage

Simply run the script to get advice for the current month:

```bash
python garden_advice.py
```

### Programmatic Usage

You can also import and use the functions in your own code:

```python
from garden_advice import get_month_advice, get_season, display_advice

# Get advice for a specific month
advice = get_month_advice(6)  # June
print(advice)

# Get season for a month
season = get_season(6, "Northern")  # Returns "Summer"
print(season)

# Display formatted advice
display_advice(month=6, hemisphere="Northern")
```

## Example Output

```
============================================================
🌱 GARDENING ADVICE 🌱
============================================================

📅 June: Harvest early vegetables. Deadhead flowers. Monitor for pests and diseases.

🍂 Summer: Maintain watering schedules, harvest regularly, and provide shade for heat-sensitive plants.

🌍 Current season (Northern hemisphere): Summer
============================================================
```

## Project Structure

```
garden_app/
├── garden_advice.py    # Main application file
├── index.html          # HTML file (untouched)
├── repo.txt            # Repository URL
└── README.md           # This file
```

## Functions

### `get_current_month()`
Returns the current month (1-12) from the system date.

### `get_season(month, hemisphere="Northern")`
Determines the season based on month and hemisphere.

**Parameters:**
- `month` (int): Month number (1-12)
- `hemisphere` (str): "Northern" or "Southern"

**Returns:** Season name (str)

### `get_month_advice(month)`
Returns gardening advice for a specific month.

**Parameters:**
- `month` (int): Month number (1-12)

**Returns:** Formatted advice string

### `get_season_advice(season)`
Returns gardening advice for a specific season.

**Parameters:**
- `season` (str): Season name

**Returns:** Advice string

### `display_advice(month=None, hemisphere="Northern")`
Displays formatted gardening advice.

**Parameters:**
- `month` (int, optional): Month number. If None, uses current month.
- `hemisphere` (str, optional): "Northern" or "Southern"

## Error Handling

The application includes comprehensive error handling:
- Validates month range (1-12)
- Validates hemisphere input ("Northern" or "Southern")
- Handles type errors
- Provides clear error messages

## Development

This project follows a Git workflow with feature branches:

1. **Initial version**: Basic implementation with TODO comments
2. **Refactored version**: Modular functions and configuration dictionaries
3. **Documented version**: Full documentation, error handling, and validation

### Git Workflow

- Feature branches: `feature/refactor-functions`, `feature/add-documentation`
- Commit messages reference GitHub issues: `closes #1`, `closes #2`
- Pull requests are created for each feature branch

## Contributing

1. Create a feature branch from `main`
2. Make your changes
3. Add tests if applicable
4. Update documentation
5. Create a pull request

## License

This project is open source and available for educational purposes.

## Repository

https://github.com/Qhayiya29-coder/garden_app.git

