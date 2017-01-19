from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# configuration
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

my_string = "hi world!!"
my_list = [1,2,3]

@app.route('/')
def index():
    return render_template('jinja_test.html', my_string=my_string, my_list=my_list)

if __name__ == '__main__':
    app.run()

