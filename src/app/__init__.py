from flask import Flask
from .exts import log
from .config import Config


def Main():
    # app 是 Flask 类的实例
    app = Flask(__name__, instance_relative_config=True)
    # 配置文件
    app.config.from_object(Config)
    # 从根目录app文件夹下的 main 蓝图 导入 蓝图对象
    from app.main import splash as main_bp
    app.register_blueprint(main_bp)

    from app.menubar import bar as bar_bp
    app.register_blueprint(bar_bp)

    log.logger.info('Microblog startup')

    return app
