from dotenv import load_dotenv
import os
import schedule
import threading
load_dotenv()

import gspread

multe_da_grupoj = False
ĉu_testo = False
atb_mode = False

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

print(path)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types = ['text', 'photo', 'video', 'animation', 'sticker', 'document', 'audio', 'voice', 'poll', "video_note"])
def sendu_tekston(message):
    elif str(message.chat.id) == str(ne_id):
      if message.from_user.id == 777000:
            bot.delete_message(message.chat.id, message.message_id)
            
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
