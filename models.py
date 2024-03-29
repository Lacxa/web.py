from _int_ import db
from flask_login import UserMixin

class Note(db.Model):
    id = db.Column(db.Integer, Primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.Foreignkey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    Password = db.Column(db.String(150))
    FirstName = db.Column(db.String(150))
    notes = db.relationship('Note')