from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence, and_, or_
from sqlalchemy.orm import sessionmaker, aliased

# configuration
# DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

engine = create_engine('sqlite:///:memory:', echo = True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password
        )
print(User.__table__)

Base.metadata.create_all(engine)

ed_user = User('simpson', 'homor simpson', '1234')
print(ed_user.name)

session = Session()
session.add(ed_user)

our_user = session.query(User).filter_by(name='simpson').first()
print(our_user)

print(ed_user is our_user)

ed_user.password = 'test1234'
print(session.dirty)

session.add_all([
    User('wendy', 'Wendy Williams', 'foobar'),
    User('mary', 'Mary Contrary', 'xxg527'),
    User('fred', 'Fred Flinstone', 'blar')]
)
print(session.new)

session.commit()


for instance in session.query(User).order_by(User.id):
    print(instance.name)
for row in session.query(User, User.name).all():
    print(row.User, row.name)
for row in session.query(User.name.label('my_label')).all():
    print(row.my_label)

user_alias = aliased(User, name='user_alias')
for row in session.query(user_alias, user_alias.name).all():
    print(row.user_alias)

for user in session.query(User).order_by(User.id)[1:3]:
    print(user)

for name in session.query(User.name).filter_by(fullname='Edward Kim'):
    print(name)

for name in session.query(User.name).filter(User.fullname=='Edward Kim'):
    print(name)

for fullname in session.query(User).filter(User.name == 'ed'):
    print(fullname)

for fullname in session.query(User).filter(User.name != 'ed'):
    print(fullname)

for fullname in session.query(User).filter(User.name.like('%ed')):
    print(fullname)

for fullname in session.query(User).filter(User.name.in_(['ed', 'wendy', 'jack'])):
    print(fullname)

for fullname in session.query(User).filter(User.name == None):
    print(fullname)

for fullname in session.query(User).filter(User.name != None):
    print(fullname)

for a in session.query(User).filter(and_(User.name == 'simpson', User.fullname == 'homor simpson')):
    print(a)

query = session.query(User).filter(User.name.like('%ed')).order_by(User.id)
print(query.all(), query.first())

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        return email

@app.route('/')
def index():
    return 'hellow'

if __name__ == '__main__':
    app.run()

