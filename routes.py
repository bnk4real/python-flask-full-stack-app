from app import app
from flask import render_template, redirect, url_for, flash
from models import loginform
from models import usersform as Users
from services import addnewuser
from services import login
from services import edituser
from services import deleteuser
    
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

# Edit user data TODO
@app.route("/edit-user/<int:user_id>", methods=['GET', 'POST'])
def edit_user(user_id):
    form = edituser.EditUser(user_id)
    if form.validate_on_submit():
        return redirect(url_for('users'))
    return render_template("edit-user.html", form=form)

# Delete user data
@app.route("/delete-user/<int:user_id>", methods=['POST'])
def delete_user(user_id):
    deleteuser.Delete(user_id)
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