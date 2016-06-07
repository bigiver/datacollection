#coding=utf-8
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    # 注册蓝本
    from src.views import views as stats_blueprint
    app.register_blueprint(stats_blueprint, url_prefix='/views')

    @app.route('/')
    def main():
        return render_template('/index.html')

    @app.route('/index')
    def index():
        return render_template('/index.html')

    return app