from flask import Flask, render_template, redirect, url_for
from dotenv import load_dotenv

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc as error

# Flask_Security implementation module
from flask_security import Security, SQLAlchemyUserDatastore, \
                           login_required, current_user

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

# Defining Flask Email parameter ( Not Implemented in this Application )
mail = Mail(app)

# Applications import config Modules. 
from flask_secure.auth.models import Role, User
from flask_secure.auth.forms import ExtendedRegisterForm

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, register_form=ExtendedRegisterForm)

# Build the database:
db.create_all()
db.session.commit()

# Creating the roles for the respective users in the system.
try:
    db.session.flush()
    user_datastore.create_role(name='admin', description="Admin Right Used")
    user_datastore.create_role(name="user", description="Normal User Roles")
    db.session.commit()
except error.IntegrityError:
    db.session.rollback()


# =================== ALL CONFIGS ABOVE THE LINE. ============================

# Application Home Page Redirect after Login or Registration. 
@app.route("/")
@login_required
def home():
    user = current_user.email
    passwd = current_user.password
    name = current_user.username
    return render_template("home.html", user=user, passwd=passwd, username=name)