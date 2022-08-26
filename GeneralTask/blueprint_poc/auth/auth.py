from flask import render_template
from blueprint_poc.auth import bp

@bp.route('/')
def index():
    # return "This is an test"
    return render_template("base.html")

@bp.route('/login')
def login():
    return render_template("login.html")


@bp.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    return render_template("sign_up.html")