import binascii
import os
from flask import Blueprint, abort, flash, jsonify, render_template, request
from flask_login import LoginManager, login_user
from werkzeug.security import generate_password_hash

from forum.forms.form_user import LoginForm, RegisterUser
from forum.models.User import User
from forum.ext.database import db
# from forum.ext.login import login_user

user_bp = Blueprint('user', __name__, url_prefix="/user")


@user_bp.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        print(form.email.data)
        user = User.find_by_username(form.email.data)
        if user is not None and User.verify_hash(user.password, form.password.data):
            login_user(user)
            return render_template('home/default.html')
        else:
            flash('error', 'Verify form field')
            return render_template('user/login.html', form=form)
    else:
        return render_template('user/login.html', form=form)


@user_bp.route('/register', methods=["GET", "POST"])
def register():

    form = RegisterUser()
    if request.method == "POST" and form.validate_on_submit():
        checkUser = User.query.filter_by(username=form.email.data).first()

        if (checkUser):
            flash("This user already registered!", "info")
            return render_template('user/register.html', form=form)
        else:
            db.session.add(User(
                name=form.name.data,
                username=form.email.data,
                password=form.password.data,
                active=False
            ))
            db.session.commit()
            return render_template('user/register.html', form=form)
    else:
        flash('error', 'Verify form field')
        return render_template('user/register.html', form=form)


@user_bp.route('/profile', methods=["GET", 'POST'])
def profile():
    return render_template('user/profile.html')
