from flask import *
import re
from flask_login import UserMixin, current_user, login_manager, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from forum.app import db, login_manager, app
from forum.model import User, Post, Comment
from sqlalchemy import select, func
from forum.utl import username_taken, email_taken, valid_username

""" User Profile Base View """
@login_required
@app.route('/user/<username>')
def user_profile(username):
    user = User.query.filter_by(username=username).first()
    user_id = current_user.id
    posts = Post.query.filter_by(user_id=user_id).all()
    comments = Comment.query.filter_by(user_id=user_id).all()
    return render_template('profile.html', user=user, posts=posts, comments=comments, titleFunc=get_post_title, countFunc=get_count)

""" Function to get post title for a comment, used in comment title in profile.html """
def get_post_title(post_id):
    comment_post = db.session.query(Post).filter(Post.id == post_id).first()
    comment_post_title = comment_post.title
    return comment_post_title

""" Funciton to get the count of a type of forum message """
def get_count(count_type):
    if count_type == "post":
        count = Post.query.filter_by(user_id=current_user.id).count()
    elif count_type == "comment":
        count = Comment.query.filter_by(user_id=current_user.id).count()
    else:
        count = 0
    return count