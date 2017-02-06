from my_server.app import db

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    ps = db.Column(db.String(80))

    def __init__(self, username, ps):
        self.username = username
        self.ps = ps

    def __repr__(self):
        return '<User %r>' %self.username

