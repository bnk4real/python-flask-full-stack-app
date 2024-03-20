from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm


class NewUserForm(FlaskForm):
    FirstName = StringField("")
    LastName = StringField("")
    EmailAddress = StringField("")
    Password = PasswordField("")
    ConfirmPass = StringField("")
    submit = SubmitField("Submit")