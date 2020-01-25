from flask import Flask

app = Flask(__name__)

####################
# Error handlers


####################
# Blueprints
from .routes import api
app.register_blueprint(api, url_prefix="/api")
