import random

rounds_count = int(input("Введите колличество раундов: "))

variant = ["Камень", "Ножницы", "Бумага"]

mashine = [0, 1, 2]

wins_mashine = 0
wins_people = 0

for round in range(rounds_count):

    choice_people = input("Введите камень, ножницы или бумага: ").lower()
    choice_mashine = variant[random.choice(mashine)].lower()

    while choice_people.lower() not in ["камень", "ножницы", "бумага"]:
        print("Неверный ввод варинта")
        choice_people = input("Повторите выбор: ")

    print(f"Вы выбрали - {choice_people}")
    print(f"Машина выбрала - {choice_mashine}")

    if choice_people == choice_mashine:
        print("Ничья")
        wins_mashine += 1
        wins_people += 1
    elif choice_people == "ножницы" and choice_mashine == "бумага":
        print("Вы победили")
        wins_people += 1
    elif choice_people == "ножницы" and choice_mashine == "камень":
        print("Вы проиграли")
        wins_mashine += 1
    elif choice_people == "камень" and choice_mashine == "ножницы":
        print("Вы победили")
        wins_people += 1
    elif choice_people == "камень" and choice_mashine == "бумага":
        print("Вы проиграли")
        wins_mashine += 1
    elif choice_people == "бумага" and choice_mashine == "камень":
        print("Вы победили")
        wins_people += 1
    elif choice_people == "бумага" and choice_mashine == "ножницы":
        print("Вы проиграли")
        wins_mashine += 1

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
