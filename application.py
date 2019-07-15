from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine.url import URL
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://andre@localhost/local"

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(512))
    avatarUrl = db.Column(db.String(255))
    firstName = db.Column(db.String(255))
    lastName = db.Column(db.String(255))

    def __repr__(self):
        return '<User %r>' % self.username

