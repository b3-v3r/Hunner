import time
import os,sys
import socket
from pexpect import pxssh
import re
import argparse

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'

parser = argparse.ArgumentParser()
parser.add_argument('host', help='Target host SSH')
parser.add_argument('user', help='Target username SSH')
parser.add_argument('password', help='Target password SSH')
parser.add_argument('method', help=' SSH' )
args = parser.parse_args()
if args.host and args.user and args.password:
	host = args.host
	user = args.user	
	method = args.method
	password = args.password

def clear():
	os.system('clear')

def banner():
	os.system('python3 banner.py ')

def connect_ssh():
	print 'Start SSH mode'
	ssh = pxssh.pxssh()
	try:
		ssh.login(host, user , password)
		print G+'Start session->'+host+E
	except:
		print F+'Error connect ssh'+E
		sys.exit(1)
	while True:
		print 'Enter comand'
		try:
			cmd = raw_input(B+'Cmd->'+E)
		except KeyboardInterrupt:
			print "Detect Ctrl+C"
			sys.exit('Good bye ;)')
		if cmd == "exit":
			sys.exit('Good by ;)')

		ssh.sendline(cmd)
		ssh.prompt()
		data = ssh.before
		print data


def main():
	clear()
	banner()
	print 'Time: '+time.ctime()
	print F+'Start HunListener'+E
	print G+'Target host -> '+W+host+E
	print G+'Target user -> '+W+user+E
	print G+'Target password-> '+W+password+E
	if method == 'ssh':
		connect_ssh()
main()