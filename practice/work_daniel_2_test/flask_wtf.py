from flask_wtf import FlaskForm # ToDo import가 안돼...
from wtforms import StringField
from wtforms.validators import DataRequired
from flask import redirect, render_template, Flask

# configuration
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired])


@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)

if __name__ == '__main__':
    app.run()