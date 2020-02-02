from flask import Blueprint
from flask_restful import Api


api_v1 = Blueprint('api_v1', __name__, template_folder="templates")
api = Api(api_v1)

####################
# Error handlers
from .error_handlers import handle_404
api_v1.register_error_handler(404, handle_404)


####################
# Api Routes
from .ping import api_ping
from .posts import Posts

api.add_resource(Posts, '/posts')
