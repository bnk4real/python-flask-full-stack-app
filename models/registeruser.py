from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm

class RegisterNewUser():
    FirstName: str
    LastName: str
    EmailAddress: str
    Password: str
    ConfirmPass: str


class NewUserForm(FlaskForm):
    FirstName = StringField("")
    LastName = StringField("")
    EmailAddress = StringField("")
    Password = StringField("")
    ConfirmPass = StringField("")
    submit = SubmitField("Submit")