from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 

# Secret Key!
app.config['SECRET_KEY'] = 'my_secret_key'

# Configure MySQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/db_development' # configure your OWN database system
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define models
class Users(db.Model):
    userID = db.Column(db.String(80), primary_key=True)
    uuid = db.Column(db.String(80), unique=True, nullable=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    password = db.Column(db.String(80), unique=True, nullable=True)
    status = db.Column(db.String(80), unique=True, nullable=True)
    
class UserForm(FlaskForm):
    username = StringField("")
    password = StringField("")
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    username = StringField("")
    password = StringField("")
    submit = SubmitField("Submit")

# define app router
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

# Create user
@app.route("/add-new", methods=['GET', 'POST'])
def userPage():
    # define and send params
    # todo
    # implement uuid and userid generator when creating a new user
    addNewForm = UserForm()
    if addNewForm.validate_on_submit():
        if request.method == 'POST':
            new_user = Users(
                username=request.form['username'],
                password=request.form['password'],
            )
            db.session.add(new_user)
            db.session.commit()
        addNewForm = UserForm()
    return render_template("add-user.html", addNewForm=addNewForm)

# Get users
@app.route("/users")
def users():
    users = Users.query.all()
    return render_template("users.html", users=users)

# Edit
@app.route("/edit-user/<string:user_id>", methods=['GET', 'POST'])
def edit_user(user_id):
    user = Users.query.get_or_404(user_id)
    form = UserForm(obj=user)
    if form.validate_on_submit():
        user.username = form.username.data
        user.password = form.password.data
        db.session.commit()
        flash('User details updated successfully!', 'success')
        return redirect(url_for('users'))
    return render_template("edit-user.html", form=form)

# Delete
@app.route("/delete-user/<string:user_id>", methods=['POST'])
def delete_user(user_id):
    user = Users.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'success')
    return redirect(url_for('users'))

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        username = loginForm.username.data
        password = loginForm.password.data
        # Query the database to find a user with the given username
        user = Users.query.filter_by(username=username).first()
        if user:
            if password == user.password:
                flash('Login successful!', 'success')
                return redirect(url_for('admin'))  # Redirect to the desire page
            else:
                flash('Incorrect password. Please try again.', 'error')
        else:
            flash('Username not found. Please register an account.', 'error')
    return render_template("login.html", loginForm=loginForm)

@app.route("/register")
def register():
    return render_template("register.html")

if (__name__) == "__main__":
    app.run(debug=True)