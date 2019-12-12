# -*- coding: utf-8 -*-

'''
サンプルプログラム
クラス利用
練習
最初は客数予測が86%以下なら変動させない
(途中で伸びてきたら変動させる)
'''

import os,sys
import datetime

if __name__ == '__main__':
    from charges import SpecialDay
    from charges import General
    from weather import GetWeather
    from weather import ShapingWeather
    from timer import GetInfluenceTime
    from weather import GetInfluenceWeather

    #obj = GetInfluenceTime.TimeInfMon(11)
    obj2 = ShapingWeather.ShapingWeather()
    obj3 = GetWeather.GetWeather().GetWeatherKobe()
    
    print(obj3)
    print(obj2.CheckWeatherHoliday(50))
    #print(obj2.data)
