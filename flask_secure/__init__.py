import os
from flask import Flask, render_template, redirect, url_for, g
from dotenv import load_dotenv
from flask_security.forms import RegisterForm

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Flask_Security implementation module
from flask_security import Security, SQLAlchemyUserDatastore, \
                           login_required, current_user, LoginForm, url_for_security, \
                           RegisterForm

#Flask email config
from flask_mail import Mail

# VARIABLE PARAMETERS
load_dotenv('.env')

# Configurations
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('settings.py')
app.debug = True

# Define the database object which is imported
db = SQLAlchemy(app)

# Defining Flask Email parameter
mail = Mail(app)

# Applications import config Modules. 
from flask_secure.auth.models import Role, User

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Loop a try and except command to create default roles 
# Catch ERROR. " sqlalchemy.exc.IntegrityError: (pymysql.err.IntegrityError) "
"""
try:
    user_datastore.create_role(name='admin', description="Admin Right Used")
    user_datastore.create_role(name="user", description="Normal User Roles")
except (EnvironmentError, TypeError):
    pass
"""

# Build the database:
db.create_all()
db.session.commit()

# =================== ALL CONFIGS ABOVE THE LINE. ============================
# Log in Parameter for Flask_Security
@app.context_processor
def login_context():
    return {
        'url_for_security': url_for_security,
        'login_user_form': LoginForm(),
    }
# Registeration Form for Flask_Security
@app.context_processor
def login_context():
    return {
        'url_for_security': url_for_security,
        'register_user_form': RegisterForm(),
    }

# Application Home Page Redirect after Login or Registration. 
@app.route("/")
@login_required
def roles():
    user = current_user.email
    passwd = current_user.password
    return render_template("home.html", user=user, passwd=passwd)