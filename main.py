# =============================================================================
# 
# =============================================================================

ĉu_testo = False
if ĉu_testo == False:
    TOKEN = os.environ("VERA_TOKEN")
    ne_id = -1001463711396
    ligila_longeco = 6
    path = "mesagharo.db"
    nomo_de_roboto = "robotino_bot"

frazoj = ["Mi jam perdis kontrolon", "Doksiĝema", "Mi havas mil...dan voĉon", "Vi uzas nur duonon de via cerbo, ĉu?", "Vi estas detruema", "Vi ne havas solvon", "Ni estas mense egalaj", "Ĉu vi havas 27 horojn en unu tago?", "Vi devus viziti", "Talpa penso", "Mi ne estas komencanto", "ALKUTIMIGXU KUNVIVI", "Al vi ne mankas minutoj", "Vi ne povas eviti diri ĉiam ion detruantan", "Memoru tion", "Vi ne volis esti ĉefo", "Hispanio dormas", "Forta malkrizo", "Forta krizo", "Laboru forte, sed vi faras tro...", '"Per unu mano ili konstruas, per alia detruas"', "Vi regas el la ombroj", "...sen limoj", "Talpo!", "Forigu vin!", "Dankon, Bertileto", "Neniu zorgas", "Ege malrespekte", "Zamenhof mortis.", "Bravaj vortoj", "Mdr", "+1", "Mi devus aĉeti pufmaizon", "Difinu", "Koran tankon", "Vi meritas esti aŭskultata", "Fakte!", "Vera kloakano!", "Forfikiĝu!", 'Vi ne estas finbenkisto', "Nedoankinde", "Vi obsede tajpas, tajpas, tajpas...", "Vi estas obsediĝema", "Ĉu pedanti aŭ pedantumi?..", "Spam', spam', spam'", "Ĉu vere?!", "mi lawa pona e jan", "Vi devas legi pli da kitaboj", "U U U U U U U U"]
kodilo = "@#$%^^&**!@#$%^&QOurjwSGlkqmalBX%@#$@fl%@GHSNXL:>QOS>XSO@sp&%$@#VLMIIDM@&NXS>DLkmpDWsOWI*@*@@__@_@JDKSLKSJDJWkld[**U*U*UJDJI*W*U*DJKJDIJDJ*J*DJJkwmxbfDDKI**JIJ**JIJJOIJ@*HDSNMeSOEO*E*@*@*@*@*@*NXNNjeleXU@KLLW@@**>OQP>MMNOiLEIWUEDMNVWI%^$^_*&^AHJS*%^!%&$%$"

versio="fina"

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
        self.unikilo = None
        self.ligilo = None

bot = telebot.TeleBot(TOKEN)
#paska ovo:
# =============================================================================
# @bot.message_handler(commands=['montrialdariafiuzantojn'])
# def send_fioj(message):
#       for fifiuzanto in cursor.execute("SELECT uzanta_id FROM blokituloj"):  
#           bot.send_message(message.chat.id, str(fifiuzanto))
# =============================================================================
@bot.message_handler(commands=['start', 'komencu'])
def send_welcome(message):
    bot.reply_to(message, "La ludo komencu!")
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(message.chat.id, "Ĵetu viajn galantvortojn, aĉulo")
    
@bot.message_handler(commands=['versio'])
def send_version_de_robotino(message):
    bot.reply_to(message, "Versio: " + versio)    
@bot.message_handler(commands=['redaktu'])
def redaktu_tekston(message):
 if message.chat.type == "private": 
    mesg = bot.send_message(message.chat.id, "Sendu mesaĝon, kiun vi volas redakti")
    #msg = bot.reply_to(message, "Ĉu vi certas ke vi volas sendi ĉi tiun aĉaĵon kloaken?", reply_markup=markup, )
    bot.register_next_step_handler(mesg, elektu_message)
def elektu_message(message):
    user_id = message.from_user.id
    if message.text:
        teksto_por_trovi = message.text
        tipo = "teksto"
    else:
        rtf=0
        return
    cu_trovite = cursor.execute("""SELECT dato FROM historio WHERE tipo = ? AND teksto = ? AND uzanta_id = ?""", (str(tipo), str(teksto_por_trovi), str(user_id)))
    #cu_trovite = str(cu_trovite)
    cu_trovite = ''.join(str(x) for x in cu_trovite)
    cu_trovite = cu_trovite.translate({ ord(c): None for c in "(),'" })
    if cu_trovite == "":
        bot.send_message(message.chat.id, "Mi ne trovis tiun mesaĝon")
    else:
        msg = bot.send_message(message.chat.id, "Sendu redaktitan tekston")
        bot.register_next_step_handler(msg, sendu_redaktitan)
def sendu_redaktitan(message):
     bot.send_message(message.chat.id, "Buu! Ĝi funkcias.")       
