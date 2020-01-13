#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time: 2020/01/10 15:41:21
# Contact: androllen#hotmail.com

from flask import render_template, make_response, send_from_directory, redirect, url_for, request
from app import log
from app.utils import spider
from app.main import bp
from app.config import Config


@bp.route('/')
def index():
    bings = spider.spider_bing()

    return render_template(
        'main/index.html',
        title='Home',
        email=Config.EMAIL,
        tasklist=Config.TabBar,
        wallpaper=bings,
    )


@bp.route('/about/', methods=['POST', 'GET'])
def about():
    return render_template('main/about.html', title='about', tasklist=Config.TabBar)
