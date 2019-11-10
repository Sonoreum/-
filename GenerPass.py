import random
import string
import os


finish = int(input('Введите длину пароля: '))
use_ru = int(input('Использовать кириллицу?\nДа - 1\tНет - 0\n'))

if finish <= 0 or use_ru != 1 and use_ru != 0:
    print('Введенны некорректные данные!')

ru_words = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
start = 0

def generpass(start, finish):

    while start <= finish:
        if use_ru == 1:
            yield random.choice(string.digits + string.ascii_letters + string.punctuation + ru_words.upper() + ru_words)
        if use_ru == 0:
            yield random.choice(string.digits + string.ascii_letters + string.punctuation)
        start += 1


password = generpass(1, finish)

with open(os.getcwd() + '\password.txt', 'w') as pas:
    for i in password:
        print(i, end = '')
        pas.write(i)
