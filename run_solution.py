import argparse
from solution.geolocation import fetch_geolocation

def main():
    parser = argparse.ArgumentParser(description="Fetch geolocation data for city/state or zip.")
    parser.add_argument("locations", nargs="+", help="List of city/state or zip codes.")
    args = parser.parse_args()

    try:
        results = fetch_geolocation(args.locations)
        for result in results:
            print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
