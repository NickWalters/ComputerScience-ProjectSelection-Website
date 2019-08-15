import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'CITS3200Group22Project'
