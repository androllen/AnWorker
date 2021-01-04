#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Time: 2020/12/25 11:02:00
# Contact: androllen#hotmail.com

from app.exts import log, db
from app.config import Config


class Song(db.Model):

    __bind_key__ = 'poet'
    # 设置表名
    __tablename__ = 'song'

    # 设置为主键之后，自动自增长
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.Text, unique=True, nullable=False)
    notes = db.Column(db.Text, nullable=False)
    author = db.Column(db.Text, unique=True, nullable=False)
    paragraphs = db.Column(db.Text, unique=True, nullable=False)
    dynasty = db.Column(db.Text, unique=True, nullable=False)
    
    def queryPerPage(self,page=1):
        pagination = Song.query.paginate(page,per_page=Config.ARTISAN_POSTS_PER_PAGE)
        return pagination    