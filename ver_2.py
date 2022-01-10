import random  # библиотека для работы с случайными числами
import string  # библиотека для работы символами ASCII


# Функция строчных букв кириллицы
def dict_russia_lower():
    rand_letter = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    return rand_letter

# Функция прописных букв кириллицы


def dict_russia_upper():
    rand_letter = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    return rand_letter


# Функция возвращающая некоторую строку из большой строки анг,рус символов, спецсимволов и цифр
def random_string(length):
   # Складываем строчки символов
    letters = string.ascii_letters + string.digits + \
        string.punctuation + dict_russia_lower() + \
        dict_russia_upper()
    # Создаем рандомную строчку используя метод random.sample
    rand_string = ''.join(random.sample(letters, length))
    return rand_string


# Воспользуемся конструкцией try - except для обработки исключений
try:
    values_pass = int(input('Введите  количество паролей: '))
    values_pass += 1  # Увеливаем на один, чтобы дальше в цикле можно начинать с 1-ого
    listik = []  # Создадим пустой список, в который будем помещать пароли
    for i in range(1, values_pass):  # Каждый раз генерируем пароли и записываем в список
        listik.append(random_string(random.randrange(6, 20, 1)))
    print('\n', listik)
    print('\nОткройте файл task2.txt в этой же папке, чтобы убедиться в записи паролей\n')

# Создадим файл и запишем в него пароли по строчно
    listik_File = open('task2.txt', 'w',  encoding='utf-8')
    for password in listik:
        listik_File.write(password)
        listik_File.write('\n')
    listik_File.close()

# Укажем исключение
except ValueError:
    print('\nВведен неправильный тип данных, запустите\nзаново программу и укажите число паролей\n')
