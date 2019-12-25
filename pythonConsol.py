import platform,os,sys,datetime,time,json,shutil,ssl,wget
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import webbrowser,wikipedia,requests
import tkinter, tkinter.messagebox
from getpass import getpass


count = 0
try:
	def main():
		try:
			usr,pwd,sysName,sysUser = secure()
			while True:
				c = str(input(usr+"@"+sysName+": "+diract(".")+"__$ "))
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
				tkInfo("Time",datetime.datetime.now())
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
				tkInfo("Browser","Opne Now")
				webbrowser.open("https://www.google.com")
			elif ex == "exit":
				exit(0)
			elif ex == "power off":
				tkInfo("Power Off","few minutiue power off")
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
						tkInfo("copy","complited !!!")
					else:
						os.system("xcopy "+src+" "+dest+" /i/e/h/s/y")
						tkInfo("copy","complited !!!")
				except Exception as e:
					tkWarr("copy","check File")
					print(e)
			elif ex == "move":
				try:
					src = str(input("src => "))
					dest = str(input("dest => "))
					if os.name == "posix":
						os.system("mv -rf "+src+" "+dest)
						tkInfo("move","complited !!!")
					else:
						os.system("move "+src+" "+dest)
						tkInfo("copy","complited !!!")
				except Exception as e:
					tkWarr("move","check File")
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
							tkInfo("Deleted","successfully ...")
						else:
							if os.path.isdir(delPath):
								os.system("rmdir /Q/S "+delPath)
								tkInfo("Deleted","successfully ...")
							elif os.path.isfile(delPath):
								os.system("del "+delPath+" /f/s/q")
								tkInfo("Deleted","successfully ...")
							else:
								shutil.rmtree(delPath)
								tkInfo("Deleted","successfully ...")
					else:
						if delete in readDir():
							delPath = os.path.join(cwd(),delete)
							if os.name == "posix":
								os.system("rm -rf "+delete)
								tkInfo("Deleted","successfully ...")
							else:
								if os.path.isdir(delPath):
									os.system("rmdir /Q/S "+delPath)
									tkInfo("Deleted","successfully ...")
								elif os.path.isfile(delPath):
									os.system("del "+delPath+" /f/s/q")
									tkInfo("Deleted","successfully ...")
								else:
									shutil.rmtree(delPath)
									tkInfo("Deleted","successfully ...")
				except Exception as e:
					tkWarr("Deleted","check file")
					print(e)
			elif ex.startswith("@"):
				os.system(exsystem)
			elif ex == "_admin_":
				print(os.environ)
			elif ex == "crawing":
				crawing()
			elif ex == "web search":
				wiki()
			elif ex == "article":
				article()
			elif ex == "fileOrg":
				src = str(input("Enter path: \n"))
				junkorg(src)
			elif ex == ".":
				exit(0)
			else:
				os.system(ex)
				print( )

	def crawing():
		py = (".py")
		pdf = (".pdf")
		exe = (".exe")
		txt = (".txt", ".in", ".out",".log")
		html = (".html5",".html",".htm",".xhtml")
		imge = (".jpeg",".jpg",".tiff",".gif",".bmp",".png",".bpg",".svg",".heif",".psd")
		aci = (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",".dmg", ".rar", ".xar", ".zip")
		vdo = (".avi",".flv",".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",".qt", ".mpg", ".mpeg", ".3gp")
		aud = (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma")
		doc = (".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt","pptx")
		url = str(input("Enter the url (or) link: \n"))
		context = ssl._create_unverified_context()
		urlMob = Request(url=url,headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'})
		cooki = urlopen(urlMob,context=context).read()
		ch = int(input("1.link\n2.content\n3.img\n4.pdf\n5.exe\n=> "))
		if ch == 1:
			con = BeautifulSoup(cooki)
			for co in con.find_all('a'):
				li = str(co.get('href'))
				if li.startswith("h"):
					print(li)
		elif ch == 2:
			li = BeautifulSoup(cooki,"html.parser").get_text().splitlines()
			print(li)
		elif ch == 3:
			c = []
			count = 0 
			con = BeautifulSoup(cooki)
			imges = con.find_all('img')
			for img in imges:
				src = img.get('src')
				if src.endswith(imge):
					if not src.startswith("h"):
						Domin = url.split("/")[-1]
						src = url.replace(Domin,src)
					c.append(src)
					print(str(count)+" "+str(src))
					count += 1
			if len(c) > 0:
				imgCount = c[int(input("enter point of value:\n"))]
				extension = imgCount.split("/")[-1]
				print(os.path.join(*[os.getcwd(),str(count)+"."+extension]))
				wget.download(imgCount,os.path.join(*[os.getcwd(),str(count)+extension]))
				print("\n")
			else:
				print("no images")
		elif ch == 4:
			c = []
			count = 0
			con = BeautifulSoup(cooki)
			for co in con.find_all('a'):
				src = str(co.get('href'))
				if src.endswith(pdf):
					if not src.startswith("h"):
						Domin = url.split("/")[-1]
						src = url.replace(Domin,src)
					c.append(src)
					print(str(count)+" "+str(src))
					count += 1
			if len(c) > 0:
				imgCount = c[int(input("enter point of value:\n"))]
				extension = imgCount.split("/")[-1]
				print(os.path.join(*[os.getcwd(),str(count)+"."+extension]))
				wget.download(imgCount,os.path.join(*[os.getcwd(),str(count)+extension]))
				print("\n")
		elif ch == 5:
			c = []
			count = 0
			con = BeautifulSoup(cooki)
			for co in con.find_all('a'):
				src = str(co.get('href'))
				if src.endswith(exe):
					if not src.startswith("h"):
						Domin = url.split("/")[-1]
						src = url.replace(Domin,src)
					c.append(src)
					print(str(count)+" "+str(src))
					count += 1
			if len(c) > 0:
				imgCount = c[int(input("enter point of value:\n"))]
				print(imgCount)
				extension = imgCount.split("/")[-1]
				print(os.path.join(*[os.getcwd(),str(count)+"."+extension]))
				wget.download(imgCount,os.path.join(*[os.getcwd(),str(count)+extension]))
				print("\n")
		
	def wiki():
		try:
			while True:
				co = []
				query = str(input(("*")*25+" WEB SEARCH "+("*")*25+"\n"+"Enter Search Queryes:\n"))
				if query == "exit()":
					exit()
				else:
					arrQuery = wikipedia.search(query)
					print(("=")*40+"\nFind Relative Title Form :"+'"'+query+'"'+"\n"+("=")*40)
					for li in arrQuery:
						co.append(li)
					c = 0
					for i in co:
						print(str(c)+" "+i)
						c += 1
					n = int(input("Enter Number Of Point Search :\n"))
					put = co[n]
					print(wikipedia.summary(put))
					if "y" == str(input("\n\nget wiki page in y/n:\n")):
						print(wikipedia.page(put).content)
		except Exception:
			print("This Title "+serQuery+"not found")
			wiki()

	def article():
		query = str(input(("*")*50+"Info Article Gobel"+("*")*50+"\n"+"Enter Search Queryes:\n"))
		arrQuery = wikipedia.search(query)
		print(("=")*40+"\nFind Relative Title Form :"+'"'+query+'"'+"\n"+("=")*40)
		try:
			while True:
				print("\n")
				for li in arrQuery:
					print(li)
				serQuery = str(input("\nEnter Query Title: ( type 'y' exit )\n"))
				if serQuery.lower() == "y":
					break
				else:
					speCheck = wikipedia.suggest(serQuery)
					if speCheck == None:
						content = wikipedia.summary(serQuery)
					else:
						content = wikipedia.summary(speCheck)
				print(content)
		except Exception:
			print("This Title "+serQuery+"not found")
			article()

	def junkorg(src):
		if src == ".":
			src = diract(".")
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
				if fil.endswith(py):
					dest = os.path.join(src,"PY")
					if not os.path.isdir(dest):
						os.mkdir(dest)
					# shutil.move(os.path.join(root,fil),dest)
					shutil.copy(os.path.join(root,fil),dest)
				if fil.endswith(pdf):
					dest = os.path.join(src,"PDF")
					if not os.path.isdir(dest):
						os.mkdir(dest)
					# shutil.move(os.path.join(root,fil),dest)
					shutil.copy(os.path.join(root,fil),dest)
				if fil.endswith(exe):
					dest = os.path.join(src,"EXE")
					if not os.path.isdir(dest):
						os.mkdir(dest)
					# shutil.move(os.path.join(root,fil),dest)
					shutil.copy(os.path.join(root,fil),dest)
				if fil.endswith(txt):
					dest = os.path.join(src,"TXT")
					if not os.path.isdir(dest):
						os.mkdir(dest)
					print(os.path.join(root,fil))
					shutil.copy(os.path.join(root,fil),dest)
					# shutil.move(os.path.join(root,fil),dest)
				if fil.endswith(html):
					dest = os.path.join(src,"HTML")
					if not os.path.isdir(dest):
						os.mkdir(dest)
					# shutil.move(os.path.join(root,fil),dest)
					print(os.path.join(root,fil))
					shutil.copy(os.path.join(root,fil),dest)
				if fil.endswith(img):
					dest = os.path.join(src,"IMAGE")
					if not os.path.isdir(dest):
						os.mkdir(dest)
					# shutil.move(os.path.join(root,fil),dest)
					print(os.path.join(root,fil))
					shutil.copy(os.path.join(root,fil),dest)
				if fil.endswith(aci):
					dest = os.path.join(src,"ZIPFILE")
					if not os.path.isdir(dest):
						os.mkdir(dest)
					# shutil.move(os.path.join(root,fil),dest)
					print(os.path.join(root,fil))
					shutil.copy(os.path.join(root,fil),dest)
				if fil.endswith(vdo):
					dest = os.path.join(src,"VIDEO")
					if not os.path.isdir(dest):
						os.mkdir(dest)
					# shutil.move(os.path.join(root,fil),dest)
					print(os.path.join(root,fil))
					shutil.copy(os.path.join(root,fil),dest)
				if fil.endswith(aud):
					dest = os.path.join(src,"AUDIO")
					if not os.path.isdir(dest):
						os.mkdir(dest)
					# shutil.move(os.path.join(root,fil),dest)
					print(os.path.join(root,fil))
					shutil.copy(os.path.join(root,fil),dest)
				if fil.endswith(doc):
					dest = os.path.join(src,"DOCUMENTS")
					if not os.path.isdir(dest):
						os.mkdir(dest)
					# shutil.move(os.path.join(root,fil),dest)
					print(os.path.join(root,fil))
					shutil.copy(os.path.join(root,fil),dest)
			else:
				tkInfo("GTI file system","complited to work ...")

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
				tkInfo("Secure","user and password complited !!!")
				print(filePath)
				with open(filePath,"w") as f:
					json.dump(sysJson,f)
				with open(filePath,"r") as f:
					val = json.loads(f.read())
				isJsonAssign = json.loads(val)
				usr = isJsonAssign["usr"]
				pwd = isJsonAssign["pwd"]
				os.system("attrib +h "+str(folderPath))
				return usr,pwd,sysName,sysUser
			else:
				with open(filePath,"r") as f:
					val = json.loads(f.read())
				isJsonAssign = json.loads(val)
				usr = isJsonAssign["usr"]
				pwd = isJsonAssign["pwd"]
				os.system("attrib +h "+str(folderPath))
				return usr,pwd,sysName,sysUser
		else:
			if not os.path.isfile(filePath):
				tkEror("Secure","Sorry Missing authorid \n Try again !!!")
				sysName = platform.node()
				userName = str(input("Enter User Name:__$ "))
				passWord = str(getpass("Enter Pass Word:__$ "))
				sysJson = '{"usr":"'+userName+'","pwd":"'+passWord+'"}'
				tkInfo("Secure","user and password complited !!!")
				print(filePath)
				with open(filePath,"w") as f:
					json.dump(sysJson,f)
				with open(filePath,"r") as f:
					val = json.loads(f.read())
				isJsonAssign = json.loads(val)
				usr = isJsonAssign["usr"]
				pwd = isJsonAssign["pwd"]
				os.system("attrib +h "+str(folderPath))
				return usr,pwd,sysName,sysUser
			else:
				with open(filePath,"r") as f:
					val = json.loads(f.read())
				isJsonAssign = json.loads(val)
				usr = isJsonAssign["usr"]
				pwd = isJsonAssign["pwd"]
				os.system("attrib +h "+str(folderPath))
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

	def tkInfo(top,mess):
		root = tkinter.Tk()
		root.withdraw()
		tkinter.messagebox.showinfo(top,mess)

	def tkWarr(top,mess):
		root = tkinter.Tk()
		root.withdraw()
		tkinter.messagebox.showwarning(top,mess)

	def tkEror(top,mess):
		root = tkinter.Tk()
		root.withdraw()
		tkinter.messagebox.showerror(top,mess)

except (Exception,KeyboardInterrupt):
	main()
finally:
	main()

if __name__=="__main__":
	try:
		main()
	except Exception:
		main()

