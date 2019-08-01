#Buscar usuario pelo ID (get)
import requests


DOMAIN_URL = 'https://gen-net.herokuapp.com/api/users/{}'

user_id = input('Digite seu id: ')

res = requests.get(DOMAIN_URL.format(user_id))

if res.status_code == 200:
	print(res.json().get('name'))
else:
	print(res.text)