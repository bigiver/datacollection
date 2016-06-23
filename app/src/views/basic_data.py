from flask import render_template , url_for , redirect

from . import views


@views.route('/basic_data', methods=['GET', 'POST'])
def basic_data():
    return render_template('basic_data.html')