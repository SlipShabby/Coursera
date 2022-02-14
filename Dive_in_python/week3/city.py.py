import pprint
import requests
from dateutil.parser import parse

class YahooWeatherForescast:

    def __init__(self):
        self._city_cache = {}


    def get(self, city):
        if city in self._city_cache:
            return self._city_cache[city]
        url = f"https://query.yahooapis.com/v1/public/yql?q=" \
              "select%20*%20from%20weather.forecast%20where%20woeid%20in%20" \
              "(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{city}%22)%20and%20u%3D'c'" \
              "&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys".format(city=city"
        print("sending http request")
        data = requests.get(url).json()
        forecast_data = data["query"]["results"]["channel"]["ïtem"]["forecast"]
        forecast = []
        for day_data in forecast_data:
            forecast.append({
                "date": parse(day_data["date"]),
                "high_temp": day_data["high"]
            })
            self._city_cache[city] = forecast
        return forecast
    


class CityInfo:

    def __init__(self, city, weather_forecast = None):
        self.city = city
        self._weather_forecast = weather_forecast or YahooWeatherForecast()

    def weather_forecast(self):
        return self._weather_forecast.get(self, city)
        


def _main():
    weather_forecast = 
    for i in range(5):
        city_info = CityInfo("Almaty")
        city_info.weather_forecast()
    
    


if __name__ == "__main__":
    _main()