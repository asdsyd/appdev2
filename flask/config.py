import os
from datetime import timedelta
MAIL_USERNAME = "wastemenmail@gmail.com"
MAIL_PASSWORD = "fijcovnxyhdodbbp"


basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True

SECRET_KEY = 'secretkey'
ADMIN_REGISTER_SECURITY_KEY= "4nNv3PPQQayr7Sj"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
JWT_ACCESS_TOKEN_EXPIRES=timedelta(days=30)
JWT_SECRET_KEY ='TICKETSHOW12345trhr'

UPLOAD_FOLDER =   os.path.join('static','posters')
USER_UPLOAD_FOLDER = os.path.join('static','propics')
MAX_CONTENT_PATH = 5000000
CELERY_BROKER_URL = "redis://localhost:6379/1"
CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
# CELERY_REDIS_USERNAME = 'default'
# CELERY_REDIS_PASSWORD = 'redispw'
CELERY_TIMEZONE = "Asia/Kolkata"

MAIL_SERVER ='smtp.gmail.com'
MAIL_PORT = 465
MAIL_DEFAULT_SENDER = ('Ticketer', MAIL_USERNAME)
MAIL_USE_TLS = False
MAIL_USE_SSL = True

