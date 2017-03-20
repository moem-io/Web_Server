from flask import render_template, session, url_for, request, redirect
from requests import post

from my_client.app import app
from my_client.routes.oauth import remote
from my_client.forms.board import writingForm


url = app.config['BASE_URL']+'upload'

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'remote_oauth' not in session:
        return remote.authorize(
            callback=url_for('authorized', _external=True)
        )

    upload_app = request.form.get('upload_app')
    payload = {'upload_app':upload_app}

    res = None
    if 'remote_oauth' in session:
        res = remote.post(url, data=payload)
    print('res', res.data.get('username'))

    return redirect(url_for('index'))














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