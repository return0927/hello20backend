def handle_404(error):
    return {
        "error": True,
        "message": "Unsupported route"
    }, 200
