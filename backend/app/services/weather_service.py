import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEATHER_URL = "https://api.weatherapi.com/v1/forecast.json"
LOCATION = "Tingo Maria, Huanuco, Peru"


class WeatherService:
    def __init__(self):
        self.api_key = os.getenv("WEATHERAPI_KEY")
        if not self.api_key:
            raise RuntimeError("No se encontró WEATHERAPI_KEY en el entorno.")

    def get_forecast(self, days: int = 7):
        response = requests.get(
            WEATHER_URL,
            params={
                "key": self.api_key,
                "q": LOCATION,
                "days": days,
                "lang": "es",
                "aqi": "no",
                "alerts": "no",
            },
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()

        return {
            "location": {
                "name": data["location"]["name"],
                "region": data["location"]["region"],
                "country": data["location"]["country"],
                "lat": data["location"]["lat"],
                "lon": data["location"]["lon"],
            },
            "current": {
                "tempC": data["current"]["temp_c"],
                "feelsLikeC": data["current"]["feelslike_c"],
                "humidity": data["current"]["humidity"],
                "windKph": data["current"]["wind_kph"],
                "description": data["current"]["condition"]["text"],
                "icon": "https:" + data["current"]["condition"]["icon"],
            },
            "days": [
                {
                    "date": day["date"],
                    "maxTempC": day["day"]["maxtemp_c"],
                    "minTempC": day["day"]["mintemp_c"],
                    "rainMm": day["day"]["totalprecip_mm"],
                    "rainChance": day["day"]["daily_chance_of_rain"],
                    "description": day["day"]["condition"]["text"],
                    "icon": "https:" + day["day"]["condition"]["icon"],
                }
                for day in data["forecast"]["forecastday"]
            ],
            "source": "WeatherAPI",
        }
