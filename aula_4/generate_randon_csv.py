
import random
import string


CABECALHO = [ 'userid', 'email', 'nome', 'idade' ]

NUMERO_DE_REGISTROS = 10 ** 3

def generate_random_email():
	return ''.join(
		random.sample(string.ascii_lowercase, random.randint(10, 21))
	) + '@gueregueremail.com'

def generate_random_nome():
	return ''.join(
		random.sample(string.ascii_lowercase, random.randint(10, 21))
	)

def generate_random_idade():
	return random.randint(18, 75)

csv = [ CABECALHO ]

for n in range(NUMERO_DE_REGISTROS):
	u = [
		generate_random_email(),
		generate_random_nome(),
		generate_random_idade()
	]
	u.insert(0, id(u))
	csv.append(u)

for linha in csv:
	print(';'.join(str(x) for x in linha))
