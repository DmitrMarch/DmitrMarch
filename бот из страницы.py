# !!!!!ЗНАЧКОМ 🤡 ПОМЕЧЕНЫ МЕСТА, ГДЕ НУЖНА ЗМЕНА!!!!!

# для связи с сервером вк
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# для функций Рандомайзера
import random

# для работы с картинками
import requests
import os
import PIL
from PIL import Image
import imagehash
import shutil
from fuzzywuzzy import fuzz

# для функций Калькулятора
from math import e, pi, sqrt, log, sin, cos, tan, factorial as f
mod = abs

# словарь имён (его можно посмотреть тут Словарь имён.txt)
with open('Словарь имён.txt', 'r') as dict_names:
    dict_names1 = eval(dict_names.read())

# значение включения (ex = 0) / выключения проги (ex = 1)
ex = 0

# превращение картинок в хэш:
def imgs_urls(val):
    return val.replace(val, f'{file}/{val}')

def imgs_open(val):
    return Image.open(val)

def imgs_hashs(val):
    return str(imagehash.phash(val))

# нахождение схожести в %
def similarity(hash2):
    return fuzz.token_sort_ratio(hash1, hash2)

# значение картинки кота (все значения есть тут Значения картинок.txt)
with open('Значения картинок.txt', 'r') as dict_values:
    cat = eval(dict_values.read())['cat']

# значение картинки собаки
with open('Значения картинок.txt', 'r') as dict_values:
    dog = eval(dict_values.read())['dog']

# значение картинки кошкодевочки
with open('Значения картинок.txt', 'r') as dict_values:
    neko = eval(dict_values.read())['neko']

# значение картинки из категории другое
with open('Значения картинок.txt', 'r') as dict_values:
    other = eval(dict_values.read())['other']

bot = '''Доступные команды бота:
1⃣  Фотоопределитель - 
👉Photo👈;
2⃣  Калькулятор - 👉Calc👈;
3⃣  Рандомайзер - 👉Rand👈;
4⃣  Смена имени - Имя 
👉Новое имя👈;
5⃣  Свой числовой id - 👉Id👈;
6⃣  Чужой числовой id - Id 
👉короткий адрес👈;
7⃣  Числовой id группы - Group id 👉короткий адрес👈.
❗P.s. короткий адрес указывайте без @.'''

calc = '''❎ Калькулятор ❎
Доступные операторы и особые числа:
1⃣  Сложение или вычитание - 👉+👈 или 👉-👈;
2⃣  Умножение или деление - 👉*👈 или 👉/👈;
3⃣  Остаток или целая часть от деления - 👉%👈 или 👉//👈;
4⃣  Возведение в степень - 
👉**👈;
5⃣  Квадратный корень из 
числа - 👉sqrt(число)👈;
6⃣  Обычный или натуральный логарифм из числа - 
👉log(число, основание)👈 
или 👉log(число)👈;
7⃣  Числа е или Пи - 
👉e👈 или 👉pi👈;
8⃣  Синус, косинус или тангенс - 
👉sin(радианы)👈 или 
👉cos(радианы)👈 или 
👉tan(радианы)👈;
9⃣  Факториал из числа - 
👉f(число)👈;
🔟 Модуль из числа - 
👉mod(число)👈.
❗P.s. ввод примера - Реши 
👉пример👈.'''

rand = '''❓ Рандомайзер ❓
Доступные команды рандомайзера:
1⃣  Выбор одного случайного числа из диапазона от 1 до 2 числа - 
👉ранд 1 число 2 число👈;
2⃣  Выбор нескольких случайных чисел(3 число) из диапазона от 1 до 2 числа - 👉несранд3 число 1 число 2 число👈;
3⃣  Выбор случайного слова из списка слов - 👉cранд 1 слово 2 слово и т.д.👈;
4⃣  Выбор нескольких случайных слов(Число) из списка слов - 👉несcрандЧисло 1 слово 2 слово и т.д.👈.
❗P.s. случайные числа или слова не повоторяются, поэтому их количество не должно превышать 
количество чисел или слов в диапазоне или списке; числа в диапазоне пишутся от и до, например, от 1 до 
10 - это числа с 1 по 9.'''

