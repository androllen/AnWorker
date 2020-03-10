#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Time: 2020/01/15 18:56:19
# Contact: androllen#hotmail.com

from flask import render_template, make_response, send_from_directory
from app import log
from app.tabbar import bp
from app.config import Config


@bp.route('/proverb')
def proverb():
    return render_template('tabbar/proverb.html', title='proverb', tasklist=Config.TabBar)