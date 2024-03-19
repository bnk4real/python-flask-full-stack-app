from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from database import database
from models import usersform as users
import uuid

def AddNewUser():
    addNewForm = users.UserForm()
    
    if addNewForm.validate_on_submit():
        new_user = users.Users(
            uuid=uuid.uuid1(),
            email=request.form['email'],
            username=request.form['username'],
            password=request.form['password'],
            firstname=request.form['firstname'],
            lastname=request.form['lastname'],
        )
        database.db.session.add(new_user)
        database.db.session.commit()
    
    return addNewForm