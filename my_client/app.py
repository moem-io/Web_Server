from flask import Flask

# configuration
DEBUG = True
SECRET_KEY = 'secret'

app = Flask(__name__)
app.config.from_object(__name__)

from my_client.routes import *