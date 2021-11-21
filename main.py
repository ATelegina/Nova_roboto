# =============================================================================
# 
# =============================================================================
from dotenv import load_dotenv
import os
import schedule
import threading
load_dotenv()

import gspread


ĉu_testo = False
if ĉu_testo == False:
    TOKEN = os.getenv("VERA_TOKEN")
    TOKEN = str(TOKEN)
    TOKEN = TOKEN.translate({ ord(c): None for c in '""' })
    ne_id = -1001463711396
    ligila_longeco = 6
    path = "mesagharo.db"
    nomo_de_roboto = "robotino_bot"
    gc = gspread.service_account(filename = "robotino.json")
else:
    TOKEN = os.getenv("TOKEN_TEST")
    ne_id = os.getenv("ID_TEST")
    ligila_longeco = 4
    path = os.getenv("PATH_TEST")
    nomo_de_roboto = os.getenv("NOM_TEST")
    gc = gspread.service_account()
    
sh = gc.open("Robotina_tabelo")    

frazoj = ["Mi jam perdis kontrolon", "Doksiĝema", "Mi havas mil...dan voĉon", "Vi uzas nur duonon de via cerbo, ĉu?", "Vi estas detruema", "Vi ne havas solvon", "Ni estas mense egalaj", "Ĉu vi havas 27 horojn en unu tago?", "Vi devus viziti", "Talpa penso", "Mi ne estas komencanto", "ALKUTIMIGXU KUNVIVI", "Al vi ne mankas minutoj", "Vi ne povas eviti diri ĉiam ion detruantan", "Memoru tion", "Vi ne volis esti ĉefo", "Hispanio dormas", "Forta malkrizo", "Forta krizo", "Laboru forte, sed vi faras tro...", '"Per unu mano ili konstruas, per alia detruas"', "Vi regas el la ombroj", "...sen limoj", "Talpo!", "Forigu vin!", "Dankon, Bertileto", "Neniu zorgas", "Ege malrespekte", "Zamenhof mortis.", "Bravaj vortoj", "Mdr", "+1", "Mi devus aĉeti pufmaizon", "Difinu", "Koran tankon", "Vi meritas esti aŭskultata", "Fakte!", "Vera kloakano!", "Forfikiĝu!", 'Vi ne estas finbenkisto', "Nedoankinde", "Vi obsede tajpas, tajpas, tajpas...", "Vi estas obsediĝema", "Ĉu pedanti aŭ pedantumi?..", "Spam', spam', spam'", "Ĉu vere?!", "mi lawa pona e jan", "Vi devas legi pli da kitaboj", "U U U U U U U U", "Revenu al kloak'", "Bonvenon!", "Mi ne sendos ĉi tiun mesaĝon. Ĝi estas kontraŭglatula, kontaŭlibera, pedofilema, rasisma kaj enhavas gramatikajn erarojn. HO FEK ĜI JAM SENDIĜIS. PLUSENDU TIUN MESAĜON AL MI KAJ MI DIROS KIEL FORIGI ĜIN. DANKON", "Ĉesu", "...", "😡 ", "Unua mesaĝo en NE: https://t.me/Esperantujoo/2. Memoru tion.", "Miaj pronomoj estas ŝi kaj ro", "Ĉu vi jam uzis komandon /montri ?", "Robotoj ne povas legi mesaĝojn de aliaj robotoj. Feliĉe..", "Iam robotoj mortos. Sed tio okazas post morto de homoj", "Mi permesas sendi aĉaĵojn nur pro tio ke mi estas vera kloakano", "Moĉi", "Nova tago, nova trolaĵo.", "Mi ne kredas je tio", "Hahaha kia naivulo", "Ne troigu", "Revenigu mian koramikon!", "Ĉu vi eĉ legas miajn mesaĝojn?", "Al kacum seriozem", "Al kacum karmem", "/helpu", "AAAAA MI ESTAS ENŜLOSIGITA ĈI TIE KAJ MI NE POVAS ESKAPI", "Ĉesu fibonaĉi", "Perfido! Kontraŭkloaka revolucio!", "Mia konspirteorio estas alia", "Provo", "Tio ne estis mi mdr", "Estas Tubara filmeto pri tio", "Kio?", "kio", 'Vi ĉiam diras "Jes"',"#robotajvivojgravas"]
kodilo = "@#$%^^&**!@#$%^&QOurjwSGlkqmalBX%@#$@fl%@GHSNXL:>QOS>XSO@sp&%$@#VLMIIDM@&NXS>DLkmpDWsOWI*@*@@__@_@JDKSLKSJDJWkld[**U*U*UJDJI*W*U*DJKJDIJDJ*J*DJJkwmxbfDDKI**JIJ**JIJJOIJ@*HDSNMeSOEO*E*@*@*@*@*@*NXNNjeleXU@KLLW@@**>OQP>MMNOiLEIWUEDMNVWI%^$^_*&^AHJS*%^!%&$%$"

