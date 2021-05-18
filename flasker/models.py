from .mysql import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200))
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr(self):
        return "<Model User - {}>".format(self.username)


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    body = db.Column(db.Text)

    def __init__(self, title, body):
        self.title = title
        self.body = body

    def __repr(self):
        return "<Model Post - {}>".format(self.title)

