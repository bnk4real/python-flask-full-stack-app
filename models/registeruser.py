from wtforms import StringField, SubmitField

class RegisterNewUser():
    FirstName: str
    LastName: str
    EmailAddress: str
    Password: str
    ConfirmPass: str


class NewUserForm():
    FirstName = StringField("")
    LastName = StringField("")
    EmailAddress = StringField("")
    Password = StringField("")
    ConfirmPass: StringField
    submit = SubmitField("Submit")