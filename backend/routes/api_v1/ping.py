from . import api_v1


@api_v1.route('/ping', methods=["GET"])
def api_ping():
    return {
        "error": False,
        "message": "Pong!"
    }, 200
