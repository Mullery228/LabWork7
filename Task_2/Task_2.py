import os
import yaml
from yaml.loader import BaseLoader


# Суть вот в чём. С (божьей) помощью библиотеки yaml мы можем юзать метод load, который считывает шаблон из нашего .yml файла(в моём случае toster2.yml)
# Потом load формирует словарь(со вложенными словарями), но перед этим еще надо соблюдать правильный синтаксис в toster2.yml, чтобы load смог это всё считать
# И остается самое сложное - разобрать паутину из словарей и создать папки и файлы в правильном порядке
# Если говорить кратко, то в процессе перебора словаря, если мы текущий файл = словарь, то переключаемся на него и начинаем перебор уже его элементов, ну а если не словарь, то просто создаем файлы в нужном формате(смотрим на конец строки)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open('toster2.yml', 'r', encoding='utf-8') as fr:
    data = yaml.load(fr, Loader=BaseLoader)
    for key in data:
        if not os.path.exists(key):
            try:
                os.mkdir(key)
                os.chdir(key)
                print("1", key)
                for i in data:
                    if type(data[i]) == dict:
                        second_dict = data[i]
                        for j in second_dict:
                            third_dict = second_dict[j]
                            os.mkdir(j)
                            os.chdir(j)
                            print("         ", "2", j)
                            for y in third_dict:
                                if str(y).endswith('.py'):
                                    print("             ", "3", y)
                                    file = open(f'{y}', "w")
                                    file.close()
                                elif type(y) == dict:
                                    fourth_dict = y
                                    for x in fourth_dict:
                                        fifth_dict = fourth_dict[x]
                                        os.mkdir(x)
                                        os.chdir(x)
                                        print("             ", "3", x)
                                        for z in fifth_dict:
                                            if type(z) == dict:
                                                sixth_dict = z
                                                for zz in sixth_dict:
                                                    seven_dict = sixth_dict[zz]
                                                    os.mkdir(zz)
                                                    os.chdir(zz)
                                                    print("                     ", "4", zz)
                                                    for xx in seven_dict:
                                                        if str(xx).endswith('.html'):
                                                            print("                         ", "5", xx)
                                                            file = open(f'{xx}', "w")
                                                            file.close()
                            os.chdir("W:\\LabWork7.2\\my_project\\")
            except Exception as err:
                print(f'Сработала ошибка: {err}')
