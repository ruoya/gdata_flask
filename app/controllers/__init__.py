__author__ = 'yanghuihui'

from flask import Blueprint

main = Blueprint('controllers', __name__, template_folder='templates')

from . import home
