from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class LoginForm(FlaskForm):
    username = StringField("")
    password = StringField("")
    submit = SubmitField("Submit")