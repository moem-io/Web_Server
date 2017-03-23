from flask import render_template, session, url_for, redirect
from requests import post

from my_client.app import app
from my_client.routes.oauth import remote
from my_client.forms.board import writingForm

# url = 'http://localhost:5000/board'
# url = 'http://13.124.19.161:5000/board'
# url_hub = 'http://13.124.19.161:5000/hub_status'
# url_hub = 'http://127.0.0.1:5000/hub_status'
# url_board = 'http://127.0.0.1:5000/board'


@app.route('/')
def index():
    remote_me = None
    if 'remote_oauth' in session:
        remote_me = remote.get('me')
        # print('remote_me', remote_me.data.get('username'))
    username = None
    if remote_me:
        username = remote_me.data.get('username')
    # print(username)

    hub_info = None
    if username:
        # payload = {'username': username}
        # response = post(url_hub, json=payload)
        # print(response.text)
        # hub_info = response.text

        # print(str(res.text))
        # return render_template('index2.html', res=res.text)

        hub_info = remote.get('hub_info')
        print(hub_info.data)
        # test
        # payload = {'abc': 'def'}
        # test = remote.post('post_test', data=payload)
        # print(test.data['test'])

    data = None
    if username:
        data = {
            'username': username,
            'hub_status': hub_info.data['hub_status'],
            'hub_id': hub_info.data['hub_id'],
            'control': False
        }

    return render_template('index.html', data=data)

@app.route('/control/app')
def control_app():
    remote_me = None
    if 'remote_oauth' in session:
        remote_me = remote.get('me')
    username = None
    if remote_me:
        username = remote_me.data.get('username')

    data = {}
    data['username'] = username
    data['control'] = True
    return render_template('control_all.html', data=data)


@app.route('/control/log')
def control_log():
    remote_me = None
    if 'remote_oauth' in session:
        remote_me = remote.get('me')
    username = None
    if remote_me:
        username = remote_me.data.get('username')

    data = {}
    data['username'] = username
    data['control'] = True
    return render_template('control_log.html', data=data)


@app.route('/control/node')
def control_node():
    remote_me = None
    if 'remote_oauth' in session:
        remote_me = remote.get('me')
    username = None
    if remote_me:
        username = remote_me.data.get('username')

    data = {}
    data['username'] = username
    data['control'] = True
    return render_template('node.html', data=data)


#
@app.route('/make')
def make():
    remote_me = None
    if 'remote_oauth' in session:
        remote_me = remote.get('me')
    username = None
    if remote_me:
        username = remote_me.data.get('username')

    data = {}
    data['username'] = username
    return render_template('block.html', data=data)


@app.route('/control')
def control():
    return redirect(url_for('control_app'))


@app.route('/share')
def share():
    remote_me = None
    if 'remote_oauth' in session:
        remote_me = remote.get('me')
    username = None
    if remote_me:
        username = remote_me.data.get('username')

    data = {}
    data['username'] = username
    return render_template('share.html', data=data)





#
@app.route('/board', methods=['GET', 'POST'])
def board():
    form = writingForm()
    if form.validate_on_submit():
        title = form.title.data
        payload = {'title': title}
        # res = post(url, data=json.dumps(payload)) # 안 됨
        # res = post(url, data=payl oad) # 되긴 하는데 json아님
        res = post(url_board, json=payload)

        # Todo 여기 성공 실패 분기 해야 함
        print(res)

        # return render_template('control_app.html')
        return str(res.text)

    return render_template('board.html', form=form)
