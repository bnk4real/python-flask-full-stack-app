from database import database

class Users(database.db.Model):
    userID = database.db.Column(database.db.String(80), primary_key=True)
    uuid = database.db.Column(database.db.String(80), unique=True, nullable=True)
    username = database.db.Column(database.db.String(80), unique=True, nullable=True)
    password = database.db.Column(database.db.String(80), unique=True, nullable=True)
    status = database.db.Column(database.db.String(80), unique=True, nullable=True)
    