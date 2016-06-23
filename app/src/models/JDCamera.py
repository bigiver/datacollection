#coding=utf-8
from app import db


class JDCamera:

    __tablename__ = "JDCameras"
    id = db.column(db.Integer, primary_key=True)
    skuid = db.column(db.String(40), uinique=True)
    price = db.column(db.Float(2))
    product_name = db.column(db.String(200))
    shop_name = db.column(db.String(200))
    brand = db.column(db.String(40))
    comment = db.column(db.Integer)
    