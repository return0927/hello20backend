from flask_restful import Resource
# from flask_sqlalchemy import

from ... import db, Post


class Posts(Resource):
    def get(self):
        print(Post.query.all())

        return {
            "error": False,
            "data": [
                {
                    "id": 1,
                    "author": {
                        "id": "<- UUID ->",
                        "nick": "고9마9웠어요"
                    },
                    "content": "<- AES Encrypted String ->"
                }
            ]
        }, 200
