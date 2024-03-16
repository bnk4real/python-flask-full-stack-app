from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from database import database

class Userform(FlaskForm):
    username = StringField("")
    password = StringField("")
    submit = SubmitField("Submit")

def AddNewUser():
    
    addNew = Userform()
    
    if addNew.validate_on_submit():
        new_user = Userform(
            username=request.form['username'],
            password=request.form['password'],
        )
        database.db.session.add(new_user)
        database.db.session.commit()
    
    return addNew