# Fetch Weather Utility

## Overview
This utility fetches geolocation data based on city/state or zip code using OpenWeather's Geocoding API.

## Setup

1. Clone this repository
2. `cd` fetch_weather_utility
3. Install Dependencies by doing `pip install -r requirements.txt`
4. Run the utility from the command line: `python run_solution.py "Madison, WI" "12345"`
Example Output
```
{'name': 'Madison', 'lat': 43.0731, 'lon': -89.4012, 'country': 'US', 'state': 'Wisconsin'} {'name': 'Schenectady', 'lat': 42.8106, 'lon': -73.9482, 'country': 'US', 'state': 'New York'}
```

## Testing

Run integration tests using pytest:
`pytest solution/test_geolocation.py`


## File Descriptions

### `solution/geolocation.py`
Handles API interaction and input parsing.

### `run_solution.py`
Entry point to execute the utility from the command line.

### `solution/test_geolocation.py`
Integration tests for the utility using pytest.

### `requirements.txt`
Contains the required Python libraries: