import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
folder = input('Введите название главной директории: ')
need_folders = ['settings', 'mainapp', 'adminapp', 'authapp']
if not os.path.exists(folder):  # проверяем на наличие с помощью экзиста(можно было isdir заюзать)
    os.mkdir(folder)  # создаем директорию, если такой не было обнаружено
    os.chdir(folder)  # переходим в неё
    for i in range(len(need_folders)):  # начинаем клепать папочки по названиям из списка
        if not os.path.exists(need_folders[i]):  # также проверяем на наличие, чтобы не словить ошибку
            os.mkdir(need_folders[i])  # создаем папку

# в список можно будет добавить возможность добавления любого кол-ва папок, по типу "Введите кол-во папок", а потом "Введите название папки" и так для каждой, но мне лень