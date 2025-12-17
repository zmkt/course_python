from decimal import Decimal
from typing import List


def parse_amount(text: str) -> tuple[Decimal, Decimal] | None:
    """Парсит сумму формата 'X руб Y коп' или 'X руб'"""
    text = text.strip().lower()
    parts = text.split()

    if len(parts) not in [2, 4] or parts[1] != 'руб':
        return None

    try:
        rub = Decimal(parts[0].replace(',', '.'))
        if len(parts) == 2:
            return rub, Decimal('0')

        if len(parts) != 4 or parts[3] != 'коп':
            return None

        cop = Decimal(parts[2]) / 100
        return rub, cop
    except (ValueError, ArithmeticError):
        return None


def add_expense(expenses: List[Decimal], value: str) -> bool:
    """Добавляет расход после парсинга. Возвращает True при успехе."""
    parsed = parse_amount(value)
    if parsed is None:
        print("Некорректный формат суммы")
        return False

    rub, cop = parsed
    total = rub + cop
    expenses.append(total)
    print(f"Добавлен расход: {total:.2f} руб.")
    return True


def delete_expense(expenses: List[Decimal], index: int) -> bool:
    """Удаляет расход по 1-based индексу. Возвращает True при успехе."""
    if 1 <= index <= len(expenses):
        removed = expenses.pop(index - 1)
        print(f"Удален расход: {removed:.2f} руб.")
        return True
    print("Некорректный номер расхода")
    return False


def get_total(expenses: List[Decimal]) -> Decimal:
    """Возвращает общую сумму расходов."""
    return sum(expenses)


def get_average(expenses: List[Decimal]) -> Decimal | None:
    """Возвращает средний расход или None если расходов нет."""
    if not expenses:
        return None
    return get_total(expenses) / len(expenses)


def print_report(expenses: List[Decimal]) -> None:
    """Печатает красивый отчет о расходах."""
    if not expenses:
        print("Расходы отсутствуют")
        return

    total = get_total(expenses)
    avg = get_average(expenses)

    print("\n" + "="*50)
    print("📊 ОТЧЕТ ПО РАСХОДАМ")
    print("="*50)
    print(f"Всего расходов: {len(expenses)}")
    print(f"Общая сумма: {total:.2f} руб.")
    print(f"Средний расход: {avg:.2f} руб." if avg else "Средний: 0.00 руб.")

    print("\n📋 СПИСОК РАСХОДОВ:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i:2d}. {expense:.2f} руб.")
    print("="*50 + "\n")

# Основная программа


def main() -> None:
    expenses: List[Decimal] = []

    while True:
        print("\n" + "-"*40)
        num = input(
            "1 - Добавить расход\n"
            "2 - Показать все расходы\n"
            "3 - Показать сумму и средний расход\n"
            "4 - Удалить расход по номеру\n"
            "5 - Выход\n"
            "Выберите действие: "
        ).strip()

        if num == "1":
            value = input(
                "Введите сумму (например, '150 руб 50 коп' или '200 руб'): ")
            add_expense(expenses, value)

        elif num == "2":
            print_report(expenses)

        elif num == "3":
            total = get_total(expenses)
            avg = get_average(expenses)
            print(f"\n💰 Общая сумма: {total:.2f} руб.")
            print(
                f"📈 Средний: {avg:.2f} руб." if avg else "📈 Средний: 0.00 руб.")

        elif num == "4":
            print_report(expenses)  # Показываем список для выбора
            index = input("Введите номер расхода для удаления: ")
            try:
                delete_expense(expenses, int(index))
            except ValueError:
                print("Введите число")

        elif num == "5":
            print("До свидания!")
            break

        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()

