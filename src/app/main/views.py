#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time: 2020/01/10 15:41:21
# Contact: androllen#hotmail.com

from flask import render_template, request
from app import log
from app.utils import spider
from app.main import bp
from app.config import Config
from app.exts import log

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

@bp.route('/bings', methods=['GET'])
def bings():
    log.logger.debug('requestMethod= % s', request.method)
    if request.method == "GET":
        paper = spider.get_bings()
        return render_template('main/bings.html', title='bings', paper=paper)
