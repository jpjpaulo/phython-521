
import sys
import hashlib


if len(sys.argv) != 3:
	print('Numero de argumentos invalidos')
	sys.exit(1)

operation, filename = sys.argv[1:]

csv = []

with open(filename, 'r') as f:
	for line in f.readlines():
		csv.append(
			line.split(';')
		)

if operation == 'encode':
	for n in range(len(csv) -1):
		csv[n+1][0] = hashlib.md5(csv[n+1][0].encode()).hexdigest()

# elif operation == 'decode':
# 	pass

for linha in csv:
	print(
		';'.join(str(x) for x in linha)
	)
