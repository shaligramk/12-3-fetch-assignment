import pytest
from solution.geolocation import fetch_geolocation

def test_city_state():
    result = fetch_geolocation(["Madison, WI"])
    assert "lat" in result[0]
    assert "lon" in result[0]

def test_zip_code():
    result = fetch_geolocation(["12345"])
    assert "lat" in result[0]
    assert "lon" in result[0]

def test_multiple_inputs():
    results = fetch_geolocation(["Madison, WI", "12345"])
    assert len(results) == 2

def test_invalid_input():
    with pytest.raises(ValueError, match="Invalid input format"):
        fetch_geolocation(["InvalidInput"])
