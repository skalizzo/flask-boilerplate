from flask import Flask, Response, jsonify

from app.home import home_bp
from app.posts.views.v1 import post_bp
from app.users.views.v1 import user_bp
from core.db import session
from core.exceptions import CustomException


def init_listeners(app: Flask) -> None:
    @app.after_request
    def after_request(response: Response) -> Response:
        session.remove()
        return response


def init_error_handler(app: Flask) -> None:
    @app.errorhandler(CustomException)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.code
        return response


def init_middlewares(app: Flask) -> None:
    pass


def init_blueprint(app: Flask) -> None:
    app.register_blueprint(home_bp)
    app.register_blueprint(post_bp, url_prefix='/api/v1/posts')
    app.register_blueprint(user_bp, url_prefix='/api/v1/users')


def init_extensions(app: Flask) -> None:
    pass


def create_app() -> Flask:
    app = Flask(__name__)
    init_blueprint(app=app)
    init_listeners(app=app)
    init_error_handler(app=app)
    return app
