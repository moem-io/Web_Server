from requests import put, get

print(put('http://localhost:5000/todo1', data={'data': 'Remember the milk'}).json())
print(get('http://localhost:5000/todo1').json())