from flask import Blueprint, render_template, redirect, request, url_for, flash, session

from service import (get_all_users, register_user, update_user, 
delete_user,get_user_by_id , add_book, get_all_books, 
get_book_by_id, update_book, delete_book,login_user,
borrow_book, get_all_borrows, get_user_borrows, return_book,get_active_borrows )


routes = Blueprint("routes",__name__)
@routes.route("/")
def home():
    return redirect(url_for("routes.login"))



@routes.route("/register", methods = ["GET","POST"])
def register():
    success = False
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        success, message = register_user(
            name,
            email,
            password
        )
        flash(message)
    if success:
        return redirect(url_for("routes.user_list"))
    return render_template("register.html")


@routes.route("/users")
def user_list():
    users = get_all_users()

    return render_template(
        "login.html",
        users=users
    )


@routes.route("/update/<int:user_id>", methods=["GET", "POST"])
def update(user_id):
    user = get_user_by_id(user_id)

    if not user:
        flash("User Not Found")
        return redirect(url_for("routes.user_list"))

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]

        success, message = update_user(
            user_id,
            name,
            email
        )

        flash(message)

        return redirect(url_for("routes.user_list"))

    return render_template(
        "update.html",
        user = user
    )

@routes.route("/delete/<int:user_id>")
def delete(user_id):
    success, message = delete_user(user_id)
    flash(message)
    return redirect(url_for("routes.user_list"))


# @routes.route("/books")
# def book_list():
#     books = get_all_books()
#     return render_template("book.html",books=books)

@routes.route("/books")
def book_list():

    if "user_id" not in session:
        flash("Please login first.", "danger")
        return redirect(url_for("routes.login"))

    books = get_all_books()

    user_id = session["user_id"]

    active_borrows = get_active_borrows(user_id)

    return render_template(
        "book.html",
        books=books,
        active_borrows=active_borrows
    )


@routes.route("/book/register", methods=["GET", "POST"])
def register_book():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        category = request.form["category"]
        quantity = int(request.form["quantity"])

        success, message = add_book(
            title,
            author,
            category,
            quantity
        )

        flash(message)

        if success:
            return redirect(url_for("routes.book_list"))

    return render_template("book_register.html")





@routes.route("/book/update/<int:book_id>", methods=["GET", "POST"])
def update_book_route(book_id):
    book = get_book_by_id(book_id)
    if not book:
        flash("Book not found")
        return redirect(url_for("routes.book_list"))

    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        category = request.form["category"]
        quantity = int(request.form["quantity"])

        success, message = update_book(
            book_id,
            title,
            author,
            category,
            quantity
        )

        flash(message)

        return redirect(url_for("routes.book_list"))

    return render_template(
        "book_update.html",
        book=book
    )




@routes.route("/book/delete/<int:book_id>")
def delete_book_route(book_id):
    success, message = delete_book(book_id)

    flash(message)
    return redirect(url_for("routes.book_list"))



# @routes.route("/login", methods = ["GET", "POST"])
# def login():
#     if request.method == "POST":
#         email = request.form["email"]
#         password = request.form["password"]

#         success, message, user = login_user(
#             email,
#             password
#         )   

#         flash(message)

#         session["user_id"] = user.id
#         session["user_name"] = user.name

#         return redirect(url_for("routes.book_list"))
#     return render_template("login.html")


@routes.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        success, message, user = login_user(
            email,
            password
        )

        if success:

            session["user_id"] = user.id
            session["user_name"] = user.name

            flash(message, "success")

            return redirect(url_for("routes.book_list"))

        else:

            flash(message, "danger")
    return render_template("login.html")



@routes.route("/borrow/<int:book_id>")
def borrow(book_id):
    if "user_id" not in session:
        flash ("Please login frist", "danger")
        return redirect(url_for("routes.login"))

    user_id = session["user_id"]

    success, message = borrow_book(
        user_id,
        book_id
    )

    flash(message, "success" if success else "danger")

    return redirect(url_for("routes.book_list"))


@routes.route("/return/<int:borrow_id>")
def return_borrow(borrow_id):

    if "user_id" not in session:
        flash("Please login first.", "danger")
        return redirect(url_for("routes.login"))

    success, message = return_book(borrow_id)

    flash(message, "success" if success else "danger")

    return redirect(url_for("routes.book_list"))


@routes.route("/my-books")
def my_books():

    if "user_id" not in session:
        flash("Please login first.", "danger")
        return redirect(url_for("routes.login"))

    user_id = session["user_id"]

    borrows = get_user_borrows(user_id)

    return render_template("my_books.html",borrows=borrows)


@routes.route("/logout")
def logout():

    session.clear()

    flash("Logged out successfully.", "success")

    return redirect(url_for("routes.login"))