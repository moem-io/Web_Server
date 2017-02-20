from flask import Flask

# configuration
DEBUG = True

app = Flask(__name__)
app.config.from_object('config')

from my_client.routes import *