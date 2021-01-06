#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Time: 2020/12/26 11:02:00
# Contact: androllen#hotmail.com

from app.exts import log, db
from app.config import Config

class Proverb(db.Model):

    __bind_key__ = 'poet'
    # 设置表名
    __tablename__ = 'proverb'

    # 设置为主键之后，自动自增长
    id = db.Column(db.Integer, primary_key=True, unique=True)
    riddle = db.Column(db.Text, unique=True, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    
    def queryModel(self,key):
        if key=='':
            response =[]
            return response 
        list_key = Proverb.query.filter(Proverb.riddle.contains(key)).all()
        return list_key   
    

        