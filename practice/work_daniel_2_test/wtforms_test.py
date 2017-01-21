from flask import Flask, redirect, request, render_template, url_for
from wtforms import Form, BooleanField, StringField, PasswordField, validators


# configuration
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


class User():
    username = None
    email = None
    password = None

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        print(request.args.get("a"))
    else:
        print(request.form.get('email'))
        # print(request.form.email.data) # can't
    return render_template('login.html')


@app.route('/register_wtforms', methods=['GET', 'POST'])
def register_wtform():
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data, form.password.data)

        print("form.username.data : ", form.username.data)
        print('user.email : ', user.email)
        return redirect(url_for('login'))
    else:
        print("get")
        return render_template('register_wtforms.html', form=form)


@app.route('/')
def index():
    return 'hello world!!'


if __name__ == '__main__':
    app.run(port=5112)
