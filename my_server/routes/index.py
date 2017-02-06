from my_server.app import app

@app.route('/')
def index():
    return 'hello'