# ---------------------------------- Задание 1---------------------------------------
# В приложении к уроку задан файл с таблицей ближайших к Земле галактик lesson09_closest_galaxies.csv. В файле
# содержатся 4 колонки:
# - Название галактики
# - Код галактики
# - Расстояние до Земли в млн. световых лет
# - Примечания
# Данные в колонках разделены запятой.
# Считайте файл, разбейте данные на ряды и колонки, сохраните их в список.
# С помощью re.search или re.match выведите названия всех галактик, у которых:
# - В названии встречаются созвездия Рыбы, Пегас или Кит
# - Название начинается с латинской буквы
# - Название заканчивается цифрой

import re

# открываем файл, читаем текст, удаляем символы переноса строки - будет мешать во время работы, парсим по запятой - получаем некий аналог таблицы со строками и столбацами\
filename = 'lesson09_closest_galaxies.csv'
splited_data = []
with open(filename , encoding = 'utf-8') as file:
    # считываем данные
    for line in file: splited_data.append(line.replace('\n', '').split(','))

# for data_line in splited_data: print(data_line)

for data_line in splited_data:
    # - В названии встречаются созвездия Рыбы, Пегас или Кит
    if re.search('Рыбы|Пегас[а-я]|Кит', data_line[0]): print(data_line[0])

for data_line in splited_data:
# - Название начинается с латинской буквы
    if re.search('[A-Z].+', data_line[0]): print(data_line[0])

for data_line in splited_data:
# - Название заканчивается цифрой
    if re.match('.+[0-9]$', data_line[0]): print(data_line[0])

# ---------------------------------- Задание 2---------------------------------------
# Используйте таблицу ближайших к Земле галактик lesson09_closest_galaxies.csv. С помощью re.search отберите те
# галактики, которые имеют отношение к созвездию Андромеды и имеют данные о расстоянии до Земли. Соберите эти
# галактики в список словарей вот в таком формате:
# [{'Название': 'Карликовая сфероидальная галактика в Пегасе (DDO 216)', 'Расстояние': 3.0, 'Примечания': 'Спутник
# Андромеды'}, ...]
# Обратите внимание, что расстояние до Земли должно быть конвертировано в тип float.
# Отсортируйте полученный список по возрастанию расстояния до Земли.

galaxy_params = [] # пустой массив куда будем кидать строки словариков
for data_line in splited_data: # перебираем каждую строку из файла
    name, distance, note = data_line[0], data_line[2], data_line[3] # в каждой стркое обращаемся к столбцу с именем, расстоянием и приечание по индексу
    # создаем переменные куда вкладываем найденные по шаблону регулярки значения, встречаемые
    # в столбце с названием или примечанием и шаблон для поиска значения расстояния
    name_match, distance_match =re.search('Андромед[а-я]+', name) or re.search('Андромед[а-я]+', note), re.search('[0-9\.*]+', distance) 
    if name_match  and  distance_match:
        galaxy_params.append({'Название':   name, # записываем в словарь, добавляем в массив
                              'Расстояние': float( distance_match[0] ),
                              'Примечания': note})

for galaxy in galaxy_params: print(galaxy) # печатаем результат

# ---------------------------------- Задание 3---------------------------------------
# В приложении к уроку задан файл lesson09_cats_of_ulthar.txt. С помощью библиотеки re посчитайте сколько раз в нем
# встречается слово “кошка” в любой форме.

filename = 'lesson09_cats_of_ulthar.txt'
with open(filename) as file:
    # считываем данные
    data_cats = file.read().replace('\n', '')
incatswetrust = re.findall('кошк[а-я]+', data_cats)
print(incatswetrust)
print('Мы встречаем всяких кошек {} раз'.format(len(incatswetrust)))

# ---------------------------------- Задание 4---------------------------------------
# В приложении к уроку задан файл lesson09_cats_of_ulthar.txt. С помощью библиотеки re посчитайте сколько раз в нем
# встречается слово “кошка” в любой форме.

import requests
from bs4 import BeautifulSoup

url = 'https://ru.wikipedia.org/wiki/Небьюла'
wikipedia = BeautifulSoup(requests.get(url).text, 'html.parser')

links = wikipedia.find_all('a') 

hrefs = []
for link in links:
    if link.get('href') != None: hrefs.append(link.get('href'))

def repair(link):
    new_link = ''
    if not ('http' or 'https' or 'www.') in link: new_link = 'https:' + link
    else: new_link = link
    return new_link

not_wiki_hrefs = []
for link in hrefs:
    if not (re.match('.+wiki.+', link) or re.match('#.+', link) or re.match('/w/.+', link)):
        not_wiki_hrefs.append(link)

rep_not_wiki_hrefs = []
for link in not_wiki_hrefs: rep_not_wiki_hrefs.append(repair(link))

for link in rep_not_wiki_hrefs: print(link)

