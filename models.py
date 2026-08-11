
from extensions import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    author = db.Column(db.String(35), nullable=False)
    category = db.Column(db.String(40))
    quantity = db.Column(db.Integer, nullable=False)
    available = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


class Borrow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))
    issue_date = db.Column(db.DateTime, default=datetime.utcnow)
    return_date = db.Column(db.DateTime)
    status = db.Column(db.String(25), default="Borrowed")

    def __repr__(self):
        return f"<Borrow User:{self.user_id} Book:{self.book_id}>"

