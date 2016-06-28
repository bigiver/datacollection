#coding=utf-8
from app import db


class JDCamera(db.Model):

    __tablename__ = "JDCameras"

    id = db.Column(db.Integer, primary_key=True)
    sku_id = db.Column(db.String(40))
    price = db.Column(db.Float(2))
    product_name = db.Column(db.String(200))
    shop_name = db.Column(db.String(200))
    brand = db.Column(db.String(40))
    comment = db.Column(db.Integer)
