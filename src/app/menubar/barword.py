#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Time: 2020/01/10 15:41:10
# Contact: androllen#hotmail.com


from flask import render_template, make_response, send_from_directory
from app.menubar import bar
from app import log


@bar.route('/word')
def bar_word():
    return render_template('menubar/bar_word.html', title='bar_word')
