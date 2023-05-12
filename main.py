import telebot

bot=telebot.TeleBot("6072034229:AAE2PES80kdX5QNOzEdWzAPjUQW2v526Q6c")

@bot.message_handler(commands=["start"])
def start(message):
    text=f"hello, <b>{message.from_user.first_name}</b> <u>{message.from_user.first_name}</u>"
    bot.send_message(message.chat.id, text,parse_mode='html')

@bot.message_handler()

def get_user_text(message):
    if message.text=="hello":
        hello_text=f"hi there {message.from_user.first_name}"
        bot.send_message(message.chat.id,hello_text,parse_mode="html")
    elif message.text=="id":

        id_text=f"your id is: {message.from_user.id}"
        
        bot.send_message(message.chat.id,id_text,parse_mode="html")
    

bot.polling(none_stop=True)