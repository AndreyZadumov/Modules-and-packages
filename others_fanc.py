import math
import random

def game():
    Musk = 'назовите дату рождения Илона Маска '
    Bezos = 'назовите дату рождения Джеффа Безоса '
    Gates = 'назовите дату рождения Билла Гейтса '
    Jobs = 'назовите дату рождения Стива Джопса '
    Korolev = 'назовите дату рождения Сергея Королева '
    Pushkin = 'назовите дату рождения Александра Пушкина '
    Lenin = 'назовите дату рождения Владимира Ленина '
    Stalin = 'назовите дату рождения Иосифа Сталина '
    Vysotsky = 'назовите дату рождения Владимира Высоцкого '
    Gagarin = 'назовите дату рождения Юрия Гагарина '

    Musk_answer = "28.06.1971"
    Bezos_answer = "12.01.1964"
    Gates_answer = "28.10.1955"
    Jobs_answer = "24.02.1955"
    Korolev_answer = "12.01.1907"
    Pushkin_answer = "16.05.1799"
    Lenin_answer = "22.04.1870"
    Stalin_answer = "09.12.1879"
    Vysotsky_answer = "25.12.1938"
    Gagarin_answer = "09.03.1934"

    people = [Musk, Bezos, Gates, Jobs, Korolev, Pushkin, Lenin, Stalin, Vysotsky, Gagarin]
    people_answer = [Musk_answer, Bezos_answer, Gates_answer, Jobs_answer, Korolev_answer, Pushkin_answer, Lenin_answer,
                     Stalin_answer, Vysotsky_answer, Gagarin_answer]

    right = 0
    wrong = 0

    for i in range(5):
        idx = random.randint(0, 9)
        answer = input(people[idx])
        if answer != people_answer[idx]:
            wrong += 1
            print('неверно')
        else:
            right += 1
    print('Ваши результаты: ')
    print('количество правильных ответов', right)
    print('количество ошибок', wrong)

def bank():
    story = {}
    while True:
        deposit = 0
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            contribution = int(input("введите сумму пополнения счета: "))
            deposit += contribution
            print(choice)
        elif choice == '2':
            price = int(input("введите сумму покупки: "))
            if price >= deposit:
                title = str(input("введите название покупки: "))
                story.fromkeys([price], title)
                deposit -= price
                print(choice)
            else:
                print("недостаточно средств для совершения покупки")
        elif choice == '3':
            print(story.items())
            print(choice)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False

