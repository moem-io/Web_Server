from flask import Flask
import pymysql

# configuration # 얘는 없어도 됨
DEBUG = True

conn = pymysql.connect(host='localhost', user='root', password='1234',
                       db='testdb', charset='utf8')

# Connection 으로부터 Dictoionary Cursor 생성
curs = conn.cursor(pymysql.cursors.DictCursor)

# SQL문 실행
# sql = "insert into entries (title, text) VALUES (%s, %s)"
# curs.execute(sql, ("my_title", "my_text"))
sql = "select * from entries where title=%s and text=%s"
curs.execute(sql, ("my_title", "my_text"))

conn.commit()
conn.close()

rows = curs.fetchall()
for row in rows:
    print(row)
    print(row['id'], row['title'], row['text'])

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return '<h1>hello world!!</h1>'

#####
if __name__ == '__main__':
    app.run()