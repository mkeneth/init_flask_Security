from flask import Flask, render_template, redirect, url_for, g
from dotenv import load_dotenv

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# VARIABLE PARAMETERS
load_dotenv('.env')

# Configurations
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('settings.py')
app.debug = True

# Define the database object which is imported
db = SQLAlchemy(app)

# Build the database:
db.create_all()

@app.route("/")
def hello():
    return render_template("home.html")
