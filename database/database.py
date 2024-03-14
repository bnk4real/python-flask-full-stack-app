from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Initialize SQLAlchemy
db = SQLAlchemy()  # Create SQLAlchemy instance

def init_app(app):
    app.config['SECRET_KEY'] = 'my_secret_key'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/db_development' # configure your OWN database system
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app) 