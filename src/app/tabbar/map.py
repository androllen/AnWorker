#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.html5tricks.com/demo/html5-css3-3d-rubik-cube/index.html
# https://www.html5tricks.com/demo/threejs-impact-checking/index.html
# https://www.html5tricks.com/demo/jquery-html5-card-game/index.html
# Time: 2020/01/13 00:25:39
# Contact: androllen#hotmail.com

from flask import render_template
from app.tabbar import bp
from app import log
from app.config import Config


@bp.route('/map')
def gomap():
    return render_template('tabbar/map.html', title='map', tasklist=Config.TabBar)
