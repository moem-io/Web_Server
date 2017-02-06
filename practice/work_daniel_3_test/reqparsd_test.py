from flask_restful import reqparse
from flask import Flask

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():

    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('rate', type=int, help='Rate cannot be converted')
    parser.add_argument('name', action='append')
    parser.add_argument('nami', dest='girl')
    parser.add_argument('User-Agent', location='headers')

    parser.add_argument('foo', type=int)
    parser_copy = parser.copy()
    parser_copy.add_argument('bar', type=int)
    parser_copy.replace_argument('foo', required=True, location='json')
    parser_copy.remove_argument('foo')


    args = parser.parse_args()
    print(args.rate, args.name, args['girl'], args.foo)

    return 'hi' + args.name[0]


app.run(debug=True)
