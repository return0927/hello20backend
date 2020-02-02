from . import dbimport uuidclass User(db.Model):    __tablename__ = 'users'    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    uuid = db.Column(db.String(36), unique=True, default=str(uuid.uuid4()))    nick = db.Column(db.VARCHAR(20), nullable=False)    posts = db.relationship('Post', backref='user')    def to_json(self):        return {            'id': self.id,            'uuid': self.uuid,            'nick': self.nick,        }class Post(db.Model):    __tablename__ = 'posts'    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    content = db.Column(db.VARCHAR(length=4000), nullable=False)    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))    # author = db.relationship("User", backref=db.backref('posts'))    def to_json(self):        author: User = self.user        return {            'id': self.id,            'content': self.content,            'author': author.to_json()        }