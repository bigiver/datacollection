from flask import render_template , url_for , redirect

from . import views


@views.route('/graphs', methods=['GET', 'POST'])
def graphs():
    return render_template('graphs.html')
