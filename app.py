from flask import Flask
from config import Config
from extensions import db
from flask_migrate import Migrate
# from models import Book,User,Borrow
import models
from routes import routes

app = Flask(__name__)


app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app,db)

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)