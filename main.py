# =============================================================================
# Antaŭ komenco de lanĉado:aldoni esceptojn :bot. ŝanĝiget_chat_member, ŝanĝi ne_id, nombron de i en def responda ligilo (devos esti 6), sendu_tekston @glumarkoj
# =============================================================================

ĉu_testo = False
if ĉu_testo:
    TOKEN = "1889084287:AAFA5Q8B9h2W5iuXS3pZm9fyfUykH0EG9aE"
    ne_id = -1001204743894
    ligila_longeco = 3
    path = "C:\\_MY THINGS_\\robotino\\mesagharo.db"
else:
    TOKEN = "1938071091:AAHF9mOw0YevCNcItxbEN94uIYwkRlUBTz0"
    ne_id = -1001463711396
    ligila_longeco = 6
    path = "mesagharo.db"

frazoj = ["Mi jam perdis kontrolon", "Mi havas mil...dan voĉon", "Vi uzas nur duonon de via cerbo, ĉu?", "Vi estas detruema", "Vi ne havas solvon", "Ni estas mense egalaj", "Ĉu vi havas 27 horojn en unu tago?", "Vi devus viziti", "Talpa penso", "Mi ne estas komencanto", "ALKUTIMIGXU KUNVIVI", "Al vi ne mankas minutoj", "Vi ne povas eviti diri ĉiam ion detruantan", "Memoru tion", "Vi ne volis esti ĉefo", "Hispanio dormas", "Forta malkrizo", "Forta krizo", "Laboru forte, sed vi faras tro...", '"Per unu mano ili konstruas, per alia detruas"', "Vi regas el la ombroj", "...sen limoj", "Talpo!", "Forigu vin!", "Dankon, Bertileto", "Neniu zorgas", "Ege malrespekte", "Zamenhof mortis.", "Bravaj vortoj", "Mdr", "+1", "Mi devus aĉeti pufmaizon", "Difinu", "Koran tankon", "Vi meritas esti aŭskultata", "Fakte!", "Vera kloakano!", "Forfikiĝu!", 'Vi ne estas finbenkisto', "Nedoankinde", "Vi obsede tajpas, tajpas, tajpas...", "Vi estas obsediĝema", "Ĉu pedanti aŭ pedantumi?..", "Spam', spam', spam'", "Ĉu vere?!"]

versio="v8"

import telebot
import time
import random
import sqlite3
from telebot import types

mesagharo = sqlite3.connect(path, check_same_thread=False)

cursor = mesagharo.cursor()

user_dict={}

class User:
    def __init__(self, name):
        self.teksto = None
        self.name = name
        self.tipo = None
        self.cu = None
        self.caption = None

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'komencu'])
def send_welcome(message):
    bot.reply_to(message, "La ludo komencu!")
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(message.chat.id, "Ĵetu viajn galantvortojn, aĉulo")
    
@bot.message_handler(commands=['montri'])
def sendu_malpermesojn(message):
 if message.chat.type == "private": 
    bot.reply_to(message, "Nun mi sendos al vi ĉiun malpermesaĵon de @Esperantujoo")
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(0.3)
    i = 0
    bot.send_message(message.chat.id, "<i>Fifrazoj:</i>", parse_mode='html')
    for frazo in cursor.execute("SELECT teksto FROM vortoj"):
        frazo = ''.join(str(x) for x in frazo)
        frazo = frazo.translate({ ord(c): None for c in "(),'" })
        bot.send_message(message.chat.id, str(frazo))
        time.sleep(0.3)
        i=+1
    if i == 0:
        bot.send_message(message.chat.id, "Nuntempe ĉiu frazo estas permesita")
    time.sleep(0.3)
    i = 0
    bot.send_message(message.chat.id, "<i>Aĉaj glumarkoj:</i>", parse_mode='html')
    for frazo in cursor.execute("SELECT teksto FROM malpermesoj WHERE tipo = 'glumarko'"):
        frazo = ''.join(str(x) for x in frazo)
        frazo = frazo.translate({ ord(c): None for c in "(),'" })
        try:
            bot.send_sticker(message.chat.id, str(frazo))
            time.sleep(0.3)
        except Exception as e:
            pass
    if i == 0:
        bot.send_message(message.chat.id, "Kloakanoj uzas normalajn glumarkojn, do mi permesas ĉiun")
    i = 0   
    for uzanto in cursor.execute("SELECT uzanta_id FROM blokituloj"): 
         i +=1
    bot.send_message(message.chat.id, "<i>Nombro de uzantoj, kiuj nuntempe ne povas regi el la ombroj:</i> " + str(i), parse_mode='html')    
 else:
     bot.send_message(message.chat.id, "Ĉi tiu komando meritas esti aŭskultata nur private")
    
