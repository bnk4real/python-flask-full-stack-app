from flask import redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from models import usersform as Users

class LoginForm(FlaskForm):
    username = StringField("")
    password = StringField("")
    submit = SubmitField("Submit")

def Login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        username = loginForm.username.data
        password = loginForm.password.data
        user = Users.query.filter_by(username=username).first()
        if user:
            if password == user.password:
                flash('Login successful!', 'success')
                return redirect(url_for('admin'))
            else:
                flash('Incorrect password. Please try again.', 'error')
        else:
            flash('Username not found. Please register an account.', 'error')
    return loginForm