from flask import request
from models import usersform as Users
from models import registeruser 

def RegisterNewUser():
    createUser = registeruser.NewUserForm()
    if createUser.validate_on_submit():
        new_user = registeruser(
            firstName = request.form['username'], # TODO add new field in database
            lastName = request.form['username'], # TODO add new field in database
            email = request.form['username'], # TODO add new field in database
            username = request.form['username'], # TODO add new field in database
            password = request.form['password'], # TODO add new field in database
            confirmPassword = request.form['username'], # TODO add new field in database
        )
        Users.Users.session.add(new_user)
        Users.Users.session.commit()
    return