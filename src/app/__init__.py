from flask import Flask
from .exts import log
from .config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 生成 app
def Main():
    # app 是 Flask 类的实例
    app = Flask(__name__, instance_relative_config=True)

    # 加载配置
    app.config.from_object(Config)

    # 加载数据库
    db.init_app(app)
    
    # 注册main包到蓝图
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    # 注册菜单包到蓝图
    from app.tabbar import bp as bar_bp
    app.register_blueprint(bar_bp)

    log.logger.info('Microblog startup')

    return app

