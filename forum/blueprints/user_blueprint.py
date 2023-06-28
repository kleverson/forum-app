from flask import Blueprint, abort, jsonify, render_template, request
from flask_restful import Resource

from forum.forms.form_user import LoginForm, RegisterUser

user_bp = Blueprint('user', __name__, url_prefix="/user")


@user_bp.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        return render_template('user/login.html', form=form)
    else:
        return render_template('user/login.html', form=form)


@user_bp.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterUser()

    if request.method == "POST" and form.validate_on_submit():
        return render_template('user/register.html', form=form)
    else:
        return render_template('user/register.html', form=form)
