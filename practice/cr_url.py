from flask import Flask, url_for
from flask import render_template
from flask import Markup
from flask import request

app = Flask(__name__)
app.debug = True

#Markup
Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'

#templates
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/')
def index(): pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

@app.route('/user/<username>')
def profile(username): pass

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'

# with app.request_context(environ):
#     assert request.method == 'POST'

# with app.test_request_context():
    # print url_for('index')
    # print url_for('login')
    # print url_for('login', next='/')
    # print url_for('profile', username='John Doe')
    # print url_for('static', filename='style.css')


if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0')
