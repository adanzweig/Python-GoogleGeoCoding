# Python Google Maps Geocoding API Connection

This Python project demonstrates how to connect to the Google Maps Geocoding API to retrieve geographical coordinates (latitude and longitude) for a specific address using the `requests` library. In this project, we provide a simple `index.py` file that fetches and displays the geocoding data for a predefined address.

## Prerequisites

Before running this project, ensure you have the following:

- Python installed on your system (at least Python 3.x).
- A Google Cloud Platform (GCP) project with the Google Maps Geocoding API enabled.
- An API key for the Google Maps Geocoding API. You can obtain one by following the [Google Maps JavaScript API documentation](https://developers.google.com/maps/gmp-get-started#step_1_get_an_api_key).

## Installation

1. Clone or download this repository to your local machine.

```bash
git clone https://github.com/adanzweig/Python-GoogleGeoCoding.git
```

2. Navigate to the project directory.

```bash
cd Python-GoogleGeoCoding
```

3. Open the `index.py` file in your code editor.

4. Replace `APIKEY` with your Google Maps Geocoding API key and `"1600 Amphitheatre Parkway, Mountain View, CA"` with the address you want to geocode.

```python
api_key = "your_api_key_here"
address = "your_address_here"
```

5. Save your changes.

## Usage

To retrieve geographical coordinates for a specific address, follow these steps:

1. Make sure you have set your API key and address in the `index.py` file as mentioned above.

2. Run the project using Python:

```bash
python index.py
```

3. The geocoding data for the specified address will be displayed in the console.

## Example

Here's an example of what the output might look like in the console:

```json
[
    {
        "address_components": [...],
        "formatted_address": "1600 Amphitheatre Parkway, Mountain View, CA 94043, USA",
        "geometry": {
            "location": {
                "lat": 37.423021,
                "lng": -122.083739
            },
            "location_type": "ROOFTOP",
            "viewport": {...}
        },
        "place_id": "ChIJ2eUgeAK6j4ARbn5u_wAGqWA",
        "plus_code": {...},
        "types": ["street_address"]
    }
]
```

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- Geocoding data is provided by the Google Maps Geocoding API.
- This project uses the `requests` library to make HTTP requests.

If you have any questions or encounter issues, please don't hesitate to reach out.

Happy coding!