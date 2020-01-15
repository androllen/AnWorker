#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time: 2020/01/10 15:41:10
# Contact: androllen#hotmail.com

from flask import render_template, make_response, send_from_directory
from app.tabbar import bp
from app import log
from app.config import Config


@bp.route('/word')
def bar_word():
    return render_template('tabbar/word.html', title='word', tasklist=Config.TabBar)
