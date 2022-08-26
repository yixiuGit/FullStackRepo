
from blueprint_poc.api import bp

@bp.route('/')
def index():
    return "This is an test"

@bp.route('/login')
def login():
    return "This is login page"

@bp.route("/register")
def register():
    return "This is register page"