category = str(input("Выберите категорию: \"напиток\", \"суп\", \"десерт\": "))

dish = ""

match category:
    case "напиток":
        dish = str(input("Выберите напиток: \"чай\", \"кофе\", \"сок\": "))
    case "суп":
        dish = str(input("Выберите суп: \"борщ\", \"щи\", \"суп-пюре\": "))
    case "десерт":
        dish = str(input("Выберите десерт: \"торт\", \"мороженое\", \"фрукты\": "))
    case _:
        print("Такой категории нет")

match dish:
    case "чай":
        print(1)
    case "кофе":
        print(2)
    case "сок":
        print(3)
    case "борщ":
        print(4)
    case "щи":
        print(5)
    case "суп-пюре":
        print(6)
    case "торт":
        print(7)
    case "мороженое":
        print(8)
    case "фрукты":
        print(9)
    case _:
        print("Такого блюда нет")
