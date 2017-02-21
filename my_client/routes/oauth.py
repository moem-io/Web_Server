from flask import Flask, redirect, request, render_template, url_for, session, jsonify
from flask_oauthlib.client import OAuth
from my_client.app import app

# CLIENT_ID = 'LYOcOFFgXql56WH2xsh9nMYOcbd4TApeCZWgV5dd'
# CLIENT_SECRET = '2D83nYX1GdvGYSq1ejWFzkYVFNApffJzc6z3PEVfUEdSnWsVre'


CLIENT_ID = app.config.get('CLIENT_ID')
CLIENT_SECRET = app.config.get('CLIENT_SECRET')

oauth = OAuth(app)

remote = oauth.remote_app(
    'remote',
    consumer_key=CLIENT_ID,
    consumer_secret=CLIENT_SECRET,
    request_token_params={'scope': 'email'},
    request_token_url=None,
    base_url=app.config.get('base_url'),
    access_token_url=app.config.get('access_token_url'),
    authorize_url=app.config.get('authorize_url'),
    # base_url='https://api.yourssu.com/api/',
    # access_token_url='https://api.yourssu.com/oauth/token',
    # authorize_url='https://api.yourssu.com/oauth/authorize'
)


@app.route('/authorized')
def authorized():
    print('authorized')
    resp = remote.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    print(resp)
    session['remote_oauth'] = (resp['access_token'], '')
    # return jsonify(oauth_token=resp['access_token'])
    return redirect(url_for('index'))

@remote.tokengetter
def get_oauth_token():
    return session.get('remote_oauth')
