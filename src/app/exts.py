#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Time: 2019/12/30 10:53:58
# Contact: androllen#hotmail.com

from .log import Logger
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

log = Logger(level='debug', filename=_filename)
