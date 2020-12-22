#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://docs.jinkan.org/docs/flask/config.html
# http://www.pythondoc.com/flask-sqlalchemy/config.html
# Time: 2019/12/30 16:59:17
# Contact: androllen#hotmail.com
import os
import json


class Config(object):

    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    DEBUG = True  # app.config["DEBUG"]
    EMAIL = "androllen#hotmail.com"
    TITLE = "-Wiki"

    # 数据库链接地址
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(os.path.dirname(APP_ROOT), 'hots.db')

    # 禁用追踪
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    SQLALCHEMY_TRACK_MODIFICATIONS=True

    #查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True


    TabBar = [{
        "id": 3,
        "title": "足迹",
        "url": "/map"
    }, {
        "id": 4,
        "title": "鸡汤",
        "url": "/soul"
    }, {
        "id": 5,
        "title": "中华古诗词",
        "url": "/poetry"
    }, {
        "id": 6,
        "title": "成语大全",
        "url": "/pithy"
    }, {
        "id": 7,
        "title": "中华大词典",
        "url": "/word"
    }, {
        "id": 8,
        "title": "歇后语",
        "url": "/proverb"
    }]

    # TabPithy =
    def tabPithy(self):
        content = None
        file = APP_ROOT
        with open(os.path.join(APP_ROOT, 'static/json/pithy.json'), 'r', encoding='utf-8') as file:
            jsonStr = json.load(file)

        data = json.dumps(jsonStr)
        return data
