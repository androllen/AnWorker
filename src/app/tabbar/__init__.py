from flask import Blueprint
bp = Blueprint('tabbar', __name__)

from app.tabbar import bardict, barword, soul, game
