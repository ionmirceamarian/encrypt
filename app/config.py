import os

class Config(object):    
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    def __init__(self):
        host = os.getenv("DB_URI", "localhost")
        port = os.getenv("DB_PORT", "3306")
        user = os.getenv("DB_USER", "root")
        pwd = os.getenv("DB_PASSWORD", "123123123")
        self.SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{pwd}@{host}:{port}/license_db'
