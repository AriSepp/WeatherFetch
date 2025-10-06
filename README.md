# WeatherFetch

A minimal Python script that fetches current and short-term forecast data from the OpenWeatherMap API for a city you enter.

This repository contains a single script, `weather.py`, which demonstrates how to:

- Lookup a city's coordinates using the OpenWeatherMap "current weather" endpoint.
- Fetch a short forecast using the forecast endpoint and print a few upcoming forecast entries.

## Files

- `weather.py` — main script. Prompts for a city name, queries OpenWeatherMap, and prints forecast information to the console.

## Requirements

- Python 3.7+
- `requests` library

Install dependencies with pip (recommended to use a virtual environment):

```powershell
python -m pip install requests
```

Optionally create a `requirements.txt` with the single line `requests` for reproducible installs.

## Setup

1. Get an API key from OpenWeatherMap: https://openweathermap.org/api
2. Edit `weather.py` and set the `API_KEY` variable to your key, or better, set an environment variable and modify the script to read it.

Recommended (safer) approach: read the API key from an environment variable. Example change to `weather.py`:

```python
import os
API_KEY = os.environ.get('OPENWEATHER_API_KEY')
```

On Windows PowerShell you can set the environment variable for the current session with:

```powershell
$env:OPENWEATHER_API_KEY = 'your_api_key_here'
```

Or set it permanently in system/user environment variables through Windows settings.

## Usage

Run the script and enter a city name when prompted:

```powershell
python weather.py
```

Example session output (localized strings may vary):

```
City: Helsinki

Aika on: 2025-10-06 12:00:00.
Sää on: selkeää.
Lämpötila on: 8.5°C
Tuulennopeus on: 3.2 m/s
... (more entries) ...
```

Notes about the current `weather.py` behavior:

- The script first requests the current weather to obtain latitude and longitude for the named city.
- It then calls the 5-day / 3-hour forecast endpoint and prints the first several forecast entries (indexes 0–7).
- If the API returns a 401 Unauthorized, the script prints the API response content.

## Improvements & Next steps

Suggested enhancements you can implement:

- Read the API key from an environment variable instead of hardcoding it.
- Add robust error handling for network errors, invalid city names, and missing JSON fields.
- Let the user configure how many forecast entries to show, or format output as a table (e.g., using `tabulate`).
- Add unit tests that mock `requests` to verify JSON parsing and output formatting.
- Add a `requirements.txt` and a short test harness for automated checks.

## License

This project has no license specified. Add a LICENSE file if you plan to share it publicly.

## Contact

If you'd like help extending the script (environment variable support, better formatting, or packaging), describe what you'd like and I can implement it.