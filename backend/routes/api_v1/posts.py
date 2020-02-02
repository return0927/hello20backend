from flask_restful import Resource
# from flask_sqlalchemy import

from ... import db, Post

import traceback

from typing import List


class Posts(Resource):
    def get(self):
        try:
            posts: List[Post] = Post.query.all()

            return {
                "error": False,
                "data": [
                    x.to_json() for x in posts
                ]
            }, 200
        except:
            return {
                "error": True,
                "data": [],
                "message": traceback.format_exc()
            }
