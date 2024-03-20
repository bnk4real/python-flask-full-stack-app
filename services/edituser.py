from flask import redirect, url_for, flash
from models import usersform as Users
from database import database

def EditUser(user_id):
    user = Users.Users.query.get_or_404(user_id)
    form = Users.UserForm(obj=user)
    if form.validate_on_submit():
        user.username = form.username.data
        user.password = form.password.data
        database.db.session.commit()
        flash('User details updated successfully!', 'success')
    return form