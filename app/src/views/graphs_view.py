from flask import render_template , url_for , redirect

from sqlalchemy import create_engine,func
engine = create_engine('mysql://root:123456@localhost/cameraSalesDB')

from . import views
from .jdCamera_view import JDCamera

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()


@views.route('/graphs', methods=['GET', 'POST'])
def graphs():

    data = session.query(JDCamera.brand, func.sum(JDCamera.comment)).group_by(JDCamera.brand)
    print type(data)
    return render_template('graphs.html', data=data)
