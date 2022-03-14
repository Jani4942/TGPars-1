@@ -1,64 +1,64 @@
из telethon.sync импорт TelegramClient
из telethon.tl.functions.messages импорт GetDialogsRequest
из telethon.tl.types import InputPeerEmpty
импорт os, sys
импорт configparser
импорт csv
 время импорта
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
    print(f"""
{re}╔ ╦ ╗{cy}┌─┐┌─┐┌─┐┌─┐┬─┐{re}╔ ═ ╗ 
{re} ║ {cy}├─┐├┤ ├─┘├─┤├┬┘{re}╚ ═ ╗ 
{re} ╩ {cy}└─┘└─┘┴ ┴ ┴┴└─{re}╚ ═ ╝ 
автор https://github.com/elizhabs
        """)
cpass = configparser.RawConfigParser()
cpass.read('config.data')
попробуйте:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    клиент = TelegramClient(phone, api_id, api_hash)
кроме KeyError:
    os.system('clear')
    баннер()
    print(re+"[!] run python3 setup.py первый !!\n")
    sys.exit(1)
client.connect()
если нет client.is_user_authorized():
    client.send_code_request(телефон)
    os.system('clear')
    баннер()
    client.sign_in(phone, input(gr+'[+] Введите код: '+re))
 
os.system('clear')
баннер()
чаты = []
last_date = Нет
chunk_size = 200
группы=[]
 
результат = клиент(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)

для чата в чатах:
    попробуйте:
        если chat.megagroup== True:
        #if chat.megagroup== True:
            groups.append(чат)
    кроме:
        продолжить
 
print(gr+'[+] Выберите группу для очистки участников :'+re)
i=0
для g в группах:
    print(gr+'['+cy+str(i)+gr+']'+cy+' - '+ g.title)
    i+=1
 
print(")
g_index = input(gr+"[+] Введите число : "+re)
target_group=группы[int(g_index)]
 
print(gr+'[+] Fetching Members...')
time.sleep(1)
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)
 
print(gr+'[+] Сохранение в файле...')
time.sleep(1)
с open("members.csv","w",encoding='UTF-8') как f:
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['имя пользователя','идентификатор пользователя', 'хэш доступа','имя','группа', 'идентификатор группы'])
    для пользователя в all_participants:
        если пользователь.имя пользователя:
            имя пользователя= user.username
        ещё:
            имя пользователя= ""
        если user.first_name:
            first_name= user.first_name
        ещё:
            first_name= ""
        если user.last_name:
            last_name= user.last_name
        ещё:
            last_name= ""
        name= (first_name + ' ' + last_name).strip()
        writer.writerow([имя пользователя,user.id,user.access_hash,name,target_group.title, target_group.id]) 
print(gr+'[+] Members scraped successfully.')