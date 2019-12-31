from flask import Flask
# from src import log as _log
from .exts import log
from .config import Config
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def Main():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    bootstrap.init_app(app)
 

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)


    log.logger.info('Microblog startup')

    return app