@bot.message_handler(commands=['montri'])
def sendu_malpermesojn(message):
 if message.chat.type == "private": 
    bot.reply_to(message, "Nun mi sendos al vi ĉiun malpermesaĵon de @Esperantujoo")
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1)
    
    i = 0
    bot.send_message(message.chat.id, "<i>Fifrazoj:</i>", parse_mode='html')
    for frazo in cursor.execute("SELECT teksto FROM vortoj"):
        frazo = ''.join(str(x) for x in frazo)
        frazo = frazo.translate({ ord(c): None for c in "(),'" })
        bot.send_message(message.chat.id, str(frazo))
        time.sleep(0.3)
        i =+ 1
    if i == 0:
        bot.send_message(message.chat.id, "Nuntempe ĉiu frazo estas permesita")
    time.sleep(0.3)
    
    i = 0
    bot.send_message(message.chat.id, "<i>Aĉaj glumarkoj:</i>", parse_mode='html')
    for frazo in cursor.execute("SELECT sendilo FROM malpermesoj WHERE tipo = 'glumarko'"):
        i += 1
        frazo = ''.join(str(x) for x in frazo)
        frazo = frazo.translate({ ord(c): None for c in "(),'" })
        try:
            bot.send_sticker(message.chat.id, str(frazo))
            time.sleep(0.3)
        except Exception as e:
            pass
    if i == 0:
        bot.send_message(message.chat.id, "Kloakanoj uzas normalajn glumarkojn, do mi permesas ĉiun")
        time.sleep(0.3)
    
    i = 0
    bot.send_message(message.chat.id, "<i>Bildoj, kiuj devas malaperi el nia pura kloako:</i>", parse_mode='html')
    for frazo in cursor.execute("SELECT sendilo FROM malpermesoj WHERE tipo = 'photo'"):
        i += 1
        frazo = ''.join(str(x) for x in frazo)
        frazo = frazo.translate({ ord(c): None for c in "(),'" })
        try:
            bot.send_photo(message.chat.id, frazo)
            time.sleep(0.3)
        except Exception as e:
            pass
    if i == 0:
        bot.send_message(message.chat.id, "...ne ekzistas, ĉar la kloako malpuras") 
        time.sleep(0.3)
    
    i = 0
    bot.send_message(message.chat.id, "<i>Movbildoj kun porkoj kaj orangutangoj</i>", parse_mode='html')
    for frazo in cursor.execute("SELECT sendilo FROM malpermesoj WHERE tipo = 'animation'"):
        frazo = ''.join(str(x) for x in frazo)
        frazo = frazo.translate({ ord(c): None for c in "(),'" })
        try:
            i += 1
            if i == 1: bot.send_message(message.chat.id, "(verdire kun aliaj aĉaĵoj, sed mi devas kapti vian atenton):")
            bot.send_animation(message.chat.id, str(frazo))
            time.sleep(0.3)
        except Exception as e:
            pass
    if i == 0:
        bot.send_message(message.chat.id, "...estas mojosaj, neniu malpermesus ilin") 
        time.sleep(0.3)
    
    i = 0
    bot.send_message(message.chat.id, "<i>Voĉoj, kiuj ne taŭgas por la Meza venko</i>", parse_mode='html')
    for frazo in cursor.execute("SELECT sendilo FROM malpermesoj WHERE tipo = 'voice'"):
        i += 1
        frazo = ''.join(str(x) for x in frazo)
        frazo = frazo.translate({ ord(c): None for c in "(),'" })
        try:
            bot.send_voice(message.chat.id, str(frazo))
            time.sleep(0.3)
        except Exception as e:
            pass
    if i == 0:
        bot.send_message(message.chat.id, "...ne ekzistas")
        time.sleep(0.3)
        
    i = 0
    bot.send_message(message.chat.id, "<i>Sonoj, kiuj ne meritas esti aŭskultataj:</i>", parse_mode='html')
    for frazo in cursor.execute("SELECT sendilo FROM malpermesoj WHERE tipo = 'audio'"):
        i += 1
        frazo = ''.join(str(x) for x in frazo)
        frazo = frazo.translate({ ord(c): None for c in "(),'" })
        try:
            bot.send_audio(message.chat.id, str(frazo))
            time.sleep(0.3)
        except Exception as e:
            pass
    if i == 0:
       bot.send_message(message.chat.id, "...jam estis aŭskultitaj")
    time.sleep(0.3)
        
    i = 0
    bot.send_message(message.chat.id, "<i>Videoj, kiuj ankoraŭ ne estas ĉe tubaro:</i>", parse_mode='html')
    for frazo in cursor.execute("SELECT sendilo FROM malpermesoj WHERE tipo = 'video'"):
        i += 1
        frazo = ''.join(str(x) for x in frazo)
        frazo = frazo.translate({ ord(c): None for c in "(),'" })
        try:
            bot.send_video(message.chat.id, str(frazo))
            time.sleep(0.3)
        except Exception as e:
            pass
    if i == 0:
        bot.send_message(message.chat.id, "Oni alŝultis jam ĉion, do nenio")
    time.sleep(0.3)    
        
    i = 0
    bot.send_message(message.chat.id, "<i>Videoj en timigaj cirkloj</i>", parse_mode='html')
    for frazo in cursor.execute("SELECT sendilo FROM malpermesoj WHERE tipo = 'video_note'"):
        i += 1
        frazo = ''.join(str(x) for x in frazo)
        frazo = frazo.translate({ ord(c): None for c in "(),'" })
        try:
            bot.send_video_note(message.chat.id, str(frazo))
            time.sleep(0.3)
        except Exception as e:
            pass
    if i == 0:
        bot.send_message(message.chat.id, "...ne estas timigaj. Se vi timus cirklojn, vi devus viziti")  
    time.sleep(0.3)    
        
    i = 0
    bot.send_message(message.chat.id, "<i>Dokumentoj, kie troviĝas idaĵoj</i>", parse_mode='html')
    for frazo in cursor.execute("SELECT sendilo FROM malpermesoj WHERE tipo = 'document'"):
        i += 1
        frazo = ''.join(str(x) for x in frazo)
        frazo = frazo.translate({ ord(c): None for c in "(),'" })
        try:
            bot.send_document(message.chat.id, str(frazo))
            time.sleep(0.3)
        except Exception as e:
            pass
    if i == 0:
        bot.send_message(message.chat.id, "...ne povas esti senditaj per veraj kloakanoj.")  
    time.sleep(0.3)    
        
    i = 0
    bot.send_message(message.chat.id, "<i>La plej malbonaj ekzemploj de enketokratio</i>", parse_mode='html')
    for frazo in cursor.execute("SELECT teksto FROM malpermesoj WHERE tipo = 'poll'"):        
        i += 1
        options = str(frazo).replace("('", "").split(kodilo)
        frazo = str(frazo).replace("('", "").split(kodilo)
        
        options.pop(0)
        options[len(options)-1] = options[len(options)-1].translate ({ord(c): "" for c in "',)"})
       # options[len(options)-1].replace("',)", "")
# =============================================================================
#         frazo = ''.join(str(x) for x in frazo)
#         frazo = frazo.translate({ ord(c): None for c in "(),'" })
# =============================================================================
        try:
            #if frazo.correct_option_id != None: enketa_tipo = 'quiz'
            bot.send_poll(message.chat.id, frazo[0], options)
           # bot.send_poll(message.chat.id, frazo.question, frazo.options, type = enketa_tipo, correct_option_id = frazo.correct_option_id, allows_multiple_answers=frazo.allows_multiple_answers, is_anonymous = frazo.is_anonymous, explanation = frazo.explanation)
            time.sleep(0.3)
        except Exception as e:
            pass
    if i == 0:
        bot.send_message(message.chat.id, "...ankoraŭ ne naskiĝis")
            
        
    i = 0   
    for uzanto in cursor.execute("SELECT uzanta_id FROM blokituloj"): 
         i += 1
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
    - /malpermesi "malpermesota frazo aŭ nenio, se vi volas malpermesi responditan mesaĝon". Ekzemple /malpermesi kitabo. Post tio, uzantoj ne povos sendi mesaĝon, kiu enhavas vorton 'kitabo'
    - /permesi "permesota frazo aŭ nenio, se vi volas permesi responditan mesaĝon". Ekzemple /permesi katedzino
    - /helpu: ricevi ĉi tiun mesaĝon
    - /montri: montras ĉiun malpermesaĵon (funkcias nur private)
