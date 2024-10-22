import os
DEBUG = True
SECRET_KEY = 'secret_key' if DEBUG else os.environ['SECRET_KEY']
