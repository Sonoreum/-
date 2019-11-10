import random # Импортирование необходимых библиотек
import string
import os


finish = int(input('Введите длину пароля: '))      # Переменная, отвечающая за длину пароля.
use_ru = int(input('Использовать кириллицу?\nДа - 1\tНет - 0\n')) # Переменная, отвечающая за использование кириллицы в пароле.

if finish <= 0 or use_ru != 1 and use_ru != 0:  # Проверка корректности введенных данных.
    print('Введенны некорректные данные!')

ru_words = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' # Создание строки русского алфавита.

def generpass(start, finish): # Функция для генерации(параметры задают длину пароля).

    while start < finish:  #Цикл для генерации(работает побуквенно).
        if use_ru == 1:   # Проверка переменной, отвечающей за использование кириллицы. 
            yield random.choice(string.digits + string.ascii_letters +      # Генератор, использующий цифры, буквы английского алфавитав двух в регистрах,
                          string.punctuation + ru_words.upper() + ru_words) # знаки пунктуации и кириллица в двух регистрах (склеивание постоянных из string и кириллицы).
        else:
            yield random.choice(string.digits + string.ascii_letters + string.punctuation) # Генератор, использующий цифры, буквы английского алфавита в
        start += 1                                                                         # двух регистрах и знаки пунктуации(склеивание постоянных из string).
        # переход к следующей букве.

password = generpass(0, finish)

with open(os.getcwd() + '\password.txt', 'w') as pas: # Открытие(создание в текущей директории) файла для записи пароля.
    for i in password:          # Побуквенная запись и вывод.
        print(i, end = '')
        pas.write(i)