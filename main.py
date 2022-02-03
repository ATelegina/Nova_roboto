from dotenv import load_dotenv
import os
import schedule
import threading
load_dotenv()
import random
import gspread
import tekstaro
import time

multe_da_grupoj = False
ĉu_testo = False
atb_mode = False
versio = "triona_venka"
if ĉu_testo == False:
    TOKEN = os.getenv("VERA_TOKEN")
    TOKEN = str(TOKEN)
    TOKEN = TOKEN.translate({ ord(c): None for c in '""' })
    #ne_id = -709830845 
    ne_id = -1001463711396    
    ligila_longeco = 6
    path = "mesagharo.db"
    nomo_de_roboto = "robotino_bot"
    gc = gspread.service_account(filename = "robotino.json")
else:
    TOKEN = os.getenv("TOKEN_TEST")
    ne_id = os.getenv("ID_TEST")
    #ne_id = -709830845
    ligila_longeco = 4
    path = os.getenv("PATH_TEST")
    nomo_de_roboto = os.getenv("NOM_TEST")
    gc = gspread.service_account()
    
sh = gc.open("Robotina_tabelo")
import telebot
from telebot import types, util
import time
import random
#import sqlite3
TOKEN = os.getenv("KVF_TOKEN")
print(path)
TOKEN = str(TOKEN)
TOKEN = TOKEN.translate({ ord(c): None for c in '""' })
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['informo', 'informu'])
def sendu_informon(message):
    if message.reply_to_message:
        bot.reply_to(message, """<i>Id-ilo:</i> {}
<i>Tempo:</i> {}
<i>Id-ilo de sendinto:</i> {}""".format(message.reply_to_message.id, message.reply_to_message.date, message.reply_to_message.from_user.id), parse_mode="html")  
    else:
        bot.reply_to(message, """<i>Id-ilo:</i> {}
<i>Tempo:</i> {}
<i>Id-ilo de sendinto:</i> {}""".format(message.id, message.date, message.from_user.id), parse_mode="html")
        
 
@bot.message_handler(commands=['versio'])
def send_version_de_robotino(message):
    bot.reply_to(message, "Versio: " + versio)

@bot.message_handler(commands=['mil'])
def sendu_milon(message):
    time.sleep(0.666)
    kiom_nun = bot.send_message(message.chat.id, "...")
    
    worksheet = sh.worksheet("kiom")
    horiz = worksheet.find("Lasta idilo:").row
    lasta_kiom = int(worksheet.cell(horiz, 2).value)
    if kiom_nun.id-lasta_kiom + 1 < 1000:
        bot.send_message(message.chat.id, "Ne, ni havas nur <b>{}</b>".format(kiom_nun.id-lasta_kiom + 1), parse_mode="HTML")    
    else:
        bot.send_message(message.chat.id, "Jes, vi havas mil")
    try:
        bot.delete_message(message.chat.id, kiom_nun.id)
    except:
        print("jojojo") 
	
@bot.chat_member_handler()
def chat_m(message: types.ChatMemberUpdated):
    old = message.old_chat_member
    new = message.new_chat_member
    if new.status == "member":
        #memeoj = ["Roboto malforta ĉar virkoko", "Grupo kloaka ĉar Luna", "Esperantujo nova ĉar Pafilogate", "Tago 27-hora ĉar Paroligxema", "Roboto stulta ĉar Daria", "Krizo forta ĉar novulo", "Pablo neadministranto ĉar ombroj"]
        bot.send_message(message.chat.id,'Bonvenon, nova kloakano! Mi estas roboto kiu faras nenion utilan. Se vi ne komprenas kio okazas ĉi tie, vizitu https://t.me/+Uba2wuP3t3QzMDYy')
    if old.status == "member":
        bot.send_message(message.chat.id, "<b><a href='tg://user?id={userid}'>{}</a> jonizulis. Forta krizo.</b>".format(old.user.first_name, userid = old.user.id), parse_mode="html")
        
