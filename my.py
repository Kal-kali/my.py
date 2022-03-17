import os
from time import sleep
from pyrogram.errors import FloodWait
from pyrogram import Client, filters, types, errors
from pyrogram.types import ChatPermissions
import time



app = Client('cmd', api_id=15897262, api_hash='90476d9c65a86b03837e1e249314cd75')



#все логины
logins = ["just_eblan", "bebra2", "a"]

#все пароли
passwd = ["123", "bebra2", "b"]

#логин и пароль юзера
u_login = input("Введите ваш логин: ")
u_pass = input("Введите ваш пароль: ")
if u_login in logins:
  #Позиция логина в базе логинов
  u_log_in = logins.index(u_login)
  if passwd[u_log_in] == u_pass:
    app.start()

    app.stop()
    if os.sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
    print('''   v0.8
         
       ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
       ┃▒▄█▀▀█▒█▀█▀█─░▄█▀▄─▒▐█▀▀▄▒▐█▀▀▀█▌░▐█▀▀░▐█▀█▄┃
       ┃▒▀▀█▄▄░░▒█░░░▐█▄▄▐█▒▐█▒▐█░▒▄▄█▀▀░░▐█▀▀░▐█▌▐█┃
       ┃▒█▄▄█▀░▒▄█▄░░▐█─░▐█▒▐█▀▄▄▒▐█▄▄▄█▌░▐█▄▄░▐█▄█▀┃
       ┃---------Telegram: @starzedscripts----------┃
       ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


''')

    print("После ввода задержки напишите в любой телеграм чат команду /help для просмотра команд!")
    print("\n Just Relax уебан!")
    print()

    cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))

    global number
    number = 0

    while cool == 0:
        print("Слишком быстро!")
        cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))

    while cool == 1:
        print("Слишком быстро!")
        cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))

    while cool == 2:
        print("Слишком быстро!")
        cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))

    while cool > 10:
        print("Слишком медленно!")
        cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))

    while cool < 0:
        print("ОЧЕНЬ БЫСТРО........")
        cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))

     @app.on_message(filters.command("oxymoron", prefixes=".") & filters.me)
    def valentine(app, msg):
        app.send_message(msg.chat.id, f'''<b>ГОВНО>''')
        sleep(1.0)
        app.send_message(msg.chat.id,f'''<b> ЗАЛУПА</b>''')
        sleep(1.0)
        app.send_message(msg.chat.id,f'''<b>ПЕНИС</b>''')
        sleep(1.0)
        app.send_message(msg.chat.id,f'''<b>ХЕР</b>''')
        sleep(1.0)
        app.send_message(msg.chat.id,f'''<b>ДАВАЛКА</b>''')
        sleep(1.0)
        app.send.message(msg.chat.id,f'''<b>ХУЙ</b>''')
        sleep(1.0)
        app.send_message(msg.chat.id,f'''<b>БЛЯДИНА</b>''')
        sleep(1.0)
        app.send_message(msg.chat.id,f'''<b>ГОЛОВКА</b>''')
        sleep(1.0)
        app.send_message(msg.chat.id,f'''<b>ШЛЮХА</b>''')
        sleep(1.0)
        app.send_message(msg.chat.id,f'''<b>ЖОПА</b>''')
        sleep(1.0)
        app.send_message(msg.chat.id,f'''<b>ЧЛЕН</b>''')
        sleep(1.0)
        app.send_message(msg.chat.id,f'''<b>ЕБЛАН</b>''')
        sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>ПЕТУХ</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>МУДИЛА</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>РУКОБЛУД</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>ССАНИНА</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>ОЧКО</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>БЛЯДУН</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>(ВАГИНА</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>СУКА</b>/''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>ЕБЛАНИЩЕ</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>ВЛАГАЛИЩЕ</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>ПЕРДУН</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>ДРОЧИЛА</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>ПИДОР</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>ПИЗДА</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>ТУЗ</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>МАЛАФЬЯ</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>ГОМИК</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>МУДИЛА</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>ПИЛОТКА</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>МАНДА</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>АНУС</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>ВАГИНА</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>ПУТАНА</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>ПЕДРИЛА</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>ШАЛАВА</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>ХУИЛА</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>МОШОНКА</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>ЕЛДА</b>''')
       sleep(1.0)
       app.send_message(msg.chat.id,f'''<b>РАУНД!!</b>''')
       sleep(1.0)
       