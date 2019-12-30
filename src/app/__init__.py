from flask import Flask
# from src import log as _log
from .exts import log
from .config import Config


def Main():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    log.logger.debug("start")
    return app