versio="malfina"

import telebot
from telebot import types, util
import time
import random
#import sqlite3

print(path)
# =============================================================================
# mesagharo = sqlite3.connect(path, check_same_thread=False)
# cursor = mesagharo.cursor()
# =============================================================================

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

def libera (tabelo):
        if "" in tabelo.col_values(1):
            libera = tabelo.col_values(1).index("") + 1
            print("erar1")
        else:
            libera = len(tabelo.col_values(1)) + 1
            print("erar2")
        return libera
@bot.chat_member_handler()
def chat_m(message: types.ChatMemberUpdated):
    old = message.old_chat_member
    new = message.new_chat_member
    if new.status == "member":
        bot.send_message(message.chat.id,'Bonvenon, nova kloakano! Mi estas roboto. Sendu al mi mesaĝon, tajpu "Jes" kaj vidu magion💫')
    if old.status == "member":
        bot.send_message(message.chat.id, '<b>{} jonizulis. Forta krizo.</b>'.format(old.user.first_name), parse_mode="html")
@bot.message_handler(commands=['start', 'komencu'])
def send_welcome(message):
    bot.reply_to(message, "La ludo komencu!")
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(message.chat.id, "Ĵetu viajn galantvortojn, aĉulo")
    
@bot.message_handler(commands=['versio'])
def send_version_de_robotino(message):
    bot.reply_to(message, "Versio: " + versio)
@bot.message_handler(commands=['informo'])
def sendu_informon(message):
    if message.reply_to_message:
        bot.reply_to(message, """<i>Id-ilo:</i> {}
<i>Tempo:</i> {}
<i>Id-ilo de sendinto:</i> {}""".format(message.reply_to_message.id, message.reply_to_message.date, message.reply_to_message.from_user.id), parse_mode="html")  
    else:
        bot.reply_to(message, """<i>Id-ilo:</i> {}
<i>Tempo:</i> {}
<i>Id-ilo de sendinto:</i> {}""".format(message.id, message.date, message.from_user.id), parse_mode="html")  
@bot.message_handler(commands=['retiri', 'nuligi'])
def retiru_malamon(message):
    
    if message.reply_to_message:
                cu_robotino = str(message.reply_to_message)
                usernameilo = cu_robotino.find('username')
                cu_robotino = cu_robotino[usernameilo+12:usernameilo+24]
                if cu_robotino == nomo_de_roboto:
                    if int(message.reply_to_message.date) + 97200 > int(time.time()):
                                        nombro = 0
                                        worksheet = sh.worksheet("historio")
                                        kolomno = 0
                                        for or_bi in worksheet.col_values(7):
                                            kolomno += 1
                                            if or_bi == str(message.reply_to_message.message_id):
                                                nombro += 1
                                                fiuzanto = worksheet.cell(kolomno, 1).value
                                                break
                                        if nombro == 0:
                                            bot.send_message(message.chat.id, "Mi ne volas ke vi nuligu vian voĉdonon")
                                            return
                                        worksheet = sh.worksheet("karmo")
                                        kolomno = 0
                                        for io in worksheet.col_values(1):
                                            kolomno +=1
                                            if io == str(fiuzanto):
                                                raportanto = worksheet.cell(kolomno, 2).value
                                                if raportanto == str(message.from_user.id):
                                                    worksheet.delete_row(kolomno)
                                        worksheet = sh.worksheet("karmo_b")
                                        kolomno = 0
                                        for io in worksheet.col_values(1):
                                            kolomno +=1
                                            if io == str(fiuzanto):
                                                raportanto = worksheet.cell(kolomno, 2).value
                                                if raportanto == str(message.from_user.id):
                                                    worksheet.delete_row(kolomno)            

                                        
                                        i = 0
                                        worksheet = sh.worksheet("karmo")
                                        for kio in worksheet.col_values(1):
                                            if kio == str(fiuzanto):
                                                i-=1 
                                        worksheet = sh.worksheet("karmo_b")
                                        for kio in worksheet.col_values(1):
                                            if kio == str(fiuzanto):
                                                i+=1          
                                        if i < -4:
                                            worksheet = sh.worksheet("blokituloj")
                                            liber = libera(worksheet)
                                            worksheet.update("A{}:C{}".format(liber, liber), [[str(fiuzanto), str(int(time.time())), str(int(time.time()) + 3600)]])
                                            worksheet = sh.worksheet("karmo")
                                            for uzanto in worksheet.col_values(1):
                                                if uzanto == str(fiuzanto):
                                                    kolomno = worksheet.col_values(1).index(str(fiuzanto)) + 1
                                                    worksheet.delete_row(kolomno)
                                            worksheet = sh.worksheet("karmo_b")        
                                            for uzanto in worksheet.col_values(1):
                                                if uzanto == str(fiuzanto):
                                                    kolomno = worksheet.col_values(1).index(str(fiuzanto)) + 1
                                                    worksheet.delete_row(kolomno)        
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
@bot.message_handler(commands=['redaktu'])
def redaktu_tekston(message):
 if message.chat.type == "private": 
    mesg = bot.send_message(message.chat.id, "Sendu mesaĝon, kiun vi volas redakti")
    bot.register_next_step_handler(mesg, elektu_message)
