from flask import redirect, url_for, flash
from models import usersform as Users
from models import loginform as newLogin

def LoginForm(loginForm):
    loginForm = newLogin.LoginForm()
    if newLogin.LoginForm.validate_on_submit(loginForm):
        username = loginForm.username.data
        password = loginForm.password.data
        user = Users.Users.query.filter_by(username=username).first()
        if user and user.password == password:
            flash('Login successful!', 'success')
            return True
        else:
            flash('Incorrect username or password.', 'error')
    return False