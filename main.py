# =============================================================================
# Antaŭ komenco de lanĉado:aldoni esceptojn :bot. ŝanĝiget_chat_member, ŝanĝi ne_id, nombron de i en def responda ligilo (devos esti 6), sendu_tekston @glumarkoj
# =============================================================================

ĉu_testo = False
if ĉu_testo:
    TOKEN = "1889084287:AAFA5Q8B9h2W5iuXS3pZm9fyfUykH0EG9aE"
    ne_id = -1001204743894
    ligila_longeco = 3
    
else:
    TOKEN = "1938071091:AAHF9mOw0YevCNcItxbEN94uIYwkRlUBTz0"
    ne_id = -1001463711396
    ligila_longeco = 6

frazoj = ["Mi jam perdis kontrolon", "Mi havas mil...dan voĉon", "Vi uzas nur duonon de via cerbo, ĉu?", "Vi estas detruema", "Vi ne havas solvon", "Ni estas mense egalaj", "Ĉu vi havas 27 horojn en unu tago?", "Vi devus viziti", "Talpa penso", "Mi ne estas komencanto", "ALKUTIMIGXU KUNVIVI", "Al vi ne mankas minutoj", "Vi ne povas eviti diri ĉiam ion detruantan", "Memoru tion", "Vi ne volis esti ĉefo", "Hispanio dormas", "Forta malkrizo", "Forta krizo", "Laboru forte, sed vi faras tro...", '"Per unu mano ili konstruas, per alia detruas"', "Vi regas el la ombroj", "...sen limoj", "Talpo!", "Forigu vin!", "Dankon, Bertileto", "Neniu zorgas", "Ege malrespekte", "Zamenhof mortis.", "Bravaj vortoj", "Mdr", "+1", "Mi devus aĉeti pufmaizon", "Difinu", "Koran tankon", "Vi meritas esti aŭskultata", "Fakte!", "Vera kloakano!", "Forfikiĝu!", 'Vi ne estas finbenkisto', "Nedoankinde", "Vi obsede tajpas, tajpas, tajpas...", "Vi estas obsediĝema", "Ĉu pedanti aŭ pedantumi?..", "Spam', spam', spam'", "Ĉu vere?!"]

versio="0.1a"

import telebot
import time
import random
import sqlite3
from telebot import types


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'komencu'])
def send_welcome(message):
    bot.reply_to(message, "La ludo komencu!")
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(message.chat.id, "Ĵetu viajn galantvortojn, aĉulo")
    
