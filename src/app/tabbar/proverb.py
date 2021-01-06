#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Time: 2020/01/15 18:56:19
# Contact: androllen#hotmail.com

from flask import render_template,request
from app import log
from app.model.proverb import Proverb
from app.tabbar import bp
from app.config import Config


@bp.route('/proverb/', methods=['GET'])
def proverb():
    args= request.args.get('search')

    if args is None:
        return render_template('tabbar/proverb.html', title='proverb', tasklist=Config.TabBar)
    
    model = Proverb()
    msg = model.queryModel(args)

    return render_template('tabbar/proverb.html', title='proverb', tasklist=Config.TabBar, posts = msg)