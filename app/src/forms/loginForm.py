from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required

CSRF_ENABLED = True
SECRET_KEY = 'A STRING'


class LoginForm(Form):
    email = StringField('What is your name', validators=[Required()])
    password = PasswordField('password')
    remember = BooleanField('remember me')
    submit = SubmitField('Sign In')