from my_client.app import app

if __name__ == '__main__':
    import os
    os.environ['DEBUG'] = 'true'
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = 'true'

    # app.run(host='0.0.0.0', port=8000, debug=True)
    # app.run(host='0.0.0.0', port=8000)
    app.run(host='0.0.0.0',port=8000, debug=True)