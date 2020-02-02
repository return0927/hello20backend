from flask_restful import Resource


class Posts(Resource):
    def get(self):
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
