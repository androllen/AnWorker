#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time: 2020/01/13 00:25:39
# Contact: androllen#hotmail.com

from flask import render_template, make_response, send_from_directory
from app.tabbar import bp
from app import log
from app.config import Config


@bp.route('/game')
def game():
    return render_template('tabbar/game.html', title='game', tasklist=Config.TabBar)
