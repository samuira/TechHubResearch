# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import StringField, PasswordField # BooleanField

# Import Form validators
from wtforms.validators import DataRequired, Email, EqualTo


# Define the login form (WTForms)

class LoginForm(FlaskForm):
    email = StringField('Email Address', [Email(), DataRequired(message='Forgot your email address?')])
    password = PasswordField('Password', [DataRequired(message='Must provide a password. ;-)')])
