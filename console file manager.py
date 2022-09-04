import os
import shutil
import sys
from others_fanc import *
import random
import json

while True:
    deposit = 0
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. сохранить содержимое рабочей директории в файл')
    print('12. выход')

    decision = input('Выберите пункт меню ')
    if decision == '1':
        os.mkdir(str(input('Введите название папки: ')))

    elif decision == '2':
        os.rmdir(str(input('Введите название папки: ')))

    elif decision == '3':
        name = str(input('Введите название папки, которую хотите копировать: '))
        name_copy = str(input('Введите название для копии: '))
        shutil.copytree(name, name_copy)

    elif decision == '4':
        print(os.listdir())

    elif decision == '6':
        files = [f for f in os.listdir('/Users/user/PycharmProjects/Modules-and-packages') if
                 os.path.isfile(os.path.join('/Users/user/PycharmProjects/Modules-and-packages', f))]
        print(files)

    elif decision == '5':
        dir = [f for f in os.listdir('/Users/user/PycharmProjects/Modules-and-packages') if
               os.path.isdir(os.path.join('/Users/user/PycharmProjects/Modules-and-packages', f))]
        print(dir)

    elif decision == '7':
        print(sys.platform)

    elif decision == '8':
        print(os.getlogin())

    elif decision == '9':
        game()

    elif decision == '10':
        bank()

    elif decision == '11':
        files = [f for f in os.listdir('/Users/user/PycharmProjects/Modules-and-packages') if
                 os.path.isfile(os.path.join('/Users/user/PycharmProjects/Modules-and-packages', f))] # Применяем генератор
        dir = [f for f in os.listdir('/Users/user/PycharmProjects/Modules-and-packages') if
               os.path.isdir(os.path.join('/Users/user/PycharmProjects/Modules-and-packages', f))] # Применяем генератор
        with open('listdir.txt', 'w') as fanc:
            fanc.write('Files: \n')
            json.dump(files, fanc)
            fanc.write('\nDirs: \n')
            json.dump(dir, fanc)

    elif decision == '12':
        break

    else:
        print('Неверный пункт меню')


