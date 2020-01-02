from flask import render_template, make_response, send_from_directory
from app.main import bp
from app import log


@bp.route('/')
def index():
    data = [{"id": 10, "name": "中华古诗词"},
            {"id": 11, "name": "成语大辞典"}]
    return render_template('main/index.html', title='Home', tasklist=data)


@bp.route('/about')
def about():
    return render_template('main/about.html', title='About')
