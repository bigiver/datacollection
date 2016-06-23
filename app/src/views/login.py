from flask import render_template, url_for , redirect, request
from flask.ext.login import login_user
from . import views

from ..forms.loginForm import LoginForm

from ..models.user import User, Role


@views.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            return redirect(url_for('index'))
    return render_template('login.html',title='Sign In', form=form)