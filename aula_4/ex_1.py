#

import os
import sys
import subprocess
import datetime #Capitura o momento atual
import time


#print(os.path.devnull)

#with open('nome.txt', 'a') as f:
#	f.write('hello, world\n')


## vai gerar um log
# for i in range(10**6):
# 	agora = datetime.datetime.now().strftime('%d-%m-%y | %H-%M-%S')
# 	print(
# 		'{} | log {}' .format(agora, i)
# 	)
# 	time.sleep(0.1)

## 
with open('log', 'r') as f:
	for line in f.readlines():
		date, hour, log = line.split('|')
		
		log_n = log.lstrip().split(' ')[-1]
		log_n = int(log_n)

		if log_n % 7 != 0:
			print(line)
