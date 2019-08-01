#Cadastra novo usuario
import requests


DOMAIN_URL = 'https://gen-net.herokuapp.com/api/users/{}'

payload = {
	'name': input('Digite seu nome: '),
	'email': input('Digite seu e-mail: '),
	'password': input('Digite sua senha: ')
}

res = requests.post(DOMAIN_URL, payload)

if res.status_code == 200:
	user_id = res.json().get('id')
	print('Usuário {} cadastrado com sucesso'.format(user_id))
else:
	print('E-mail já cadastrado')