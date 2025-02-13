import telebot
import random


Token = '6792059260:AAFaoYMoybrMEY9a38sL2DKtQyUoyK6eHAQ'
bot = telebot.TeleBot(Token)


hangman = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    0   |
        |
        |
       ===''', '''
    +---+
    0   |
    |   |
        |
       ===''', '''
    +---+
    0   |
   /|   |
        |
       ===''', '''
    +---+
    0   |
   /|\  |
        |
       ===''', '''
    +---+
    0   |
   /|\  |
   /    |
       ===''', '''
    +---+
    0   |
   /|\  |
   / \  |
       ===''']

words = 'акула баран бегемот верблюд ворона гепард гиена дельфин дятел ехидна жаба жираф заяц зебра игуана кабан козёл лебедь ленивец медведь мангуст норка носорог олень пингвин попугай собака суслик тюлень утконос фазан хорёк хомяк цапля чайка щегол ягуар ястреб'.split()

def RandomWord(WordList):
    word = random.randint(0, len(WordList) - 1)
    return WordList[word]

def interface(unCorrectLetters, CorrectLetter, Riddle):
    person = hangman[len(unCorrectLetters)]


    UNCletter = str('Неправильные буквы:', end=' ')
    for letter in unCorrectLetters:
        a = str(letter, end=' ')
    

    spaces = '_' * len(Riddle)

    for i in range(len(Riddle)):
        if Riddle[i] in CorrectLetter:
            spaces = spaces[:i] + Riddle[i] + spaces[i+1:]

    for letter in spaces:
        b = str(letter, end=' ')
    
    input_letter = 'Введите букву:'
    def BotMessage():
        bot_message = person
        bot_message += "\n" + UNCletter
        bot_message += "\n" + spaces
        bot_message += "\n" + input_letter
        return bot_message



def Guess(already):
    while True:
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Введите одну букву')
        elif guess in already:
            print('Вы уже называли эту букву, введите другую')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Вводить можно только буквы')
        else:
            return guess
    
print('Игра "Виселица"')
unCorrectLetters = ''
CorrectLetter = ''
Riddle = RandomWord(words)

while True:
    interface(unCorrectLetters, CorrectLetter, Riddle)
    guess = Guess(unCorrectLetters + CorrectLetter)
    if guess in Riddle:
        CorrectLetter = CorrectLetter + guess

        allLetters = True
        for i in range(len(Riddle)):
            if Riddle[i] not in CorrectLetter:
                allLetters = False
                break
        if allLetters:
            print('Вы угадали! Загаданное слово - "' + Riddle + '"!')
            break

    else:
        unCorrectLetters = unCorrectLetters + guess

        if len(unCorrectLetters) == len(hangman) - 1:
            interface(unCorrectLetters, CorrectLetter, Riddle)
            print('Вы исчерпали все попытки! Загаданное слово - "' + Riddle + '"!')
            break
            

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == 'Виселица':
        txt = 'Игра "Виселица" \n' + BotMessage()
        bot.send_message(message.from_user.id, txt)














        '''elif message.text == "/help":
        bot.send_message(message.from_user.id, help)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")'''
        

bot.polling(none_stop=True, interval=0, timeout=120)