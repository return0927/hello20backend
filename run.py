from backend import app

app.run(
    host="0.0.0.0",
    port=8000,
    threaded=True,
    debug=True
)
