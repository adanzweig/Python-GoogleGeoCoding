#python -m pip install requests
#python3 -m pip install python-dotenv
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_geocode_data(address):
    api_key = os.getenv('GOOGLEMAPS_API_KEY')

    if not api_key:
        return "Google Maps API Key not found. Please set the API key in your environment variables."

    params = {
        "address": address,
        "key": api_key
    }

    try:
        response = requests.get("https://maps.googleapis.com/maps/api/geocode/json", params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data['results']
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    except KeyError:
        return "Unable to parse response data."

# Example usage:
address = "1600 Amphitheatre Parkway, Mountain View, CA"
geocode_data = get_geocode_data(address)
print(geocode_data)
