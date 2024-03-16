from app import app
from flask import render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from models import registeruser, loginform
from models import usersform as Users
from database import database
from services import addnewuser
from services import login as newLogin
from services import register as newRegister

# # Define models
# class Users(db.Model):
#     userID = db.Column(db.String(80), primary_key=True)
#     uuid = db.Column(db.String(80), unique=True, nullable=True)
#     username = db.Column(db.String(80), unique=True, nullable=True)
#     password = db.Column(db.String(80), unique=True, nullable=True)
#     status = db.Column(db.String(80), unique=True, nullable=True)

class UserForm(FlaskForm):
    username = StringField("")
    password = StringField("")
    submit = SubmitField("Submit")
    
# class LoginForm(FlaskForm):
#     username = StringField("")
#     password = StringField("")
#     submit = SubmitField("Submit")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/add-new", methods=['GET', 'POST'])
def userPage():
    # addNewForm = UserForm()
    # if addNewForm.validate_on_submit():
    #     new_user = UserForm(
    #         username=request.form['username'],
    #         password=request.form['password'],
    #     )
    #     database.db.session.add(new_user)
    #     database.db.session.commit()
    addNewForm = addnewuser.AddNewUser()
    return render_template("add-user.html", addNewForm=addNewForm)

@app.route("/users")
def users():
    users = Users.Users.query.all()
    return render_template("users.html", users=users)

@app.route("/edit-user/<string:user_id>", methods=['GET', 'POST'])
def edit_user(user_id):
    user = Users.Users.query.get_or_404(user_id)
    form = UserForm(obj=user)
    if form.validate_on_submit():
        user.username = form.username.data
        user.password = form.password.data
        database.db.session.commit()
        flash('User details updated successfully!', 'success')
        return redirect(url_for('users'))
    return render_template("edit-user.html", form=form)

@app.route("/delete-user/<string:user_id>", methods=['POST'])
def delete_user(user_id):
    user = Users.Users.query.get_or_404(user_id)
    Users.Users.session.delete(user)
    Users.Users.session.commit()
    flash('User deleted successfully!', 'success')
    return redirect(url_for('users'))

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    # loginForm = loginform.LoginForm()
    # if loginForm.validate_on_submit():
    #     username = loginForm.username.data
    #     password = loginForm.password.data
    #     user = Users.Users.query.filter_by(username=username).first()
    #     if user:
    #         if password == user.password:
    #             flash('Login successful!', 'success')
    #             return redirect(url_for('admin'))
    #         else:
    #             flash('Incorrect password. Please try again.', 'error')
    #     else:
    #         flash('Username not found. Please register an account.', 'error')
    loginForm = newLogin.Login()
    return render_template("login.html", loginForm=loginForm)

@app.route("/register")
def register():
    # createUser = registeruser.NewUserForm()
    # if createUser.validate_on_submit():
    #     new_user = registeruser(
    #         firstName = request.form['username'], # TODO add new field in database
    #         lastName = request.form['username'], # TODO add new field in database
    #         email = request.form['username'], # TODO add new field in database
    #         username = request.form['username'], # TODO add new field in database
    #         password = request.form['password'], # TODO add new field in database
    #         confirmPassword = request.form['username'], # TODO add new field in database
    #     )
    #     Users.Users.session.add(new_user)
    #     Users.Users.session.commit()
    createUser = newRegister.RegisterNewUser()
    return render_template("register.html", register = createUser)