# авторизация с помощью токена пользователя🤡
session = vk_api.VkApi(token="СЮДА СВОЙ ТОКЕН")

# метод отправки сообщений
def write_msg(peer_id, message):
    session.method('messages.send', {
        'peer_id': peer_id,
        'message': message,
        'random_id': 0
    })

# метод получения информации о сообщении
def msg_info(msg_id):
    return session.method('messages.getById', {
        'message_ids': msg_id,
        'extended': 1
    })

# метод получения инфы о пользователе по его айди
def user_info(user_id):
    return session.method('users.get', {
        "user_ids": user_id
    })

# вечный цикл вайл
while 1:

    # секретная команда включения бота
    if ex == 1:
        for event in VkLongPoll(session).listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:
                text = event.text.lower()
                user_id = event.user_id
                peer_id = event.peer_id
                if 'start' == text:
                    if user_id == СЮДА АЙДИ:  # твой айди пользователя🤡
                        write_msg(peer_id, '☕Запуск бота☕')
                        break

    # проверка на ошибки основного цикла фор
    try:

        # бот слушает события от сервера вк
        for event in VkLongPoll(session).listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:  # проверка события
                text = event.text.lower()  # текст сообщения
                peer_id = event.peer_id  # универсальный айди чата (для группы, беседы или пользователя)
                user_id = event.user_id  # айди пользователя
                atchs = event.attachments  # вложения
                user = user_info(user_id)
                name = user[0]['first_name'] + ' ' + user[0]['last_name']  # получение имени пользователя

                # проверка на наличие нового имени у пользователя в словаре
                if user_id in dict_names1:
                    name = dict_names1[user_id]  # присвоение нового имени пользователю при наличии его в словаре

                # главная инфо команда Бота
                if 'bot' == text:
                    write_msg(peer_id, f'🤖 {name}, бот вас приветсвует 🤖\n' + bot)

                # Калькулятор инфо
                elif 'calc' == text:
                    write_msg(peer_id, calc)

                # Рандомайзер инфо
                elif 'rand' == text:
                    write_msg(peer_id, rand)

                # Фотоопределитель инфо
                elif 'photo' == text:
                    write_msg(peer_id, '📷Фотоопределитель📷\nНапишите 👉Фото👈 вместе с отправкой фотографии, и бот '
                                       'попытается её распознать.\nP.s. пока доступны только фотографии котов, собак '
                                       'и кошкодевочек.')

                # команды Фотоопределителя
                elif 'фото' == text and atchs != {} and atchs['attach1_type'] == 'photo':
                    try:
                        url = 0
                        cat_distance = 0
                        dog_distance = 0
                        neko_distance = 0
                        other_distance = 0
                        user_id1 = event.user_id
                        msg_id = event.message_id
                        info = msg_info(msg_id)
                        sizes = (info['items'][0]['attachments'][0]['photo']['sizes'])
                        s_w = []
                        for size in sizes:
                            width = size['width']
                            s_w.append(width)
                        max_w = max(s_w)
                        min_w = min(s_w)
                        if max_w == min_w:
                            url = sizes[0]['url']
                        else:
                            for size in sizes:
                                width = size['width']
                                if width == max_w:
                                    url = size['url']
                        img = requests.get(
                            url,
                            headers={
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                              "(KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
                            }).content
                        with open('photo.jpg', 'wb') as handler:
                            handler.write(img)
                        img = Image.open('photo.jpg')
                        hash1 = str(imagehash.phash(img))
                        file = 'Cats'  # папка с котами
                        cat_imgs = os.listdir(file)
                        cat_url_imgs = list(map(imgs_urls, cat_imgs))
                        cat_open_imgs = list(map(imgs_open, cat_url_imgs))
                        cat_hashs = list(map(imgs_hashs, cat_open_imgs))
                        cat_distances = list(map(similarity, cat_hashs))
                        file = 'Dogs'  # папка с соаками
                        dog_imgs = os.listdir(file)
                        dog_url_imgs = list(map(imgs_urls, dog_imgs))
                        dog_open_imgs = list(map(imgs_open, dog_url_imgs))
                        dog_hashs = list(map(imgs_hashs, dog_open_imgs))
                        dog_distances = list(map(similarity, dog_hashs))
                        file = 'Neko'  # папка с неко тян
                        neko_imgs = os.listdir(file)
                        neko_url_imgs = list(map(imgs_urls, neko_imgs))
                        neko_open_imgs = list(map(imgs_open, neko_url_imgs))
                        neko_hashs = list(map(imgs_hashs, neko_open_imgs))
                        neko_distances = list(map(similarity, neko_hashs))
                        file = 'Other'  # папка с пикчами из категории другое
                        other_imgs = os.listdir(file)
                        other_url_imgs = list(map(imgs_urls, other_imgs))
                        other_open_imgs = list(map(imgs_open, other_url_imgs))
                        other_hashs = list(map(imgs_hashs, other_open_imgs))
                        other_distances = list(map(similarity, other_hashs))
                        other_dict = dict(zip(other_hashs, other_imgs))
                        other_dict2 = dict(zip(other_distances, other_imgs))
                        for distance in cat_distances:
                            if distance >= 60:
                                cat_distance += 1
                        for distance in dog_distances:
                            if distance >= 50:
                                dog_distance += 1
                        for distance in neko_distances:
                            if distance >= 55:
                                neko_distance += 1
                        for distance in other_distances:
                            if distance >= 44:
                                other_distance += 1
                        if hash1 in cat_hashs:
                            write_msg(peer_id, 'Это картинка кота.')
                        elif hash1 in dog_hashs:
                            write_msg(peer_id, 'Это картинка собаки.')
                        elif hash1 in neko_hashs:
                            write_msg(peer_id, 'Это картинка кошкодевочки.')
                        elif hash1 in other_hashs:
                            other_name = other_dict[hash1]
                            if '_' in other_name:
                                other_name = other_name[:other_name.index('_')]
                            else:
                                other_name = other_name[:other_name.index('.')]
                            write_msg(peer_id, f'На фото {other_name}.')
                        elif cat_distance >= 1:
                            write_msg(peer_id, 'Бот обнаружил кота на фотографии, это правильно? Напишите Да или Нет.')
                            for event in VkLongPoll(session).listen():
                                if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:
                                    user_id2 = event.user_id
                                    text = event.text.lower()
                                    if 'да' == text and user_id2 == user_id1:
                                        cat += 1
                                        shutil.move('photo.jpg', f'Cats/cat_{cat}.jpg')
                                        write_msg(peer_id, 'Хорошо, распознавание котов улучшилось.')
                                        break
                                    elif 'нет' == text and user_id2 == user_id1:
                                        write_msg(peer_id, 'Бот ещё учится, напишите свой вариант того, что на фото.')
                                        for event in VkLongPoll(session).listen():
                                            if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:
                                                user_id2 = event.user_id
                                                text = event.text.lower()
                                                other_value = 0
                                                for value in other_dict.values():
                                                    if '_' in value:
                                                        value = value[:value.index('_')]
                                                    else:
                                                        value = value[:value.index('.')]
                                                    if text == value:
                                                        other_value = value
                                                if 'кот' in text or 'кошка' == text or 'кошки' == text or 'кошак' in \
                                                        text and user_id2 == user_id1:
                                                    cat += 1
                                                    shutil.move('photo.jpg', f'Cats/cat_{cat}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание котов улучшилось.')
                                                    break
                                                elif 'собак' in text or 'щено' in text or 'пес' in text or 'пёс' in \
                                                        text and user_id2 == user_id1:
                                                    dog += 1
                                                    shutil.move('photo.jpg', f'Dogs/dog_{dog}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание собак улучшилось.')
                                                    break
                                                elif 'неко' in text or 'кошкодевочка' == text or 'кошкодевочки' == \
                                                        text and user_id2 == user_id1:
                                                    neko += 1
                                                    shutil.move('photo.jpg', f'Neko/neko_{neko}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание кошкодевочек улучшилось.')
                                                    break
                                                elif text == other_value:
                                                    other += 1
                                                    shutil.move('photo.jpg', f'Other/{text}_{other}.jpg')
                                                    write_msg(peer_id, f'Распознавание фотографий из категории '
                                                                       f'"{text}" улучшено')
                                                elif user_id2 == user_id1:
                                                    other += 1
                                                    shutil.move('photo.jpg', f'Other/{text}_{other}.jpg')
                                                    write_msg(peer_id, 'Бот ещё не научился его(её) распознавать, фото '
                                                                       'добавлено в папку с будущими фотографиями для '
                                                                       'распознавания.')
                                                    break
                                        break
                        elif dog_distance >= 1:
                            write_msg(peer_id, 'Бот обнаружил собаку на фотографии, это правильно? Напишите Да или '
                                               'Нет.')
                            for event in VkLongPoll(session).listen():
                                if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:
                                    user_id2 = event.user_id
                                    text = event.text.lower()
                                    if 'да' == text and user_id2 == user_id1:
                                        dog += 1
                                        shutil.move('photo.jpg', f'Dogs/dog_{dog}.jpg')
                                        write_msg(peer_id, 'Хорошо, распознавание собак улучшилось.')
                                        break
                                    elif 'нет' == text and user_id2 == user_id1:
                                        write_msg(peer_id, 'Бот ещё учится, напишите свой вариант того, что на фото.')
                                        for event in VkLongPoll(session).listen():
                                            if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:
                                                user_id2 = event.user_id
                                                text = event.text.lower()
                                                other_value = 0
                                                for value in other_dict.values():
                                                    if '_' in value:
                                                        value = value[:value.index('_')]
                                                    else:
                                                        value = value[:value.index('.')]
                                                    if text == value:
                                                        other_value = value
                                                if 'кот' in text or 'кошка' == text or 'кошки' == text or 'кошак' in \
                                                        text and user_id2 == user_id1:
                                                    cat += 1
                                                    shutil.move('photo.jpg', f'Cats/cat_{cat}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание котов улучшилось.')
                                                    break
                                                elif 'собак' in text or 'щено' in text or 'пес' in text or 'пёс' in \
                                                        text and user_id2 == user_id1:
                                                    dog += 1
                                                    shutil.move('photo.jpg', f'Dogs/dog_{dog}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание собак улучшилось.')
                                                    break
                                                elif 'неко' in text or 'кошкодевочка' == text or 'кошкодевочки' == \
                                                        text and user_id2 == user_id1:
                                                    neko += 1
                                                    shutil.move('photo.jpg', f'Neko/neko_{neko}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание кошкодевочек улучшилось.')
                                                    break
                                                elif text == other_value:
                                                    other += 1
                                                    shutil.move('photo.jpg', f'Other/{text}_{other}.jpg')
                                                    write_msg(peer_id, f'Распознавание фотографий из категории '
                                                                       f'"{text}" улучшено')
                                                elif user_id2 == user_id1:
                                                    other += 1
                                                    shutil.move('photo.jpg', f'Other/{text}_{other}.jpg')
                                                    write_msg(peer_id, 'Бот ещё не научился его(её) распознавать, фото '
                                                                       'добавлено в папку с будущими фотографиями для '
                                                                       'распознавания.')
                                                    break
                                        break
                        elif neko_distance >= 1:
                            write_msg(peer_id, 'Бот обнаружил кошкодевочку на фотографии, это правильно? Напишите Да '
                                               'или Нет.')
                            for event in VkLongPoll(session).listen():
                                if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:
                                    user_id2 = event.user_id
                                    text = event.text.lower()
                                    if 'да' == text and user_id2 == user_id1:
                                        neko += 1
                                        shutil.move('photo.jpg', f'Neko/neko_{neko}.jpg')
                                        write_msg(peer_id, 'Хорошо, распознавание кошкодевочек улучшилось.')
                                        break
                                    elif 'нет' == text and user_id2 == user_id1:
                                        write_msg(peer_id, 'Бот ещё учится, напишите свой вариант того, что на фото.')
                                        for event in VkLongPoll(session).listen():
                                            if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:
                                                user_id2 = event.user_id
                                                text = event.text.lower()
                                                other_value = 0
                                                for value in other_dict.values():
                                                    if '_' in value:
                                                        value = value[:value.index('_')]
                                                    else:
                                                        value = value[:value.index('.')]
                                                    if text == value:
                                                        other_value = value
                                                if 'кот' in text or 'кошка' == text or 'кошки' == text or 'кошак' in \
                                                        text and user_id2 == user_id1:
                                                    cat += 1
                                                    shutil.move('photo.jpg', f'Cats/cat_{cat}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание котов улучшилось.')
                                                    break
                                                elif 'собак' in text or 'щено' in text or 'пес' in text or 'пёс' in \
                                                        text and user_id2 == user_id1:
                                                    dog += 1
                                                    shutil.move('photo.jpg', f'Dogs/dog_{dog}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание собак улучшилось.')
                                                    break
                                                elif 'неко' in text or 'кошкодевочка' == text or 'кошкодевочки' == \
                                                        text and user_id2 == user_id1:
                                                    neko += 1
                                                    shutil.move('photo.jpg', f'Neko/neko_{neko}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание кошкодевочек улучшилось.')
                                                    break
                                                elif text == other_value:
                                                    other += 1
                                                    shutil.move('photo.jpg', f'Other/{text}_{other}.jpg')
                                                    write_msg(peer_id, f'Распознавание фотографий из категории '
                                                                       f'"{text}" улучшено')
                                                elif user_id2 == user_id1:
                                                    other += 1
                                                    shutil.move('photo.jpg', f'Other/{text}_{other}.jpg')
                                                    write_msg(peer_id, 'Бот ещё не научился его(её) распознавать, фото '
                                                                       'добавлено в папку с будущими фотографиями для '
                                                                       'распознавания.')
                                                    break
                                        break
                        elif other_distance >= 1:
                            mnum = max(other_distances)
                            other_name2 = other_dict2[19]
                            if '_' in other_name2:
                                other_name2 = other_name2[:other_name2.index('_')]
                            else:
                                other_name2 = other_name2[:other_name2.index('.')]
                            write_msg(peer_id, f'На фото, возможно {other_name2}, это правильно? Напишите Да или Нет.')
                            for event in VkLongPoll(session).listen():
                                if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:
                                    user_id2 = event.user_id
                                    text = event.text.lower()
                                    if 'да' == text and user_id2 == user_id1:
                                        other += 1
                                        shutil.move('photo.jpg', f'Other/{text}_{other}.jpg')
                                        write_msg(peer_id, f'Распознавание фотографий из категории "{other_name2}" '
                                                           f'улучшено.')
                                        break
                                    elif 'нет' == text and user_id2 == user_id1:
                                        write_msg(peer_id, 'Бот ещё учится, напишите свой вариант того, что на фото.')
                                        for event in VkLongPoll(session).listen():
                                            if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:
                                                user_id2 = event.user_id
                                                text = event.text.lower()
                                                other_value = 0
                                                for value in other_dict.values():
                                                    if '_' in value:
                                                        value = value[:value.index('_')]
                                                    else:
                                                        value = value[:value.index('.')]
                                                    if text == value:
                                                        other_value = value
                                                if 'кот' in text or 'кошка' == text or 'кошки' == text or 'кошак' in \
                                                        text and user_id2 == user_id1:
                                                    cat += 1
                                                    shutil.move('photo.jpg', f'Cats/cat_{cat}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание котов улучшилось.')
                                                    break
                                                elif 'собак' in text or 'щено' in text or 'пес' in text or 'пёс' in \
                                                        text and user_id2 == user_id1:
                                                    dog += 1
                                                    shutil.move('photo.jpg', f'Dogs/dog_{dog}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание собак улучшилось.')
                                                    break
                                                elif 'неко' in text or 'кошкодевочка' == text or 'кошкодевочки' == \
                                                        text and user_id2 == user_id1:
                                                    neko += 1
                                                    shutil.move('photo.jpg', f'Neko/neko_{neko}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание кошкодевочек улучшилось.')
                                                    break
                                                elif text == other_value:
                                                    other += 1
                                                    shutil.move('photo.jpg', f'Other/{text}_{other}.jpg')
                                                    write_msg(peer_id, f'Распознавание фотографий из категории '
                                                                       f'"{text}" улучшено')
                                                elif user_id2 == user_id1:
                                                    other += 1
                                                    shutil.move('photo.jpg', f'Other/{text}_{other}.jpg')
                                                    write_msg(peer_id, 'Бот ещё не научился его(её) распознавать, фото '
                                                                       'добавлено в папку с будущими фотографиями для '
                                                                       'распознавания.')
                                                    break
                                        break
                        else:
                            write_msg(peer_id, 'Бот не смог распознать фотографию.\nНапишите, что же на ней.')
                            for event in VkLongPoll(session).listen():
                                if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:
                                    user_id2 = event.user_id
                                    text = event.text.lower()
                                    other_value = 0
                                    for value in other_dict.values():
                                        if '_' in value:
                                            value = value[:value.index('_')]
                                        else:
                                            value = value[:value.index('.')]
                                        if text == value:
                                            other_value = value
                                    if 'кот' in text or 'кошка' == text or 'кошки' == text or 'кошак' in text and \
                                            user_id2 == user_id1:
                                        cat += 1
                                        shutil.move('photo.jpg', f'Cats/cat_{cat}.jpg')
                                        write_msg(peer_id, 'Хорошо, распознавание котов улучшилось.')
                                        break
                                    elif 'собак' in text or 'щено' in text or 'пес' in text or 'пёс' in text and \
                                            user_id2 == user_id1:
                                        dog += 1
                                        shutil.move('photo.jpg', f'Dogs/dog_{dog}.jpg')
                                        write_msg(peer_id, 'Хорошо, распознавание собак улучшилось.')
                                        break
                                    elif 'неко' in text or 'кошкодевочка' == text or 'кошкодевочки' == text and \
                                            user_id2 == user_id1:
                                        neko += 1
                                        shutil.move('photo.jpg', f'Neko/neko_{neko}.jpg')
                                        write_msg(peer_id, 'Хорошо, распознавание кошкодевочек улучшилось.')
                                        break
                                    elif text == other_value:
                                        other += 1
                                        shutil.move('photo.jpg', f'Other/{text}_{other}.jpg')
                                        write_msg(peer_id, f'Распознавание фотографий из категории "{text}" улучшено')
                                    elif user_id2 == user_id1:
                                        other += 1
                                        shutil.move('photo.jpg', f'Other/{text}_{other}.jpg')
                                        write_msg(peer_id, 'Бот ещё не научился его(её) распознавать, фото добавлено в '
                                                           'папку с будущими фотографиями для распознавания.')
                                        break
                    except requests.exceptions.InvalidURL:
                        write_msg(peer_id, '🚫Ошибка, некорректная ссылка🚫')
                    except requests.exceptions.MissingSchema:
                        write_msg(peer_id, '🚫Ошибка, некорректная ссылка🚫')
                    except PIL.UnidentifiedImageError:
                        write_msg(peer_id, '🚫Ошибка, бот не смог открыть фотографию🚫')
                    except TypeError:
                        write_msg(peer_id, '🚫Произошла ошибка со стороны сервера фотографии🚫')
                    except requests.exceptions.ConnectionError:
                        write_msg(peer_id, '🚫Ошибка, не получилось скачать фотографию🚫')

                # работа с именами пользователей:

                # установка нового имени пользователю
                elif 'имя ' == text[:4]:
                    nick = event.text[4:]
                    dict_names1[user_id] = nick
                    with open('Словарь имён.txt', 'w') as dict_names:
                        dict_names.write(str(dict_names1))
                    write_msg(peer_id, f'@id{user_id} ({name}), ваше новое имя - {nick}.\nЧтобы посмотреть топ новых '
                                       f'имён напишите 👉Имена👈.\nЧтобы удалить новое имя напишите 👉Кик имя👈.')

                # выведение списка новых имён у пользователей
                elif 'имена' == text:
                    s = []
                    for b in dict_names1.items():
                        user = user_info(user_id)
                        username = user[0]['first_name'] + ' ' + user[0]['last_name']
                        s.append(f'@id{b[0]} ({username}) - {b[1]}')
                    top = '\n'.join(s)
                    write_msg(peer_id, 'Топ новых имён:\n' + top)

                # удаление новго имени пользователя
                elif 'кик имя' == text:
                    try:
                        nick = dict_names1[user_id]
                        with open('Словарь имён.txt', 'w') as dict_names:
                            dict_names.write(str(dict_names1))
                        name = user[0]['first_name'] + ' ' + user[0]['last_name']
                        del dict_names1[user_id]
                        write_msg(peer_id, f'@id{user_id} ({nick}), теперь вы снова {name}.')
                    except KeyError:
                        write_msg(peer_id, 'У вас и так нет нового имени.')

                # работа с разными айди:

                # получение своего айди
                elif 'id' == text:
                    write_msg(peer_id, f'Твой айди: {user_id}')

                # получение чужого айди
                elif 'id ' == text[:3]:
                    try:
                        text = text.replace('id ', '')
                        user = user_info(user_id)
                        ids = user[0]['id']
                        write_msg(peer_id, f'Айди пользователя: {ids}')
                    except vk_api.exceptions.ApiError:
                        write_msg(peer_id, '🚫Ошибка, неправильно введён короткий адрес🚫')

                # получение айди группы
                elif 'group id ' == text[:9]:
                    try:
                        text = text.replace('group id ', '')
                        group = session.method('groups.getById', {
                            "group_id": text
                        })
                        group_id = group[0]['id']
                        write_msg(peer_id, f'Айди группы: {group_id}')
                    except vk_api.exceptions.ApiError:
                        write_msg(peer_id, '🚫Ошибка, неправильно введён короткий адрес🚫')

                # секретная команда выключения Бота
                elif 'exit' == text:
                    if user_id == СЮДА АЙДИ:  # опять твой айди пользователя🤡
                        write_msg(peer_id, '💤Выключение бота💤')
                        ex = 1
                        break

                # команды Калькулятора
                elif 'реши ' == text[:5]:
                    try:
                        string = text.replace('реши ', '')
                        b = 'Ответ: ' + str(eval(string))
                        if '.0' == b[-2:]:
                            c = b.replace('.0', '')
                            write_msg(peer_id, c)
                        else:
                            write_msg(peer_id, b)
                    except NameError:
                        write_msg(peer_id, '🚫Ошибка, проверьте пример🚫')
                    except SyntaxError:
                        write_msg(peer_id, '🚫Ошибка, проверьте пример🚫')
                    except TypeError:
                        write_msg(peer_id, '🚫Ошибка, проверьте пример🚫')
                    except ZeroDivisionError:
                        write_msg(peer_id, '🚫На 0 делить нельзя🚫')

                # команды Рандомайзера:

                # случайные числа:

                # 1 число
                elif 'ранд ' == text[:5]:
                    try:
                        text = text.replace('ранд ', '').split()
                        d = int(text[0])
                        e = int(text[1])
                        f = range(d, e)
                        g = str(random.choice(f))
                        write_msg(peer_id, 'Рандомное число: ' + g)
                    except ValueError:
                        write_msg(peer_id, '🚫Неправильно введён диапазон чисел🚫')
                    except NameError:
                        write_msg(peer_id, '🚫Неправильно введён диапазон чисел🚫')
                    except IndexError:
                        write_msg(peer_id, '🚫Неправильно введён диапазон чисел🚫')
                    except TypeError:
                        write_msg(peer_id, '🚫Неправильно введён диапазон чисел🚫')
                    except SyntaxError:
                        write_msg(peer_id, '🚫Неправильно введён диапазон чисел🚫')

                # несколько чисел
                elif 'несранд' == text[:7]:
                    try:
                        text = text.replace('несранд', '')
                        g = int(text[:text.index(' ')])
                        text = text[text.index(' '):].split()
                        d = int(text[0])
                        e = int(text[1])
                        f = range(d, e)
                        h = str(random.sample(f, g))
                        write_msg(peer_id, 'Рандомные числа: ' + h[1:-1])
                    except ValueError:
                        write_msg(peer_id, '🚫Количество случайных чисел превышает количество чисел в диапазоне, или '
                                           'они неправильно введены🚫')
                    except NameError:
                        write_msg(peer_id, '🚫Неправильно введены диапазон чисел или количество случайных чисел🚫')
                    except IndexError:
                        write_msg(peer_id, '🚫Неправильно введены диапазон чисел или количество случайных чисел🚫')
                    except TypeError:
                        write_msg(peer_id, '🚫Неправильно введены диапазон чисел или количество случайных чисел🚫')
                    except SyntaxError:
                        write_msg(peer_id, '🚫Неправильно введены диапазон чисел или количество случайных чисел🚫')

                # случайные слова:

                # 1 слово
                elif 'сранд' == text[:5]:
                    try:
                        lw = text.replace('сранд ', '').split()
                        rw = random.choice(lw)
                        write_msg(peer_id, 'Случайное слово: ' + rw)
                    except ValueError:
                        write_msg(peer_id, '🚫Неправильно введён список слов🚫')
                    except NameError:
                        write_msg(peer_id, '🚫Неправильно введён список слов🚫')
                    except IndexError:
                        write_msg(peer_id, '🚫Неправильно введён список слов🚫')
                    except TypeError:
                        write_msg(peer_id, '🚫Неправильно введён список слов🚫')
                    except SyntaxError:
                        write_msg(peer_id, '🚫Неправильно введён список слов🚫')

                # несколько слов
                elif 'нессранд' == text[:8]:
                    try:
                        text = text.replace('нессранд', '')
                        n = int(text[:text.index(' ')])
                        lw = text = text[text.index(' '):].split()
                        lrw = str(random.sample(lw, n))[1:-1].replace("'", '')
                        write_msg(peer_id, 'Рандомные слова: ' + lrw)
                    except ValueError:
                        write_msg(peer_id, '🚫Количество случайных слов превышает количество слов в списке, или они '
                                           'неправильно введены🚫')
                    except NameError:
                        write_msg(peer_id, '🚫Неправильно введены список слов или количество случайных слов🚫')
                    except IndexError:
                        write_msg(peer_id, '🚫Неправильно введены список слов или количество случайных слов🚫')
                    except TypeError:
                        write_msg(peer_id, '🚫Неправильно введены список слов или количество случайных слов🚫')
                    except SyntaxError:
                        write_msg(peer_id, '🚫Неправильно введены список слов или количество случайных слов🚫')

    except IndexError:  # что бот делает в случае ошибки
        pass  # ничего
    except AttributeError:
        pass
