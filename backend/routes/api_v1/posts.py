from flask_restful import Resource, reqparse

from ... import db, Post

import traceback

from typing import List


class Posts(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('limit', type=int)
            parser.add_argument('author_id', type=int)

            args = parser.parse_args()
            author_id = args.get("author_id", 0)
            limit = args.get("limit", 100)

            if author_id:
                posts: List[Post] = Post.query.filter(Post.author_id == author_id).limit(limit).all()
            else:
                posts: List[Post] = Post.query.limit(limit).all()

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
