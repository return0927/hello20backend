from flask_restful import Resource
# from flask_sqlalchemy import

from ... import db, Post


class Posts(Resource):
    def get(self):
        return {
            "error": False,
            "data": Post.query.all()
        }, 200
