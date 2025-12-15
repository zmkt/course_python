import random


def select_variant():
    choice_people = input("Введите камень, ножницы или бумага: ").lower()
    while choice_people.lower() not in ["камень", "ножницы", "бумага"]:
        print("Неверный ввод варинта")
        choice_people = input("Повторите выбор: ")
    return choice_people


def compute_game_result(choice_people: str, choice_machine: str):
    if choice_people == choice_machine:
        print("Ничья")
        return (0, 0)
    elif (choice_people == "ножницы" and choice_machine == "бумага") or \
         (choice_people == "камень" and choice_machine == "ножницы") or \
         (choice_people == "бумага" and choice_machine == "камень"):
        print("Вы победили")
        return (1, 0)
    else:
        print("Вы проиграли")
        return (0, 1)


def print_result(wins_mashine: int, wins_people: int):
    print(f"Счет: Машина - {wins_mashine}, Вы - {wins_people}")

    if rounds_count == round + 1:
        if wins_mashine == wins_people:
            print("Результат игры ----------> Победила дружба")
            exit()
        elif wins_mashine > wins_people:
            print("Результат игры ----------> Вы програли(")
            exit()
        else:
            print("Результат игры ----------> Вы победили! )")
            exit()


rounds_count = int(input("Введите колличество раундов: "))

variant = ["Камень", "Ножницы", "Бумага"]

mashine = [0, 1, 2]

wins_mashine = 0
wins_people = 0

for round in range(rounds_count):
    choice_people = select_variant()
    choice_mashine = variant[random.choice(mashine)].lower()

    print(f"Вы выбрали - {choice_people}")
    print(f"Машина выбрала - {choice_mashine}")

    user_mod, computer_mod = compute_game_result(choice_people, choice_mashine)
    wins_people += user_mod
    wins_mashine += computer_mod

    print_result(wins_mashine, wins_people)
