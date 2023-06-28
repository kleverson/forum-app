from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SelectField, SelectMultipleField, \
    widgets, DateField, FileField


class LoginForm(FlaskForm):
    email = StringField(label="Username", name="email", validators=[validators.Length(
        min=4, max=255), validators.DataRequired(), validators.Email()])
    password = PasswordField(label="Password", name="password", validators=[validators.Length(
        min=4, max=25), validators.DataRequired()])


class RegisterUser(FlaskForm):
    name = StringField(label="Name", name="name", validators=[validators.Length(
        min=4, max=255), validators.DataRequired()])
    email = StringField(label="Username", name="email", validators=[validators.Length(
        min=4, max=255), validators.DataRequired(), validators.Email()])
    password = PasswordField(label="Password", name="password", validators=[validators.Length(
        min=4, max=25), validators.DataRequired()])
    confirm_password = PasswordField(label="Password", name="password", validators=[validators.Length(
        min=4, max=25), validators.DataRequired()])
