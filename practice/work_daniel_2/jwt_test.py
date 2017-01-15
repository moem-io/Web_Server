from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import jwt


# configuration
DEBUG = True
secret = 'secret'


app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        encoded = jwt.encode({email:password}, secret, algorithm='HS256')
        return encoded

@app.route('/')
def index():
    return 'hellow'

if __name__ == '__main__':
    app.run()


