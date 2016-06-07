from flask import render_template , url_for , redirect

from . import views


@views.route('/calendar', methods=['GET', 'POST'])
def calendar():
    return render_template('views/calendar.html')