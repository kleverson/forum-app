from flask import Blueprint, abort, jsonify, render_template
from flask_restful import Resource

from forum.forms.form_user import LoginForm

home_bp = Blueprint('/home', __name__, url_prefix="/")


@home_bp.route('/')
def home():
    form = LoginForm()
    return render_template('home/default.html', form=form)
