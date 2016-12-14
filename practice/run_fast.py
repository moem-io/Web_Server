from flask import Flask # WSGI(Web Server Gateway Interface) : 인터페이스 정의 규칙
from flask import url_for
from flask import request
from flask import render_template
from flask import Markup
# from werkzeug import secure_filename
from flask import make_response
from flask import abort, redirect
from flask import session, escape

import os

app = Flask(__name__)
app.debug = True

#세션
@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' %escape(session['username'])
    return 'U r not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return 0

@app.route('/logout')
def logout():
    session.pop('username', None)
    return  redirect(url_for('index'))
app.secret_key = os.urandom(24)

#쿠키
@app.route('/')
def hello_world():
    #쿠키 읽기
    username = request.cookies.get('username')
    #쿠키 저장
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return 'Hello World!'+Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'+Markup.escape('<blink>hacker</blink>')+Markup('<em>Marked up</em> &raquo; HTML').striptags()

#리디렉션
@app.route('/')
def index():
    return redirect(url_for('login'))

#일찍 중단
@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()

#에러페이지
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

#<>로 정보받기
@app.route('/user/<username>/')
def show_user_profile(username):
    return 'User %s' %username
@app.route('/post/<int:post_id>/')
def show_post(post_id):
    return 'Post %d' %post_id

#로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    searchword = request.args.get('key', '')
    if request.method == 'POST':
        # print('POST')
        # return 'POST'
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            # print('GET')
            # return 'GET'
            error = 'Invalid username/password'

    return render_template('login.html', error=error)

#파일
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
        # f.save('/var/www/uploads/' + secure_filename(f.filename)

#값 넘기기
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

#라우팅이 설정된 함수의 URL을 얻기위해 실제 요청처럼 처리
with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('show_user_profile', username='Jhon'))
    print(url_for('login', next='/'))
    print(url_for('static', filename='style.css'))

#ToDO ?
with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'

#ToDo ?
# with app.request_context(environ):
#     assert request.method == 'POST'

#TODO ? 메시지 플래싱?

#로깅
app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')

#미들웨어에서 후킹
from werkzeug.contrib.fixers import LighttpdCGIRootFix
app.wsgi_app = LighttpdCGIRootFix(app.wsgi_app)

#실행
if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0')