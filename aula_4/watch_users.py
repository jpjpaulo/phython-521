
import os
import sys
import time
import subprocess

import ldap3

if len(sys.argv) < 2:
	print('Diretorio nao especificado')
	sys.exit(1)

dirname = sys.argv[1]

USERNAME = 'cn=admin, dc=dexter, dc=com, dc=br'
PASSWORD = '4linux'

object_class = [
	'top',
	'person',
	'organizationalPerson',
	'inetOrgPerson',
	'posixAccount',
]

done = False
while not done:
	for filename in os.listdir(dirname):
		
		conn = ldap3.Connection(
			ldap3.Server('ldap://127.0.0.1'),
			USERNAME,
			PASSWORD
		)
		conn.bind()

		success, failure = 0, 0
		with open(dirname + '/' + filename, 'r') as f:
			for n, line in enumerate(f.readlines()):
				if n == 0:
					continue
				userid, email, name, age = line.strip().split(';')
				user = {
					'cn': name,
					'sn': name,
					'mail': email,
					'uidNumber': age,
					'gidNumber': age,
					'uid': email,
					'homeDirectory': '/home' + email,
					'userPassword': 'admin',
				}
				user_registered = conn.add(
					'uid={},dc=dexter,dc=com,dc=br'.format(email),
					object_class,
					user
				)

				if user_registered:
					success +=1
				else:
					failure +=1

		print('{} cadastrados, {} erros'.format(success, failure))			
		os.remove(dirname + '/' + filename)
	time.sleep(1)

