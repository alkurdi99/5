import requests,uuid,instaloader,os
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
C = '\033[0;97m'
os.system('pip install requests')
os.system('clear')
os.system('pip install uuid')
os.system('clear')
os.system('pip install instaloader')
os.system('clear')
os.system('pip install os')
os.system('clear')
def Followers():
 os.system('clear')
 L = instaloader.Instaloader()
 username=input('[+] UserName ==> ')
 password=input('[+] PassWord ==> ')
 getuser=input('[+] User To Get Followers ==> ')
 os.system('cd /storage/emulated/0/')
 os.system('rm -rf id.txt')
 L.login(username,password)
 profile = instaloader.Profile.from_username(L.context, getuser)
 follow_list = []
 count=0
 for followee in profile.get_followers():
    user=str(followee)
    idd=user.split('(')[1]
    id=idd.split(')')[0]
    follow_list.append(id)
    file = open("id.txt","a+")
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    print(follow_list[count])
    count=count+1
 
def coin():
 os.system('clear')
 token=input (" TOKEN TELEGRAM : ")
 os.system('clear')
 ID=input (" ID TELEGRAM : ")
 os.system('clear')
 file=input('Name file : ')
 md=0
 for Whisper in open(file,'r').read().splitlines():
  username=str(Whisper.split('\n')[0])
  url=f'https://test.marcjune.repl.co/?uid={username}&submit=submit'
  whisper=str(requests.get(url).text)
  if 'coins":"' in whisper:
   coin=str(whisper.split('coins":"')[1])
   coins=str(coin.split('"')[0])
   md+=1
   print(f'{G}《 ✓ 》 {username} Coins ==> {B}{coins}')
   if int(coins) > 400:
    md+=1
    masg = ("ID  ==> "+str(username)+"\nCoins  ==> "+str(coins)+"\n𝐅𝐫𝐎𝐦 : @nnXoo")
    req = requests.post("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(masg))
     
  else:
   md+=1
   print(f'{C}《 {md} 》{E} {username} ==> {S}ERROR')

Choose=input(f'''{S}[1] Get List   
{B}[2] Checker Coins
{G}[+] Choose ==> ''')
if Choose == '1':
 Followers()
if Choose == '2':
 coin()