from backend import app

app.run(
    host="0.0.0.0",
    port=80,
    threaded=True,
    debug=True
)
