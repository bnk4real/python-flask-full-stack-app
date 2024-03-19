from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField

class LoginForm(FlaskForm):
    username = StringField("")
    password = PasswordField("Password")
    submit = SubmitField("Submit")