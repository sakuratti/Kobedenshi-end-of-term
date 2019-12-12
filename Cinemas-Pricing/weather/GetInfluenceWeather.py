# -*- coding: utf-8 -*-

'''
天候が及ぼす影響(平日と休日で別)
'''

import numpy as np
import pandas as pd

from sklearn import linear_model
clf = linear_model.LinearRegression()

# 平日
def WeatherInfWeekday(weather,ave_rate):
    #csv読み込み()
    weekday = pd.read_csv("weather/data/weather-weekday.csv", sep=",", header=0 , dtype=float)
    #(天候判断)
    # 晴
    if weather == 1:
        # 説明変数に平均客席稼働率を利用
        X = weekday.loc[:,['average']].values
        # 目的変数に天候(晴)の影響を利用
        Y = weekday['sunny magnification'].values
    # 雨
    else:
        # 説明変数に平均客席稼働率を利用
        X = weekday.loc[:,['average']].values
        # 目的変数に天候(雨)の影響を利用
        Y = weekday['rainy magnification'].values

    #予測モデルを作成
    clf.fit(X, Y)
    #予測したいもの
    sample = np.array([[ave_rate]])
    #予測
    inf = clf.predict(sample)
    return inf[0]

# 休日
def WeatherInfHoliday(weather,ave_rate):
    #csv読み込み()
    weekday = pd.read_csv("weather/data/weather-weekday.csv", sep=",", header=0 , dtype=float)
    #(天候判断)
    # 晴
    if weather == 1:
        # 説明変数に平均客席稼働率を利用
        X = weekday.loc[:,['average']].values
        # 目的変数に天候(晴)の影響を利用
        Y = weekday['sunny magnification'].values
    # 雨
    else:
        # 説明変数に平均客席稼働率を利用
        X = weekday.loc[:,['average']].values
        # 目的変数に天候(雨)の影響を利用
        Y = weekday['rainy magnification'].values

    #予測モデルを作成
    clf.fit(X, Y)
    #予測したいもの
    sample = np.array([[ave_rate]])
    #予測
    inf = clf.predict(sample)
    return inf[0]