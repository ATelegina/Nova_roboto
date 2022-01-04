import json
import random
import os
from dotenv import load_dotenv
load_dotenv()
# =============================================================================
# with open("C:\\Users\\dasha\\Downloads\\Telegram Desktop\\ChatExport_2021-12-20\\result.json", encoding="UTF-8") as jsonFile:
#     jsonObject = json.load(jsonFile)
#     jsonFile.close()
# listo = []    
# for i in jsonObject["messages"]:
#     if i.get("from_id") == "user1688104773":
#         if str(i.get("text")).find("bot_command") == -1:
#             listo.append(str(i.get("text")) + "\n")
#     
# #print(listo[1])
# fajlo = open("C:\\Users\\dasha\\Downloads\\Telegram Desktop\\ChatExport_2021-12-20\\listo.txt","w+", encoding="UTF-8")
# for elemento in listo:
#     fajlo.write(str(elemento))
# =============================================================================
import telebot
from telebot import types, util
wren_token = os.getenv("WRENA_TOKENO")
wren_token = str(wren_token)
wren_token = wren_token.translate({ ord(c): None for c in '""' })
wren = telebot.TeleBot(wren_token)
@wren.message_handler(commands=['start', "komencu"])
def wren_komencu(message):
    wren.send_message(message.chat.id, "Ni komencu")  
@wren.message_handler(func=lambda call: True)
def wren_citato(message):
    if message.text == "/citato" or message.text.find("@wren_robot") != -1 or message.chat.type == "private":
        listo = open("listo.txt", "r", encoding="UTF-8").read()
        listo = str(listo)
        wren.send_message(message.chat.id, random.choice(listo.splitlines()))
        
# =============================================================================
# listo = open("C:\\Users\\dasha\\Downloads\\Telegram Desktop\\ChatExport_2021-12-20\\listo.txt", "r", encoding="UTF-8").read()
# listo = str(listo)
# print(random.choice(listo.splitlines()))
# =============================================================================

wren.infinity_polling(allowed_updates=util.update_types)  
