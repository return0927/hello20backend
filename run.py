from backend import app, db
from backend.models import User, Post

# Migrate DB
db.create_all()

# Make templates
if not User.query.all():
    print("Creating test values")

    u = User(nick="고9마9웠어요")
    db.session.add(u)
    db.session.commit()

    p = Post(content="L E G E N O", author_id=u.id)
    db.session.add(p)
    db.session.commit()

app.run(
    host="0.0.0.0",
    port=80,
    threaded=True,
    debug=True
)