Se vi volas silentigi uzanton, sed vi ne estas administranto, respondu al mesaĝo per '-' aŭ '-1'. Se la uzanto ricevos kvin 'minusojn', la ulo (li/ŝi/ĝi/ŝli/ri/oni/ĥi/hi/di/pfi/oĝi/*alia_pronomo*) estos silentigita dum unu horo
Se vi volas pozitive influi karmon de anonima uzanto, respondu al mesaĝo per '+' aŭ '+1'.
Se vi volas respondi al mesaĝo, sendu al mi la ligilon aŭ metu ĝin en vian mesaĝon""", parse_mode='html')


@bot.message_handler(content_types = ['text', 'photo', 'video', 'animation', 'sticker', 'document', 'audio', 'voice', 'poll', "video_note"])
def sendu_tekston(message):
# =============================================================================
#     info = str(message)
#     if len(info) > 4096:
#         for x in range(0, len(info), 4096):
#             bot.send_message(message.chat.id, info[x:x+4096])
#     else:
#         bot.send_message(message.chat.id, info)
# =============================================================================
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
                        elif message.photo:
                                 if message.photo[-1].file_unique_id == teksto:
                                     bot.send_message(message.chat.id, "La bildo estas malpermesita")
                                     return
                        elif message.voice:
                                 if message.voice.file_unique_id == teksto:
                                     bot.send_message(message.chat.id, "Vi forte laboras por la Meza venko, sed talpoj ne permesas sendi ĉi tiun voĉdosieron")
                                     return         
                        elif message.audio:
                                 if message.audio.file_unique_id == teksto:
                                     bot.send_message(message.chat.id, "Vi forte laboras por la Meza venko, sed talpoj ne permesas sendi ĉi tiun sondosieron")
                                     return
                        elif message.video:
                                 if message.video.file_unique_id == teksto:
                                     bot.send_message(message.chat.id, "Ĉi tiu videaĵo ne meritas esti ĉe tubaro, do mi ne sendas ĝin")
                                     return
                        elif message.video_note:
                                 if message.video_note.file_unique_id == teksto:
                                     bot.send_message(message.chat.id, "Ĉi tiu cirkla videaĵo timigas min")
                                     return
                        elif message.animation:
                                 if message.animation.file_unique_id == teksto:
                                     bot.send_message(message.chat.id, "Ĉi tiu videaĵo ne meritas esti ĉe tubaro, do mi ne sendas ĝin")
                                     return
                        elif message.document:
                                 if message.document.file_unique_id == teksto:
                                     bot.send_message(message.chat.id, "La dosiero estas kontraŭfundamenta")
                                     return
                        elif str(message).find("poll") != -1:                                
                                 el_sms = message.poll
                                 unikilo = el_sms.question
                                 tipo = 'poll'
                                 i = 0
                                 while i < 11:
                                     try:    
                                         opcioj = el_sms.options[i].text
                                         i +=1
                                         unikilo = unikilo + kodilo + opcioj
                                     except Exception as e:
                                         i = 11
                                 if str(unikilo) == str(teksto):
                                     bot.send_message(message.chat.id, "Mi ne ŝatas la enketokration")
                                     return
                                 
                     def nova_teksto(mesg):
                          time.sleep(0.5)
                          try:
                              bot.edit_message_text(chat_id=ne_id, text=mesg.text, message_id = idilo)
                              cursor.execute("UPDATE historio SET teksto = ? WHERE uzanta_id = ? AND teksto = ?", (str(mesg.text), str(message.from_user.id), str(message.text)))
                              mesagharo.commit()
                          except Exception as e:
                              bot.send_message(mesg.chat.id, "Mi ne sukcesis vin. Pardonu!")
                              return
                          time.sleep(0.5)
                          bot.send_message(mesg.chat.id, frazoj[random.randint(0,len(frazoj)-1)])
                          return
                      
                     if message.forward_from:
                         if message.forward_from.username == nomo_de_roboto:
                             if message.text:
                                 time.sleep(0.3)
                                 idilo = cursor.execute("SELECT idilo FROM historio WHERE uzanta_id = ? AND teksto = ?", (str(message.from_user.id), str(message.text)))
                                 idilo = ''.join(str(x) for x in idilo)
                                 idilo = idilo.translate({ ord(c): None for c in "(),'" })
                                 print(idilo)
                                 if idilo == "" or idilo == " ":
                                     bot.send_message(message.chat.id, "Ne, tiu mesaĝo mojosas, mi ne redaktos ĝin")
                                 else:
                                     mesg = bot.send_message(message.chat.id, "Skribu novan tekston de la mesaĝo")
                                     bot.register_next_step_handler(mesg, nova_teksto)                                 
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
                         user.unikilo = message.sticker.file_unique_id
                     elif message.video_note:
                         teksto = message.video_note.file_id
                         user.tipo = "video_note"
                         user.unikilo = message.video_note.file_unique_id
                     elif message.video:
                         teksto = message.video.file_id
                         user.tipo = "video"
                         user.unikilo = message.video.file_unique_id
                     elif message.audio:
                         teksto = message.audio.file_id
                         user.tipo = "audio"
                         user.unikilo = message.audio.file_unique_id
                     elif message.voice:
                         teksto = message.voice.file_id
                         user.tipo = "voice"
                         user.unikilo = message.voice.file_unique_id
                     elif message.document:
                         teksto = message.document.file_id
                         user.tipo = "document"
                         user.unikilo = message.document.file_unique_id
                     elif message.photo:
                         teksto = message.photo[-1].file_id
                         user.tipo = "bildo"
                         user.unikilo = message.photo[-1].file_unique_id
                     elif message.animation:
                         teksto = message.animation.file_id
                         user.tipo = "movbildo"
                         user.unikilo = message.animation.file_unique_id
                     elif message.poll:
                         teksto = message.poll
                         user.tipo = 'poll'
                         i = 0
                         user.unikilo = teksto.question
                         while i < 11:
                             try: 
                                 
                                 opcioj = teksto.options[i].text
                                 i +=1
                                 user.unikilo = user.unikilo + kodilo + opcioj
                             except Exception as e:
                                 i = 11
                                 
                     
                     if message.caption:
                         caption = message.caption
                     else:
                         caption = None
                        
                     user.teksto = teksto
                     user.caption = caption
                     
                 
                     markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
                     itembtn1 = types.KeyboardButton('Jes')
                     itembtn2 = types.KeyboardButton('Ne')
                     markup.add(itembtn1, itembtn2)
                     msg = bot.reply_to(message, "Ĉu vi certas ke vi volas sendi ĉi tiun aĉaĵon kloaken?", reply_markup=markup, )
                     bot.register_next_step_handler(msg, certas_demando)
    elif str(message.chat.id) == str(ne_id):
      if message.text:
        if message.text.find('/bloki') != -1:
            if message.text.find('/bloki') == 0:
                if message.reply_to_message:
                    cu_robotino = str(message.reply_to_message)
                    usernameilo = cu_robotino.find('username')
                    cu_robotino = cu_robotino[usernameilo+12:usernameilo+24]
                    if cu_robotino == nomo_de_roboto:
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
                                    bot.send_message(message.chat.id, "Vi forgesis tajpi longecon de la silentigo (en horoj). Maksimuma nombro de horoj estas 27. Ekzemple: /bloki 24")
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
                                            unikilo = None
                                        if message.reply_to_message.video_note: 
                                            teksto = message.reply_to_message.video_note.file_id
                                            tipo = "video_note"
                                            unikilo = message.reply_to_message.video_note.file_unique_id
                                        if message.reply_to_message.video: 
                                            teksto = message.reply_to_message.video.file_id
                                            tipo = "video"
                                            unikilo = message.reply_to_message.video.file_unique_id
                                        elif message.reply_to_message.sticker: 
                                            teksto = message.reply_to_message.sticker.file_id
                                            unikilo = message.reply_to_message.sticker.file_unique_id                                          
                                            tipo = "glumarko"
                                        elif message.reply_to_message.audio:
                                            teksto = message.reply_to_message.audio.file_id
                                            tipo = "audio"
                                            unikilo = message.reply_to_message.audio.file_unique_id
                                        elif message.reply_to_message.voice:
                                            teksto = message.reply_to_message.voice.file_id
                                            tipo = "voice"
                                            unikilo = message.reply_to_message.voice.file_unique_id
                                        elif message.reply_to_message.document:
                                            teksto = message.reply_to_message.document.file_id
                                            tipo = "document"
                                            unikilo = message.reply_to_message.document.file_unique_id
                                        elif message.reply_to_message.photo:
                                            teksto = message.reply_to_message.photo[-1].file_id
                                            unikilo = message.reply_to_message.photo[-1].file_unique_id
                                            tipo = "bildo"
                                        elif message.reply_to_message.animation:
                                            teksto = message.reply_to_message.animation.file_id
                                            tipo = "movbildo"
                                            unikilo = message.reply_to_message.animation.file_unique_id
                                        elif str(message.reply_to_message).find("poll") != -1:
                                            teksto = message.reply_to_message.poll
                                            unikilo = teksto.question
                                            tipo = 'poll'
                                            i = 0
                                            while i < 11:
                                                try:    
                                                    opcioj = teksto.options[i].text
                                                    i +=1
                                                    unikilo = unikilo + kodilo + opcioj
                                                except Exception as e:
                                                    i = 11
                                        #print("Reply-unikilo por bloki" + unikilo)    
                                        if tipo != "teksto":    
                                            uzanta_id = cursor.execute("""SELECT uzanta_id FROM historio WHERE tipo = ? AND unikilo = ?""", (str(tipo), str(unikilo)))
                                        else:
                                            uzanta_id = cursor.execute("""SELECT uzanta_id FROM historio WHERE tipo = ? AND teksto = ?""", (str(tipo), str(teksto)))
                                        uzanta_id = ''.join(str(x) for x in uzanta_id)
                                        uzanta_id = uzanta_id.translate({ ord(c): None for c in "(),'" })
                                        cursor.execute("""INSERT INTO blokituloj VALUES (?, ?, ?)""", (str(uzanta_id), str(int(time.time())), str(int(time.time()) + 3600*horoj)))
                                        mesagharo.commit()
                                        idilo = message.chat.id
                                        try:
                                            bot.delete_message(idilo, message.reply_to_message.message_id)  
                                            time.sleep(0.2)
                                        except Exception as e: 
                                            pass
                                        try:
                                            bot.delete_message(idilo, message.message_id)
                                            time.sleep(0.2)
                                        except Exception as e:
                                            pass
                                        for frazo in cursor.execute("SELECT uzanta_id FROM blokituloj").fetchall():
                                            frazo = ''.join(str(x) for x in frazo)
                                            frazo = frazo.translate({ ord(c): None for c in "(),'" })
                                            if frazo == "":
                                                bot.send_message(idilo, "Ĉi tiu mesaĝo estas mia, sed bone, mi forigos ĝin")
                                                cursor.execute("""DELETE FROM blokituloj WHERE uzanta_id = ''""").fetchall()
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
                #bot.send_message(message.chat.id, "La mesaĝo devas komenci per /bloki")
                rtf = 0
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
                                            sendilo = teksto
                                            tipo_malp = "teksto"
                                            cursor.execute("""INSERT INTO vortoj VALUES (?)""", (teksto,))
                                        elif message.reply_to_message.sticker: 
                                            teksto = message.reply_to_message.sticker.file_unique_id
                                            sendilo = message.reply_to_message.sticker.file_id
                                            tipo_malp = "glumarko"
                                        elif message.reply_to_message.photo: 
                                            teksto = message.reply_to_message.photo[-1].file_unique_id
                                            tipo_malp = "photo"
                                            sendilo = message.reply_to_message.photo[-1].file_id
                                        elif message.reply_to_message.voice: 
                                            teksto = message.reply_to_message.voice.file_unique_id
                                            tipo_malp = "voice"  
                                            sendilo = message.reply_to_message.voice.file_id
                                        elif message.reply_to_message.audio: 
                                            teksto = message.reply_to_message.audio.file_unique_id
                                            tipo_malp = "audio"
                                            sendilo = message.reply_to_message.audio.file_id
                                        elif message.reply_to_message.video:
                                            sendilo = message.reply_to_message.video.file_id
                                            teksto = message.reply_to_message.video.file_unique_id
                                            tipo_malp = "video"
                                        elif message.reply_to_message.video_note: 
                                            sendilo = message.reply_to_message.video_note.file_id
                                            teksto = message.reply_to_message.video_note.file_unique_id
                                            tipo_malp = "video_note"    
                                        elif message.reply_to_message.document: 
                                            teksto = message.reply_to_message.document.file_unique_id
                                            tipo_malp = "document"
                                            sendilo = message.reply_to_message.document.file_id
                                        elif message.reply_to_message.animation:
                                            sendilo = message.reply_to_message.animation.file_id
                                            teksto = message.reply_to_message.sticker.file_unique_id
                                            tipo_malp = "movbildo"
                                        elif str(message.reply_to_message).find("poll") != -1: 
                                            teksto = message.reply_to_message.poll
# =============================================================================
#                                             kiaj_opcioj = teksto.options
#                                             kiaj_opcioj = ''.join(str(x) for x in kiaj_opcioj)
#                                             sendilo = str(teksto.question) + kodilo + str(kiaj_opcioj)
# =============================================================================
                                            sendilo = None
                                            i = 0
                                            unikilo = teksto.question
                                            while i < 11:
                                                try:    
                                                    opcioj = teksto.options[i].text
                                                    i +=1
                                                    unikilo = unikilo + kodilo + opcioj
                                                except Exception as e:
                                                    i = 11
                                            teksto = unikilo        
                                            tipo_malp = "poll"
                                        else:
                                            bot.send_message(message.chat.id, "MI ne povas trovi la mesaĝon en la datumbazo.")
                                            return
                                        cursor.execute("""INSERT INTO malpermesoj VALUES (?, ?, ?)""", (tipo_malp, teksto, str(sendilo)))
                                        mesagharo.commit()
                                           
                                        if tipo_malp != "teksto":
                                            bot.send_message(idilo, "La aĉaĵo estas malpermesita ekde nun")
                                        elif tipo_malp == "teksto":
                                            if str(teksto).find(" ") != -1:
                                                bot.send_message(idilo, """La frazo '""" + teksto + """' estas malpermesita ekde nun""")
                                            else:
                                                bot.send_message(idilo, """La vorto '""" + teksto + """' estas malpermesita ekde nun""")
                                        time.sleep(0.3)
                                        try:
                                            bot.delete_message(idilo, message.reply_to_message.message_id)
                                        except Exception as e:
                                            bot.send_message(message.chat.id, "La mesaĝo ne povas esti forigita, sed la enhavo estas malpermesita ekde nun")
                                        try:
                                            bot.delete_message(idilo, message.id)
                                        except Exception as e:
                                            pass
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
                                        try:
                                            bot.delete_message(idilo, message.message_id)
                                            time.sleep(0.2)
                                        except Exception as e:
                                            pass
                                        bot.send_message(idilo, "La frazo '" + str(vortoj) + "' ekde nun estas malpermesita")
                                        time.sleep(0.2)
                else:
                    bot.send_message(message.chat.id, "Vi ne estas aŭtoritato, " + message.from_user.first_name)
                    return
            else:
                #bot.send_message(message.chat.id, "La mesaĝo devas komenci per /malpermesi")
                rtf = 0
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
                                            if str(teksto).find(" ") != -1:
                                                bot.send_message(idilo, """La frazo '""" + teksto + """' estas permesita ekde nun""")
                                            else:
                                                bot.send_message(idilo, """La vorto '""" + teksto + """' estas permesita ekde nun""")
                                            mesagharo.commit()
                                            return
                                        elif message.reply_to_message.sticker: 
                                            teksto = message.reply_to_message.sticker.file_unique_id
                                            tipo = "glumarko"
                                        elif message.reply_to_message.photo: 
                                            teksto = message.reply_to_message.photo[-1].file_unique_id
                                            tipo = "photo"
                                        elif message.reply_to_message.video: 
                                            teksto = message.reply_to_message.video.file_unique_id
                                            tipo = "video"  
                                        elif message.reply_to_message.video_note: 
                                            teksto = message.reply_to_message.video_note.file_unique_id
                                            tipo = "video_note" 
                                        elif message.reply_to_message.audio: 
                                            teksto = message.reply_to_message.audio.file_unique_id
                                            tipo = "audio"  
                                        elif message.reply_to_message.voice: 
                                            teksto = message.reply_to_message.voice.file_unique_id
                                            tipo = "voice" 
                                        elif message.reply_to_message.document: 
                                            teksto = message.reply_to_message.document.file_unique_id
                                            tipo = "document"
                                        elif message.reply_to_message.animation: 
                                            teksto = message.reply_to_message.animation.file_unique_id
                                            tipo = "movbildo"  
                                        elif str(message.reply_to_message).find("poll") != -1: 
                                            teksto = message.reply_to_message.poll
                                            i = 0
                                            unikilo = teksto.question
                                            while i < 11:
                                                try:    
                                                    opcioj = teksto.options[i].text
                                                    i += 1
                                                    unikilo = unikilo + kodilo + opcioj
                                                except Exception as e:
                                                    i = 11
                                            teksto = unikilo        
                                            tipo = "poll"    
                                        else:
                                            time.sleep(0.2)
                                            bot.send_message(idilo, "/permesi nuntempe ne funkcias por ĉi tiu tipo de mesaĝoj")
                                            return
                                        bot.send_message(idilo, "La aĵo ne plu blokitas per talpoj")
                                        try:
                                            bot.delete_message(idilo, message.id)
                                        except Exception as e:
                                            pass
                                        cursor.execute("""DELETE FROM malpermesoj WHERE tipo = ? AND teksto = ?""", (tipo, teksto))
                                        mesagharo.commit()
                                           
                    else:
                                if len(message.text) == 8:
                                    bot.send_message(message.chat.id, "Se vi volas permesi ion, respondu al ĝi. Se vi volas permesi frazon, tajpu /permesi 'permesota frazo aŭ vorto'. Ekzemple /permesi Luna")
                                    return
                                elif message.text[8] != " ":
                                    bot.send_message(message.chat.id, "La ĝusta uzo de la komando: /permesi 'permesota frazo aŭ nenio, se vi volas permesi respondatan mesaĝon'. Ekzemple /permesi Forigu min")
                                    return
                                else:
                                        vortoj = message.text[9: len(message.text)]
                                        if vortoj.isnumeric():
                                            bot.send_message(message.chat.id, "Oni ne povas malmalpermesi nombrojn")
                                            return
                                        cursor.execute("""DELETE FROM vortoj WHERE teksto = ?""", (str(vortoj),))
                                        mesagharo.commit()
                                        idilo = message.chat.id
                                        try:
                                            bot.delete_message(idilo, message.message_id)
                                            time.sleep(0.2)
                                        except Exception as e:    
                                            pass
                                        if str(vortoj).find(" ") != -1:
                                            bot.send_message(idilo, "La frazo '" + str(vortoj) + "' ekde nun estas permesita")
                                        else: 
                                            bot.send_message(idilo, "La vorto '" + str(vortoj) + "' ekde nun estas permesita")
                                        time.sleep(0.2)
                else:
                    bot.send_message(message.chat.id, "Vi ne estas aŭtoritato, " + message.from_user.first_name)
                    return
            else:
                #bot.send_message(message.chat.id, "La mesaĝo devas komenci per /permesi")
                rtf = 0
                return
        elif message.text == "-" or message.text == "-1":
            if message.reply_to_message:
                cu_robotino = str(message.reply_to_message)
                usernameilo = cu_robotino.find('username')
                cu_robotino = cu_robotino[usernameilo+12:usernameilo+24]
                #bot.send_message(message.chat.id, message)
                if cu_robotino == nomo_de_roboto:
                    if int(message.reply_to_message.date) + 3600 > int(time.time()):
                                        if message.reply_to_message.text: 
                                            teksto = message.reply_to_message.text
                                            tipo = "teksto"
                                        elif message.reply_to_message.video_note: 
                                            teksto = message.reply_to_message.video_note.file_unique_id
                                            tipo = "video_note"
                                        elif message.reply_to_message.video: 
                                            teksto = message.reply_to_message.video.file_unique_id
                                            tipo = "video"
                                        elif message.reply_to_message.sticker: 
                                            teksto = message.reply_to_message.sticker.file_unique_id
                                           
                                            tipo = "glumarko"
                                        elif message.reply_to_message.audio:
                                            teksto = message.reply_to_message.audio.file_unique_id
                                            tipo = "audio"
                                        elif message.reply_to_message.voice:
                                            teksto = message.reply_to_message.voice.file_unique_id
                                            tipo = "voice"
                                        elif message.reply_to_message.document:
                                            teksto = message.reply_to_message.document.file_unique_id
                                            tipo = "document"
                                        elif message.reply_to_message.photo:
                                            teksto = message.reply_to_message.photo[-1].file_unique_id
                                            tipo = "bildo"
                                        elif message.reply_to_message.animation:
                                            teksto = message.reply_to_message.animation.file_unique_id
                                            tipo = "movbildo"
                                        elif str(message.reply_to_message).find("poll") != -1:
                                            teksto = message.reply_to_message.poll
                                            unikilo = teksto.question
                                            i = 0
                                            while i < 11:
                                                try:    
                                                    opcioj = teksto.options[i].text
                                                    i +=1
                                                    unikilo = unikilo + kodilo + opcioj
                                                except Exception as e:
                                                    i = 11
                                            tipo = 'poll'
                                            teksto = unikilo
                                        if tipo != "teksto":    
                                            nombro = 0
                                            for or_bi in cursor.execute("""SELECT uzanta_id FROM historio WHERE unikilo = ?""", (str(teksto),)).fetchall():
                                                nombro += 1
                                            fiuzanto = cursor.execute("""SELECT uzanta_id FROM historio WHERE unikilo = ?""", (str(teksto),))                                           
                                        else:
                                            nombro = 0
                                            for i in cursor.execute("""SELECT uzanta_id FROM historio WHERE teksto = ?""", (str(teksto),)).fetchall():
                                                nombro += 1
                                            fiuzanto = cursor.execute("""SELECT uzanta_id FROM historio WHERE teksto = ?""", (str(teksto),))
                                        fiuzanto = ''.join(str(x) for x in fiuzanto)
                                        fiuzanto = fiuzanto.translate({ ord(c): None for c in "(),'" })
                                        if nombro != 0:
                                            nombro = len(fiuzanto) / nombro
                                            fiuzanto = fiuzanto[:int(nombro)]
                                        if fiuzanto == "":
                                            bot.send_message(message.chat.id, "Laboru forte, sed ne tro. Vi ne povas silentigi min.")
                                            cursor.execute("""DELETE FROM karmo WHERE fiuzanto = ''""").fetchall()
                                            return
                                        for cu_jam in cursor.execute("""SELECT raportanto FROM karmo WHERE fiuzanto = ?""", (fiuzanto,)).fetchall(): 
                                            cu_jam = ''.join(str(x) for x in cu_jam)
                                            cu_jam = cu_jam.translate({ ord(c): None for c in "(),'"})
                                            if str(message.from_user.id) == cu_jam:
                                                bot.send_message(message.chat.id, "Vi jam raportis ĉi tiun aĉulon")
                                                return
                                        cursor.execute("""INSERT INTO karmo VALUES (?,?)""", (str(fiuzanto), str(message.from_user.id)))
                                        mesagharo.commit()
                                        
                                        i = 0
                                        for kio in cursor.execute("""SELECT raportanto FROM karmo WHERE fiuzanto = ?""", (str(fiuzanto),)).fetchall():
                                            i-=1 
                                        for kio in cursor.execute("""SELECT raportanto FROM karmo_b WHERE bonulo = ?""", (str(fiuzanto),)).fetchall():
                                            i+=1    
                                        if i < -4:
                                            cursor.execute("""INSERT INTO blokituloj VALUES (?,?,?)""", (str(fiuzanto), str(int(time.time())), str(int(time.time()) + 3600),))
                                            cursor.execute("""DELETE FROM karmo WHERE fiuzanto = ?""", (str(fiuzanto),)).fetchall()
                                            cursor.execute("""DELETE FROM karmo_b WHERE bonulo = ?""", (str(fiuzanto),)).fetchall()
                                            mesagharo.commit()
                                            bot.send_message(message.chat.id, "La uzanto estos silentigita dum unu horo")
                                            try:
                                                time.sleep(0.3)
                                                bot.delete_message(message.chat.id, message.reply_to_message.message_id)
                                            except Exception as e:
                                                pass
                                        else:
                                            if i > 0 : bot.send_message(message.chat.id, "Karmo de la uzanto: +" + str(i))
                                            else: bot.send_message(message.chat.id, "Karmo de la uzanto: " + str(i))
                    else:
                        bot.send_message(message.chat.id, "La mesaĝo estas tro malnova, mi ne scias, kiu sendis ĝin")
                else:
                    #bot.send_message(message.chat.id, "Respondu al sendita per **mi** messaĝo")
                    rtf = 0
            else:
                #bot.send_message(message.chat.id, "Respondu al mesaĝo por influi karmon de uzanto")
                rtf = 0
        elif message.text == "+" or message.text == "+1":
            if message.reply_to_message:
                cu_robotino = str(message.reply_to_message)
                usernameilo = cu_robotino.find('username')
                cu_robotino = cu_robotino[usernameilo+12:usernameilo+24]
                #bot.send_message(message.chat.id, message)
                if cu_robotino == nomo_de_roboto:
                    if int(message.reply_to_message.date) + 3600 > int(time.time()):
                                        if message.reply_to_message.text: 
                                            teksto = message.reply_to_message.text
                                            tipo = "teksto"
                                        elif message.reply_to_message.video_note: 
                                            teksto = message.reply_to_message.video_note.file_unique_id
                                            tipo = "video_note"
                                        elif message.reply_to_message.video: 
                                            teksto = message.reply_to_message.video.file_unique_id
                                            tipo = "video"
                                        elif message.reply_to_message.sticker: 
                                            teksto = message.reply_to_message.sticker.file_unique_id
                                           
                                            tipo = "glumarko"
                                        elif message.reply_to_message.audio:
                                            teksto = message.reply_to_message.audio.file_unique_id
                                            tipo = "audio"
                                        elif message.reply_to_message.voice:
                                            teksto = message.reply_to_message.voice.file_unique_id
                                            tipo = "voice"
                                        elif message.reply_to_message.document:
                                            teksto = message.reply_to_message.document.file_unique_id
                                            tipo = "document"
                                        elif message.reply_to_message.photo:
                                            teksto = message.reply_to_message.photo[-1].file_unique_id
                                            tipo = "bildo"
                                        elif message.reply_to_message.animation:
                                            teksto = message.reply_to_message.animation.file_unique_id
                                            tipo = "movbildo"
                                        elif str(message.reply_to_message).find("poll") != -1:
                                            teksto = message.reply_to_message.poll
                                            unikilo = teksto.question
                                            i = 0
                                            while i < 11:
                                                try:    
                                                    opcioj = teksto.options[i].text
                                                    i +=1
                                                    unikilo = unikilo + kodilo + opcioj
                                                except Exception as e:
                                                    i = 11
                                            tipo = 'poll'
                                            teksto = unikilo  
                                        if tipo != "teksto":    
                                            nombro = 0
                                            for or_bi in cursor.execute("""SELECT uzanta_id FROM historio WHERE unikilo = ?""", (str(teksto),)).fetchall():
                                                nombro += 1
                                            bonuzanto = cursor.execute("""SELECT uzanta_id FROM historio WHERE unikilo = ?""", (str(teksto),))                                           
                                        else:
                                            nombro = 0
                                            for i in cursor.execute("""SELECT uzanta_id FROM historio WHERE teksto = ?""", (str(teksto),)).fetchall():
                                                nombro += 1
                                            bonuzanto = cursor.execute("""SELECT uzanta_id FROM historio WHERE teksto = ?""", (str(teksto),))
                                        bonuzanto = ''.join(str(x) for x in bonuzanto)
                                        bonuzanto = bonuzanto.translate({ ord(c): None for c in "(),'" })
                                        if nombro != 0:
                                            nombro = len(bonuzanto) / nombro
                                            bonuzanto = bonuzanto[:int(nombro)]
                                        if bonuzanto == "":
                                            bot.send_message(message.chat.id, "Ho, ĉu vi simpas?")
                                            cursor.execute("""DELETE FROM karmo_b WHERE bonulo = ''""").fetchall()
                                            return
                                        for cu_jam in cursor.execute("""SELECT raportanto FROM karmo_b WHERE bonulo = ?""", (bonuzanto,)).fetchall(): 
                                            cu_jam = ''.join(str(x) for x in cu_jam)
                                            cu_jam = cu_jam.translate({ ord(c): None for c in "(),'"})
                                            if str(message.from_user.id) == cu_jam:
                                                bot.send_message(message.chat.id, "Via simpado por ĉi tiu uzanto ne havas limojn")
                                                return
                                        cursor.execute("""INSERT INTO karmo_b VALUES (?,?)""", (str(bonuzanto), str(message.from_user.id)))
                                        mesagharo.commit()
                                        
                                        i = 0
                                        for kio in cursor.execute("""SELECT raportanto FROM karmo_b WHERE bonulo = ?""", (str(bonuzanto),)).fetchall():
                                            i+=1
                                        for kiob in cursor.execute("""SELECT raportanto FROM karmo WHERE fiuzanto = ?""", (str(bonuzanto),)).fetchall():
                                            i-=1    
                                        if i < -4:
                                            cursor.execute("""INSERT INTO blokituloj VALUES (?,?,?)""", (str(fiuzanto), str(int(time.time())), str(int(time.time()) + 3600),))
                                            cursor.execute("""DELETE FROM karmo WHERE fiuzanto = ?""", (str(fiuzanto),)).fetchall()
                                            cursor.execute("""DELETE FROM karmo_b WHERE bonulo = ?""", (str(fiuzanto),)).fetchall()
                                            mesagharo.commit()
                                            bot.send_message(message.chat.id, "La uzanto estos silentigita dum unu horo")
                                            try:
                                                time.sleep(0.3)
                                                bot.delete_message(message.chat.id, message.reply_to_message.message_id)
                                            except Exception as e:
                                                pass
                                        else:
                                            if i > 0 : bot.send_message(message.chat.id, "Karmo de la uzanto: +" + str(i))
                                            else: bot.send_message(message.chat.id, "Karmo de la uzanto: " + str(i))
                    else:
                        bot.send_message(message.chat.id, "La mesaĝo estas tro malnova, mi ne scias, kiu sendis ĝin")
                else:
                    #bot.send_message(message.chat.id, "Respondu al sendita per **mi** messaĝo")
                    rtf = 0
            else:
                #bot.send_message(message.chat.id, "Respondu al mesaĝo por influi karmon de uzanto")
                rtf = 0
    else:
        bot.send_message(message.chat.id, "Via mesaĝo ne povas esti sendita pro talpoj. Identilo de babilejo: " + str(ne_id) + " tamen devus esti " + str(message.chat.id) + ". Tipo de babilejo: " + str(message.chat.type))
def responda_ligilo(tekst):
    if tekst.find('https://t.me/Esperantujoo/') != -1 and len(tekst) > 26 + ligila_longeco:  
        i = 0
        respondato = ""
        kie_ligilo = tekst.find('https://t.me/Esperantujoo/')
        while i < ligila_longeco:
            id_j = str(tekst[kie_ligilo + 26 + i])
            respondato = respondato + id_j
            i+=1
         
        tekst = tekst[:kie_ligilo] + tekst[kie_ligilo + 26 + ligila_longeco:]
        return respondato, tekst
    elif tekst.find("https://t.me/Esperantujoo/") != -1 and len(tekst) == 26 + ligila_longeco:
        respondato = str(tekst[26:])
        tekst = "👆"
        return respondato, tekst
    else: 
        respondato = None
        return respondato, tekst
    
def certas_demando(message):
        #try:
                 user_id = message.from_user.id
                 if message.text:
                     cu = message.text
                 else:
                     sendu_tekston(message)
                     return
                 user = user_dict[user_id]
                 if (cu.lower() == u'jes'):
                     user.cu = cu
                 elif cu.lower() == u'ne':
                     time.sleep(0.3)
                     bot.reply_to(message, 'Okej')
                     return
                 else:
                    sendu_tekston(message)
                    return                   
                 
                 bot.send_chat_action(message.chat.id, 'typing')
                 bot.send_chat_action(ne_id, 'typing')

                 time.sleep(2)
                                 
                 capcio = user.caption
                 
                 if user.tipo == 'teksto': 
                     if responda_ligilo(user.teksto) != None:
                         respondato, tekst = responda_ligilo(user.teksto)   
                         try:
                             msg = bot.send_message(ne_id, tekst, reply_to_message_id=respondato)
                         except Exception as e:
                             msg = bot.send_message(ne_id, user.teksto)
                     else:
                         msg = bot.send_message(ne_id, user.teksto)
                 elif user.tipo != "poll" and user.tipo != "glumarko": 
                    if responda_ligilo(str(user.caption)) != None:
                         respondato, capcio = responda_ligilo(user.caption)
                    else:
                        respondato = None
                         
                 if user.tipo == 'glumarko': msg = bot.send_sticker(ne_id, user.teksto)
                 if user.tipo == 'movbildo': msg = bot.send_animation(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato)
                 if user.tipo == 'voice': msg = bot.send_voice(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato)
                 if user.tipo == 'document': msg = bot.send_document(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato)
                 if user.tipo == 'video': msg = bot.send_video(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato)
                 if user.tipo == 'video_note': msg = bot.send_video_note(ne_id, user.teksto)
                 if user.tipo == 'audio': msg = bot.send_audio(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato)
                 if user.tipo == 'bildo': msg = bot.send_photo(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato) 
                 if user.tipo == 'poll' : 
                     if user.teksto.correct_option_id != None: enketa_tipo = 'quiz'
                     else: enketa_tipo = None
                     msg = bot.send_poll(ne_id, user.teksto.question, user.teksto.options, type = enketa_tipo, correct_option_id = user.teksto.correct_option_id, allows_multiple_answers=user.teksto.allows_multiple_answers, is_anonymous = user.teksto.is_anonymous, explanation = user.teksto.explanation)
                 idilo = msg.id
                 
                 if user.tipo != "poll":
                     if responda_ligilo(user.teksto) != None: 
                         respondilo, teksto_sen_ligilo = responda_ligilo(user.teksto)
                         if teksto_sen_ligilo[-1] == " ": teksto_sen_ligilo = teksto_sen_ligilo[:-1]
                         elif teksto_sen_ligilo[0] == " ": teksto_sen_ligilo = teksto_sen_ligilo[1:]
                     else:
                         respondilo = ""
                         teksto_sen_ligilo = user.teksto
                     cursor.execute("""INSERT INTO historio VALUES (?, ?, ?, ?, ?, ?, ?)""", (str(message.from_user.id), str(teksto_sen_ligilo), str(user.unikilo), str(user.tipo), str(int(time.time())), str(respondilo), str(idilo)))
                 else:
                     respondilo = None
                     #if user.teksto.correct_option_id != None: enketa_tipo = 'quiz'
                     kiaj_opcioj = user.teksto.options
                     kiaj_opcioj = ''.join(str(x) for x in kiaj_opcioj)
                     #uzanta_id = uzanta_id.translate({ ord(c): None for c in "(),'" })
                     enketa_teksto = str(user.teksto.question) + kodilo + str(kiaj_opcioj)
                     cursor.execute("""INSERT INTO historio VALUES (?, ?, ?, ?, ?, ?, ?)""", (str(message.from_user.id), str(enketa_teksto), str(user.unikilo), str(user.tipo), str(int(time.time())), str(respondilo), str(idilo)))
                 mesagharo.commit()
                 
                 for tempo in cursor.execute("SELECT dato FROM historio").fetchall():
                     tempo = ''.join(str(x) for x in tempo)
                     if int(tempo) + 3600 < int(time.time()):
                         cursor.execute("DELETE FROM historio WHERE dato = '" + tempo + "'")
                 mesagharo.commit()
                 
                 bot.send_message(message.chat.id, frazoj[random.randint(0,len(frazoj)-1)])


# =============================================================================
#         except Exception as e:
#               time.sleep(0.3)
#               bot.send_message(message.chat.id, "Eraro okazis. Provu denove")
# =============================================================================



bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()  
               
bot.polling()
