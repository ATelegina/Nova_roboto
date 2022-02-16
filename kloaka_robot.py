import telebot 
TOKEN = '5242116953:AAEoEIDLyAS9YCQl7zA3mjOi-zKfRZ05Xz4'
bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")
ne_id = -1001463711396 
malbono = -1001638499087
message = None

@bot.message_handler(content_types = ['text', 'photo', 'video', 'animation'])
def resendo(message):
    if message.chat.type == "private":
        if bot.get_chat_member(ne_id, message.from_user.id).status == 'left':   
             bot.send_message(message.chat.id, "Vi ne estas vera kloakano. Aliĝu: @Esperantujoo")
        else:
            print("sal1")
            if message.content_type == 'photo':
                bot.send_message(ne_id, "Sendita de {} ({})".format(message.from_user.first_name, message.from_user.id))
                bot.forward_message(ne_id, message.chat.id, message.id)
            elif message.text:
                if message.text != "/start":
                    bot.send_message(ne_id, "Sendita de {} ({})".format(message.from_user.first_name, message.from_user.id))
                    bot.forward_message(ne_id, message.chat.id, message.id)
            elif message.video:
                bot.send_message(malbono, "Sendita de {} ({})".format(message.from_user.first_name, message.from_user.id))
                peko = bot.forward_message(malbono, message.chat.id, message.id)
                bot.send_message(ne_id, "Sendita de {} ({})".format(message.from_user.first_name, message.from_user.id))
                bot.send_message(ne_id, """Aĉaĵo (filmeto): https://t.me/c/1638499087/{}
Invitligilo al aĉaĵejo: https://t.me/+AVo37AXCVVI5ZDdi""".format(peko.id))
            elif message.animation:
                bot.send_message(malbono, "Sendita de {} ({})".format(message.from_user.first_name, message.from_user.id))
                peko = bot.forward_message(malbono, message.chat.id, message.id)
                bot.send_message(ne_id, "Sendita de {} ({})".format(message.from_user.first_name, message.from_user.id))
                bot.send_message(ne_id, """Aĉaĵo (movbildo): https://t.me/c/1638499087/{}
Invitligilo al aĉaĵejo: https://t.me/+AVo37AXCVVI5ZDdi""".format(peko.id))
                
bot.polling()