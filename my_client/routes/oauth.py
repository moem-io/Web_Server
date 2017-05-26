from flask import redirect, request, url_for, session
from flask_oauthlib.client import OAuth
from functools import wraps

from my_client.app import app
from urllib.parse import urlparse, urlencode, parse_qs

# CLIENT_ID = 'LYOcOFFgXql56WH2xsh9nMYOcbd4TApeCZWgV5dd'
# CLIENT_SECRET = '2D83nYX1GdvGYSq1ejWFzkYVFNApffJzc6z3PEVfUEdSnWsVre'


CLIENT_ID = app.config.get('CLIENT_ID')
CLIENT_SECRET = app.config.get('CLIENT_SECRET')

oauth = OAuth(app)

base_url = app.config.get('BASE_URL')
access_token_url = app.config.get('ACCESS_TOKEN_URL')
authorize_url = app.config.get('AUTHORIZE_URL')

remote = oauth.remote_app(
    'remote',
    consumer_key=CLIENT_ID,
    consumer_secret=CLIENT_SECRET,
    request_token_params={'scope': 'email'},
    request_token_url=None,
    base_url=base_url,
    access_token_url=access_token_url,
    authorize_url=authorize_url,
    # base_url='https://api.yourssu.com/api/',
    # access_token_url='https://api.yourssu.com/oauth/token',
    # authorize_url='https://api.yourssu.com/oauth/authorize'
)


@remote.tokengetter
def get_oauth_token():
    return session.get('remote_oauth')





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

    next_url = request.referrer
    next_url = request.args.get('next')
    params = parse_qs(urlparse(request.referrer).query)
    next_url = params['next'][0] if 'next' in params else url_for('index')

    return redirect(url_for('index'))
