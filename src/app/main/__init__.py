from flask import Blueprint
# 将main 蓝图,进行注册,返回蓝图对象实例
splash = Blueprint('main', __name__)

from app.main import views
