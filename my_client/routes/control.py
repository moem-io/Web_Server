from flask import render_template, session
from requests import post

from my_client.app import app
from my_client.routes.oauth import remote
from my_client.forms.board import writingForm

@app.route('/')
def index():
    resp = None
    if 'remote_oauth' in session:
        resp = remote.get('upload')

    username = None
    if resp:
        username = resp.data.get('username')
    print(username)

    res = None
    if username:
        payload = {'username': username}
        response = post(url_hub, json=payload)
        print(response.text)
        res = response.text
        # print(str(res.text))

        # return render_template('index2.html', res=res.text)
    # return render_template('index2.html', res=res)
    data = {
        'username':username,
        'res':res,
    }
    return render_template('app.html', data=data)