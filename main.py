# COMMANDS go FIRSTLY

import telebot
from telebot import types

# token from telegram
bot=telebot.TeleBot("6072034229:AAE2PES80kdX5QNOzEdWzAPjUQW2v526Q6c")

# catch command "/start"
@bot.message_handler(commands=["start"])

def start(message):

    # f means format string
    text=f"hello, <b>{message.from_user.first_name}</b> <u>{message.from_user.first_name}</u>"
    bot.send_message(message.chat.id, text,parse_mode='html')



@bot.message_handler(commands=["website"])

def website(message):

    # button in answer message
    markup=types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("visit the website", url= "https://www.cyberforum.ru/python/thread2007924.html?ysclid=lhlp73h4pa582816413"))
    bot.send_message(message.chat.id,"go on the website", reply_markup=markup)



@bot.message_handler(commands=["help"])

def website_in_field(message):

    # button in message field with adaptive on the screen, 1 button 1 string
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    website=types.KeyboardButton("web site")
    start=types.KeyboardButton("start")
    markup.add(website,start)
    bot.send_message(message.chat.id,"go on the website", reply_markup=markup)



# this block takes ALL TEXT MESSAGES
@bot.message_handler()

def get_user_text(message):

    # {} there write py code
    if message.text=="hello":
        hello_text=f"hi there {message.from_user.first_name}"
        bot.send_message(message.chat.id,hello_text,parse_mode="html")


    elif message.text=="id":
        id_text=f"your id is: {message.from_user.id}"
        bot.send_message(message.chat.id,id_text,parse_mode="html")

        # send photo 
    if message.text=="photo":
        photo=open("wget1.png","rb")
        bot.send_photo(message.chat.id,photo)


# if you give photo , you have looks nice
@bot.message_handler(content_types=["photo"])

def get_user_photo(message):
    bot.send_message(message.chat.id, "looks nice")



# to work always

bot.polling(none_stop=True)