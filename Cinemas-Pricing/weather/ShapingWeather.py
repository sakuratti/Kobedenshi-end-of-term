'''
GetWeather.pyで取得したデータを整形する
天気(晴・雨)
不快指数
当日券にのみ反映
'''

from weather import GetWeather
from weather import GetInfluenceWeather as InfWea

obj = GetWeather.GetWeather()

class ShapingWeather():
    def __init__(self):
        self.data = obj.GetWeatherKobe()
        pass

    #温度取得
    def ShapingTemperature(self):
        self.temperature = self.data["main"]["temp"]
        return self.temperature

    #湿度取得
    def ShapingHumidity(self):
        self.humidity = self.data["main"]["humidity"]
        return self.humidity

    #天候判断(平日)
    def CheckWeatherWeekday(self,ave_rate):
        #雨天時(引数は天候,平均入場者数)
        if "10n" in str(self.data):
            self.today_weather = InfWea.WeatherInfWeekday(2,ave_rate)
        elif "10d" in str(self.data):
            self.today_weather = InfWea.WeatherInfWeekday(2,ave_rate)
        elif "09d" in str(self.data):
            self.today_weather = InfWea.WeatherInfWeekday(2,ave_rate)
        elif "09n" in str(self.data):
            self.today_weather = InfWea.WeatherInfWeekday(2,ave_rate)
        elif "11d" in str(self.data):
            self.today_weather = InfWea.WeatherInfWeekday(2,ave_rate)
        elif "11n" in str(self.data):
            self.today_weather = InfWea.WeatherInfWeekday(2,ave_rate)
        #晴天時(引数は天候,平均入場者数)
        else:
            self.today_weather = InfWea.WeatherInfWeekday(1,ave_rate)
        return self.today_weather

    #天候判断(土日)
    #二人客は多くなる(カップル効果?)
    def CheckWeatherHoliday(self,ave_rate):
        #雨天時
        if "10n" in str(self.data):
            self.today_weather = InfWea.WeatherInfHoliday(2,ave_rate)
        elif "10d" in str(self.data):
            self.today_weather = InfWea.WeatherInfHoliday(2,ave_rate)
        elif "09d" in str(self.data):
            self.today_weather = InfWea.WeatherInfHoliday(2,ave_rate)
        elif "09n" in str(self.data):
            self.today_weather = InfWea.WeatherInfHoliday(2,ave_rate)
        elif "11d" in str(self.data):
            self.today_weather = InfWea.WeatherInfHoliday(2,ave_rate)
        elif "11n" in str(self.data):
            self.today_weather = InfWea.WeatherInfHoliday(2,ave_rate)
        #晴天時
        else:
            self.today_weather = InfWea.WeatherInfHoliday(1,ave_rate)
        return self.today_weather
