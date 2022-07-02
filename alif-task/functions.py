def add_goods(file_name, SEPARATOR_SIGN):
    with open(file_name, "a", encoding='utf-8') as list:
        while True:
            name = input("\nНименование товара: ").capitalize().rstrip()
            price = input("Цена товара: ").rstrip()
            if name == '' and price == '':
                break
            if price.isnumeric(): # Проверка на число
                list.write("\n" + name + SEPARATOR_SIGN + price)
                print( "Товар " + name + " по цене " + price + " успешно добавлен!")
            else:
                print("Пожалуйста, запишите цену как число или выйдете двойным нажатием 'Enter'.")
                continue

# Функция copy_data отвечает за то, чтобы скопирповать содержимое тестового файла в список,
# чтобы было дегче рабоать с данными и изменять или удалять значения
def copy_data(file_name):   
    with open(file_name, "r", encoding='utf-8') as list:
        goods_list = []
        for line in list.readlines():
            goods_list.append(str(line))
        return goods_list

# В этой функции реализован простой интерфейс управления списком товаров. 
# Присутствуют проверки на корректность введенных данных и обработчики исключений,
# чтобы программа была надежнее.
def change_value(goods_list, SEPARATOR_SIGN):
     while True:
        try:
            set_id =int(input("\nВведите id изменяемого товара: "))
            
            print(goods_list[set_id])
        except ValueError:
            print("\nid может быть только целым числом.")
            continue
        except IndexError:
            print("\nВведите существующий индекс (они представлены в списке сверху).")
            continue

        name = input("\nВведите наименование нового товара: ").capitalize()
        price = input("Введите цену нового товара: ")
        if price.isnumeric():
            goods_list[set_id] = name + SEPARATOR_SIGN + price + "\n" # Заменяем интересующий нас товар на другой по индексу
        else:
            print("Цена может быть только числом.")
            continue
        return goods_list # Возвращаем обновленный список