from flask import Flask, render_template
from src.views import views as stats_blueprint


app = Flask(__name__)

app.register_blueprint(stats_blueprint, url_prefix='/views')

app.config['SECRET_KEY'] = 'hard to guess string'


@app.route('/')
def main():
    return render_template('/index.html')


@app.route('/index')
def index():
    return render_template('/index.html')


if __name__ == '__main__':
    app.run()