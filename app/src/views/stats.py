from flask import render_template , url_for , redirect

from . import views


@views.route('/stats', methods=['GET', 'POST'])
def stats():
    return render_template('views/stats.html')
