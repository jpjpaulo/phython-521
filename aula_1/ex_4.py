
import requests

URL = 'https://gen-net.herokuapp.com/api/users/'

response = requests.get(URL)

users = response.json()

name = input('Digite seu name: ')

for user in users:
	if user.get('name') == name:
		print(user)

print(response.json())