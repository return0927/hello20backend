from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

####################
# DB Models
from .models import *

####################
# Error handlers


####################
# Blueprints
from .routes import api
app.register_blueprint(api, url_prefix="/api")
