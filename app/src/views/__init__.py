from flask import Blueprint

views = Blueprint('views', __name__, template_folder='templates')

from . import basic_data, graphs, login