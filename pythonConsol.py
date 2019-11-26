import platform,os,sys,datetime,time,json
from getpass import getpass


count = 0

def main():
	usr,pwd,sysName,sysUser = secure()
	while True:
		c = str(input(sysUser+"@"+sysName+": "+diract(".")+"__$ "))
		history(c)
		commandLib(c)
		continue

def commandLib(ex):
	if len(ex) > 0:
		if ex == "..*..":
			print(" ")
		elif ex == "clear":
			if platform.system() == 'Windows':
				os.system("cls")
			else:
				os.system("clear")
		elif ex == "ip":
			if platform.system() == 'Windows':
				os.system("ipconfig")
			else:
				os.system("ifconfig")
		elif ex == "time":
			return print(datetime.datetime.now())
		elif ex in ["ls","l","dir"]:
			for ls in readDir():
				print(ls)
		elif ex == "history":
			for h in history("|(*"):
				print(h.rstrip())
		elif ex.startswith("cd "):
			diract(ex)
		elif ex == "exit":
			exit(0)
		# elif 


def diract(src):
	global count
	dirReplce = src.replace("cd ","")
	folderPath = os.path.join(os.getcwd(),"Activity")
	tryFileInpath = os.path.join(folderPath,"temp.txt")
	batFileInPath = os.path.join(folderPath,"diract.bat")
	if src == ".":
		while count == 0:
			with open(batFileInPath,"w") as f:
				f.writelines("cd > "+tryFileInpath)
			os.popen(batFileInPath).read()
			count =+1
		with open(tryFileInpath,"r") as f:
			readLine = f.readline().rstrip()
		return readLine
	elif src == "cd ..":
		with open(batFileInPath,"a+") as f:
			f.writelines(src+"\ncd  > "+tryFileInpath)
		os.popen(batFileInPath).read()
	elif dirReplce in readDir():
		with open(batFileInPath,"a+") as f:
			f.writelines("cd "+dirReplce+"\ncd  > "+tryFileInpath)
		os.popen(batFileInPath).read()
	elif dirReplce in ["c:","C:","d:","D:","e:","E:","f:","F:","h:","H:","x:","X:","i:","I:"]:
		with open(batFileInPath,"w+") as f:
			f.writelines(dirReplce+"\ncd >"+tryFileInpath)
		os.popen(batFileInPath).read()

def secure():
	sysName = platform.node()
	sysUser = os.environ["USERNAME"]
	folderPath = os.path.join(os.getcwd(),"Activity")
	filePath = os.path.join(folderPath,"authority.json")
	if not os.path.isdir(folderPath):
		os.mkdir(folderPath)
		if not os.path.isfile(filePath):
			sysName = platform.node()
			userName = str(input("Enter User Name:__$ "))
			passWord = str(getpass("Enter Pass Word:__$ "))
			sysJson = '{"usr":"'+userName+'","pwd":"'+passWord+'"}'
			print(filePath)
			with open(filePath,"w") as f:
				json.dump(sysJson,f)
			with open(filePath,"r") as f:
				val = json.loads(f.read())
			isJsonAssign = json.loads(val)
			usr = isJsonAssign["usr"]
			pwd = isJsonAssign["pwd"]
			return usr,pwd,sysName,sysUser
		else:
			with open(filePath,"r") as f:
				val = json.loads(f.read())
			isJsonAssign = json.loads(val)
			usr = isJsonAssign["usr"]
			pwd = isJsonAssign["pwd"]
			return usr,pwd,sysName,sysUser
	else:
		with open(filePath,"r") as f:
			val = json.loads(f.read())
		isJsonAssign = json.loads(val)
		usr = isJsonAssign["usr"]
		pwd = isJsonAssign["pwd"]
		return usr,pwd,sysName,sysUser

def history(comm):
	folderPath = os.path.join(os.getcwd(),"Activity")
	historyFileInPath = os.path.join(folderPath,"history.txt")
	if comm == "|(*":
		with open(historyFileInPath,"r") as r:
			return r.readlines()
	else:
		if not os.path.isfile(historyFileInPath):
			with open(historyFileInPath,"w+") as f:
				f.writelines("0 "+comm+"\n")
		else:	
			txtLine = len(open(historyFileInPath).read().splitlines())
			with open(historyFileInPath,"w+") as f:
				f.writelines(str(txtLine)+" "+comm+"\n")
				txtLine =+ 1

def readDir():
	folderPath = os.path.join(os.getcwd(),"Activity")
	tryFileInpath = os.path.join(folderPath,"temp.txt")
	with open(tryFileInpath,"r") as f:
		readLine = f.readline().rstrip()
	findFile = os.listdir(readLine)
	return findFile

if __name__=="__main__":
	main()