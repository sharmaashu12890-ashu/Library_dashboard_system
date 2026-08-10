from models import Borrow, User, Book
from extensions import db
from datetime import datetime


def register_user(name, email, password):
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return False, "Email already exists"
    user = User(
        name=name,
        email=email,
        password=password
    )
    db.session.add(user)
    db.session.commit()
    return True, "Registration Successful"


def get_all_users():
    return User.query.order_by(User.id.asc()).all()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def update_user(user_id, name, email):
    user = User.query.get(user_id)
    if not user:
        return False, "User Not Found"
    user.name = name
    user.email = email
    db.session.commit()
    return True, "User Updated Successfully"


def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return False, "User Not Found"
    db.session.delete(user)
    db.session.commit()
    return True, "User Deleted Successfully"


  
def add_book(title, author, category, quantity):
    exisiting_book = Book.query.filter_by(title=title).first()
    if exisiting_book:
        return False,"Book already exists"
    book = Book(
        title=title,
        author=author,
        category=category,
        quantity=quantity,
        available=quantity
    )
    db.session.add(book)
    db.session.commit()
    return True, "Book added successfully"


def get_all_books():
    return Book.query.all()


def get_book_by_id(book_id):
    return Book.query.get(book_id)


def update_book(book_id, title, author, category, quantity):
    book = Book.query.get(book_id)
    if not book:
        return False, "Book  ot found"
    issued = book.quantity - book.available
    book.title = title
    book.author = author
    book.category = category
    book.quantity = quantity
    book.available = quantity - issued
    if book.available < 0:
        book.available = 0
    db.session.commit()
    return True, "Book updated successfully"





def login_user(email, password):
    user = User.query.filter_by(email=email).first()
    if not user:
        return False, "Email not found", None
    
    if  user.password != password:
        return False, "Incorrect password", None
    
    return True, "Login successfully", user




# def borrow_book(user_id, book_id):

#     user = User.query.get(user_id)
#     book = Book.query.get(book_id)

#     if not user:
#         return False, "User not found."

#     if not book:
#         return False, "Book not found."

#     if book.available <= 0:
#         return False, "Book is not available."

    
#     existing_borrow = Borrow.query.filter_by(
#         user_id=user_id,
#         book_id=book_id,
#         status="Borrowed"
#     ).first()

#     if existing_borrow:
#         return False, "You already borrowed this book."


#     borrow = Borrow(
#         user_id=user_id,
#         book_id=book_id,
#         status="Borrowed"
#     )

#     db.session.add(borrow)

#     book.available -= 1

#     db.session.commit()

#     return True, "Book borrowed successfully."


def borrow_book(user_id, book_id):

    user = User.query.get(user_id)
    book = Book.query.get(book_id)

    if not user:
        return False, "User not found."

    if not book:
        return False, "Book not found."

    if book.available <= 0:
        return False, "Book is not available."

    # Check if user already borrowed this book
    existing_borrow = Borrow.query.filter_by(
        user_id=user_id,
        book_id=book_id,
        status="Borrowed"
    ).first()

    if existing_borrow:
        return False, "You already borrowed this book."

    # Create Borrow OBJECT
    borrow = Borrow(
        user_id=user_id,
        book_id=book_id,
        issue_date=datetime.utcnow(),
        status="Borrowed"
    )

    db.session.add(borrow)

    
    book.available -= 1

    db.session.commit()

    return True, "Book borrowed successfully."




def return_book(borrow_id):

    borrow = Borrow.query.get(borrow_id)

    if not borrow:
        return False, "Borrow record not found"

    if borrow.status == "Returned":
        return False, "This book is already returned"

    book = Book.query.get(borrow.book_id)

    if not book:
        return False, "Book not found"

    borrow.status = "Returned"
    borrow.return_date = datetime.utcnow()

    book.available += 1
    db.session.commit()

    return True, "Book returned successfully"


def delete_book(book_id):

    book = Book.query.get(book_id)

    if not book:
        return False, "Book not found"


    borrow_records = Borrow.query.filter_by(
        book_id=book_id
    ).first()

    if borrow_records:
        return False, "This book cannot be deleted because it has borrow records."

    db.session.delete(book)
    db.session.commit()

    return True, "Book deleted successfully"


def get_all_borrows():

    return Borrow.query.all()



def get_user_borrows(user_id):
    return Borrow.query.filter_by(user_id=user_id).all()

def get_active_borrows(user_id):

    borrows = Borrow.query.filter_by(
        user_id=user_id,
        status="Borrowed"
    ).all()

    return {
        borrow.book_id: borrow.id
        for borrow in borrows
    }


# def delete_book(book_id):
#     book = Book.query.get(book_id)
#     if not book:
#         return False, "Book not found"
#     db.session.delete(book)
#     db.session.commit()
#     return True, "Book deleted successfully"







