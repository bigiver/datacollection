#coding=utf-8
from flask import Flask,render_template,url_for,redirect
from flask.ext.sqlalchemy import SQLAlchemy
import json
# from ..models.jdCamera import JDCamera

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/datacollection'
db = SQLAlchemy(app)
# from app import db


class JDCamera(db.Model):

    __tablename__ = "JDCameras"
    id = db.Column(db.Integer, primary_key=True)
    sku_id = db.Column(db.String(40))
    price = db.Column(db.Float(2))
    product_name = db.Column(db.String(200))
    shop_name = db.Column(db.String(200))
    brand = db.Column(db.String(40))
    comment = db.Column(db.Integer)


class DataTool:

    def __init__(self):
        pass

    def import_data(self):

            # print url_for('jdDataList.json')
        with open('jdDataList.json', 'r') as j:
            jdCameras = json.load(j)

        # print jdCameras
        for jdcList in jdCameras:
            # print jdcList
            # jdcDics = jdcList
            for jdcDic in jdcList:
                # print jdcDic.get('productName')
                jdCamera = JDCamera(sku_id=jdcDic.get('skuid'), price=jdcDic.get('price'),
                                    product_name=jdcDic.get('productName'),
                                    shop_name=jdcDic.get('shop'),
                                    brand=jdcDic.get('brand'), comment=jdcDic.get('comment'))
                db.session.add(jdCamera)
                db.session.commit()




if __name__=='__main__':
    dt = DataTool()
    dt.import_data()