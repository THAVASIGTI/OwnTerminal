import platform,os,sys,datetime,time,json,shutil
from pathlib import Path
import webbrowser
from getpass import getpass


count = 0

def main():
	try:
		usr,pwd,sysName,sysUser = secure()
		while True:
			c = str(input(sysUser+"@"+sysName+": "+diract(".")+"__$ "))
			history(c)
			commandLib(c)
			continue
	except (KeyboardInterrupt,Exception) :
		os.system("\npython pythonConsol.py")

def commandLib(ex):
	try:
		exsystem = ex.split("@")[1]
	except:
		pass
	if len(ex) > 0:
		if ex == "..*..":
			print("QWER THAVASI GTI POIU")
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
		elif ex == "broswer":
			webbrowser.open("https://www.google.com")
		elif ex == "exit":
			exit(0)
		elif ex == "power off":
			if platform.system() == 'Windows':
				os.system("shutdown /s")
			else:
				os.system("shutdown -h now")
		elif ex == "copy":
			try:
				src = str(input("src => "))
				dest = str(input("dest => "))
				if os.name == "posix":
					os.system("cp -rf "+src+" "+dest)
				else:
					os.system("xcopy "+src+" "+dest+" /i/e/h/s/y")
			except Exception as e:
				print(e)
		elif ex == "move":
			try:
				src = str(input("src => "))
				dest = str(input("dest => "))
				if os.name == "posix":
					os.system("mv -rf "+src+" "+dest)
				else:
					os.system("move "+src+" "+dest)
			except Exception as e:
				print(e)
		elif ex == "delete":
			try:
				for li in readDir():
					print(li)
				delete = str(input("Del => "))
				if delete.startswith("~ "):
					delPath = delete.split(" ")[1]
					if os.name == "posix":
						os.system("rm -rf "+delete)
					else:
						if os.path.isdir(delPath):
							os.system("rmdir /Q/S "+delPath)
						elif os.path.isfile(delPath):
							os.system("del "+delPath+" /f/s/q")
						else:
							shutil.rmtree(delPath)
				else:
					if delete in readDir():
						delPath = os.path.join(cwd(),delete)
						if os.name == "posix":
							os.system("rm -rf "+delete)
						else:
							if os.path.isdir(delPath):
								os.system("rmdir /Q/S "+delPath)
							elif os.path.isfile(delPath):
								os.system("del "+delPath+" /f/s/q")
							else:
								shutil.rmtree(delPath)	
			except Exception as e:
				print(e)
		elif ex.startswith("@"):
			os.system(exsystem)
		elif ex == "_admin_":
			print(os.environ)
		elif ex == "org":
			src = str(input("Enter path: \n"))
			junkorg(src)
		else:
			os.system(ex)
			print( )

def junkorg(src = os.getcwd()):
	py = (".py")
	pdf = (".pdf")
	exe = (".exe")
	txt = (".txt", ".in", ".out",".log")
	html = (".html5",".html",".htm",".xhtml")
	img = (".jpeg",".jpg",".tiff",".gif",".bmp",".png",".bpg",".svg",".heif",".psd")
	aci = (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",".dmg", ".rar", ".xar", ".zip")
	vdo = (".avi",".flv",".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",".qt", ".mpg", ".mpeg", ".3gp")
	aud = (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma")
	doc = (".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt","pptx")
	for root,die,folder in os.walk(src):
		for fil in folder:
			if fil.endswith(exe):
				with open("exe.txt","a+") as f:
					f.writelines(fil+"\n")
			if fil.endswith(py):
				with open("py.txt","a+") as f:
					f.writelines(fil+"\n")
			if fil.endswith(pdf):
				with open("pdf.txt","a+") as f:
					f.writelines(fil+"\n")
			if fil.endswith(html):
				with open("html.txt","a+") as f:
					f.writelines(fil+"\n")
			if fil.endswith(img):
				with open("image.txt","a+") as f:
					f.writelines(fil+"\n")
			if fil.endswith(vdo):
				with open("video.txt","a+") as f:
					f.writelines(fil+"\n")
			if fil.endswith(doc):
				with open("docutment.txt","a+") as f:
					f.writelines(fil+"\n")
			if fil.endswith(aci):
				with open("achive.txt","a+") as f:
					f.writelines(fil+"\n")
			if fil.endswith(aud):
				with open("adiuo.txt","a+") as f:
					f.writelines(fil+"\n")
			if fil.endswith(txt):
				with open("PailnText.txt","a+") as f:
					f.writelines(fil+"\n")

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
	elif src == "cd /":
		with open(batFileInPath,"a+") as f:
			f.writelines(src+"\ncd  > "+tryFileInpath)
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

def history(comm):
	folderPath = os.path.join(os.getcwd(),"Activity")
	historyFileInPath = os.path.join(folderPath,"history.txt")
	if comm == "|(*":
		with open(historyFileInPath,"r") as r:
			return r.readlines()
	else:
		if not os.path.isfile(historyFileInPath):
			with open(historyFileInPath,"a") as f:
				f.writelines("0 "+comm+"\n")
		else:	
			txtLine = len(open(historyFileInPath).read().splitlines())
			with open(historyFileInPath,"a") as f:
				f.writelines(str(txtLine)+" "+comm+"\n")
				txtLine =+ 1

def readDir():
	folderPath = os.path.join(os.getcwd(),"Activity")
	tryFileInpath = os.path.join(folderPath,"temp.txt")
	with open(tryFileInpath,"r") as f:
		readLine = f.readline().rstrip()
	findFile = os.listdir(readLine)
	return findFile

def cwd():
	folderPath = os.path.join(os.getcwd(),"Activity")
	tryFileInpath = os.path.join(folderPath,"temp.txt")
	with open(tryFileInpath,"r") as f:
			readLine = f.readline().rstrip()
	return readLine

if __name__=="__main__":
	main()