from flask import Flask

# configuration
DEBUG = True

app = Flask(__name__)
app.config.from_object('config')

app.config.update({
    'OAUTH1_PROVIDER_ENFORCE_SSL': False
})

from my_client.routes import *