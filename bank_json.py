import os

FILE_NAME = 'deposit.txt'
orders =[]
deposit_list = []

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'r') as f:
        for change in f:
            deposit_list.append(change.replace('\n', ''))


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
        deposit_list.append(deposit)
        print(choice)
    elif choice == '2':
        price = int(input("введите сумму покупки: "))
        if price >= deposit:
            title = str(input("введите название покупки: "))
            orders.append(title)
            deposit -= price
            deposit_list.append(deposit)
            print(choice)
        else:
            print("недостаточно средств для совершения покупки")
    elif choice == '3':
        for order in orders:
            print(order)
        print(choice)
    elif choice == '4':
        with open(FILE_NAME, 'w') as f:
            for i in deposit_list:
                f.write(f'{i}\n')
        break
    else:
        print('Неверный пункт меню')
