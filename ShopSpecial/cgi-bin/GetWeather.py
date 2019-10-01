#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import cgi
import requests
import json

city_name = "Kobe" 
API_KEY = "197c07cf21a1282fd883eda7ef15ae51" 
api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"

url = api.format(city = city_name, key = API_KEY)
response = requests.get(url)
data = response.json()

#天候取得

#雨天時
if "10n" in str(data):
    weather = 1
elif "10d" in str(data):
    weather = 1
elif "09d" in str(data):
    weather = 1
elif "09n" in str(data):
    weather = 1
elif "11d" in str(data):
    weather = 1
elif "11n" in str(data):
    weather = 1
#晴天時
else:
    weather = 2

#気温取得
temperature = data["main"]['temp']

#湿度取得
humidity = data["main"]['humidity']