import telebot


Token = '6792059260:AAFaoYMoybrMEY9a38sL2DKtQyUoyK6eHAQ'
bot = telebot.TeleBot(Token)

hi = 'hi friend'

@bot.message_handler(commands=['start'])

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == 'привет': 

        bot.send_message(message.from_user.id, hi)
    
bot.polling(none_stop=True, interval=0, timeout=120)