#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://github.com/yeliulee/PoisonWords
# Time: 2020/01/13 00:25:45
# Contact: androllen#hotmail.com

from flask import render_template, redirect, request, abort
from app.tabbar import bp
from app import log
from app.config import Config
from app.utils import souler


@bp.route('/soul')
def soul():
    # 判断请求来路域名，防止采集和盗链
    if '127.0.0.1' not in str(request.referrer):
        abort(403)
    else:
        msg = souler.soul()

    return render_template('tabbar/soul.html', title='soul', tasklist=Config.TabBar, message=msg)

# 防止直接获取到数据文件
@bp.route('/static/json/soul.json')
def not_allowed():
    abort(403)
