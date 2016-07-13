from flask import render_template , url_for , redirect
from sqlalchemy import create_engine,func
from . import views
from .jdCamera_view import JDCamera
from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql://root:123456@localhost/datacollection?charset=utf8')
# engine = create_engine('mysql://root:123456@localhost/datacollection',connect_args={'charset':'utf8'})
Session = sessionmaker(bind=engine)
session = Session()


@views.route('/graphs', methods=['GET', 'POST'])
def graphs():

    data = session.query(JDCamera.brand, func.sum(JDCamera.comment)).group_by(JDCamera.brand).order_by(func.sum(JDCamera.comment).desc()).all

    print data
    return render_template('graphs.html', data=data)