@bot.message_handler(func=lambda m: True)
def i_donisto(message):
	
  if message.chat.type == "private" and message.from_user.id == 602309534:
      if message.text == "Al duona venko!":
          bot.send_message(message.chat.id, "La venko proksimiĝas")
          tv = False
          while tv != True:
              a = bot.send_message(ne_id, "Triona venko proksimiĝas! 🎄🎁")
              if 499980 < int(a.id) < 499990:
                  tv = True
              else:
                  bot.delete_message(ne_id, int(a.id))
                  time.sleep(0.1)
      else:
          bot.send_message(ne_id, message.text)
  else:    
     print(message.text.find("fartas"))
           
     babilido = str(message.chat.id)
     print("Nova mesaĝo ĉe " + babilido + "\n")
     
     #if (message.text.lower() =='kiel vi fartas?' or message.text.lower() == "fartas kiel vi?" or message.text.lower() == "kiel fartas vi?" or message.text.lower() == "fartas vi kiel?" or message.text.lower() == "vi fartas kiel?" or message.text.lower() == "vi kiel fartas?"):
     if (message.text.lower().find('fartas') != -1 and message.text.lower().find('kiel') != -1):
        
        frazilo = random.randint(0,11)
        idilo = random.randint(0,23)
        
        print(frazilo, " ", idilo)
        if (frazilo==5):
            bot.reply_to(message, tekstaro.frazoj[frazilo], parse_mode="html")
        else:
            bot.reply_to(message, tekstaro.frazoj[frazilo] + tekstaro.ideoj[idilo], parse_mode="html") 
     elif (message.text.lower().find("?") != -1 and message.text.lower().find("duona")!=-1 and message.text.lower().find("venko")!=-1) and (message.text.lower().find("kiam")!=-1 or message.text.lower().find("kiom")!=-1):
	     bot.send_message(message.chat.id, "Ĝis duona venko restas {} mesaĝoj".format(499999 - int(message.id)))
		
     elif(message.text.lower().find('ĉu mi estas') != -1):    
        bot.reply_to(message, "Jes, vi estas")
	
     elif(message.text.lower().find('dankon') != -1 and message.text.lower().find('bot') != -1):    
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECOgdghHodXZzYd6-o8kNZ_MKkh1RvmAACQwADr8ZRGmSWUHOeMBH3HwQ")
     
     elif(message.text.lower().find('stulta') != -1 and message.text.lower().find('boto') != -1):
        bot.reply_to(message, "Eĉ se vi parolas ne pri mi, insulti robotojn estas hontaĵo")
	     
     elif(message.text.lower().find('li havas mil') != -1):
        bot.reply_to(message, "...dan voĉon")
	
     elif(message.text.lower().find('kvfb, ĉu vi vivas?') != -1):
        bot.send_message(message.chat.id, text="Roboto forta ĉar kielvifarta")

def kiom_da_mesagxoj():
    kiom_nun = bot.send_message(ne_id, "Bonan tageron, kloako")
    bot.send_chat_action(ne_id, "typing")
    
    worksheet = sh.worksheet("kiom")
    horiz = worksheet.find("Lasta idilo:").row
    lasta_kiom = int(worksheet.cell(horiz, 2).value)
    
    bot.send_message(ne_id, "En la lastaj 24 horoj estis senditaj <b>{}</b> mesaĝoj".format(kiom_nun.id-lasta_kiom + 1), parse_mode="HTML")
    
    worksheet.update_cell(horiz, 2, int(kiom_nun.id) + 1)
   
schedule.every().day.at("03:27").do(kiom_da_mesagxoj)
#03:27

def forever():
    while True:
        schedule.run_pending()
        time.sleep(5)

t1 = threading.Thread(target = forever)
t1.start()

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()  
               
bot.infinity_polling(allowed_updates=util.update_types)
os.system('python wren_roboto.py')
