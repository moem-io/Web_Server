from flask import session, redirect, url_for

from my_client.app import app
from my_client.routes.oauth import remote


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    # next_url = request.args.get('next') or request.referrer or None
    next_url = None  # 왜 None일때만 되는가?
    print('next_url', next_url)
    return remote.authorize(
        callback=url_for('authorized', next=next_url, _external=True)
    )

@app.route('/signout')
def signout():
    session.pop('remote_oauth', None)
    # session.pop('id', None)
    return redirect(url_for('index'))


@app.route('/signup')
def signup():
    return redirect("http://127.0.0.1:5000/signup")

@app.route('/signdel')
def signdel():
    return redirect(url_for('index'))
