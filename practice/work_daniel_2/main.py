from flask import Flask

# configuration # 얘는 없어도 됨
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return '<h1>hello world!!</h1>'

####
if __name__ == '__main__':
    app.run()