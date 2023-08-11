from flask.config import Config

class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = 'mysql:///user:password@localhostprod_db.db'
    SECRET_KEY = 'ErMJseKIzNPYRspdFA8Z8gXZWDA'
    PORT = 5000
    HOST = 'prod_host'
    

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'sqlite:///dev_db.db'
    SECRET_KEY = 'oYl4kfHrWiulmW4kd8BR6Q'
    PORT = 2310
    HOST = 'localhost'
    
