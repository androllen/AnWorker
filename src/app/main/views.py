from flask import render_template, make_response, send_from_directory
from app.main import bp
from app import log


@bp.route('/')
def index():
    return render_template('main/index.html', title='Home')


@bp.route('/about')
def about():
    return render_template('main/about.html', title='About')
