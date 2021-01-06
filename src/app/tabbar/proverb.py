#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Time: 2020/01/15 18:56:19
# Contact: androllen#hotmail.com

from flask import render_template
from app import log
from app.model.proverb import Proverb
from app.tabbar import bp
from app.config import Config


@bp.route('/proverb')
def proverb():
    return render_template('tabbar/proverb.html', title='proverb', tasklist=Config.TabBar)


@bp.route('/getproverb/<data>', methods=['GET'])
def getproverb(data):
    # msg = Proverb.queryModel(data)
    log.logger.info(data)
    return render_template('tabbar/proverb.html', title='proverb', tasklist=Config.TabBar, content = "msg")