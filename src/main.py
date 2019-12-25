#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Time: 2019/12/25 18:50:41
#Author: androllen
#Contact: androllen#hotmail.com

from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
   return "Hello world!"

if __name__ == "__main__":
  app.run()