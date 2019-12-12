# -*- coding: utf-8 -*-

'''
曜日毎　上映開始・終了時刻の影響
'''

import numpy as np
import pandas as pd

from sklearn import linear_model
clf = linear_model.LinearRegression()

#開始時刻の影響(月曜日)
def TimeInfMon(start_time):
    #csv読み込み
    monday = pd.read_csv("timer/data/Monday-influence.csv", sep=",", header=0 , dtype=int)
    # 説明変数に上映開始時刻を利用
    X = monday.loc[:,['start time']].values
    # 目的変数に売り上げを利用
    Y = monday['sold'].values
    #予測モデルを作成
    clf.fit(X, Y)
    #予測したいもの
    sample = np.array([[start_time]])
    #予測
    inf = clf.predict(sample)
    return inf[0]

#(火曜日)
def TimeInfTue(start_time):
    #csv読み込み
    tuesday = pd.read_csv("timer/data/Monday-influence.csv", sep=",", header=0 , dtype=int)
    # 説明変数に上映開始時刻を利用
    X = tuesday.loc[:,['start time']].values
    # 目的変数に売り上げを利用
    Y = tuesday['sold'].values
    #予測モデルを作成
    clf.fit(X, Y)
    #予測したいもの
    sample = np.array([[start_time]])
    #予測
    inf = clf.predict(sample)
    return inf[0]

#(水曜日)
def TimeInfWed(start_time):
    #csv読み込み
    wednesday = pd.read_csv("timer/data/Monday-influence.csv", sep=",", header=0 , dtype=int)
    # 説明変数に上映開始時刻を利用
    X = wednesday.loc[:,['start time']].values
    # 目的変数に売り上げを利用
    Y = wednesday['sold'].values
    #予測モデルを作成
    clf.fit(X, Y)
    #予測したいもの
    sample = np.array([[start_time]])
    #予測
    inf = clf.predict(sample)
    return inf[0]

#(木曜日)
def TimeInfThu(start_time):
    #csv読み込み
    thursday = pd.read_csv("timer/data/Monday-influence.csv", sep=",", header=0 , dtype=int)
    # 説明変数に上映開始時刻を利用
    X = thursday.loc[:,['start time']].values
    # 目的変数に売り上げを利用
    Y = thursday['sold'].values
    #予測モデルを作成
    clf.fit(X, Y)
    #予測したいもの
    sample = np.array([[start_time]])
    #予測
    inf = clf.predict(sample)
    return inf[0]

#(金曜日)
def TimeInfFri(start_time):
    #csv読み込み
    friday = pd.read_csv("timer/data/Monday-influence.csv", sep=",", header=0 , dtype=int)
    # 説明変数に上映開始時刻を利用
    X = friday.loc[:,['start time']].values
    # 目的変数に売り上げを利用
    Y = friday['sold'].values
    #予測モデルを作成
    clf.fit(X, Y)
    #予測したいもの
    sample = np.array([[start_time]])
    #予測
    inf = clf.predict(sample)
    return inf[0]

#(土曜日)
def TimeInfSat(start_time):
    #csv読み込み
    saturday = pd.read_csv("timer/data/Monday-influence.csv", sep=",", header=0 , dtype=int)
    # 説明変数に上映開始時刻を利用
    X = saturday.loc[:,['start time']].values
    # 目的変数に売り上げを利用
    Y = saturday['sold'].values
    #予測モデルを作成
    clf.fit(X, Y)
    #予測したいもの
    sample = np.array([[start_time]])
    #予測
    inf = clf.predict(sample)
    return inf[0]

#(日曜日)
def TimeInfSun(start_time):
    #csv読み込み
    sunday = pd.read_csv("timer/data/Monday-influence.csv", sep=",", header=0 , dtype=int)
    # 説明変数に上映開始時刻を利用
    X = sunday.loc[:,['start time']].values
    # 目的変数に売り上げを利用
    Y = sunday['sold'].values
    #予測モデルを作成
    clf.fit(X, Y)
    #予測したいもの
    sample = np.array([[start_time]])
    #予測
    inf = clf.predict(sample)
    return inf[0]