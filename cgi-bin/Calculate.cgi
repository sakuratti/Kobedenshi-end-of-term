#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb
cgitb.enable()
import os
import sys
import GetWeather
import json
import requests
import io
import datetime
import html

#htmlボディ
 
if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    print('Content-Type: text/html; charset=UTF-8\n')
 
    #入力データ取得
    form = cgi.FieldStorage()
    #残り時間入力
    time = int(form.getvalue('Time',''))
    #その商品の1日の平均売り上げ
    speed = int(form.getvalue('Speed',''))
    #対象の在庫数
    total = int(form.getvalue('Amount',''))

    #時間帯毎の販売数の割合
    timezone = [0.01,0.02,0.01,0.01,0.01,0.01,0.01,0.01,0.02,0.07,0.11,0.12,0.14,0.1,0.07,0.06,0.05,0.05,0.07,0.12,0.04,0.03,0.02,0.01]

    #曜日取得&曜日指数計算
    Youbi = datetime.datetime.now().weekday()
    if Youbi <= 1:
        yobi = 0.6
    elif Youbi == 2:
        yobi = 0.7
    elif Youbi == 3:
        yobi = 1
    elif Youbi == 4:
        yobi = 1.2
    else:
        yobi = 1.4

    #日付取得
    day = datetime.date.today()
    #曜日を字に変換
    youbi = ["月","火","水","木","金","土","日"]

    #現在時刻取得
    timenow = datetime.datetime.now().hour
    #一時的に！！！今●●時やとする。
    #timenow = 20
    #廃棄時刻取得 8時までは使用不可設定つき
    if timenow + time < 24 and timenow >= 8:
        haiki = timenow + time
    elif timenow + time == 24 and timenow >= 8:
        haiki = 0
    elif timenow + time == 25 and timenow >= 8:
        haiki = 1
    else:
    #計算できないようにする
        haiki = 56

    #総売上に対して販売する時間帯の販売数の割合
    i = timenow
    percent = 0
    if haiki == 0:
        while i < 24:
            percent += timezone[i]
            i += 1
    elif haiki == 1:
        while i < 25:
            if i == 24:
                percent += timezone[0]
                break
            percent += timezone[i]
            i += 1
    elif haiki < 9:
        percent = 0
    else:
        if haiki != 56:
            while i < haiki + 1:
                percent += timezone[i]
                i += 1
    #気温取得
    temperature = GetWeather.temperature
    humidity = GetWeather.humidity
    #天気によって字変える。
    if GetWeather.weather == 1:
        tenki = "雨"
        hareame = 1
    else:
        tenki = "晴"
        hareame = 0

    #不快指数
    discomfort = int(0.81 * temperature + 0.01 * humidity * (0.99 * temperature - 14.3) + 46.3)

    #月取得&月(季節)指数
    Month = int(datetime.datetime.now().month)

    #天候をまとめた指数
    shop = [0.75,0.9,1,1.2,1,0.9,0.8,0.75]
    if 5 <= Month <= 9:
        if discomfort >= 85:
            shopping = shop[7]
        elif discomfort >= 80:
            shopping = shop[6]
        elif discomfort >= 75:
            shopping = shop[5]
        elif discomfort >= 70:
            shopping = shop[4]
        elif discomfort >= 65:
            shopping = shop[3]
        elif discomfort >= 60:
            shopping = shop[2]
        elif discomfort >= 55:
            shopping = shop[1]
        elif discomfort < 55:
            shopping = shop[0]
    elif Month == 4 or Month == 10:
        shopping = 1
    else:
        if discomfort <= 55:
            shopping = shop[7]
        elif discomfort <= 60:
            shopping = shop[6]
        elif discomfort <= 65:
            shopping = shop[5]
        elif discomfort <= 70:
            shopping = shop[4]
        elif discomfort <= 75:
            shopping = shop[3]
        elif discomfort <= 80:
            shopping = shop[2]
        elif discomfort <= 85:
            shopping = shop[1]
        elif discomfort > 85:
            shopping = shop[0]



    #割引率計算
    #廃棄までの予想販売数
    Anticipation_Amount = int(speed * percent * shopping * yobi)
    #割引きなしで売れる数(%)
    imanomama = Anticipation_Amount / total
    #割引率計算
    if imanomama >= 1:
        answer = 0
    elif imanomama >= 0.9:
        answer = 10
    elif imanomama >= 0.85:
        answer = 20
    elif imanomama >= 0.75:
        answer = 30
    elif imanomama >= 0.7:
        answer = 40
    else:
        answer = 50


    #売れ残りが多いか
    if imanomama < 0.7:
        urenokori = 1
    else:
        urenokori = 0
    #残り時間が少ないか
    if time <= 3:
        nokorizikan = 1
    else:
        nokorizikan = 0

    #平均気温
    avetemperature = [0,5.6,7.2,10.6,13.6,20.0,21.8,24.1,28.4,26.7,19.1,14.0,8.3,16.8]


    #割引理由説明
    #aiの文章パーツ(天候)
    if 5 <= Month <= 9:
        part1 = ["涼しく過ごしやすい天候です。","不快指数が高く、<br>販売数は期待できません","比較的過ごしやすい天候です。","暑い1日となりそうです。","雨が降ります。"]
    elif Month == 4:
        part1 = ["少し肌寒い1日となりそうです。","比較的過ごしやすい天候です。","暖かく春の気持ち良い1日となりそうです。","雨が降ります。"]
    elif Month == 10:
        part1 = ["少し肌寒い1日となりそうです。","比較的過ごしやすい天候です。","暖かい1日となりそうです。","雨が降ります。"]
    else:
        part1 = ["いつもに増して<br>寒い1日となりそうです。","いつも通り冬の1日です。","少し暖かい1日となりそうです。","雨が降ります。"]
    

    ai = ""

    if 5 <= Month <= 9:
        if hareame == 0:
            if temperature < avetemperature[Month] - 3:
                if discomfort < 75:
                    if answer == 0:
                        ai = "%s<br>多少の販売数の増加が見込めます。割引きは必要ありません" % part1[0]
                    elif urenokori == 1 and nokorizikan == 1:
                        ai = "%s<br>しかし売れ残りが多く残り時間が少ないため%d%%の割引きが必要です" % (part1[0],answer)
                    elif urenokori == 1:
                        ai = "%s<br>しかし売れ残りが多いため%d%%の割引きが必要です" % (part1[0],answer)
                    else:
                        ai = "%s<br>残りの販売時間では売り切れないので%d%%の割引きが必要です" % (part1[0],answer)
                else:
                    if answer == 0:
                        ai = "%s<br>しかしこのままでも十分売り切れる可能性が高いため割引きは必要ありません"
                    elif urenokori == 1 and nokorizikan == 1:
                        ai = "%s<br>さらに売れ残りが多く残り時間が少ないため%d%%の割引きが必要です" % (part1[1],answer)
                    elif urenokori == 1:
                        ai = "%s<br>しかし売れ残りが多いため%d%%の割引きが必要です" % (part1[1],answer)
                    else:
                        ai = "%s<br>しかし残りの販売時間では売り切れないので%d%%の割引きが必要です" % (part1[1],answer)
            elif temperature < avetemperature[Month] + 3:
                if discomfort < 75:
                    if answer == 0:
                        ai = "%s<br>現段階で割引きは必要ありません" % part1[2]
                    elif urenokori == 1 and nokorizikan == 1:
                        ai = "%s<br>しかし売れ残りが多く、販売時間も少ないため%d%%の割引きが必要です" % (part1[2],answer)
                    elif urenokori == 1:
                        ai = "%s<br>時間はまだありますが、売れ残りが多いため%d%%の割引きが必要です" % (part1[2],answer)
                    else:
                        ai = "%s<br>残りの販売時間では売り切れないので%d%%の割引きが必要です" % (part1[2],answer)
                else:
                    if answer == 0:
                        ai = "%s<br>しかしこのままでも十分売り切れる可能性が高いため割引きは必要ありません" % part1[1]
                    elif urenokori == 1 and nokorizikan == 1:
                        ai = "%s<br>さらに売れ残りが多く残り時間が少ないため%d%%の割引きが必要です" % (part1[1],answer)
                    elif urenokori == 1:
                        ai = "%s<br>時間はまだありますが、売れ残りが多いため%d%%の割引きが必要です" % (part1[1],answer)
                    else:
                        ai = "%s<br>残りの販売時間では売り切れないので%d%%の割引きが必要です" % (part1[1],answer)
            else:
                if answer == 0:
                    ai = "%s<br>しかしこのままでも十分売り切れる可能性が高いため割引きは必要ありません" % part1[3]
                elif urenokori == 1 and nokorizikan == 1:
                    ai = "%s<br>売れ残りが多く、販売時間も少ないため%d%%の割引きが必要です" % (part1[3],answer)
                elif urenokori == 1:
                    ai = "%s<br>時間はまだありますが、売れ残りが多いため%d%%の割引きが必要です" % (part1[3],answer)
                else:
                    ai = "%s<br>残りの販売時間では売り切れないので%d%%の割引きが必要です" % (part1[3],answer)
        else:
            if answer == 0:
                ai = "%s<br>しかし十分に売り切れる時間と在庫数なので割引きは必要ありません" % part1[4]
            elif urenokori == 1 and nokorizikan == 1:
                ai = "%s<br>売れ残りが多く、販売時間も残り少ないため%d%%の割引きが必要です" % (part1[4],answer)
            elif urenokori == 1:
                ai = "%s,<br>時間はまだありますが、売れ残りが多いため%d%%の割引きが必要です" % (part1[4],answer)
            else:
                ai = "%s<br>残りの時間では売り切れないので%d%%の割引きが必要です" % (part1[4],answer)
    elif Month == 4:
        if hareame == 0:
            if temperature < avetemperature[Month] - 3:
                if answer == 0:
                    ai = "%s<br>しかし十分売り切れる可能性が高いため割引きは必要ありません" % part1[0]
                elif urenokori == 1 and nokorizikan == 1:
                    ai = "%s<br>売れ残りが多く残り時間が少ないため%d%%の割引きが必要です" % (part1[0],answer)
                elif urenokori == 1:
                    ai = "%s<br>売れ残りが多いため%d%%の割引きが必要です" % (part1[0],answer)
                else:
                    ai = "%s<br>残りの販売時間では売り切れないので%d%%の割引きが必要です" % (part1[0],answer)
            elif temperature < avetemperature[Month] + 3:
                if answer == 0:
                    ai = "%s<br>現段階で割引きは必要ありません" % part1[1]
                elif urenokori == 1 and nokorizikan == 1:
                    ai = "%s<br>しかし売れ残りが多く、販売時間も少ないため%d%%の割引きが必要です" % (part1[1],answer)
                elif urenokori == 1:
                    ai = "%s<br>時間はまだありますが、売れ残りが多いため%d%%の割引きが必要です" % (part1[1],answer)
                else:
                    ai = "%s<br>残りの販売時間では売り切れないので%d%%の割引きが必要です" % (part1[1],answer)
            else:
                if answer == 0:
                    ai = "%s<br>このままでも十分売り切れる可能性が高いため割引きは必要ありません" % part1[2]
                elif urenokori == 1 and nokorizikan == 1:
                    ai = "%s<br>しかし売れ残りが多く残り時間が少ないため%d%%の割引きが必要です" % (part1[2],answer)
                elif urenokori == 1:
                    ai = "%s<br>しかし売れ残りが多いため%d%%の割引きが必要です" % (part1[2],answer)
                else:
                    ai = "%s<br>しかし残りの販売時間では売り切れないので%d%%の割引きが必要です" % (part1[2],answer)
        else:
            if answer == 0:
                ai = "%s<br>しかし十分に売り切れる時間と在庫数なので割引きは必要ありません" % part1[3]
            elif urenokori == 1 and nokorizikan == 1:
                ai = "%s<br>売れ残りが多く、販売時間も残り少ないため%d%%の割引きが必要です" % (part1[3],answer)
            elif urenokori == 1:
                ai = "%s,<br>時間はまだありますが、売れ残りが多いため%d%%の割引きが必要です" % (part1[3],answer)
            else:
                ai = "%s<br>残りの時間では売り切れないので%d%%の割引きが必要です" % (part1[3],answer)
    elif Month == 10:
        if hareame == 0:
            if temperature < avetemperature[Month] - 3:
                if answer == 0:
                    ai = "%s<br>しかし十分売り切れる可能性が高いため割引きは必要ありません" % part1[0]
                elif urenokori == 1 and nokorizikan == 1:
                    ai = "%s<br>売れ残りが多く残り時間が少ないため%d%%の割引きが必要です" % (part1[0],answer)
                elif urenokori == 1:
                    ai = "%s<br>売れ残りが多いため%d%%の割引きが必要です" % (part1[0],answer)
                else:
                    ai = "%s<br>残り時間が少ないため%d%%の割引きが必要です" % (part1[0],answer)
            elif temperature < avetemperature[Month] + 3:
                if answer == 0:
                    ai = "%s<br>現段階で割引きは必要ありません" % part1[1]
                elif urenokori == 1 and nokorizikan == 1:
                    ai = "%s<br>しかし売れ残りが多く、販売時間も少ないため%d%%の割引きが必要です" % (part1[1],answer)
                elif urenokori == 1:
                    ai = "%s<br>時間はまだありますが、売れ残りが多いため%d%%の割引きが必要です" % (part1[1],answer)
                else:
                    ai = "%s<br>残りの販売時間では売り切れないので%d%%の割引きが必要です" % (part1[1],answer)
            else:
                if answer == 0:
                    ai = "%s<br>このままでも十分売り切れる可能性が高いため割引きは必要ありません" % part1[2]
                elif urenokori == 1 and nokorizikan == 1:
                    ai = "%s<br>売れ残りが多く残り時間が少ないため%d%%の割引きが必要です" % (part1[2],answer)
                elif urenokori == 1:
                    ai = "%s<br>売れ残りが多いため%d%%の割引きが必要です" % (part1[2],answer)
                else:
                    ai = "%s<br>残りの販売時間では売り切れないので%d%%の割引きが必要です" % (part1[2],answer)
        else:
            if answer == 0:
                ai = "%s<br>しかし十分に売り切れる時間と在庫数なので割引きは必要ありません" % part1[3]
            elif urenokori == 1 and nokorizikan == 1:
                ai = "%s<br>売れ残りが多く、販売時間も残り少ないため%d%%の割引きが必要です" % (part1[3],answer)
            elif urenokori == 1:
                ai = "%s,<br>時間はまだありますが、売れ残りが多いため%d%%の割引きが必要です" % (part1[3],answer)
            else:
                ai = "%s<br>残りの時間では売り切れないので%d%%の割引きが必要です" % (part1[3],answer)
    else:
        if hareame == 0:
            if temperature > avetemperature[Month] + 3:
                if discomfort < 55:
                    if answer == 0:
                        ai = "%s<br>しかし十分に売り切れる時間と在庫数なので、割引きは必要ありません" % part1[0]
                    elif urenokori == 1 and nokorizikan == 1:
                        ai = "%s<br>売れ残りが多く残り時間が少ないため%d%%の割引きが必要です" % (part1[0],answer)
                    elif urenokori == 1:
                        ai = "%s<br>売れ残りが多いため%d%%の割引きが必要です" % (part1[0],answer)
                    else:
                        ai = "%s<br>残り時間が少ないため%d%%の割引きが必要です" % (part1[0],answer)
                else:
                    if answer == 0:
                        ai = "%s<br>このままでも十分売り切れる可能性が高いため割引きは必要ありません"
                    elif urenokori == 1 and nokorizikan == 1:
                        ai = "%s<br>売れ残りが多く残り時間が少ないため%d%%の割引きが必要です" % (part1[2],answer)
                    elif urenokori == 1:
                        ai = "%s<br>時間はまだありますが、売れ残りが多いため%d%%の割引きが必要です" % (part1[2],answer)
                    else:
                        ai = "%s<br>残りの販売時間では売り切れないので%d%%の割引きが必要です" % (part1[2],answer)
            elif temperature > avetemperature[Month] - 3:
                if discomfort < 55:
                    if answer == 0:
                        ai = "%s<br>しかし現段階で割引きは必要ありません" % part1[2]
                    elif urenokori == 1 and nokorizikan == 1:
                        ai = "%s<br>売れ残りが多く、販売時間も少ないため%d%%の割引きが必要です" % (part1[0],answer)
                    elif urenokori == 1:
                        ai = "%s<br>時間はまだありますが、売れ残りが多いため%d%%の割引きが必要です" % (part1[0],answer)
                    else:
                        ai = "%s<br>残りの販売時間では売り切れないので%d%%の割引きが必要です" % (part1[0],answer)
                else:
                    if answer == 0:
                        ai = "%s<br>このままでも十分売り切れる可能性が高いため割引きは必要ありません" % part1[1]
                    elif urenokori == 1 and nokorizikan == 1:
                        ai = "%s<br>売れ残りが多く残り時間が少ないため%d%%の割引きが必要です" % (part1[1],answer)
                    elif urenokori == 1:
                        ai = "%s<br>時間はまだありますが、売れ残りが多いため%d%%の割引きが必要です" % (part1[1],answer)
                    else:
                        ai = "%s<br>残りの販売時間では売り切れないので%d%%の割引きが必要です" % (part1[1],answer)
            else:
                if answer == 0:
                    ai = "%s<br>しかしこのままでも十分売り切れる可能性が高いため割引きは必要ありません" % part1[0]
                elif urenokori == 1 and nokorizikan == 1:
                    ai = "%s<br>売れ残りが多く、販売時間も少ないため%d%%の割引きが必要です" % (part1[0],answer)
                elif urenokori == 1:
                    ai = "%s<br>時間はまだありますが、売れ残りが多いため%d%%の割引きが必要です" % (part1[0],answer)
                else:
                    ai = "%s<br>残りの販売時間では売り切れないので%d%%の割引きが必要です" % (part1[0],answer)
        else:
            if answer == 0:
                ai = "%s<br>しかし十分に売り切れる時間と在庫数なので割引きは必要ありません" % part1[3]
            elif urenokori == 1 and nokorizikan == 1:
                ai = "%s<br>売れ残りが多く、販売時間も残り少ないため%d%%の割引きが必要です" % (part1[3],answer)
            elif urenokori == 1:
                ai = "%s,<br>時間はまだありますが、売れ残りが多いため%d%%の割引きが必要です" % (part1[3],answer)
            else:
                ai = "%s<br>残りの販売時間では売り切れないので%d%%の割引きが必要です" % (part1[3],answer)


    if ai == "":
        ai = "データが計測できませんでした。"


    #HTML表示
    if timenow < 8:
        print(html.unusable_body % ("現在利用不可です(AM0:00~AM8:00)"))
    elif haiki != 56 and hareame != 1:
        print(html.ok_Sunnybody % (answer,Anticipation_Amount,day,youbi[Youbi],temperature,discomfort,ai))
    elif haiki != 56 and hareame == 1:
        print(html.ok_Rainybody % (answer,Anticipation_Amount,day,youbi[Youbi],temperature,discomfort,ai))
    else:
        print(html.unusable_body % ("計算するのはAM1:00までに廃棄予定の商品のみです"))
    

