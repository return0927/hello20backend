from flask_restful import Resource, reqparse

from ... import db, Post as PostModel

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
                posts: List[PostModel] = PostModel.query.filter(PostModel.author_id == author_id).limit(limit).all()
            else:
                posts: List[PostModel] = PostModel.query.limit(limit).all()

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


class Post(Resource):
    def get(self, post_id: int):
        post: PostModel = PostModel.query.filter(PostModel.id == post_id).first()

        if post:
            return {
                "error": False,
                "data": post.to_json()
            }, 200
        else:
            return {
                "error": True,
                "data": [],
                "message": "No post found with id `{}`".format(post_id)
            }
