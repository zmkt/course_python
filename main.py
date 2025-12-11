floor = int(input("Введите номер этажа: "))

match floor:
    case -1:
        print("Подвал: здесь находится склад")
    case 1:
        print("Холл и ресепшен")
    case 10:
        print("Технический этаж - вход запрещен")
    case _:
        print("Такого этажа нет")

if 1 < floor < 10:
    if floor % 2 == 0:
        print("Четный этаж")
    else:
        print("Нечетный этаж")
