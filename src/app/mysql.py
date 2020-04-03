#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://spoprod-a.akamaihd.net/files/odsp-next-prod-amd_2020-03-06_20200316.004/odsp-media/images/error/error2.svg
# Time: 2020/03/10 12:35:13
# Contact: androllen#hotmail.com

from app import db

class Bing(db.Model):
  # 设置表名
    __tablename__ = 'bing'
  # 设置为主键之后，自动自增长
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(20), unique=True, nullable=False)
    title = db.Column(db.Text, nullable=True)
    pub_date = db.Column(db.String(), nullable=True)

    def __repr__(self):
        return self.name
