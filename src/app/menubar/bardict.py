from flask import render_template, make_response, send_from_directory
from app import log
from app.menubar import bar


@bar.route('/dict')
def bar_dict():
    return render_template('menubar/bar_dict.html', title='bar_dict')
