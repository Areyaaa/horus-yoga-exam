import os
from datetime import timedelta

class Config:
    # Basic Flask Configuration
    SECRET_KEY = 'dev-secret-key'
    
    # Database Configuration
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/horus_yoga_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    
    # JWT Configuration
    JWT_SECRET_KEY = 'jwt-secret-key'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    
    # CORS Configuration
    CORS_HEADERS = 'Content-Type'
    
    @staticmethod
    def init_app(app):
        pass