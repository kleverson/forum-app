
from flask import redirect
from flask_login import LoginManager

from forum.models.User import User


def init_app(app):
    lm = LoginManager()
    lm.init_app(app)

    @lm.user_loader
    def load_user(id):
        return User.query.filter_by(id=id).first()

    @lm.unauthorized_handler
    def handle_needs_login():
        redirect('/')
