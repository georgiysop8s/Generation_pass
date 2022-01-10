import random  # библиотека для работы с случайными числами
import string  # библиотека для работы символами ASCII


# Функция случайных пяти строчных букв кириллицы
def dict_russia_lower():
    rand_letter = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    empty_list = []
    for i in range(0, 5):
        empty_list.append(random.choice(rand_letter))
    return empty_list

# Функция случайных пяти прописных букв кириллицы


def dict_russia_upper():
    rand_letter = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    empty_list = []
    for i in range(0, 5):
        empty_list.append(random.choice(rand_letter))
    return empty_list

# Функция случайных шести  спецсимволов


def dict_simbol():
    rand_letter = '+-/*!#&$?=@<>'
    empty_list = []
    for i in range(0, 6):
        empty_list.append(random.choice(rand_letter))
    return empty_list

# Функция случайных 15-ти строчных и прописных латинских букв


def dict_EN_lower_and_upper():
    rand_letter = string.ascii_letters
    empty_list = []
    for i in range(0, 15):
        empty_list.append(random.choice(rand_letter))
    return empty_list

# Функция написания цифр от 0-9


def dict_digits():
    rand_letter = string.digits
    empty_list = []
    for i in range(0, 10):
        empty_list.append(str(i))
    return empty_list


# Воспользуемся конструкцией try - except для обработки исключений
try:
    values_pass = int(input('Введите  количество паролей: '))
    values_pass += 1  # Увеливаем на один, чтобы дальше в цикле можно начинать с 1-ого
    listik = []  # Создадим пустой список, в который будем помещать пароли
    for i in range(1, values_pass):  # Каждый раз генерируем список разных символов
       # Внесем в список все полученные символы
        linkk = dict_russia_lower() + dict_russia_upper() + dict_simbol() + \
            dict_EN_lower_and_upper() + dict_digits()
      # Создадим случайную строку из этих символов
        password_string = "".join(random.sample(
            linkk, random.randrange(6, 20, 1)))
      # Добавим в список пароль
        listik.append(password_string)

    print('\n', listik)
    print('\nОткройте файл task1.txt в этой же папке, чтобы убедиться в записи паролей\n')

# Создадим файл и запишем в него пароли по строчно
    listik_File = open('task1.txt', 'w', encoding='utf-8')
    for password in listik:
        listik_File.write(password)
        listik_File.write('\n')
    listik_File.close()
# Укажем исключение
except ValueError:
    print('\nВведен неправильный тип данных, запустите\nзаново программу и укажите число паролей\n')