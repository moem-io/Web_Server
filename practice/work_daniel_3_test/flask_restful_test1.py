from flask import Flask, request
from flask_restful import Resource, Api

# configuration
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)

# 이거 넣으면 작동 안함...........왜지?
# 이거 뭔지도 모르겠음
# parser = reqparse.RequestParser()
# parser.add_argument('rate', type=int, help='Rate to charge for this resource')
# args = parser.parse_args()

todos = {}

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class ToDoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

class Todo1(Resource):
    def get(self):
        # Default to 200 OK
        return {'task': 'Hello world'}

class Todo2(Resource):
    def get(self):
        # Set the response code to 201
        return {'task': 'Hello world'}, 201

class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}

# data formatting
from collections import OrderedDict
from flask_restful import fields, marshal_with

resource_fields = {
    'task': fields.String,
    'uri': fields.Url('todo_ep')
}

class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        self.status = 'active'


class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')



api.add_resource(HelloWorld,
    '/',
    '/hello')
api.add_resource(ToDoSimple, '/<string:todo_id>')

api.add_resource(ToDoSimple,
    '/todo/<int:todo_id>', endpoint='todo_ep') # endpoint가 뭔지 잘 모르겠음

if __name__ == '__main__':
    app.run()
