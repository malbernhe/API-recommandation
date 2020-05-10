
import requests

people = [
    {'name': 'Marc'},
    {'age': 22}
]

print('hello Marc')
print (people)


# api-endpoint
URL = "https://api.github.com/user"
auth=('malbernhe', 'MDQ6VXNlcjM1NjMxNTk0')

# sending get request and saving the response as response object
r = requests.get(url=URL, auth=auth)

print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json)
