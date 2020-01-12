from flask import Blueprint
bp = Blueprint('menubar', __name__)

from app.menubar import bardict, barword, soul, game