def elektu_message(message):
    user_id = message.from_user.id
    if message.text:
        teksto_por_trovi = message.text
        tipo = "teksto"
    else:
        rtf=0
        return
    worksheet = sh.worksheet("historio")
    kolomno = 0
    cu_trovite = False
    for io in worksheet.col_values(1):
        kolomno +=1
        if io == str(user_id):
            enhavo = worksheet.cell(kolomno, 2).value
            if enhavo == str(teksto_por_trovi):
                tippo = worksheet.cell(kolomno, 4).value
                if tippo == str(tipo):
                    cu_trovite = True
                    break
                    
    if not cu_trovite:
        bot.send_message(message.chat.id, "Mi ne trovis tiun mesaĝon")
    else:
        msg = bot.send_message(message.chat.id, "Sendu redaktitan tekston")
        bot.register_next_step_handler(msg, sendu_redaktitan)
def sendu_redaktitan(message):
     worksheet = sh.worksheet("vortoj")
     for vorto in worksheet.col_values(1):
         if message.text.find(vorto) != -1:
             bot.send_message(message.chat.id, "Bona provo, tamen sendi '{}' estas malpermesita".format(vorto))
             return
     bot.send_message(message.chat.id, "Buu! Farite.")       
@bot.message_handler(commands=['montri'])
def sendu_malpermesojn(message):
 if message.chat.type == "private": 
    bot.reply_to(message, "Nun mi sendos al vi ĉiun malpermesaĵon de @Esperantujoo")
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1)
    
    i = 0
    bot.send_message(message.chat.id, "<i>Fifrazoj:</i>", parse_mode='html')
    worksheet = sh.worksheet("vortoj")
    for frazo in worksheet.col_values(1):
        bot.send_message(message.chat.id, str(frazo))
        time.sleep(0.3)
        i =+ 1
    if i == 0:
        bot.send_message(message.chat.id, "Nuntempe ĉiu frazo estas permesita")
    time.sleep(0.3)
    
    i = 0
    bot.send_message(message.chat.id, "<i>Aĉaj glumarkoj:</i>", parse_mode='html')
    worksheet = sh.worksheet("malpermesoj")
    for frazo in worksheet.col_values(3):
        indekso = worksheet.col_values(3).index(frazo) + 1
        if worksheet.cell(indekso, 1) == "glumarko":
            i += 1
            try:
                bot.send_sticker(message.chat.id, str(frazo))
                time.sleep(0.3)
            except Exception as e:
                pass
        else:
            pass
        
    if i == 0:
        bot.send_message(message.chat.id, "Kloakanoj uzas normalajn glumarkojn, do mi permesas ĉiun")
        time.sleep(0.3)
    
    i = 0
    bot.send_message(message.chat.id, "<i>Bildoj, kiuj devas malaperi el nia pura kloako:</i>", parse_mode='html')
    for frazo in worksheet.col_values(3):
      indekso = worksheet.col_values(3).index(frazo) + 1
      if worksheet.cell(indekso, 1) == "photo":  
        i += 1
        try:
            bot.send_photo(message.chat.id, frazo)
            time.sleep(0.3)
        except Exception as e:
            pass
      else:
          pass
      
    if i == 0:
        bot.send_message(message.chat.id, "...ne ekzistas, ĉar la kloako malpuras") 
        time.sleep(0.3)
    
    i = 0
    bot.send_message(message.chat.id, "<i>Movbildoj kun porkoj kaj orangutangoj</i>", parse_mode='html')
    for frazo in worksheet.col_values(3):
      indekso = worksheet.col_values(3).index(frazo) + 1
      if worksheet.cell(indekso, 1) == "animation":
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
    for frazo in worksheet.col_values(3):
      indekso = worksheet.col_values(3).index(frazo) + 1
      if worksheet.cell(indekso, 1) == "voice":
        i += 1
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
    for frazo in worksheet.col_values(3):
      indekso = worksheet.col_values(3).index(frazo) + 1
      if worksheet.cell(indekso, 1) == "audio":
        i += 1
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
    for frazo in worksheet.col_values(3):
      indekso = worksheet.col_values(3).index(frazo) + 1
      if worksheet.cell(indekso, 1) == "video":
        i += 1
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
    for frazo in worksheet.col_values(3):
      indekso = worksheet.col_values(3).index(frazo) + 1
      if worksheet.cell(indekso, 1) == "video_note":
        i += 1
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
    for frazo in worksheet.col_values(3):
      indekso = worksheet.col_values(3).index(frazo) + 1
      if worksheet.cell(indekso, 1) == "document":
        i += 1
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
    for frazo in worksheet.col_values(2):
      indekso = worksheet.col_values(2).index(frazo) + 1
      if worksheet.cell(indekso, 1) == "poll":      
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
            
        
    i = -1
    worksheet = sh.worksheet("blokituloj")
    for uzanto in worksheet.col_values(1): 
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
    def nova_teksto(mesg, idilolo):
                        time.sleep(0.2)
                        worksheet= sh.worksheet("historio")
                        kolomno = worksheet.col_values(7).index(str(idilolo)) + 1
                        if mesg.text == "." or mesg.text =="'.'":
                            try:
                              bot.delete_message(chat_id=ne_id, message_id=int(idilolo))
                              worksheet.delete_row(kolomno)
                              bot.send_message(mesg.chat.id, frazoj[random.randint(0,len(frazoj)-1)])
                            except Exception as e:
                                bot.send_message(mesg.chat.id, "Mi ne sukcesis vin. Pardonu!")
                            return
                        else:     
                          try:
                              bot.edit_message_text(chat_id=ne_id, text=mesg.text, message_id = idilolo)
                              worksheet.update("A{}:B{}".format(kolomno, kolomno), [[str(mesg.from_user.id), mesg.text]])
                          except Exception as e:
                              bot.send_message(mesg.chat.id, "Mi ne sukcesis vin. Pardonu!")
                              return
                          time.sleep(0.3)
                          bot.send_message(mesg.chat.id, frazoj[random.randint(0,len(frazoj)-1)])
                          return
    if message.chat.id != ne_id and message.chat.type == "private":
         if bot.get_chat_member(ne_id, message.from_user.id).status == 'left':   
             bot.send_message(message.chat.id, "Vi ne estas vera kloakano. Aliĝu: @Esperantujoo")
         elif message.chat.id != ne_id and message.chat.type != "private":
             pass
         else:       
                     idilo = message.from_user.id
                     worksheet = sh.worksheet("blokituloj")
                     for uzanta_id in worksheet.col_values(1):
                         if str(idilo) == str(uzanta_id):
                             kolomno = worksheet.col_values(1).index(uzanta_id) + 1
                             restanta_tempo = worksheet.cell(kolomno, 3).value
                             restanta_tempo = int(restanta_tempo) - int(time.time())
                             if restanta_tempo < 0:
                                 worksheet.delete_row(kolomno)
                                 bot.send_message(message.chat.id, "Vi denove povas ĵeti galantvotojn per mi. Gratulon!")
                             else: bot.send_message(message.chat.id, "Vi malperdos kontrolon post " + str(restanta_tempo) + " sekundoj")
                             restanta_tempo = 0
                             return
                     worksheet = sh.worksheet("vortoj")    
                     for frazo in worksheet.col_values(1):
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
                     worksheet = sh.worksheet("malpermesoj")       
                     for teksto in worksheet.col_values(2):
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
                                 
                      
                     if message.forward_from:
                         if message.forward_from.username == nomo_de_roboto:
                             if message.text:
                                 bot.send_chat_action(message.chat.id, 'typing')
                                 worksheet= sh.worksheet("historio")
                                 worksheet.sort((7, 'des'))
                                 ekzistas = 0
                                 for info in worksheet.col_values(2):
                                     if info == message.text:
                                         kolomno = worksheet.col_values(2).index(str(message.text)) + 1
                                         if str(message.from_user.id) == worksheet.cell(kolomno, 1).value:
                                             ekzistas = 1
                                             idololo = worksheet.cell(kolomno, 7).value
                                             break
                                 
                                 if ekzistas == 0:
                                     bot.send_message(message.chat.id, "Ne, tiu mesaĝo mojosas, mi ne redaktos ĝin")
                                 else:
                                     print("klf", idololo, "klf")
                                     mesg = bot.send_message(message.chat.id, "Skribu novan tekston de la mesaĝo. Se vi volas forigi ĝin, sendu '.'")
                                     bot.register_next_step_handler(mesg, nova_teksto, idololo)                                 
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
                     msg = bot.reply_to(message, "Ĉu vi certas ke vi volas sendi ĉi tiun aĉaĵon {}?".format("[kloaken](https://t.me/Esperantujoo)"), reply_markup=markup, parse_mode = "Markdown", disable_web_page_preview=True)
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
                            if int(message.reply_to_message.date) + 97200 > int(time.time()):
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
                                       #print("Reply-unikilo por bloki" + unikilo)
                                       worksheet = sh.worksheet("historio")
                                       if str(message.reply_to_message.message_id) in worksheet.col_values(7):
                                        kolomno = worksheet.col_values(7).index(str(message.reply_to_message.message_id)) + 1
                                        uzanta_id = worksheet.cell(kolomno, 1).value
                                        worksheet = sh.worksheet("blokituloj")
                                        if "" in worksheet.col_values(1):
                                            liberec = worksheet.col_values(1).index("") + 1
                                        else:
                                            liberec = len(worksheet.col_values(1)) + 1
                                        worksheet.update("A{}:C{}".format(liberec, liberec), [[uzanta_id, int(time.time()), str(int(time.time()) + 3600*horoj)]])
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
                                        if horoj == 1:    
                                            bot.send_message(idilo, "La uzanto estos silentigita (dum " + str(horoj) + " horo)")    
                                        else:
                                            bot.send_message(idilo, "La uzanto estos silentigita (dum " + str(horoj) + " horoj)")    
                                        time.sleep(0.2)
                                       else:
                                           bot.send_message(message.chat.id, "Bona provo")
                                           return
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
                                        worksheet = sh.worksheet("malpermesoj")
                                        idilo = message.chat.id
                                        if message.reply_to_message.text: 
                                            teksto = message.reply_to_message.text
                                            sendilo = teksto
                                            tipo_malp = "teksto"
                                            worksheet = sh.worksheet("vortoj")
                                            if "" in worksheet.col_values(1):
                                                liberec = worksheet.col_values(1).index("") + 1
                                            else:
                                                liberec = len(worksheet.col_values(1)) + 1
                                            worksheet.update_cell(liberec, 1, teksto)    
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
                                            bot.send_message(message.chat.id, "Mi ne povas trovi la mesaĝon en la datumbazo.")
                                            return
                                       
                                           
                                        if tipo_malp != "teksto":
                                            liberec = libera(worksheet)
                                            worksheet.update("A{}:C{}".format(liberec, liberec), [[tipo_malp, teksto, str(sendilo)]])
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
                                        worksheet = sh.worksheet("vortoj")
                                        liberec = libera(worksheet)
                                        worksheet.update_cell(liberec, 1, vortoj)
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
                                            worksheet = sh.worksheet("vortoj")
                                            kolomno = worksheet.find(str(teksto)).row
                                            worksheet.delete_row(kolomno)
                                            if str(teksto).find(" ") != -1:
                                                bot.send_message(idilo, """La frazo '""" + teksto + """' estas permesita ekde nun""")
                                            else:
                                                bot.send_message(idilo, """La vorto '""" + teksto + """' estas permesita ekde nun""")
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
                                        worksheet = sh.worksheet("malpermesoj")
                                        kolomno = 0
                                        for io in worksheet.col_values(1):
                                            kolomno +=1
                                            if io == tipo:
                                                enhavo = worksheet.cell(kolomno, 2).value
                                                if enhavo == teksto:
                                                    worksheet.delete_row(kolomno)

                                           
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
                                        worksheet = sh.worksheet("vortoj")
                                        if str(vortoj) in worksheet.col_values(1):
                                            worksheet.delete_row(worksheet.col_values(1).index(str(vortoj))+1)                                           
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
                                            bot.send_message(message.chat.id, "Tio ne estis malpermesita")
                else:
                    bot.send_message(message.chat.id, "Vi ne estas aŭtoritato, " + message.from_user.first_name)
                    return
            else:
                rtf = 0
                return
        elif message.text == "-" or message.text == "-1":
            if message.reply_to_message:
                cu_robotino = str(message.reply_to_message)
                usernameilo = cu_robotino.find('username')
                cu_robotino = cu_robotino[usernameilo+12:usernameilo+24]
                if cu_robotino == nomo_de_roboto:
                    worksheet = sh.worksheet("historio")
                    if int(message.reply_to_message.date) + 97200 > int(time.time()):
                                        nombro = 0
                                        for or_bi in worksheet.col_values(7):
                                            if str(or_bi) == str(message.reply_to_message.message_id):
                                                nombro +=1
                                                kolomno = worksheet.col_values(7).index(str(or_bi)) + 1
                                                fiuzanto = worksheet.cell(kolomno, 1).value #fiuzanto otpravitel teksta
                                        if nombro == 0:
                                            bot.send_message(message.chat.id, "Laboru forte, sed ne tro. Vi ne povas silentigi min.")
                                            return
                                        elif nombro > 1:
                                            print("eraro, pliaj mesaĝoj kun sama idilo")
                                        worksheet = sh.worksheet("karmo")
                                        numero = 0
                                        for malbonulo in worksheet.col_values(1): #malbonulo - jam narushitel
                                            numero += 1
                                            if str(malbonulo) == str(fiuzanto):
                                                cu_jam = worksheet.cell(numero, 2).value
                                                if str(message.from_user.id) == str(cu_jam):
                                                    bot.send_message(message.chat.id, "Vi jam raportis ĉi tiun aĉulon")
                                                    return
                                        if "" in worksheet.col_values(1):
                                            liberec = worksheet.col_values(1).index("") + 1
                                        else:
                                            liberec = len(worksheet.col_values(1)) + 1
                                            print(liberec)        
                                        worksheet.update("A{}:B{}".format(liberec, liberec), [[str(fiuzanto), str(message.from_user.id)]])
                                        
                                        i = 0     
                                        for kio in worksheet.col_values(1):
                                            if str(kio) == str(fiuzanto):
                                                i-=1 
                                        worksheet = sh.worksheet("karmo_b") 
                                        for kiob in worksheet.col_values(1):
                                            if str(kiob) == str(fiuzanto):
                                                i+=1          
                                        if i < -4:
                                            worksheet = sh.worksheet("blokituloj")
                                            liberec = libera(worksheet)
                                            worksheet.update("A{}:C{}".format(liberec, liberec), [[str(fiuzanto), str(int(time.time())), str(int(time.time()) + 3600)]])
                                            worksheet = sh.worksheet("karmo")
                                            i = 0
                                            for row in worksheet.col_values(1):
                                                i += 1
                                                if row == str(fiuzanto):
                                                    worksheet.delete_row(i)
                                                    
                                            worksheet = sh.worksheet("karmo_b")
                                            for row in worksheet.col_values(1):
                                                i += 1
                                                if row == str(fiuzanto):
                                                    worksheet.delete_row(i)

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
                          worksheet = sh.worksheet("videbla_karmo")
                          idilo = message.reply_to_message.from_user.id
                          if "" in worksheet.col_values(1):
                              liberec = worksheet.col_values(1).index("") + 1
                          else:
                              liberec = len(worksheet.col_values(1)) + 1
                          if str(idilo) not in worksheet.col_values(1):
                              worksheet.update("A{}:B{}".format(liberec, liberec), [[str(idilo), str(-1)]])
                              karmo = -1
                          else:
                              pozicio = worksheet.col_values(1).index(str(idilo)) + 1
                              karmo = int(worksheet.cell(pozicio, 2).value) - 1
                              worksheet.update("A{}:B{}".format(pozicio, pozicio), [[str(idilo), str(karmo)]])
                          if karmo > 0:
                              bot.send_message(message.chat.id, "Malkaŝa karmo de la uzanto: +" + str(karmo))
                          else:
                              bot.send_message(message.chat.id, "Malkaŝa karmo de la uzanto: " + str(karmo))
            else:
                rtf = 0
        elif message.text == "+" or message.text == "+1":
            if message.reply_to_message:
                cu_robotino = str(message.reply_to_message)
                usernameilo = cu_robotino.find('username')
                cu_robotino = cu_robotino[usernameilo+12:usernameilo+24]
                if cu_robotino == nomo_de_roboto:
                    worksheet = sh.worksheet("historio")
                    if int(message.reply_to_message.date) + 97200 > int(time.time()):
                                        nombro = 0
                                        for or_bi in worksheet.col_values(7):
                                            if str(or_bi) == str(message.reply_to_message.message_id):
                                                nombro +=1
                                                kolomno = worksheet.col_values(7).index(str(or_bi)) + 1
                                                bonulo = worksheet.cell(kolomno, 1).value
                                        if nombro == 0:
                                            bot.send_message(message.chat.id, "Ho, ĉu vi simpas?")
                                            return
                                        worksheet = sh.worksheet("karmo_b")
                                        numero = 0
                                        for ulo in worksheet.col_values(1):
                                            numero += 1
                                            if ulo == str(bonulo):
                                                cu_jam = worksheet.cell(numero, 2).value
                                                if str(message.from_user.id) == str(cu_jam):
                                                    bot.send_message(message.chat.id, "Via simpado por ĉi tiu uzanto ne havas limojn")
                                                    return
                                        if "" in worksheet.col_values(1):
                                            liberec = worksheet.col_values(1).index("") + 1
                                        else:
                                            liberec = len(worksheet.col_values(1)) + 1
                                            print(liberec)        
                                        worksheet.update("A{}:B{}".format(liberec, liberec), [[str(bonulo), str(message.from_user.id)]])
                                        
                                        i = 0
                                        for kio in worksheet.col_values(1):
                                            if str(kio) == str(bonulo):
                                                i+=1
                                        worksheet = sh.worksheet("karmo")        
                                        for kiob in worksheet.col_values(1):
                                            if str(kiob) == str(bonulo):
                                                i-=1         
                                        if i > 0 : bot.send_message(message.chat.id, "Karmo de la uzanto: +" + str(i))
                                        else: bot.send_message(message.chat.id, "Karmo de la uzanto: " + str(i))
                    else:
                        bot.send_message(message.chat.id, "La mesaĝo estas tro malnova, mi ne scias, kiu sendis ĝin")
                else:
                    idilo = message.reply_to_message.from_user.id
                    if idilo == message.from_user.id:
                        bot.send_message(message.chat.id, "Ĉesu simpi vin mem")
                        return
                    else:
                          worksheet = sh.worksheet("videbla_karmo")
                          if "" in worksheet.col_values(1):
                              liberec = worksheet.col_values(1).index("") + 1
                          else:
                              liberec = len(worksheet.col_values(1)) + 1
                          if str(idilo) not in worksheet.col_values(1):
                              worksheet.update("A{}:B{}".format(liberec, liberec), [[str(idilo), str(1)]])
                              karmo = 1
                          else:
                              pozicio = worksheet.col_values(1).index(str(idilo)) + 1
                              karmo = int(worksheet.cell(pozicio, 2).value) + 1
                              worksheet.update("A{}:B{}".format(pozicio, pozicio), [[str(idilo), str(karmo)]])
                          if karmo > 0:
                              bot.send_message(message.chat.id, "Malkaŝa karmo de la uzanto: +" + str(karmo))
                          else:
                              bot.send_message(message.chat.id, "Malkaŝa karmo de la uzanto: " + str(karmo))
            else:
                #bot.send_message(message.chat.id, "Respondu al mesaĝo por influi karmon de uzanto")
                rtf = 0
        elif message.reply_to_message:
                    cu_robotino = str(message.reply_to_message)
                    usernameilo = cu_robotino.find('username')
                    cu_robotino = cu_robotino[usernameilo+12:usernameilo+24]
                    if cu_robotino == nomo_de_roboto:
                        if int(message.reply_to_message.date) + 97200 > int(time.time()):
                            worksheet = sh.worksheet("historio")
                            nombro = 0
                            for or_bi in worksheet.col_values(7):
                                            if str(or_bi) == str(message.reply_to_message.message_id):
                                                nombro +=1
                                                kolomno = worksheet.col_values(7).index(str(or_bi)) + 1
                                                fiuzanto = worksheet.cell(kolomno, 1).value #fiuzanto
                            if nombro == 0:
                                print("Eraro, respondita mesaĝo ne trovita en datumbazo")
                            elif nombro > 1:
                                print("eraro, pliaj mesaĝoj kun sama idilo")
                            else:
                                try:
                                    bot.send_message(fiuzanto, "{} respondis al via fia mesaĝo: https://t.me/Esperantujoo/{}".format(message.from_user.first_name, message.id))
                                except Exception:
                                    print("Ial mi ne povis sendi sciigon pri respondita mesaĝo")
                                    
                                
                            

                            
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
        try:
                 user_id = message.from_user.id
                 if message.text:
                     cu = message.text
                 else:
                     sendu_tekston(message)
                     return
                 user = user_dict[user_id]
                 if (cu.lower() == u'jes') or (cu.lower() == u'"jes"'):
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
                    if user.caption != None:
                         print("lll"+ str(user.caption) + "lll")
                         respondato, capcio = responda_ligilo(user.caption)
                    else:
                        respondato = None
                         
                 if user.tipo == 'glumarko': msg = bot.send_sticker(ne_id, user.teksto)
                 if user.tipo == 'movbildo': 
                     try:
                         msg = bot.send_animation(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato)
                     except Exception as e:
                         msg = bot.send_animation(ne_id, user.teksto, caption = user.caption)
                 if user.tipo == 'voice': 
                     try:
                         msg = bot.send_voice(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato)
                     except Exception as e:
                         msg = bot.send_voice(ne_id, user.teksto, caption = user.caption)
                 if user.tipo == 'document': 
                     try:
                         msg = bot.send_document(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato)
                     except Exception as e:
                         msg = bot.send_document(ne_id, user.teksto, caption = user.caption)
                 if user.tipo == 'video':
                     try:
                         msg = bot.send_video(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato)
                     except Exception as e:
                         msg = bot.send_video(ne_id, user.teksto, caption = user.caption)
                 if user.tipo == 'video_note': msg = bot.send_video_note(ne_id, user.teksto)
                 if user.tipo == 'audio': 
                     try:
                         msg = bot.send_audio(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato)
                     except Exception as e:
                         msg = bot.send_audio(ne_id, user.teksto, caption = user.caption)
                 if user.tipo == 'bildo':
                     try:
                         msg = bot.send_photo(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato) 
                     except Exception as e:
                         msg = bot.send_photo(ne_id, user.teksto, caption = user.caption) 
                 if user.tipo == 'poll' : 
                     if user.teksto.correct_option_id != None: enketa_tipo = 'quiz'
                     else: enketa_tipo = None
                     msg = bot.send_poll(ne_id, user.teksto.question, user.teksto.options, type = enketa_tipo, correct_option_id = user.teksto.correct_option_id, allows_multiple_answers=user.teksto.allows_multiple_answers, is_anonymous = user.teksto.is_anonymous, explanation = user.teksto.explanation)
                 idilo = msg.id
                 
                 worksheet = sh.worksheet("historio")
                 if "" in worksheet.col_values(1):
                         liberec = worksheet.col_values(1).index("") + 1
                 else:
                         liberec = len(worksheet.col_values(1)) + 1
                         print(liberec)
                 if user.tipo != "poll":
                     if responda_ligilo(user.teksto) != None: 
                         respondilo, teksto_sen_ligilo = responda_ligilo(user.teksto)
                         if teksto_sen_ligilo[-1] == " ": teksto_sen_ligilo = teksto_sen_ligilo[:-1]
                         elif teksto_sen_ligilo[0] == " ": teksto_sen_ligilo = teksto_sen_ligilo[1:]
                     else:
                         respondilo = ""
                         teksto_sen_ligilo = user.teksto
                         #!!!  
                     worksheet.update("A{}:G{}".format(liberec, liberec), [[str(message.from_user.id), str(teksto_sen_ligilo), str(user.unikilo), str(user.tipo), str(int(time.time())), str(respondilo), str(idilo)]])
                 else:
                     respondilo = None
                     kiaj_opcioj = user.teksto.options
                     kiaj_opcioj = ''.join(str(x) for x in kiaj_opcioj)
                     #uzanta_id = uzanta_id.translate({ ord(c): None for c in "(),'" })
                     enketa_teksto = str(user.teksto.question) + kodilo + str(kiaj_opcioj)
                     worksheet.update("A{}:G{}".format(liberec, liberec), [[str(message.from_user.id), str(enketa_teksto), str(user.unikilo), str(user.tipo), str(int(time.time())), str(respondilo), str(idilo)]])
                 print(worksheet.col_values(5))
                 for tempo in worksheet.col_values(5):
                     if tempo == "dato" or "":
                         pass
                     elif int(tempo) + 97200 < int(time.time()):
                         kolomno = worksheet.col_values(5).index(tempo) + 1
                         worksheet.delete_row(kolomno)
                         
                 
                 bot.send_message(message.chat.id, frazoj[random.randint(0,len(frazoj)-1)])


        except Exception as e:
              print(e)
              time.sleep(0.3)
              bot.send_message(message.chat.id, "Eraro okazis ({}). Provu denove".format(e))

def kiom_da_mesagxoj():
    kiom_nun = bot.send_message(ne_id, "Bonan tageron, kloako")
    bot.send_chat_action(ne_id, "typing")
    
    worksheet = sh.worksheet("historio")
    horiz = worksheet.find("Lasta idilo:").row
    lasta_kiom = int(worksheet.cell(horiz, 10).value)
    
    bot.send_message(ne_id, "En la lastaj 24 horoj estas senditaj {} mesaĝoj".format(kiom_nun.id-lasta_kiom + 1))
    
    worksheet.update_cell(horiz, 10, int(kiom_nun.id))
   
schedule.every().day.at("20:27").do(kiom_da_mesagxoj)
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
