from functools import wraps
from flask import render_template, session, url_for, request, redirect, jsonify
from requests import post, get

from my_client.app import app
from my_client.routes.oauth import remote
from my_client.forms.board import writingForm
import paho.mqtt.client as mqtt

import time

base_url = app.config['BASE_URL']
api_url = app.config['API_URL']

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # if 'remote_oauth' not in session:
    #     return remote.authorize(
    #         callback=url_for('authorized', _external=True)
    #     )

    upload_app_title = request.form.get('title')
    # print('title:', upload_app_title)
    upload_app_sub = request.form.get('sub_title')
    upload_app = request.form.get('upload_app')

    payload = {'upload_app_title': upload_app_title,
               'upload_app_sub': upload_app_sub,
               'upload_app': upload_app}

    res = None
    if 'remote_oauth' in session:
        res = remote.post(base_url+'upload', data=payload)
    else:
        res = post(api_url+'upload', data=payload)
        # print('res', jsonify(res.text).get('username'))

    # return redirect(url_for('index'))
    return redirect(request.referrer)


@app.route('/hub_register', methods=['GET', 'POST'])
def hub_register():
    if 'remote_oauth' not in session:
        return remote.authorize(
            callback=url_for('authorized', _external=True)
        )
    hub_register = remote.get('hub_register')
    return redirect(url_for('index'))


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)

    return decorated_function


@app.route('/test/mqtt', methods=['GET', 'POST'])
@login_required
def test_mqtt():
    res = get('https://api.moem.io/test/mqtt')
    return redirect(request.referrer)


    # post
    # res = None
    # if True:
    # response = post(url, json=payload)
    # print(response.text)
    # res = response.text
    # print(str(res.text))

    # return render_template('index2.html', res=res.text)
    # return render_template('index2.html', res=res)
    # data = {
    #     'username':username,
    #     'res':res,
    # }

    # return render_template('control_app.html', data=data)


@app.route('/switch/<int:id>')
def switch(id):
    # res = get(api_url+'switch/'+str(id))

    mqttc = mqtt.Client("python_pub")  # MQTT Client 오브젝트 생성
    mqttc.connect("13.124.19.161", 1883)  # MQTT 서버에 연결
    mqttc.publish("app/switch_toggle/00001214", id)  # 'hello/world' 토픽에 "Hello World!"라는 메시지 발행
    mqttc.loop(2)

    return redirect(request.referrer)


@app.route('/output/<int:id>')
def output(id):
    # res = get(api_url+'switch/'+str(id))

    mqttc = mqtt.Client("python_pub")  # MQTT Client 오브젝트 생성
    mqttc.connect("13.124.19.161", 1883)  # MQTT 서버에 연결
    mqttc.publish("app/output_toggle/00001214", id)  # 'hello/world' 토픽에 "Hello World!"라는 메시지 발행
    mqttc.loop(2)

    return redirect(request.referrer)
