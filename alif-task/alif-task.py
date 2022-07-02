import os
import functions as fn

SEPARATOR_SIGN = ' - '
CLEAR = lambda: os.system('cls')

while True:
    # Выбрать файл для работы
    print("Возможные для использования файлы: list.txt")
    file_name = input("\n\nНазвание файла: ")
    try:
        with open(file_name) as list:
            pass
    except FileNotFoundError:
        print("\nВведите название существующего файла.\n\n")
        continue

    while True:
        # Меню для удобства
        CLEAR()
        action = input(
        "\n\nОткрыт файл '" + file_name + "'. Выберете действия над ним: \n"
        "0. Выйти из программы\n"
        "1. Добавить в список\n"
        "2. Изменить запись в списке\n"
        "3. Удалить из списка\n"
        "4. Вычислить общую сумму\n"
        "Ваш выбор: ")

        if action == "0":
            quit()
        if action == "1":
            fn.add_goods(file_name, SEPARATOR_SIGN)
        if action == "2":
            CLEAR()
            goods_list = fn.copy_data(file_name)
            #Вывод списка с пронумерованными индексами элементов для удобства 
            i = 0
            for element in goods_list:                  
                print(str(i) + ". " + element + "\n")
                i += 1
            goods_list = fn.change_value(goods_list, SEPARATOR_SIGN)
            with open(file_name, 'w', encoding='utf-8') as list: 
                for element in goods_list:
                    list.write(element)
        if action == "3":
            CLEAR()
            goods_list = fn.copy_data(file_name)
            i = 0
            for element in goods_list:
                print(str(i) + ". " + element + "\n")
                i += 1
            id = int(input("Введите id товара, который хотите удалить: "))
            goods_list.pop(id)
            with open(file_name, 'w', encoding='utf-8') as list: 
                for element in goods_list:
                    list.write(element)
        if action == "4":
            sum = 0
            with open(file_name, 'r') as file:
                for line in file.readlines():
                    name, price = line.split(SEPARATOR_SIGN)
                    sum += int(price)

            input("Общая сумма: " + str(sum))