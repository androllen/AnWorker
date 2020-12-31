#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Time: 2020/01/15 18:56:15
# Contact: androllen#hotmail.com

from flask import render_template, make_response, send_from_directory
from app import log
from app.tabbar import bp
from app.config import Config

@bp.route('/poetry')
def poetry():
    return render_template('tabbar/poetry.html', title='poetry', tasklist=Config.TabBar)


@bp.route('/song')
def song():
    return render_template('tabbar/poet-song.html', title='宋词', tasklist=Config.TabBar)


@bp.route('/tang')
def tang():
    return render_template('tabbar/poet-tang.html', title='唐诗', tasklist=Config.TabBar)   


@bp.route('/sound')
def sound():
    return render_template('tabbar/poet-sound.html', title='声律', tasklist=Config.TabBar)


@bp.route('/poet')
def poet():
    return render_template('tabbar/poet-poet.html', title='诗经', tasklist=Config.TabBar)   


@bp.route('/three')
def three():
    return render_template('tabbar/poet-three.html', title='三字经', tasklist=Config.TabBar)


@bp.route('/edubook')
def edubook():
    return render_template('tabbar/poet-edubook.html', title='教科书', tasklist=Config.TabBar)           


