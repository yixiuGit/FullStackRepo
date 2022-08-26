from flask import Flask
from blueprint_poc.auth import bp as auth_bp
from blueprint_poc.api import bp as api_bp
from blueprint_poc.config import Config

# def create_app():
app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(auth_bp)
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)