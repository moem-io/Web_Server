from flask import Flask
import json
from flask import make_response
from flask_restful import Api
from flask_restful import fields, reqparse, Resource

app = Flask(__name__)
api = Api(app)

@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(json.dump(data), code)
    resp.headers.extend(headers or {})
    return resp

class AllCapsString(fields.Raw):
    def format(self, value):
        return value.upper()


def odd_number(value, name):
    if value % 2 == 0:
        raise ValueError("The parameter '{}' is not odd. You gave us the value: {}".format(name, value))

    return value

fields = {
    'name': fields.String,
    'all_caps_name': AllCapsString(attribute='name')
}
print(fields)

print('odd_number', odd_number(5, 'hi'))

def task_status(value):
    statuses = [u"init", u"in-progress", u"completed"]
    return statuses.index(value)
# print('task_status', task_status(1))

# @api.resource('/')
# class index(Resource):
@app.route('/ab')
def index():
    parser = reqparse.RequestParser()
    parser.add_argument('OddNumber', type=odd_number)
    parser.add_argument('Status', type=task_status)
    args = parser.parse_args()
    return args

@api.representation('text/csv')
def output_csv(data, code, headers=None):
    pass


app.run(debug=True)