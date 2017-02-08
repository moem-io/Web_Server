from flask import Flask, redirect, request, render_template, url_for, session, jsonify
from flask_oauthlib.client import OAuth
from my_client.app import app

CLIENT_ID = 'Xi6k7bRQZf1XrQIqoYRL687QgByYht7O5K8Mijmz'
CLIENT_SECRET = 'HSdWIxtLtNmt6ET6hJn6ZluFu6yGTH13h3zEBedrK4dtXhOVLm'

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


@app.route('/authorized')
def authorized():
    print('authorized')
    resp = myssu.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    print(resp)
    session['remote_oauth'] = (resp['access_token'], '')
    return jsonify(oauth_token=resp['access_token'])
