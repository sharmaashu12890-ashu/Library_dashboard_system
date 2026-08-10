import os
# from .env import *   
from dotenv import load_dotenv  
load_dotenv()  


class Config:
#     DB_USER =  os.getenv(DB_USER)
#     DB_PASSWORD =
#     DB_HOST
#     DB_NAME
#     SECRET_KEY




    DB_USER = "root"
    DB_PASSWORD = "ashishdb"
    DB_HOST = "localhost"
    DB_NAME = "library_db"
    SECRET_KEY = "ashish@123"



    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False   