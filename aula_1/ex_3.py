
import requests

URL = 'http://viacep.com.br/ws/{}/json'

cep = input('Digite seu cep: ')

response = requests.get(URL.format(cep))
print(response.json())