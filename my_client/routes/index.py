from flask import render_template, session, url_for, redirect, jsonify, request
from requests import post, get

from my_client.app import app
from my_client.routes.oauth import remote
from my_client.forms.board import writingForm

from functools import wraps
from urllib.parse import urlparse, urlencode, parse_qs
import json
import paho.mqtt.client as mqtt
import time

api_url = app.config['API_URL']

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'remote_oauth' not in session:
            # return redirect(get_oauth_url())
            next_url = None  # 왜 None일때만 되는가?
            next_url = request.referrer
            next_url = 'http://127.0.0.1:8000/controll/app'
            # print('next_url', next_url)
            return remote.authorize(
                callback=url_for('authorized', next=next_url, _external=True)
            )
        return f(*args, **kwargs)

    return decorated_function

@app.route('/')
def index():
    remote_me = None
    if 'remote_oauth' in session:
        remote_me = remote.get('me')
        # return jsonify(remote_me.data)
        # print('remote_me', remote_me.data.get('username'))
    username = None
    if remote_me and remote_me.status == 200:
        username = remote_me.data.get('username')
        print('username', username)
    else:
        session.pop('remote_oauth', None)

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
    if remote_me and remote_me.status == 200:
        username = remote_me.data.get('username')
        # print('username', username)
    else:
        session.pop('remote_oauth', None)

    data = {}
    data['username'] = username
    data['control'] = True
    data['app'] = True

    mqttc = mqtt.Client("python_pub")  # MQTT Client 오브젝트 생성
    mqttc.connect("13.124.19.161", 1883)  # MQTT 서버에 연결
    mqttc.publish("control/app/00001214", 'get_app_status')  # 'hello/world' 토픽에 "Hello World!"라는 메시지 발행
    mqttc.loop(2)

    time.sleep(1)

    res = get(api_url + 'app_info')
    data.update(json.loads(res.text))
    # print('data', data['apps'])
    for i in data['apps']:
        # print('i', type(eval(json.dumps(i['app_input_detail']))))
        # i['app_input_detail'] = json.loads(json.dumps(i['app_input_detail']))
        # print('i', type(i['app_input_detail']))
        # print('i', i)
        # i['app_input_detail'] = json.loads(json.dumps(eval(i['app_input_detail'])))
        i['app_input_detail'] = eval(i['app_input_detail'])

    # print('data type', type(json.loads(res.text)))

    return render_template('control_all.html', data=data)


@app.route('/control/log')
def control_log():
    remote_me = None
    if 'remote_oauth' in session:
        remote_me = remote.get('me')

    username = None
    if remote_me and remote_me.status == 200:
        username = remote_me.data.get('username')
        # print('username', username)
    else:
        session.pop('remote_oauth', None)

    data = {}
    data['username'] = username
    data['control'] = True
    data['log'] = True

    mqttc = mqtt.Client("python_pub")  # MQTT Client 오브젝트 생성
    mqttc.connect("13.124.19.161", 1883)  # MQTT 서버에 연결
    mqttc.publish("control/app/00001214", 'get_app_status')  # 'hello/world' 토픽에 "Hello World!"라는 메시지 발행
    mqttc.loop(2)

    time.sleep(1)

    res = get(api_url + 'app_info')
    data.update(json.loads(res.text))
    # print('data', data['apps'])
    for i in data['apps']:
        # print('i', type(eval(json.dumps(i['app_input_detail']))))
        # i['app_input_detail'] = json.loads(json.dumps(i['app_input_detail']))
        # print('i', type(i['app_input_detail']))
        # print('i', i)
        # i['app_input_detail'] = json.loads(json.dumps(eval(i['app_input_detail'])))
        i['app_input_detail'] = eval(i['app_input_detail'])

    # print('data type', type(json.loads(res.text)))

    return render_template('control_all.html', data=data)


@app.route('/control/node')
def control_node():
    remote_me = None
    if 'remote_oauth' in session:
        remote_me = remote.get('me')

    username = None
    if remote_me and remote_me.status == 200:
        username = remote_me.data.get('username')
        # print('username', username)
    else:
        session.pop('remote_oauth', None)

    data = {}
    data['username'] = username
    data['control'] = True
    data['node'] = True

    mqttc = mqtt.Client("python_pub")  # MQTT Client 오브젝트 생성
    mqttc.connect("13.124.19.161", 1883)  # MQTT 서버에 연결
    mqttc.publish("control/app/00001214", 'get_app_status')  # 'hello/world' 토픽에 "Hello World!"라는 메시지 발행
    mqttc.loop(2)

    time.sleep(1)

    res = get(api_url + 'app_info')
    data.update(json.loads(res.text))
    # print('data', data['apps'])
    for i in data['apps']:
        # print('i', type(eval(json.dumps(i['app_input_detail']))))
        # i['app_input_detail'] = json.loads(json.dumps(i['app_input_detail']))
        # print('i', type(i['app_input_detail']))
        # print('i', i)
        # i['app_input_detail'] = json.loads(json.dumps(eval(i['app_input_detail'])))
        i['app_input_detail'] = eval(i['app_input_detail'])

    # print('data type', type(json.loads(res.text)))

    return render_template('control_all.html', data=data)



#
@app.route('/make')
def make():
    remote_me = None
    if 'remote_oauth' in session:
        remote_me = remote.get('me')

    username = None
    if remote_me and remote_me.status == 200:
        username = remote_me.data.get('username')
        print('username', username)
    else:
        session.pop('remote_oauth', None)

    res = get(api_url + 'ex_info')

    data = {}
    data['username'] = username
    data['ex_info'] = json.loads(res.text)

    # print(data)
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
    if remote_me and remote_me.status == 200:
        username = remote_me.data.get('username')
        print('username', username)
    else:
        session.pop('remote_oauth', None)

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




def get_oauth_url():

    params = {
        'response_type': 'code',
        'client_id': app.config.get('CLIENT_ID'),
        'redirect_uri': 'http://127.0.0.1:8000/authorized',
        'scope': 'email',
    }
    return "{0}?{1}".format(app.config.get('AUTHORIZE_URL'), urlencode(params))
