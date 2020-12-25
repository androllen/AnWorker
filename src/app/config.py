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
    BASEDIR = os.path.dirname(APP_ROOT)
    # 数据库链接地址
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'hots.db')
    SQLALCHEMY_BINDS = {
        'poet':'sqlite:///' + os.path.join(BASEDIR, 'poet.db')
    }

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
        # https://chengyu.911cha.com/
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
    
    def tabPithy(self):
        file = self.APP_ROOT
        pithyPath = os.path.join(self.APP_ROOT, 'static/json/pithy.json')
        with open(pithyPath, 'r', encoding='utf-8') as file:
            jsonStr = json.load(file)

        data = json.dumps(jsonStr)
        return data
