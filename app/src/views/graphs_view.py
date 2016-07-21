from flask import render_template , url_for , redirect
from sqlalchemy import create_engine,func
from . import views
from .jdCamera_view import JDCamera
from sqlalchemy.orm import sessionmaker
import json

engine = create_engine('mysql://root:123456@localhost/cameraSalesDB?charset=utf8')
# engine = create_engine('mysql://root:123456@localhost/datacollection',connect_args={'charset':'utf8'})
Session = sessionmaker(bind=engine)
session = Session()


@views.route('/graphs', methods=['GET', 'POST'])
def graphs():

    data = session.query(JDCamera.brand, func.sum(JDCamera.comment)).group_by(JDCamera.brand).order_by(func.sum(JDCamera.comment).desc())
    brands = []
    counts = []
    # print data
    for d in data:

        # print d[1]
        # print d[0]
        brands.append(d[0])
        counts.append(float(d[1]))

    # print brands,counts
    return render_template('graphs.html', brands=json.dumps(brands), counts=counts)
