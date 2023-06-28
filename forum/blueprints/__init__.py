from flask import Blueprint
from flask_restful import Api

from forum.blueprints.home_blueprint import home_bp
from forum.blueprints.user_blueprint import user_bp

bp_app = Blueprint("app", __name__)


def init_app(app):
    # api.add_resource(HomeResource, "/")
    # api.add_resource(UserResource, "/user")
    app.register_blueprint(home_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(bp_app)
    # app.register_blueprint(bp_api)
