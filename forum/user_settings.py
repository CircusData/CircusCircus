"""
Matching merged Dev on 11/27
"""

from flask import *
import re
from flask_login import UserMixin, current_user, login_manager, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from forum.app import db, login_manager, app
from forum.model import User
from forum.utl import username_taken, email_taken, valid_username


""" 
Change Settings View
Base view that shows the user settings that can be changed and their action buttons
"""

@login_required
@app.route('/user_settings')
def user_settings():
    return render_template("user_settings.html")



""" Change Username View
login will be required for the view (request)
Will be a POST method I think, 
need to return to a user settings page - html (still going to /)
on error render user settings again with errors
"""


@login_required
@app.route('/user_settings/action_change_username', methods=['POST'])
def action_change_username():

    # Get the current user name and desired updated user name from the user_settings form
    update_username = request.form['new_username']

    # Check if new user name entered is valid
    errors = []
    retry = False
    if username_taken(update_username):
        errors.append("Username is already taken!")
        retry=True
    if not valid_username(update_username):
        errors.append("Username is not valid!")
        retry = True
    if retry:
        return render_template("user_settings.html", errors=errors)

    # Use sql alchemy session method to update username in db
    # db.session.execute("UPDATE User SET username = ? WHERE username = ?;", (update_username, current_username), )

    # Set the User object in session to new username
    current_user.username = update_username

    # Save changes to session db
    db.session.commit()

    # Send the user back to forum page
    # return render_template("user_settings.html", user=current_user)

    return redirect("/user_settings")


""" Change Email View
login will be required for the view (request)
Will be a POST method I think, 
need to return to a user settings page - html (still going to /)
on error redner user settings html with error this time
"""


@login_required
@app.route('/user_settings/action_change_email', methods=['POST'])
def action_change_email():

    # Get the current user name and desired updated user name from the user_settings form
    current_email = current_user.email

    # Get the current user name and desired updated user name from the user_settings form
    update_email = request.form['new_email']

    # Check if new user name entered is valid
    errors = []
    retry = False
    if email_taken(update_email):
        errors.append("Email is already taken!")
        retry=True
    if retry:
        return render_template("user_settings.html", errors=errors)

    # (Use sql alchemy session instead?) Update username
    # user.email = update_email

    # Use sql alchemy session method to update username in db
    # db.session.execute("UPDATE User SET email = ? WHERE email = ?;", (update_email, current_email), )
    current_user.email = update_email

    # Save changes to session db
    db.session.commit()

    # Send the user back to forum page
    # return render_template("user_settings.html", user=current_user)
    return redirect("/user_settings")


