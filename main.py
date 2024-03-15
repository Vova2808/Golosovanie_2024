import telebot
from telebot import types
import os

bot = telebot.TeleBot('6753419308:AAGXkFCZkNi4ex0lhVtbu2CN1lhKGWcjTdU')

f = open('id.txt', 'r')
id_name = f.read()


@bot.message_handler(commands=['start', 'help'])
def start(message):
    text_start = '''Вы можете проголосовать только один раз'''
    bot.send_photo(message.chat.id, 'https://bfm74.ru/upload/medialibrary/ab3/cvqz70hr0g3us2flvtgf8vlzh77syj4v.jpg')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    nadejd = types.KeyboardButton("Надеждин")
    davan = types.KeyboardButton("Даванков")
    putin = types.KeyboardButton("Путин")
    slud = types.KeyboardButton("Слуцкий")
    harit = types.KeyboardButton("Харитонов")
    markup.add(nadejd, davan, putin, slud, harit)
    bot.send_message(message.chat.id, text_start, reply_markup=markup)


kandidat = ['Надеждин', 0,
            'Даванков', 0,
            'Путин', 0,
            'Слуцкий', 0,
            'Харитонов', 0]


@bot.message_handler(content_types=['text'])
def golos(message):
    if message.from_user.id in id_name:
        bot.send_message(message.chat.id,"Вы уже проголосовали")

    else:
        for i in range(len(kandidat)):
            if message.from_user.id in id_name:
                bot.send_message(message.chat.id, "Вы уже проголосовали")
                break

            if kandidat[i] == message.text:
                kandidat[i + 1] += 1
                bot.send_message(message.chat.id,'Спасибо')
                bot.send_message(message.chat.id,"Вы проголосовали за "+ message.text)
                id_name.append(message.from_user.id)

                open("id.txt", 'w').close()
                print(list(id_name),file=open("id.txt", "a"))

                print(f"Пользователь с ником {message.from_user.username} проголосовал за {message.text}\n",
                      f"{kandidat}",
                      file=open("log.txt", "a"))
                break

            else:
                bot.send_message(message.chat.id,"Кандидата с таким именем не существует")
                break

        print(kandidat)
        print(id_name)


bot.polling(none_stop=True)