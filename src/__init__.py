from flask import Flask
# from src import log as _log
from src.log import Logger

log = Logger("anWorker.log", level='debug')

log.logger.debug("debug log")
log.logger.info("info log")
log.logger.warning("warning log")
