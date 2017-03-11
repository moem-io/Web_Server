from my_client.app import app
from flask import render_template, session, redirect, url_for
from requests import get, post, put, delete, Request

from my_client.forms.board import writingForm
from my_client.routes.oauth import remote

# url = 'http://localhost:5000/board'
# url = 'http://13.124.19.161:5000/board'
url_hub = 'http://13.124.19.161:5000/hub_status'
url_board = 'http://localhost:5000/board'

@app.route('/')
def index():
    resp = None
    if 'remote_oauth' in session:
        resp = remote.get('me')
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
    return render_template('index2.html', data=data)

@app.route('/board', methods=['GET', 'POST'])
def board():
    form = writingForm()
    if form.validate_on_submit():
        title = form.title.data
        payload = {'title': title}
        # res = post(url, data=json.dumps(payload)) # 안 됨
        # res = post(url, data=payl oad) # 되긴 하는데 json아님
        res = post(url_board, json=payload)

        #Todo 여기 성공 실패 분기 해야 함
        print(res)

        # return render_template('index.html')
        return str(res.text)

    return render_template('board.html', form=form)