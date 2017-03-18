from flask import render_template, session
from requests import post

from my_client.app import app
from my_client.routes.oauth import remote
from my_client.forms.board import writingForm


url = 'http://13.124.19.161:5000/upload'


@app.route('/upload')
def upload():
    resp = None
    if 'remote_oauth' in session:
        resp = remote.get('upload')

    # username = None
    username = 'a'
    if resp:
        username = resp.data.get('username')
    print(username)

    res = None
    # if username:
    if True:
        payload = {'username': username}
        response = post(url, json=payload)
        print(response.text)
        res = response.text
        # print(str(res.text))

        # return render_template('index2.html', res=res.text)
    # return render_template('index2.html', res=res)
    data = {
        'username':username,
        'res':res,
    }
    return render_template('control_app.html', data=data)