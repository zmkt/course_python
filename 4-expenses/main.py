# from decimal import Decimal


# def parse_amount(text: str) -> tuple[Decimal, Decimal] | None:
#     """Парсит сумму формата 'X руб Y коп' или 'X руб'"""
#     # Нормализация: нижний регистр + убираем лишние пробелы
#     text = text.strip().lower()

#     # Разбиваем по словам
#     parts = text.split()

#     if len(parts) not in [2, 4]:
#         return None

#     # Проверяем обязательные слова "руб" и (опционально) "коп"
#     if parts[1] != 'руб':
#         return None

#     try:
#         rub = Decimal(parts[0].replace(',', '.'))

#         # Формат "X руб" — коп = 0
#         if len(parts) == 2:
#             return rub, Decimal('0')

#         # Формат "X руб Y коп"
#         if len(parts) != 4 or parts[3] != 'коп':
#             return None

#         cop = Decimal(parts[2]) / 100
#         return rub, cop

#     except (ValueError, ArithmeticError):
#         return None


# # Основная программа
# number = input("Введите число: ").strip()

# result = parse_amount(number)
# if result is None:
#     print("Некорректный формат суммы")
# else:
#     rub, cop = result
#     total = rub + cop
#     print(f"{total:.2f} ")

while True:
    num = input(
        "1 - Добавить расход \n"
        "2 - Показать все расходы \n"
        "3 - Показать сумму и средний расход \n"
        "4 - Удалить расход по номеру \n"
        "5 - Выход \n"
        "Введите число: "
    )
    if num == "5":
        break
