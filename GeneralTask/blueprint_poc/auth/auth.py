from blueprint_poc.auth import bp

@bp.route('/')
def index():
    return "This is an test"
    

@bp.route('/login')
def login():
    return "This is login"


@bp.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    return "This is sign up"
