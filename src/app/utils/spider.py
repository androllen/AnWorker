#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time: 2020/01/13 10:53:48
# Contact: androllen#hotmail.com

import requests
import urllib.request
import urllib.parse
import json
from datetime import datetime
from app.model.bing import Bing


def spider_bing():
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
    }
    bingURL = 'http://www.bing.com/HPImageArchive.aspx'

    params_json = {
        'format': 'js',
        'idx': -1,
        'n': 1,
        'pid': 'hp',
        'mkt': 'en-US'
    }

    params = urllib.parse.urlencode(params_json)
    try:
        response = requests.get(bingURL, params=params, headers=headers)

        if response.status_code == 200:
            data = json.loads(response.text)
            bings = data.get('images', None)

            for item in bings:
                enddate = datetime.strptime(item.get('enddate'), '%Y%m%d')
                startdate = datetime.strftime(enddate, '%Y-%m-%d')
                url = 'https://www.bing.com' + item.get('url', None)
                title = item.get('copyright', None)

        model = Bing(url=url, title=title, pub_date=startdate).insert()

    except Exception as e:
        print(e)

    return model


def get_bings():
    model = Bing().allmodel()
    return model
