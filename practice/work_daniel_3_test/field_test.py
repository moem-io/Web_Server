import random

from flask_restful import Resource, fields, marshal_with, Api
from flask import Flask, request


app = Flask(__name__)
api = Api(app)


# resource_fields = {
#     'name': fields.String(attribute='private_name'),
#     'address': fields.String(default='Anonymous User'),
#     'date_updated': fields.String
#     'date_updated': fields.DateTime(dt_format='rfc822')
# }

class UrgentItem(fields.Raw):
    def format(self, value):
        return "urgent" if value & 0x01 else "Normal"

class UnreadItem(fields.Raw):
    def format(self, value):
        return "Unread" if value & 0x02 else "Read"

field = {
    'name': fields.String,
    'priority': UrgentItem(attribute='flags'),
    'status': UnreadItem(attribute='flags'),
}

class RandomNumber(fields.Raw):
    def output(self, key, obj):
        return random.random()

field2 = {
    'name': fields.String,
    # todo_resource is the endpoint name when you called api.add_resource()
    'uri': fields.Url('todo_resource'),
    'random': RandomNumber,
}


from flask_restful import marshal
import json

# resource_fields2 = {'name': fields.String}
# resource_fields2['address'] = {}
# resource_fields2['address']['line 1'] = fields.String(attribute='addr1')
# resource_fields2['address']['line 2'] = fields.String(attribute='addr2')
# resource_fields2['address']['city'] = fields.String
# resource_fields2['address']['state'] = fields.String
# resource_fields2['address']['zip'] = fields.String
# data = {'name': 'bob', 'addr1': '123 fake street', 'addr2': '', 'city': 'New York', 'state': 'NY', 'zip': '10468'}
# print('json : ', json.dumps(marshal(data, resource_fields2)))

address_fields = {}
address_fields['line 1'] = fields.String(attribute='addr1')
address_fields['line 2'] = fields.String(attribute='addr2')
address_fields['city'] = fields.String(attribute='city')
address_fields['state'] = fields.String(attribute='state')
address_fields['zip'] = fields.String(attribute='zip')

resource_fields = {}
resource_fields['name'] = fields.String
resource_fields['billing_address'] = fields.Nested(address_fields)
resource_fields['shipping_address'] = fields.Nested(address_fields)
address1 = {'addr1': '123 fake street', 'city': 'New York', 'state': 'NY', 'zip': '10468'}
address2 = {'addr1': '555 nowhere', 'city': 'New York', 'state': 'NY', 'zip': '10468'}
data = { 'name': 'bob', 'billing_address': address1, 'shipping_address': address2}
print(json.dumps(marshal_with(data, resource_fields)))


@api.resource('/')
class Index(Resource):
    @marshal_with(resource_fields, envelope='resource') # marshal is used when data is picked up from db
    def get(self, **kwargs):
        # resource_fields['name'] = kwargs.get('name')
        # print(kwargs['name'])
        return resource_fields



app.run(debug=True)
