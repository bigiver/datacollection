from flask import render_template , url_for , redirect, request

from . import views
from .jdCamera_view import JDCamera


@views.route('/basic_data', methods=['GET', 'POST'])
def basic_data():
    page = request.args.get('page', 1, type=int)
    pagination = JDCamera.query.order_by(JDCamera.comment.desc()).paginate(page, per_page=20,error_out=False)

    jdc = pagination.items
    # print jdc
    return render_template('basic_data.html', jdc=jdc, pagination=pagination)
