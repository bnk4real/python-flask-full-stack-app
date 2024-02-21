from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 

# Secret Key!
app.config['SECRET_KEY'] = 'my_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/db_development' # configure your OWN database system
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

class Users(db.Model):
    userID = db.Column(db.String(80), primary_key=True)
    uuid = db.Column(db.String(80), unique=True, nullable=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    password = db.Column(db.String(80), unique=True, nullable=True)
    status = db.Column(db.String(80), unique=True, nullable=True)