import bcrypt
from flask import Flask, render_template, request, redirect, session, url_for, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from project.models import Profile
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
    return 'Welcome to the Home Page'

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        hashed_password = generate_password_hash(password)
        
        # Create a new profile in the database
        new_profile = Profile(username=username, email=email, password=hashed_password)
        db.session.add(new_profile)
        db.session.commit()
        
        # Redirect to the login page
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Find the profile with the given username
        profile = Profile.query.filter_by(username=username).first()
        
        if profile and check_password_hash(profile.password, password):
            # Set the user's username in the session
            session['username'] = profile.username
            
            return redirect(url_for('views.dashboard', profile_id=profile.id))
        else:
            return 'Invalid username or password'
    
    # Move the render_template line inside the GET request block
    return render_template('login.html')


@auth.route('/logout')
def logout():
    # Remove the username from the session
    session.pop('username', None)
    
    return redirect(url_for('views.home'))
