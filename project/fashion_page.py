from flask import Flask, render_template, request, Blueprint
import random
from flask import Flask, request, redirect, url_for
from project.models import Profile
from flask_login import current_user

fashion = Blueprint('fashion', __name__)

# Define the route for the main page
@fashion.route('/explore/<int:profile_id>', methods=['GET', 'POST'])
def home(profile_id):
    
    profile = Profile.query.get(profile_id)
    return render_template('explore.html',profile=profile, profile_id=profile_id)

# Define the route for the official pictures page
@fashion.route('/official/<int:profile_id>', methods=['GET', 'POST'])
def official(profile_id):
    
    profile = Profile.query.get(profile_id)
    return render_template('official.html', profile=profile, profile_id=profile_id)

# Define the route for the casual pictures page
@fashion.route('/casual/<int:profile_id>', methods=['GET', 'POST'])
def casual(profile_id):
    
    profile = Profile.query.get(profile_id)
    return render_template('casual.html', profile=profile, profile_id=profile_id)

# Define the route for the kids pictures page
@fashion.route('/kids/<int:profile_id>', methods=['GET', 'POST'])
def kids(profile_id):
    
    profile = Profile.query.get(profile_id)
    return render_template('kids.html', profile=profile, profile_id=profile_id)
