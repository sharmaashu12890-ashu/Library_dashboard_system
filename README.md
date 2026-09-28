# 📚 Library Dashboard

A web-based **Library Management Dashboard** built using **Flask, Jinja2, MySQL, and SQLAlchemy**.

This project allows users to register and log in, manage books, update book information, delete books, and view their personal book collection through a simple and user-friendly dashboard.

---

## 🚀 Features

- 🔐 User Registration
- 🔑 User Login and Logout
- 📚 Add/Register Books
- ✏️ Update Book Information
- 🗑️ Delete Books
- 📖 View Books
- 📋 View My Books
- 👤 User Profile
- 🖥️ Library Dashboard
- 🗄️ MySQL Database Integration
- 🔄 Database Migrations
- 🧩 Jinja2 Template Rendering
- 🛠️ SQLAlchemy ORM

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| Flask | Web framework |
| Jinja2 | HTML templating |
| MySQL | Database |
| SQLAlchemy | Database ORM |
| HTML5 | Frontend structure |
| CSS3 | Frontend styling |

---

## 📁 Project Structure

```text
Library_Dashboard_Project/
│
├── migrations/
│
├── screenshots/
│   ├── library_dashboard.png
│   ├── my_books.png
│   └── register_login.png
│
├── templates/
│   ├── base.html
│   ├── book_register.html
│   ├── book_update.html
│   ├── book.html
│   ├── delete.html
│   ├── login.html
│   ├── my_books.html
│   ├── register.html
│   ├── update.html
│   └── user.html
│
├── venv/
│
├── app.py
├── service.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

Clone this project using Git:

```bash
git clone <your-github-repository-url>
```

Navigate to the project directory:

```bash
cd Library_Dashboard_Project
```

---

## 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv venv
```

---

## 3. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

## 4. Install Required Libraries

Install the required Python packages:

```bash
pip install -r requirements.txt
```


# 🗄️ Database Configuration

This project uses **MySQL** as the database and **SQLAlchemy** as the ORM.

First, create a database in MySQL.

```sql
CREATE DATABASE library_dashboard;
```

Then configure the database connection in your Flask application.

Example:

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/library_dashboard"
```

Replace:

- `username` with your MySQL username
- `password` with your MySQL password
- `library_dashboard` with your database name

---

# ▶️ Run the Application

After activating the virtual environment and configuring the MySQL database, run:

```bash
python app.py
```

The application should start on:

```text
http://127.0.0.1:5000/
```

Open the URL in your browser to access the Library Dashboard.

---

# 📸 Screenshots

## 🏠 Library Dashboard

The main dashboard provides an overview of the library and available books.

![Library Dashboard](screenshots/library_dashboard.png)

---

## 📚 My Books

The **My Books** page allows users to view the books associated with their account.

![My Books](screenshots/my_books.png)

---

## 🔐 Register & Login

Users can register a new account and log in to access the library dashboard.

![Register and Login](screenshots/register_login.png)

---

# 📖 Application Pages

## 🔐 Authentication

The project provides authentication functionality through the following templates:

- `register.html` — User registration
- `login.html` — User login
- `user.html` — User information

---

## 📚 Book Management

The application provides several pages for managing books:

- `book.html` — Display book information
- `book_register.html` — Add/register a new book
- `book_update.html` — Update book information
- `delete.html` — Delete a book
- `update.html` — Update functionality
- `my_books.html` — Display books belonging to the current user

---

## 🧩 Jinja2 Templates

The project uses **Jinja2 templates** to dynamically render HTML pages.

The common layout is defined in:

```text
templates/base.html
```

Other pages extend or use the base template to maintain a consistent design throughout the application.

---

# 🐍 Backend

The backend of the application is developed using **Flask**.

Flask is responsible for:

- URL routing
- User authentication
- Form handling
- Book management
- Database operations
- Rendering Jinja2 templates
- Handling requests and responses

The main Flask application is:

```text
app.py
```

Additional application/service logic is contained in:

```text
service.py
```

---

# 🗄️ Database & SQLAlchemy

The project uses:

- **MySQL** for data storage
- **SQLAlchemy** for database interaction

SQLAlchemy provides an ORM layer that allows the application to work with database records using Python objects and models.

The application supports common CRUD operations:

```text
Create
Read
Update
Delete
```

These operations are used for managing library books and user-related data.

---

# 🔄 Database Migrations

Database migration files are stored in:

```text
migrations/
```

If you are using **Flask-Migrate**, you can create a migration using:

```bash
flask db migrate -m "Initial migration"
```

Apply the migration using:

```bash
flask db upgrade
```

---

# 🔐 Security

For production use, sensitive information should be stored using environment variables instead of being written directly into the source code.

For example:

```text
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
```

Do not commit the following to GitHub:

- Database passwords
- Secret keys
- API keys
- Other sensitive credentials

---

# 🎯 Project Workflow

The basic workflow of the application is:

```text
User
  │
  ▼
Register / Login
  │
  ▼
Library Dashboard
  │
  ├── View Books
  │
  ├── Add Book
  │
  ├── Update Book
  │
  ├── Delete Book
  │
  └── View My Books
  │
  ▼
MySQL Database
```

---

# 📂 Important Files

| File/Folder | Description |
|-------------|-------------|
| `app.py` | Main Flask application |
| `service.py` | Application/service logic |
| `templates/` | Jinja2 HTML templates |
| `migrations/` | Database migration files |
| `screenshots/` | Project screenshots |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

# 🔮 Future Improvements

Some possible improvements for this project include:

- 🔍 Book search functionality
- 📑 Pagination
- 🏷️ Book categories
- 📅 Book issue and return system
- 👥 Admin dashboard
- 📊 Library statistics
- 📱 Responsive mobile UI
- 🔒 Improved authentication and authorization
- ☁️ Cloud deployment
- 📧 Email notifications

---

# 👨‍💻 Author

**Your Name**

Built with ❤️ using:

**Flask • Jinja2 • MySQL • SQLAlchemy**

---

# ⭐ Support

If you like this project, consider giving the repository a ⭐ on GitHub.
