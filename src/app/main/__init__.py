from flask import Blueprint
# 将 main 注册到蓝图,返回蓝图对象实例
bp = Blueprint('main', __name__)

from app.main import views
