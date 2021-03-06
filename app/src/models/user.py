#coding=utf-8
# from flask import Flask,render_template,url_for,redirect
# from flask.ext.sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/datacollection'
# db = SQLAlchemy(app)
from app import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(320), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    def verify_password(self, password):
        return self.password == password


class Role(db.Model):

    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

if __name__ == '__main__':
    db.create_all()
    #新增
    inset = User(name='dajiang',password='123',email='dajiang@sina.com')
    db.session.add(inset)
    db.session.commit();
    user = User.query.all()
    user[1].email = 'dajiang@sina.com'
    print user[1].email
    # form = LoginForm()
    #
    # if form.validate_on_submit():
    #     user = User.query.fillter_by(email=form.email.data).first()
    #     if user is not None and user.verify_password(form.password.data):
    #         redirect(url_for('index.html'))
    # render_template('user/login.html', title='Sign In', form=form)