from app import app
from flask import render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from models import loginform
from models import usersform as Users
from database import database
from services import addnewuser
from services import login
from services import register as newRegister
    
class LoginForm(FlaskForm):
    username = StringField("")
    password = StringField("")
    submit = SubmitField("Submit")
    
# Home Page
@app.route("/")
def index():
    return render_template("index.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Create New User
@app.route("/add-new", methods=['GET', 'POST'])
def userPage():
    addNewForm = addnewuser.AddNewUser()
    return render_template("add-user.html", addNewForm=addNewForm)

# Get All Users
@app.route("/users")
def users():
    users = Users.Users.query.all()
    return render_template("users.html", users=users)

# Edit user data
@app.route("/edit-user/<int:user_id>", methods=['GET', 'POST'])
def edit_user(user_id):
    user = Users.Users.query.get_or_404(user_id)
    form = Users.UserForm(obj=user)
    if form.validate_on_submit():
        user.username = form.username.data
        user.password = form.password.data
        database.db.session.commit()
        flash('User details updated successfully!', 'success')
        return redirect(url_for('users'))
    return render_template("edit-user.html", form=form)

# Delete user data
@app.route("/delete-user/<string:user_id>", methods=['POST'])
def delete_user(user_id):
    user = Users.Users.query.get_or_404(user_id)
    Users.Users.session.delete(user)
    Users.Users.session.commit()
    flash('User deleted successfully!', 'success')
    return redirect(url_for('users'))

# Admin Panel
@app.route("/admin")
def admin():
    return render_template("admin.html")

# Authentication
@app.route("/login", methods=['GET', 'POST'])
def loginPage():
    loginForm = loginform.LoginForm() 
    if loginForm.validate_on_submit():
        if login.LoginForm(loginForm):
            return redirect(url_for('admin'))
    return render_template("login.html", loginForm=loginForm)

@app.route("/register")
def register():
    createUser = newRegister.RegisterNewUser()
    return render_template("register.html", register = createUser)