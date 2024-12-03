import requests

API_KEY = "f897a99d971b5eef57be6fafa0d83239"
BASE_URL = "http://api.openweathermap.org/geo/1.0"

def get_location_by_city(city_state):
    url = f"{BASE_URL}/direct"
    params = {"q": city_state, "limit": 1, "appid": API_KEY}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    if not data:
        raise ValueError(f"No location found for '{city_state}'")
    return data[0]

def get_location_by_zip(zip_code):
    url = f"{BASE_URL}/zip"
    params = {"zip": zip_code, "appid": API_KEY}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data

def fetch_geolocation(inputs):
    results = []
    for input_value in inputs:
        if "," in input_value:
            results.append(get_location_by_city(input_value))
        elif input_value.isdigit():
            results.append(get_location_by_zip(input_value))
        else:
            raise ValueError(f"Invalid input format: {input_value}")
    return results
