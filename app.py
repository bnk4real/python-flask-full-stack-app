from flask import Flask
from database import database

app = Flask(__name__) 

# # Secret Key!
app.config['SECRET_KEY'] = 'my_secret_key'

# Configure MySQL connection
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/db_development' # configure your OWN database system
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Import routes
from routes import *

# Initialize the application with SQLAlchemy
database.init_app(app)

if (__name__) == "__main__":
    app.run(debug=True)