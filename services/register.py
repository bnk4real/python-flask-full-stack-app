from flask import request
from models import usersform as Users
from models import registeruser
import uuid

def RegisterNewUser():
    current_id = 1  # Initialize counter
    formatted_id = f"SSD{current_id:04d}"  # Format with leading zeros
    yield formatted_id  # Yield the generated ID
    current_id += 1  # Increment counter
    
    createUser = registeruser.NewUserForm()
    if createUser.validate_on_submit():
        new_user = registeruser(
            userId = current_id, # TODO userId
            uuId = uuid.uuid4(), # TODO random gen uuid
            email = request.form['email'], # TODO add new field in database
            username = request.form['username'], # TODO add new field in database
            password = request.form['password'], # TODO add new field in database
            firstName = request.form['firstname'], # TODO add new field in database
            lastName = request.form['lastname'], # TODO add new field in database
        )
        Users.Users.session.add(new_user)
        Users.Users.session.commit()
        
    return createUser