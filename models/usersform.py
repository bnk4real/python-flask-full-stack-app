from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from database import database

class Users(database.db.Model):
    userid = database.db.Column(database.db.Integer(), primary_key=True)
    uuid = database.db.Column(database.db.String(80), unique=True)
    email = database.db.Column(database.db.String(80), unique=True, nullable=True)
    username = database.db.Column(database.db.String(80), unique=True, nullable=True)
    password = database.db.Column(database.db.String(80), unique=True, nullable=True)
    firstname = database.db.Column(database.db.String(80), unique=True, nullable=True)
    lastname = database.db.Column(database.db.String(80), unique=True, nullable=True)

class UserForm(FlaskForm):
    uuid = StringField("")
    email = StringField("")
    username = StringField("")
    password = PasswordField("")
    firstname = StringField("")
    lastname = StringField("")
    submit = SubmitField("Submit")