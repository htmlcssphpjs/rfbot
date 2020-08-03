import telebot
import random
from models.start import bot
from telebot import types
#сообщения
@bot.message_handler(commands=['send'])
def training(message):
    sendmsg = message.text.replace('/send ', '')
    print(sendmsg)
    bot.send_message(message.chat.id, "Успешно отправленно!")
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '/start':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Заказать доставку")
            item2 = types.KeyboardButton("О нас")
            item3 = types.KeyboardButton("Наш сайт")
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id,"Добро пожаловать, {0.first_name}!\nЯ - {1.first_name}, бот для заказа доставки.".format(message.from_user, bot.get_me()), reply_markup=markup)
            #данные пользователя
            name = message.from_user.first_name
            name1 = message.from_user.last_name
            url = message.from_user.username
            iduser = message.from_user.id
            #/данные пользователя
            print("Имя: " + str(name) + " " + str(name1) + "\nСсылка: @" + str(url) + "\nID: " + str (iduser))
        elif message.text == '/help':
            bot.send_message(message.chat.id, "Всё очень просто, есть три команды:\n\"Заказать доставку\"\n\"О нас\"\n\"Наш сайт\"")
        elif message.text == 'Заказать доставку':
            bot.send_message(message.chat.id, "Напишите далее в таком формате данные, и мы с вами <i>обязательно</i> свяжемся:<b>\n/send и ваше сообщение, обязательно представьтесь и оставьте контакты для связи!</b>", parse_mode='html')
            print("Заказанна доставка!\n@" + message.from_user.username)
        elif message.text == 'О нас':
            bot.send_message(message.chat.id, "<b>RF First</b> - \nПервые в нашей стране по поиску производителей и доставке из <i>Китая</i>🇨🇳, мы готовы предложить Вам самые конкурентоспособные <u>цены</u> и <u>лучшие условия</u>, свяжитесь с нами сейчас и убедитесь в этом сами!", parse_mode='html')
        elif message.text == 'Наш сайт':
            bot.send_message(message.chat.id, "Наш сайт находится в стадии разработки, поэтому используйте пока меня!😉")
        elif message.text == '/me':
            #данные пользователя
            name = message.from_user.first_name
            name1 = message.from_user.last_name
            url = message.from_user.username
            iduser = message.from_user.id
            #/данные пользователя
            bot.send_message(message.chat.id, "Имя: " + str(name) + " " + str(name1) + "\nСсылка: @" + str(url) + "\nID: " + str (iduser))
        else:
            msg = message.text
            bot.send_message(message.chat.id, 'Я не знаю что ответить вам на \"<b>' + str(msg) + "</b>\"🤔, <i>/help</i> для получения помощи", parse_mode='html')