from flask import Flask, redirect, request, render_template, url_for, session, jsonify
from flask_oauthlib.client import OAuth

from user import User
from registration import RegistrationForm

# oauth_server
# CLIENT_ID = 'zkuYDhPdCNFWtDIV0G7sqZF8B11AVadTGzNh6SY7'
# CLIENT_SECRET = 'ZbzRADpSV46ULHduImU9yVmMmnSCVZIHlsgLDlZkgaxr3eApR2'

# api_server_test
CLIENT_ID = '8raj6Vk9H5Q0gQEA3pe7Pq953MVbjKL7pWJ8cUJj'
CLIENT_SECRET = 'klP2FQUKVTvhpZNnXx8VBYTDjphnwAn9Oo9ibzzORAPdzf1HXU'

# configuration
# DEBUG = True
SECRET_KEY = 'my hi secret'

app = Flask(__name__)
app.config.from_object(__name__)
oauth = OAuth(app)

myssu = oauth.remote_app(
    'myssu',
    consumer_key=CLIENT_ID,
    consumer_secret=CLIENT_SECRET,
    request_token_params={'scope': 'email'},
    request_token_url=None,
    base_url='http://127.0.0.1:5000/api/',
    access_token_url='http://127.0.0.1:5000/oauth/token',
    authorize_url='http://127.0.0.1:5000/oauth/authorize',
    # base_url='https://api.yourssu.com/api/',
    # access_token_url='https://api.yourssu.com/oauth/token',
    # authorize_url='https://api.yourssu.com/oauth/authorize'
)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # next_url = request.args.get('next') or request.referrer or None
    next_url = None  # 왜 None일때만 되는가?
    print('next_url', next_url)
    return myssu.authorize(
        callback=url_for('authorized', next=next_url, _external=True)
    )


@app.route('/account/signup', methods=['GET', 'POST'])
def account_signup():
    next_url = None  # 왜 None일때만 되는가?
    print('next_url', next_url)
    return myssu.authorize(
        callback=url_for('authorized', next=next_url, _external=True)
    )


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


@app.route('/authorized')
def authorized():
    print('authorized')
    resp = myssu.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    print('resp', resp)
    session['remote_oauth'] = (resp['access_token'], '')
    return jsonify(oauth_token=resp['access_token'])


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    import os

    os.environ['DEBUG'] = 'true'
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = 'true'
    app.run(host='localhost', port=8000)
