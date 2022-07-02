import os
import shutil
import sys
from other_funk import *
import random

def program():
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
        print('11. выход')


        decision = input('Выберите пункт меню ')
        if decision == '1':
            os.mkdir(str(input('Введите название папки: ')))
            print(decision)

        elif decision == '2':
            os.rmdir(str(input('Введите название папки: ')))
            print(decision)

        elif decision == '3':
            name = str(input('Введите название папки, которую хотите копировать: '))
            name_copy = str(input('Введите название для копии: '))
            shutil.copytree(name, name_copy)
            print(decision)

        elif decision == '4':
            print(os.listdir())
            print(decision)


        elif decision == '6':
            files = [f for f in os.listdir('/Users/user/PycharmProjects/Мodules') if os.path.isfile(os.path.join('/Users/user/PycharmProjects/Мodules', f))]
            print(files)
            print(decision)

        elif decision == '5':
            dir = [f for f in os.listdir('/Users/user/PycharmProjects/Мodules') if
                     os.path.isdir(os.path.join('/Users/user/PycharmProjects/Мodules', f))]
            print(dir)
            print(decision)

        elif decision == '7':
            print(sys.platform)
            print(decision)

        elif decision == '8':
            print(os.getlogin())
            print(decision)

        elif decision == '9':
            game()
            print(decision)

        elif decision == '10':
            bank()
            print(decision)

        elif decision == '11':
            break

        else:
            print('Неверный пункт меню')


program()