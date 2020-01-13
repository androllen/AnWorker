#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://docs.jinkan.org/docs/flask/config.html
# Time: 2019/12/30 16:59:17
# Contact: androllen#hotmail.com
import os

class Config(object):

    DEBUG = True  # app.config["DEBUG"]
    EMAIL = "androllen#hotmail.com"
    TITLE = "-Wiki"

    APP_ROOT = os.path.dirname(os.path.abspath(__file__))

    TabBar = [{
        "id": 10,
        "title": "游戏",
        "url": "/game"
    }, {
        "id": 11,
        "title": "鸡汤",
        "url": "/soul"
    }, {
        "id": 12,
        "title": "中华古诗词",
        "url": "/dict"
    }, {
        "id": 13,
        "title": "成语大辞典",
        "url": "/word"
    }]
