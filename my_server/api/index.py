from flask_restful import Resource
from my_server.app import api

@api.resource('/')
class index(Resource):
    def get(self):
        return 'hello api server!!'

