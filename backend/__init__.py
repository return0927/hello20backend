from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

####################
# Error handlers


####################
# Blueprints
from .routes import api
app.register_blueprint(api, url_prefix="/api")
