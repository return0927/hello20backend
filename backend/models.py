from . import dbclass User(db.Model):    __tablename__ = 'users'    id = db.Column(db.Integer, primary_key=True)    nick = db.Column(db.String(20), nullable=False)    posts = db.relationship('Post', backref='user')class Post(db.Model):    __tablename__ = 'posts'    id = db.Column(db.Integer, primary_key=True)    content = db.Column(db.VARCHAR(length=4000), nullable=False)    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))    # author = db.relationship("User", backref=db.backref('posts'))