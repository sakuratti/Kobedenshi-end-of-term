'''
天候取得
OpenWeatherMap
当日券にのみ反映
'''

class GetWeather():
    def __init__(self):
        pass

    #神戸市の天候情報取得
    def GetWeatherKobe(self):
        import requests
        import json

        city_name = "Kobe" 
        API_KEY = "197c07cf21a1282fd883eda7ef15ae51"
        api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"

        url = api.format(city = city_name, key = API_KEY)
        response = requests.get(url)
        data = response.json()

        return data