# 🌱 Garden Advice Application

A simple Python application that provides gardening advice based on the month/season you specify.

## Features

- 📅 **Month-based advice**: Enter any month and get season-specific gardening tips
- 🍂 **Season detection**: Automatically determines the season from the month
- ✅ **Simple and easy to use**: Just run the script and enter a month

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Qhayiya29-coder/garden_app.git
cd garden_app
```

2. No additional installation needed - just run the script!

## Usage

### Basic Usage

Run the script and enter a month when prompted:

```bash
python garden_advice.py
```

Example interaction:
```
Which month is it? march

Season detected: Spring
Tip: Start seeds indoors, prep beds, and feed the soil with compost.
```

### Supported Months

The application recognizes all 12 months (case-insensitive):
- **Spring months**: March, April, May
- **Summer months**: June, July, August
- **Autumn months**: September, October, November
- **Winter months**: December, January, February

You can enter the month in any format (e.g., "march", "March", "MARCH", "  march  ").

## Project Structure

```
garden_app/
├── garden_advice.py    # Main application file
├── README.md           # This file
└── repo.txt            # Repository URL
```

## Functions

### `get_season(month: str) -> str`
Determines the season for a given month name.

**Parameters:**
- `month` (str): Month name (case-insensitive)

**Returns:** Season name as string ("spring", "summer", "autumn", or "winter")

**Example:**
```python
>>> get_season("March")
'spring'
```

### `get_user_input() -> str`
Prompts the user to enter a month name.

**Returns:** User input with whitespace removed

### `get_advice(season: str) -> str`
Retrieves gardening advice for a specific season.

**Parameters:**
- `season` (str): Season name

**Returns:** Gardening advice string

**Example:**
```python
>>> get_advice("spring")
'Start seeds indoors, prep beds, and feed the soil with compost.'
```

### `display_advice(season: str, advice: str) -> None`
Displays the season and gardening advice to the user.

**Parameters:**
- `season` (str): Season name
- `advice` (str): Gardening advice to display

### `main() -> None`
Main entry point that orchestrates the garden advice flow.

## How It Works

1. The application prompts you to enter a month
2. It looks up the month in the `MONTH_TO_SEASON` dictionary to determine the season
3. It retrieves the appropriate gardening advice from the `SEASON_TASKS` dictionary
4. It displays the season and advice in a formatted way

## Development

This project demonstrates a complete Git workflow:

1. **Initial version**: Basic implementation with TODO comments
2. **Refactored version** (Issue #1): Code organized into reusable functions
3. **Documented version** (Issue #2): Comprehensive documentation and comments added

### Git Workflow

- Feature branches: `feature/refactor-into-functions`, `feature/add-documentation`
- Commit messages reference GitHub issues: `closes #1`, `closes #2`
- Pull requests created for each feature branch

## Contributing

1. Create a feature branch from `main`
2. Make your changes
3. Update documentation if needed
4. Create a pull request

## License

This project is open source and available for educational purposes.

## Repository

https://github.com/Qhayiya29-coder/garden_app.git
