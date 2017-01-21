from flask import Flask, redirect, request, render_template, url_for
from user import User
from registration import RegistrationForm

# configuration
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

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
