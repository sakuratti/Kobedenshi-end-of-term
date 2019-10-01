#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import cgi
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print('Content-Type: text/html; charset=UTF-8\n')
ok_Sunnybody = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
    <title>割引決定支援システム</title>
    <link rel="stylesheet" type="text/css" href="CSS/answer.css">
    <link rel="shortcut icon" type="image/png" href="/img/app2.png">
</haed>
<body>
<div class="main">
    <h1>おすすめ割引率は<span id="Check1">%s</span>%%です</h1>
    <h2>廃棄までの予想販売数は<span id="Check2">%s</span>個です</h2>
</div>
<div class="discription">
    <ul>
        <li>%s</li>
        <li>%s曜日</li>
        <li>気温 %s ℃</li>
        <li>天候 <img src="/img/tenki.png" class="weather_icon"></li>
        <li>不快指数 %s</li>
    </ul>
    <div id="aoao">
    %s
    </div>
</div>
<div id="support">
    <button type="button" onclick="location.href='../index.html'" id="back">戻る</button>
</div>
    <p id="footer"><a href="../HTML/help.html">ヘルプ</a>　｜　©️2019 割引決定支援システム</p>
</body>
</html>
"""

ok_Rainybody = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
    <title>割引決定支援システム</title>
    <link rel="stylesheet" type="text/css" href="CSS/answer.css">
    <link rel="shortcut icon" type="image/png" href="/img/app2.png">
</haed>
<body>
<div class="main">
    <h1>おすすめ割引率は<span id="Check1">%s</span>%%です</h1>
    <h2>廃棄までの予想販売数は<span id="Check2">%s</span>個です</h2>
</div>
<div class="discription">
    <ul>
        <li>%s</li>
        <li>%s曜日</li>
        <li>気温 %s ℃</li>
        <li>天候 <img src="/img/tenki2.png" class="weather_icon"></li>
        <li>不快指数 %s</li>
    </ul>
    <div id="aoao">
    %s
    </div>
</div>
<div id="support">
    <button type="button" onclick="location.href='../index.html'" id="back">戻る</button>
</div>
    <p id="footer"><a href="../HTML/help.html">ヘルプ</a>　｜　©️2019 割引決定支援システム</p>
</body>
</html>
"""

unusable_body = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>割引決定支援システム</title>
        <link rel="stylesheet" type="text/css" href="CSS/Calculate.css">
        <link rel="shortcut icon" type="image/png" href="/img/SmartFavicon.png">
    </haed>
    <body>
    <div class="attention"><p>%s</p></div>
    <button type="button" onclick="location.href='/index.html'" id="back">戻る</button>
    <p id="footer"><a href="/HTML/help.html">ヘルプ</a>　｜　©️2019 割引決定支援システム</p>
    </body>
</html>
"""
