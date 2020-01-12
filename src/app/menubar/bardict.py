#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://blog.csdn.net/auserbb/article/details/80003381
# Time: 2020/01/10 15:41:00
# Contact: androllen#hotmail.com


from flask import render_template, make_response, send_from_directory
from app import log
from app.menubar import bp


@bp.route('/dict')
def bar_dict():
    return render_template('menubar/bar_dict.html', title='bar_dict')
