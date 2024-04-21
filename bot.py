import telebot
import random


Token = '6792059260:AAFaoYMoybrMEY9a38sL2DKtQyUoyK6eHAQ'
bot = telebot.TeleBot(Token)




            
a = 'првиеь'

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == "hi":
        bot.send_message(message.from_user.id, a)

        

bot.polling(none_stop=True, interval=0, timeout=120)
