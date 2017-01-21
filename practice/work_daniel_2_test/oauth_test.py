from oauthlib import oauth2
from flask_oauthlib import __author__
from flask import Flask
import this

# configuration
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


if __name__ == '__main__':
    app.run(port=5112)


