# ---------------------------------- Задание 1---------------------------------------
# Используя библиотеку pyTelegramBotAPI напишите телеграм-бота, который получает от пользователя сообщение и
# возвращает это же сообщение со словами, переставленными в случайном порядке.
# Например, “Мама мыла раму” может превратиться в “мыла Мама раму”.

# ---------------------------------- Задание 2---------------------------------------
# Используя библиотеку pyTelegramBotAPI напишите телеграм-бота, который ждет от пользователя команду /game. При
# получении этой команды, бот заходит на страницу бесплатных игр на сайте Steam
# (https://store.steampowered.com/genre/Free%20to%20Play/), находит таблицу игр
# выбирает из таблицы случайную игру и выводит пользователю ее название и список тегов.
# Используйте re.findall для того, чтобы обнаружить пользовательские команды.

# ---------------------------------- Задание 3---------------------------------------
# Используя библиотеку pyTelegramBotAPI напишите телеграм-бота, который получает от пользователя команду в
# формате /index <почтовый_индекс>, затем обращается к бесплатному API https://api.zippopotam.us/ru/ и возвращает
# пользователю сообщение в формате ИНДЕКС, СТРАНА, ГОРОД
# Например, /index 101000 должен вернуть 101000: Russia Москва.

import telebot, random, requests, re, json
from bs4 import BeautifulSoup
token = '1771239734:AAEdb0Dh9lL1gSnKMYpHbrCgcxzIOpOCaEU'

# создаем бота
bot = telebot.TeleBot(token)

url = 'https://store.steampowered.com/genre/Free%20to%20Play/' 
steam_data = BeautifulSoup(requests.get(url).text, 'html.parser') # достаем данные с сайта стима

cards = steam_data.find_all('a', class_ = 'tab_item' ) # получили все теги <a href = ...> </a> в которых находится по сути вся нужная информация по карточке

game_titles_and_info = {} 
for card in cards:
    game_title, game_tags = card.find('div', class_ = 'tab_item_name'), card.find('div', class_ = 'tab_item_top_tags') 
    game_titles_and_info[game_title.text] = game_tags.text.split(',')

@bot.message_handler(commands = ['start'])
def say_hello(message):
    bot.reply_to(message, 'Добро пожаловать!')

@bot.message_handler(content_types = ['text'])
def shuffle_all_messages(message): 
    mes = message.text.split() # берем с телеги сообщение, удаляем пробелы
    if len(mes) > 2 and  mes[0] != mes[1]: # если больше одного слова и слова не похожи
        random.shuffle(mes) # перемешиваем полученный набор слов
        new_message = ' '.join(mes) # соединяем слова из списка, добавляем между ними пробелы
        bot.send_message(message.chat.id, 
                         new_message # выводим в чат телеги
                         )
    
    if '/game' in re.findall('/game', message.text): # если регулярка нашла в сообщении телеги такое слово то
        random_key = random.choice(list(game_titles_and_info.keys())) # берем из заранее полученного словаря игр случайный ключик и по нему уже соответствующие теги
        game_data = game_titles_and_info[random_key]
        bot.send_message(message.chat.id, 
                         'Тайтл:\n {}\n Жанр:\n {}'.format(random_key, game_data)
                         )
        
    if '/index' in re.findall('/index', message.text): # если есть слово индекс
        postal_code = re.findall('[0-9]+', message.text)[0]
        # по реквесту с апишника зиппопотама берем данные - это джос, лоудим их, достаем из них нужные данные
        data =  json.loads(str(BeautifulSoup(requests.get('https://api.zippopotam.us/ru/{}'.format(postal_code)).text, 'html.parser'))) #
        bot.send_message(message.chat.id, 
                         '{}: {} {}'.format(data['post code'], data['country'],
                                   data['places'][0]['place name'])
                         )

bot.infinity_polling()