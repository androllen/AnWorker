#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time: 2020/01/10 18:05:25
# Contact: androllen#hotmail.com

import time
import datetime
from .exts import log, db


class Bing(db.Model):

  # 设置表名
    __tablename__ = 'bings'

  # 设置为主键之后，自动自增长
    id = db.Column(db.Integer, primary_key=True, unique=True)
    url = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, unique=True, nullable=False)
    pub_date = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self):
        return 'Bing %r' % self.id

    def insert(self):
        try:
            model = Bing.query.filter(Bing.pub_date == self.pub_date).first()
            if model is None:
                model = Bing(url=self.url, title=self.title,
                             pub_date=self.pub_date)
                db.session.add(model)
                db.session.commit()

        except Exception as ex:
            db.session.rollback()
            log.logger.critical("exception %s", ex.message)
        finally:
            return model

    def allmodel(self):
        model = Bing.query.all()
        return model
