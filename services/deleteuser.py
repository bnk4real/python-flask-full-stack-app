from flask import flash
from models import usersform as users

def Delete(user_id):
    user = users.Users.query.get_or_404(user_id)
    users.Users.session.delete(user)
    users.Users.session.commit()
    flash('User deleted successfully!', 'success')
    return