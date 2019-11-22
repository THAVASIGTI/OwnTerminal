import platform,os,sys,datetime,time
from getpass import getpass
from subprocess import call

global palce
palce = os.getcwd()

def libSys(ex,palce):
	if len(ex) > 0:
		if ex == "time":
			return print(datetime.datetime.now())
		# find the time find working module	
		elif ex in ["ls","l","dir"]:
			for l in os.listdir(palce):
				print(l)
		# when list os diractory working module
		elif ex == "clear":
			if os.name == 'posix':
				os.system("clear")
			else:
				os.system("cls")
		# In clear screen useage and module
		elif ex == "ip":
			if os.name == 'posix':
				os.system("ifconfig")
			else:
				os.system("ipconfig")
		# when module of ip address geting module
		elif ex == ex+"-s":
			os.system(ex)
		else:
			print("Command Not Found "+ex)


def cwd(src,palce):
	p = str(palce)
	fold = os.listdir(p)
	if src == ".":
		return os.getcwd()
	elif src == "cd ..":
		palc = os.path.dirname(palce)
		return palc
	elif src in ["cd "+f for f in fold]:
		 


def main(usr,pwd,sysName,palce):
	try:
		while True:
			time.sleep(0)
			comm = str(input(usr+"@"+sysName+":"+str(palce)+"$ "))
			if comm == "exit":
				exit(0)
			elif comm.startswith("cd"):
				palce = cwd(comm,palce)
			else:
				libSys(comm,palce)
	except (KeyboardInterrupt, SystemExit):
		print(".")

if __name__=="__main__":
	sysName = platform.node()
	usr = str(input("Enter the UserName: "))
	pwd = str(getpass("Enter the passWord: "))
	main(usr,pwd,sysName,palce)