# ---------------------------------- Задание 1---------------------------------------
# С помощью библиотек requests и bs4 прочитайте содержимое страницы бесплатных игр на сайте Steam
# (https://store.steampowered.com/genre/Free%20to%20Play/)
# Получите все ссылки (тег <a href = ‘...’>), для каждой ссылки получите текст ссылки и url.
# Сформируйте словарь, состоящий только из тех ссылок, у которых в тексте встречается фраза “Free To Play”.
# Выведите словарь на экран.

import requests
from bs4 import BeautifulSoup

url = 'https://store.steampowered.com/genre/Free%20to%20Play/' 
steam_data = BeautifulSoup(requests.get(url).text, 'html.parser') # трансформируем сырой html в структурированные набор тегов

cards = steam_data.find_all('a', class_ = 'tab_item' ) # получили все теги <a href = ...> </a> в которых находится по сути вся нужная информация по карточке

for card in cards:
    print(card.find('div', class_ = 'discount_final_price'))

game_titles_and_links = {}
for card in cards:  # для каждой карточке по игре
     # ищем дивы с нужным классом в которых помещена название и цена игры
    game_price, game_title = card.find('div', class_ = 'discount_final_price'), card.find('div', class_ = 'tab_item_name') 
    try: # можем встретить пустые или еще что-то ненужное, поэтому пробуем 
        # если текст внутри дива равен ФриТуПлау - обновляем словарь
        if game_price.text == 'Free To Play': game_titles_and_links[game_title.text] = card.get('href')
    except AttributeError: continue # иначе иди на следующий шаг цикла
        # печатаем
for title, link in game_titles_and_links.items(): print('Game title is {} and tou can get it for free!\n just click {}'.format(title, link))

# ---------------------------------- Задание 2---------------------------------------
# Сформируйте словарь, в котором ключами будут имена тегов, а значениями - количества игр, относящихся к
# этим тегам. Например: {‘Indie’: 2355, ... }
# Обратите внимание, что теги можно найти вот по такому bs-запросу: .find_all('div', class_ = 'tag_count_button')

# далее все действия практически аналогичны первому заданию:
    # Ищем нужный блок на сайте инспектом, смотрим что у него за класс, наводимся на него, выдергиваем текст - в которой любая нужная нам инфа
    # добавляяем в словарь, профит

popular_tags = steam_data.find('div', class_ = 'contenthub_popular_tags' ) # получили все теги <a href = ...> </a>

tag_info = {}
for tag in popular_tags.find_all('div', class_ = 'tag_count_button' ):
    tag_info[tag.find('span', class_ = 'tag_name').text] = tag.find('span', class_ = 'tag_count tab_filter_control_count').text
for title, count in tag_info.items(): print('Game genre is {} with count of {} copies'.format(title, count))

# ---------------------------------- Задание 3---------------------------------------
# Используйте функцию Inspect Element в вашем браузере, чтобы понять, какие теги и классы вам нужно
# обрабатывать.
# Составьте и распечатайте словарь игр и их тегов. Например, {'Incremental Epic Breakers': ['2D Platformer', ', Puzzle
# Platformer', ', Idler', ', Destruction'], ... }

game_titles_and_info = {} # 
for card in cards:
    game_title, game_tags = card.find('div', class_ = 'tab_item_name'), card.find('div', class_ = 'tab_item_top_tags') 
    game_titles_and_info[game_title.text] = game_tags.text.split(',')
for title, tags in game_titles_and_info.items(): print('Game title is {} with tags {}'.format(title, tags))

