from flask import Blueprint

bp = Blueprint('auth', __name__)

from blueprint_poc.auth import auth