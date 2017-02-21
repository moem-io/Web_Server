import os

SECRET_KEY = os.environ['SECRET_KEY']
MYSQL_DB_NAME = os.environ['MYSQL_DB_NAME']
MYSQL_DB_ROOT = os.environ['MYSQL_DB_ROOT']
MYSQL_DB_PS = os.environ['MYSQL_DB_PS']

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']

base_url = os.environ['base_url']
access_token_url = os.environ['access_token_url']
authorize_url = os.environ['authorize_url']