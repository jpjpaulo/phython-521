import os
import sys
import subprocess
import datetime
import time


# for i in range(10 ** 6):
#     agora = datetime.datetime.now().strftime('%d-%m-%Y | %H-%M-%S')
#     print(
#         '{} | log {}'.format(agora, i)
#     )
#     time.sleep(0.1)


with open('log', 'r') as f:
    
    for line in f.readlines():
        
        date, hour, log = line.split('|')
        
        log_n = log.lstrip().split(' ')[-1]
        log_n = int(log_n)

        args = sys.argv
        if len(args) > 1:
            for log in args[1::]:
                if log_n == int(log):
                    print(line)
        elif log_n % 7 != 0:
            print(line)