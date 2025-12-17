from typing import Literal


def calculation(one_num: int, two_num: int, action: Literal['*', '/', '+', '-']):
    """
    Делает математическую операцию над 2-мя числами

    :param a: первое число
    :param b: второе число
    :param action: действие
    :return: возвращает результат
    """
    match action:
        case "*":
            return one_num * two_num
        case "/":
            return one_num / two_num
        case "+":
            return one_num + two_num
        case "-":
            return one_num - two_num
        case _:
            print("Такого действия не существует")
            exit()


print(calculation(13, 2, '*'))
