# This class gets the weather and forecast information from OWM api.
# Written by Eason Chen
# 07/04/2017
#
# TODO: update the method to store API key.


import requests
from pprint import pprint

class DailyForecast:
    # input: city name as a string.
    def __init__(self, city):
        self.city = city
        self.API_key = 'd8fe3c768df84c5386e2468462ddafbd'
        self.forecast = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q={}&appid={}'.format(city, self.API_key))
        self.forecast = self.forecast.json()

    def get_tmr_weather(self):
        weather = self.forecast['list'][0]['weather'][0]
        # key: main, description, id, icon
        return weather

    def get_tmr_temperature(self):
        temp = self.forecast['list'][0]['temp']
        # convert the temperature into Celcius
        temp = {k:round(v-273.15, 1) for (k, v) in temp.items()}
        # key: morn, eve, day, night, min, max
        return temp

    def get_tmr_humidity(self):
        humidity = self.forecast['list'][0]['humidity']
        return humidity

    def construct_weather_forecast_msg(self):
        weather = self.get_tmr_weather()['description']
        temperature = self.get_tmr_temperature()
        min_temp, max_temp, day_temp, night_temp = temperature['min'], temperature['max'], \
                                                   temperature['day'], temperature['night']
        humidity = self.get_tmr_humidity()
        msg = 'Today\'s weather in {}:{}, {}-{}C, day/night {}/{}C, humidity:{}%'.format(self.city, weather, min_temp, max_temp, day_temp, night_temp, humidity)
        return msg

if __name__ == "__main__":
    f = DailyForecast('Berkeley, CA')
    print(f.get_tmr_weather())
    print(f.get_tmr_temperature())
    print(f.get_tmr_humidity())

    print(f.construct_weather_forecast_msg())
