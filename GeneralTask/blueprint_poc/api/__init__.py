from flask import Blueprint

bp = Blueprint('api', __name__)

from blueprint_poc.api import api