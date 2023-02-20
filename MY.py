import os,re,sys,time,json,random,datetime,requests

m_fb = "m.facebook.com"
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
web_fb = "https://www.facebook.com/"
head_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

def jalan(xnxx):
	for hengker in xnxx + '\n':
		sys.stdout.write(hengker);sys.stdout.flush();time.sleep(0.05)

logo = ('''\033[1;93m
 .d8888b.  8888888b.     d8888 888b     d888 
d88P  Y88b 888   Y88b   d88888 8888b   d8888 
Y88b.      888    888  d88P888 88888b.d88888 
 "Y888b.   888   d88P d88P 888 888Y88888P888 
    "Y88b. 8888888P" d88P  888 888 Y888P 888 
      "888 888      d88P   888 888  Y8P  888 
Y88b  d88P 888     d8888888888 888   "   888 
 "Y8888P"  888    d88P     888 888       888 

[+]=============================================[+]
[+] CREATED BY   :  U7P4L IN                    [+]
[+] COUNTRY      :  BANGLADESH                  [+]
[+] ON GITHUB    :  U7P4L-IN                    [+]
[+] TOOL STATUS  :  FB POST ATO COMMENT         [+]
[+] TOOL VERSION :  0.5                         [+]
[+]=============================================[+]
''')

def login():
	os.system('clear')
	print(logo)
	cookie = str(input(f"\033[1;97m(+) cookie : \033[1;92m"))
	with requests.Session() as xyz:
		try:
			get_tok = xyz.get(url_businness+'/business_locations',headers = {"user-agent":ua_business,"referer": web_fb,"host": "business.facebook.com","origin": url_businness,"upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
			token = re.search("(EAAG\w+)", get_tok.text).group(1)
			open('cookie.txt','w').write(cookie) 
			open('token.txt','w').write(token)
			jalan ("\n\033[1;97m(+) Entering wait a moment...")
			menu()
		except requests.exceptions.ConnectionError:
			print ("\033[1;97m(+) problem internet connection !!!")
			exit()
		except (KeyError,IOError):
			print ("\033[1;97m(+) your cookie is invalid !!!")
			os.system("rm -rf cookie.txt")
			os.system("rm -rf token.txt")
			login()

def menu():
	os.system('clear')
	token  = open('token.txt','r').read()
	cookie = {'cookie':open('cookie.txt','r').read()}
	get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
	jsx = json.loads(get.text)
	nama = jsx["name"]
	id = jsx["id"]
	os.system('clear')
	print(logo)
	print ("\033[1;97m(+) Active User : "+ nama + "")
	print ("\033[1;97m(+) Facebook Id : "+ id + "")
	print ("")
	print ("\033[1;97m(1) spam comments facebook posts ")
	print ("\033[1;97m(0) log out ( go out )")
	pahrul = input ("\n\033[1;97m(+) choose : ")
	if pahrul =="1":
		os.system('clear')
		komen()
	elif pahrul =="0":
		jalan ("\033[1;97m(+) wait a moment deleting cookies...")
		os.system("rm cookie.txt")
		os.system("rm token.txt")
		login()
	else:
		print("\033[1;97m(+) what are you typing goat!!!")
		exit()
	
def komen():
	ok,no=[],[]
	cookie = open('cookie.txt', 'r').read()
	token = open('token.txt', 'r').read()
	coki = {"cookie":cookie}
	os.system("clear")
	print(logo)
	id = input(f"\033[1;97m(+) post id : ")
	komen = input("\033[1;97m(+) comment : ")
	limit = int(input("\033[1;97m(+) limit : "))
	print ("")
	for x in range(limit):
		_pahrul_ = requests.post(f'https://graph.facebook.com/{id}/comments/?message={komen}&access_token={token}',cookies={'cookie':cookie})
		cek_st = json.loads(_pahrul_.text)
		print(f'\r\033[1;97m[\033[1;92m✓\033[1;97m] SUCCES : {len(ok)} \033[1;97m[\033[1;91m!\033[1;97m] FAILED : {len(no)}', end=' ')
		if 'id' in cek_st:
			ok.append('succes')
		else:
			no.append('failed')
               
	
	
login()
