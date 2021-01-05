#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://blog.csdn.net/u011146423/article/details/87605812
# https://segmentfault.com/a/1190000017748417
# https://blog.csdn.net/weixin_44517681/article/details/88778812
# Time: 2020/01/15 18:56:15
# Contact: androllen#hotmail.com

from flask import render_template
from app import log
from app.model.tang import Tang
from app.tabbar import bp
from app.config import Config
from app.model.song import Song

@bp.route('/poetry')
def poetry():
    return render_template('tabbar/poetry.html', title='poetry', tasklist=Config.TabBar)


@bp.route('/song/<int:page>')
def song(page=None):
    if page is None:
        page = 1  
    model = Song()
    paginates = model.queryPerPage(page)
    totalpage = model.totalPage(paginates)
    return render_template('tabbar/poet-song.html', title='宋词', tasklist=Config.TabBar, paginate = paginates, posts = paginates.items, totalpage = totalpage)

@bp.route('/tang/<int:page>')
def tang(page=None):
    if page is None:
        page = 1  
    model = Tang()
    paginates = model.queryPerPage(page)
    totalpage = model.totalPage(paginates)    
    return render_template('tabbar/poet-tang.html', title='唐诗', tasklist=Config.TabBar, paginate = paginates, posts = paginates.items, totalpage = totalpage)   


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


