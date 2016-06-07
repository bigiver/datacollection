from flask import Blueprint

views = Blueprint('views', __name__, template_folder='templates')

from . import calendar, stats, login