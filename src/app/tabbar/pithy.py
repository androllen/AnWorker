#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Time: 2020/01/15 15:58:52
# Contact: androllen#hotmail.com

from flask import render_template, make_response, send_from_directory
from app import log
from app.tabbar import bp
from app.config import Config


@bp.route('/pithy')
def pithy():
    return render_template('tabbar/pithy.html', title='pithy', tasklist=Config.TabBar)
