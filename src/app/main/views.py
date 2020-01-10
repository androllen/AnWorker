#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time: 2020/01/10 15:41:21
# Contact: androllen#hotmail.com

from flask import render_template, make_response, send_from_directory
from app.main import splash
from app import log
import requests
import urllib.request
import urllib.parse
import json
from datetime import datetime

from app.main.model import Bing


@splash.route('/')
def index():
    data = [{"id": 10, "name": "中华古诗词"},
            {"id": 11, "name": "成语大辞典"}]

    bings = spider_bing()

    return render_template('main/index.html', title='Home', tasklist=data, wallpaper=bings)


@splash.route('/about/')
def about():
    return render_template('main/about.html', title='about')


def spider_bing():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    bingURL = 'http://www.bing.com/HPImageArchive.aspx'

    params_json = {
        'format': 'js',
        'idx': -1,
        'n': 1,
        'pid': 'hp',
        'mkt': 'en-US'
    }

    params = urllib.parse.urlencode(params_json)

    response = requests.get(bingURL, params=params, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)
        bings = data.get('images', None)
        for item in bings:
            enddate = datetime.strptime(item.get('enddate'), '%Y%m%d')
            startdate = datetime.strftime(enddate,'%Y-%m-%d')
            url = 'https://www.bing.com' + item.get('url', None)
            title = item.get('copyright', None)

    wallpaper = Bing(url=url, title=title, pub_date=startdate)

    return wallpaper
