from flask import Blueprint
bar = Blueprint('menubar', __name__)

from app.menubar import bardict, barword