@bot.message_handler(commands=['helpu'])
def sendu_helpon(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(message.chat.id, """Mi estas Robotino, ina roboto kreita speciale por @Esperantujoo. Sendu al mi private mesaĝon, kaj, se vi estas vera kloakano, mi resendos ĝin al Nova Esperantujo.
<b>Komandoj:</b>
    - /bloki "daŭreco": respondu al sendita per mi mesaĝo por silentigi la anoniman uzanton (maksimume dum unu tago, do dum 27 horoj). Ekzemple /bloki 24
    - /malpermesi "malpermesota frazo aŭ nenio, se vi volas malpermesi glumarkon". Ekzemple /malpermesi kitabo. Post tio, uzantoj ne povos sendi mesaĝon, kiu enhavas vorton 'kitabo'
    - /permesi "permesota frazo aŭ nenio, se vi volas permesi glumarkon". Ekzemple /permesi katedzino
    - /helpu: ricevi ĉi tiun mesaĝon
    - /montri: montras ĉiun malpermesaĵon (funkcias nur private)""", parse_mode='html')


@bot.message_handler(content_types = ['text', 'photo', 'video', 'animation', 'sticker', 'document', 'audio', 'voice', 'poll', "video_note"])
def sendu_tekston(message):
    print(message.chat.id)
    if message.chat.id != ne_id and message.chat.type == "private":
         if bot.get_chat_member(ne_id, message.from_user.id).status == 'left':   
             bot.send_message(message.chat.id, "Vi ne estas vera kloakano. Aliĝu: @Esperantujoo")
         elif message.chat.id != ne_id and message.chat.type != "private":
             pass
         else:       
                     idilo = message.from_user.id
                     
                     for uzanta_id in cursor.execute("SELECT uzanta_id FROM blokituloj"):
                         uzanta_id = ''.join(str(x) for x in uzanta_id)
                         if str(idilo) == uzanta_id:
                             restanta_tempo = cursor.execute("""SELECT fino FROM blokituloj WHERE uzanta_id = ?""", (uzanta_id,))
                             restanta_tempo = ''.join(str(x) for x in restanta_tempo)
                             restanta_tempo = restanta_tempo.translate({ ord(c): None for c in "(),'" })
                             restanta_tempo = int(restanta_tempo) - int(int(time.time()))
                             if restanta_tempo < 0:
                                 cursor.execute("""DELETE FROM blokituloj WHERE uzanta_id = ?""", (str(uzanta_id),)).fetchall()
                                 bot.send_message(message.chat.id, "Vi denove povas ĵeti galantvotojn per mi. Gratulon!")
                             else: bot.send_message(message.chat.id, "Vi malperdos kontrolon post " + str(restanta_tempo) + " sekundoj")
                             return
                     for frazo in cursor.execute("SELECT teksto FROM vortoj"):
                        frazo = ''.join(str(x) for x in frazo)
                        frazo = frazo.translate({ ord(c): None for c in "(),'" })
                        if message.text:
                            if message.text.lower().find(frazo.lower()) != -1:
                                if frazo.find(" ") != -1: 
                                    bot.send_message(message.chat.id, "Talpo, la frazo '" + frazo + "' estas malpermesita")
                                else:
                                    bot.send_message(message.chat.id, "Talpo, la vorto '" + frazo + "' estas malpermesita")
                                return
                        if message.caption:
                            if message.caption.lower().find(frazo.lower()) != -1:
                                bot.send_message(message.chat.id, "La frazo '" + frazo + "' estas malpermesita. Memoru tion")
                                return
                            
                     for teksto in cursor.execute("SELECT teksto FROM malpermesoj"):
                        teksto = ''.join(str(x) for x in teksto)
                        teksto = teksto.translate({ ord(c): None for c in "(),'" })
                        if message.sticker: 
                                 if message.sticker.file_unique_id == teksto:
                                     bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAOAYQaXnIR7KlEyVZogq_MwSCyvfZcAAvcPAAJ8AolL872FFh8Mc-ogBA")
                                     return
       
             
                     user_id = message.from_user.id
                     name=message.text
                     user = User(name)
                     user_dict[user_id] = user
                     user = user_dict[user_id]
                     
                     if message.text: 
                         teksto = message.text
                         user.tipo = "teksto"
                     elif message.sticker: 
                         teksto = message.sticker.file_id
                         user.tipo = "glumarko"
                     elif message.video_note:
                         teksto = message.video_note.file_id
                         user.tipo = "video_note"
                     elif message.video:
                         teksto = message.video.file_id
                         user.tipo = "video"
                     elif message.audio:
                         teksto = message.audio.file_id
                         user.tipo = "audio"
                     elif message.voice:
                         teksto = message.voice.file_id
                         user.tipo = "voice"
                     elif message.document:
                         teksto = message.document.file_id
                         user.tipo = "document"
                     elif message.photo:
                         teksto = message.photo[-1].file_id
                         user.tipo = "bildo"
                     elif message.animation:
                         teksto = message.animation.file_id
                         user.tipo = "movbildo"
                     elif message.poll:
                         teksto = message.poll
                         user.tipo = 'poll'
                     if message.caption:
                         caption = message.caption
                     else:
                         caption = None
                        
                     user.teksto = teksto
                     user.caption = caption
                     
                 
                     markup = types.ReplyKeyboardMarkup(row_width=2)
                     itembtn1 = types.KeyboardButton('Jes')
                     itembtn2 = types.KeyboardButton('Ne')
                     markup.add(itembtn1, itembtn2)
                     msg = bot.reply_to(message, "Ĉu vi certas ke vi volas sendi ĉi tiun aĉaĵon kloaken?", reply_markup=markup)
                     bot.register_next_step_handler(msg, certas_demando)
    else:
      if message.text:
        if message.text.find('/bloki') != -1:
            if message.text.find('/bloki') == 0:
                if message.reply_to_message:
                    cu_robotino = str(message.reply_to_message)
                    usernameilo = cu_robotino.find('username')
                    cu_robotino = cu_robotino[usernameilo+12:usernameilo+24]
                    if cu_robotino == 'robotino_bot':
                        cu_rego = bot.get_chat_member(ne_id, message.from_user.id).status
                        if cu_rego == "administrator" or cu_rego == "creator" or message.from_user.id == 602309534:
                            if int(message.reply_to_message.date) + 3600 > int(time.time()):
                                if len(message.text) == 6:
                                    bot.send_message(message.chat.id, "Vi forgesis tajpi longecon de bloko (en horoj). Maksimuma nombro de horoj estas 27. Ekzemple: /bloki 24")
                                    return
                                elif len(message.text) > 9:
                                    bot.send_message(message.chat.id, "La ĝusta uzo de la komando: /bloki 'daŭreco de bloko en horoj'. Ekzemple: /bloki 27")
                                    return
                                elif message.text[6] != " ":
                                    bot.send_message(message.chat.id, "La ĝusta uzo de la komando: /bloki 'daŭreco de bloko en horoj'. Ekzemple: /bloki 27")
                                    return
                                elif len(message.text) == 7:
                                    bot.send_message(message.chat.id, "Vi forgesis tajpi longecon de bloko (en horoj). Maksimuma nombro de horoj estas 27. Ekzemple: /malpermesi 24")
                                    return
                                elif len(message.text) == 8:
                                    horoj = message.text[7]
                                elif len(message.text) == 9:
                                    horoj = message.text[7:9]
                                if horoj.isnumeric():
                                    horoj = int(horoj)
                                    if horoj < 28:
                                        if message.reply_to_message.text: 
                                            teksto = message.reply_to_message.text
                                            tipo = "teksto"
                                        if message.reply_to_message.video_note: 
                                            teksto = message.reply_to_message.video_note.file_id
                                            tipo = "video_note"
                                        if message.reply_to_message.video: 
                                            teksto = message.reply_to_message.video.file_id
                                            tipo = "video"
                                        elif message.reply_to_message.sticker: 
                                            teksto = message.reply_to_message.sticker.file_id
                                            tipo = "glumarko"
                                        elif message.reply_to_message.audio:
                                            teksto = message.reply_to_message.audio.file_id
                                            tipo = "audio"
                                        elif message.reply_to_message.voice:
                                            teksto = message.reply_to_message.voice.file_id
                                            tipo = "voice"
                                        elif message.reply_to_message.document:
                                            teksto = message.reply_to_message.document.file_id
                                            tipo = "document"
                                        elif message.reply_to_message.photo:
                                            teksto = message.reply_to_message.photo[-1].file_id
                                            tipo = "bildo"
                                        elif message.reply_to_message.animation:
                                            teksto = message.reply_to_message.animation.file_id
                                            tipo = "movbildo"
                                        elif message.reply_to_message.poll:
                                            teksto = message.reply_to_message.poll
                                            tipo = 'poll'
                                        uzanta_id = cursor.execute("""SELECT uzanta_id FROM historio WHERE tipo = ? AND teksto = ?""", (str(tipo), str(teksto)))
                                        uzanta_id = ''.join(str(x) for x in uzanta_id)
                                        uzanta_id = uzanta_id.translate({ ord(c): None for c in "(),'" })
                                        cursor.execute("""INSERT INTO blokituloj VALUES (?, ?, ?)""", (str(uzanta_id), str(int(time.time())), str(int(time.time()) + 3600*horoj)))
                                        mesagharo.commit()
                                        idilo = message.chat.id
                                        bot.delete_message(idilo, message.reply_to_message.message_id)  
                                        time.sleep(0.2)
                                        bot.delete_message(idilo, message.message_id)
                                        time.sleep(0.2)
                                        for frazo in cursor.execute("SELECT uzanta_id FROM blokituloj"):
                                            frazo = ''.join(str(x) for x in frazo)
                                            frazo = frazo.translate({ ord(c): None for c in "(),'" })
                                            if frazo == "":
                                                bot.send_message(idilo, "Ĉi tiu mesaĝo estas mia, sed bone mi forigos ĝin")
                                                cursor.execute("""DELETE FROM blokituloj WHERE uzanta_id = ''""")
                                                return
                                            else:
                                                pass
                                        if horoj == 1:    
                                            bot.send_message(idilo, "La uzanto estos silentigita (dum " + str(horoj) + " horo)")    
                                        else:
                                            bot.send_message(idilo, "La uzanto estos silentigita (dum " + str(horoj) + " horoj)")    
                                        time.sleep(0.2)
                                    else:
                                        bot.send_message(message.chat.id, "Maksimuma daŭreco de bloko estas 27 horoj")
                                        return
                                else:
                                    bot.send_message(message.chat.id, "La ĝusta uzo de la komando: /bloki 'daŭreco de bloko en horoj'. Ekzemple: /bloki 27")
                                    return
                            else:
                                bot.send_message(message.chat.id, "La mesaĝo estas tre malnova, mi ne scias kiu sendis ĝin")
                        else:
                            bot.send_message(message.chat.id, "Vi ne estas aŭtoritato, " + message.from_user.first_name)
                    else:
                        bot.send_message(message.chat.id, "Mi ne povas bloki tiun, kiu nuntempe ne regas el la ombroj. Respondu al sendita per **mi** mesaĝo")
                        return
                else:
                    bot.send_message(message.chat.id, "Por bloki uzanton, respondu al mia mesaĝo. Se vi volas malpermesi frazon, uzu /malpermesi 'frazo', ekzemple /malpermesi PF estas aĉulo")
                    return
            else:
                bot.send_message(message.chat.id, "La mesaĝo devas komenci per /bloki")
                return
        elif message.text.find('/malpermesi') !=-1:
            if message.text.find('/malpermesi') == 0:
                cu_rego = bot.get_chat_member(ne_id, message.from_user.id).status
                if cu_rego == "administrator" or cu_rego == "creator" or message.from_user.id == 602309534:
                    if message.reply_to_message:
                        if len(message.text) != 11:
                            bot.send_message(message.chat.id, "Se vi volas malpermesi glumarkon, respondu al ĝi. Se vi volas malpermesi frazon, tajpu /malpermesi 'malpermesota frazo aŭ nenio, se vi volas bloki glumarkon'. Ekzemple /malpermesi kitabo")
                            return
                        else:
                                        idilo = message.chat.id
                                        if message.reply_to_message.text: 
                                            teksto = message.reply_to_message.text
                                            tipo_malp = "teksto"
                                            cursor.execute("""INSERT INTO vortoj VALUES (?)""", (teksto,))
                                        elif message.reply_to_message.sticker: 
                                            teksto = message.reply_to_message.sticker.file_unique_id
                                            tipo_malp = "glumarko"
                                            cursor.execute("""INSERT INTO malpermesoj VALUES (?, ?)""", (tipo_malp, teksto))
                                        else:
                                            tipo_malp = None
                                            time.sleep(0.2)
                                            bot.send_message(idilo, "La mesaĝo (se ĝi ne estas tro malnova) estas forigita, sed /malpermesi funkcias nur por teksto kaj glumarkoj")
                                        mesagharo.commit()
                                           
                                        if tipo_malp == "glumarko":
                                            bot.send_message(idilo, "La glumarko estas malpermesita ekde nun")
                                        elif tipo_malp == "teksto":
                                            bot.send_message(idilo, """La frazo '""" + teksto + """' estas malpermesita ekde nun""")
                                        try:
                                            bot.delete_message(idilo, message.reply_to_message.message_id)
                                        except Exception as e:
                                            pass
                                        time.sleep(0.2)
                                        bot.delete_message(idilo, message.message_id)
                    else:
                                if len(message.text) == 11:
                                    bot.send_message(message.chat.id, "Se vi volas malpermesi glumarkon, respondu al ĝi. Se vi volas malpermesi frazon, tajpu /malpermesi 'malpermesota frazo aŭ nenio, se vi volas bloki glumarkon'. Ekzemple /malpermesi kitabo")
                                    return
                                elif message.text[11] != " ":
                                    bot.send_message(message.chat.id, "La ĝusta uzo de la komando: /malpermesi 'malpermesota frazo aŭ nenio, se vi volas malpermesi glumarkon'. Ekzemple /malpermesi kitabo")
                                    return
                                else:
                                        vortoj = message.text[12: len(message.text)]
                                        if vortoj.isnumeric():
                                            bot.send_message(message.chat.id, "Oni ne povas malpermesi nombrojn")
                                            return
                                        cursor.execute("""INSERT INTO vortoj VALUES (?)""", (str(vortoj),))
                                        mesagharo.commit()
                                        idilo = message.chat.id
                                        bot.delete_message(idilo, message.message_id)
                                        time.sleep(0.2)
                                        bot.send_message(idilo, "La frazo '" + str(vortoj) + "' ekde nun estas malpermesita")
                                        time.sleep(0.2)
                else:
                    bot.send_message(message.chat.id, "Vi ne estas aŭtoritato, " + message.from_user.first_name)
                    return
            else:
                bot.send_message(message.chat.id, "La mesaĝo devas komenci per /malpermesi")
                return
        elif message.text.find("/permesi") != -1:
            if message.text.find('/permesi') == 0:
                cu_rego = bot.get_chat_member(ne_id, message.from_user.id).status
                if cu_rego == "administrator" or cu_rego == "creator" or message.from_user.id == 602309534:
                    if message.reply_to_message:
                        if len(message.text) != 8:
                            bot.send_message(message.chat.id, "Se vi volas malmalpermesi glumarkon, respondu al ĝi. Se vi volas permesi frazon, tajpu /permesi 'permesota frazo aŭ nenio, se vi volas malbloki glumarkon'. Ekzemple /permesi katedzino")
                            return
                        else:
                                        idilo = message.chat.id
                                        if message.reply_to_message.text: 
                                            teksto = message.reply_to_message.text
                                            tipo = "teksto"
                                            cursor.execute("""DELETE FROM vortoj WHERE teksto = ?""", (teksto,))
                                        elif message.reply_to_message.sticker: 
                                            teksto = message.reply_to_message.sticker.file_unique_id
                                            tipo = "glumarko"
                                            cursor.execute("""DELETE FROM malpermesoj WHERE tipo = ? AND teksto = ?""", (tipo, teksto))
                                        else:
                                            time.sleep(0.2)
                                            bot.send_message(idilo, "/permesi nuntempe funkcias nur por teksto kaj glumarkoj")
                                        mesagharo.commit()
                                           
                                        if tipo == "glumarko":
                                            bot.send_message(idilo, "La glumarko estas permesita ekde nun")
                                        elif tipo == "teksto":
                                            bot.send_message(idilo, """La frazo '""" + teksto + """' estas permesita ekde nun""")
                                        time.sleep(0.2)
                                        bot.delete_message(idilo, message.message_id)
                    else:
                                if len(message.text) == 8:
                                    bot.send_message(message.chat.id, "Se vi volas permesi glumarkon, respondu al ĝi. Se vi volas malpermesi frazon, tajpu /permesi 'permesota frazo aŭ nenio, se vi volas malbloki glumarkon'. Ekzemple /permesi Luna")
                                    return
                                elif message.text[8] != " ":
                                    bot.send_message(message.chat.id, "La ĝusta uzo de la komando: /permesi 'permesota frazo aŭ nenio, se vi volas permesi glumarkon'. Ekzemple /permesi Forigu min")
                                    return
                                else:
                                        vortoj = message.text[9: len(message.text)]
                                        if vortoj.isnumeric():
                                            bot.send_message(message.chat.id, "Oni ne povas malmalpermesi nombrojn")
                                            return
                                        cursor.execute("""DELETE FROM vortoj WHERE teksto = ?""", (str(vortoj),))
                                        mesagharo.commit()
                                        idilo = message.chat.id
                                        bot.delete_message(idilo, message.message_id)
                                        time.sleep(0.2)
                                        bot.send_message(idilo, "La frazo '" + str(vortoj) + "' ekde nun estas permesita")
                                        time.sleep(0.2)
                else:
                    bot.send_message(message.chat.id, "Vi ne estas aŭtoritato, " + message.from_user.first_name)
                    return
            else:
                bot.send_message(message.chat.id, "La mesaĝo devas komenci per /permesi")
                return
            
            
def responda_ligilo(tekst):
    if tekst.find('https://t.me/Esperantujoo/') != -1 and len(tekst) > 26 + ligila_longeco:  
        i = 0
        respondato = ""
        kie_ligilo = tekst.find('https://t.me/Esperantujoo/')
        while i < ligila_longeco:
            id_j = str(tekst[kie_ligilo + 26 + i])
            respondato = respondato + id_j
            i+=1
        print("Jen respondato" + respondato)    
        tekst = tekst[:kie_ligilo] + tekst[kie_ligilo + 26 + ligila_longeco:]
        return respondato, tekst
    
def certas_demando(message):
        try:
                 user_id = message.from_user.id
                 cu = message.text
                 user = user_dict[user_id]
                 if (cu.lower() == u'jes'):
                     user.cu = cu
                 elif cu.lower() ==u'ne':
                     time.sleep(0.3)
                     bot.reply_to(message, 'Okej')
                     return
                 else:
                    sendu_tekston(message)
                    return                   
                 
                 bot.send_chat_action(message.chat.id, 'typing')
                 bot.send_chat_action(ne_id, 'typing')

                 time.sleep(2)
                 
                 cursor.execute("""INSERT INTO historio VALUES (?, ?, ?, ?)""", (str(message.from_user.id), str(user.teksto), str(user.tipo), str(int(time.time()))))
                 mesagharo.commit()
                 
                 for tempo in cursor.execute("SELECT dato FROM historio").fetchall():
                     tempo = ''.join(str(x) for x in tempo)
                     if int(tempo) + 3600 < int(time.time()):
                         cursor.execute("DELETE FROM historio WHERE dato = '" + tempo + "'")
                 mesagharo.commit()
                 
                 capcio = user.caption
                 
                 if user.tipo == 'teksto': 
                     if responda_ligilo(user.teksto) != None:
                         respondato, tekst = responda_ligilo(user.teksto)   
                         try:
                             bot.send_message(ne_id, tekst, reply_to_message_id=respondato)
                         except Exception as e:
                             bot.send_message(ne_id, user.teksto)
                     else:
                         bot.send_message(ne_id, user.teksto)
                 else: 
                    if responda_ligilo(user.caption) != None:
                         respondato, capcio = responda_ligilo(user.caption)
                    else:
                        respondato = None
                         
                 if user.tipo == 'glumarko': 
                     bot.send_sticker(ne_id, user.teksto)
                 if user.tipo == 'movbildo':
                     bot.send_animation(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato)
                 if user.tipo == 'voice': bot.send_voice(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato)
                 if user.tipo == 'document': bot.send_document(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato)
                 if user.tipo == 'video': bot.send_video(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato)
                 if user.tipo == 'video_note': bot.send_video_note(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato)
                 if user.tipo == 'audio': bot.send_audio(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato)
                 if user.tipo == 'bildo': 
                     bot.send_photo(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato) 
                 if user.tipo == 'poll' : 
                     if user.teksto.correct_option_id != None: enketa_tipo = 'quiz'
                     else: enketa_tipo = None
                     bot.send_poll(ne_id, user.teksto.question, user.teksto.options, type = enketa_tipo, correct_option_id = user.teksto.correct_option_id, allows_multiple_answers=user.teksto.allows_multiple_answers, is_anonymous = user.teksto.is_anonymous, explanation = user.teksto.explanation)
                 
                 bot.send_message(message.chat.id, frazoj[random.randint(0,len(frazoj)-1)])

        except Exception as e:
             time.sleep(0.3)
             bot.send_message(message.chat.id, "Eraro okazis. Provu denove")


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()  
               
bot.polling()
