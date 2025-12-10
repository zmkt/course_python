role = input("Введите роль: ")

if role == "admin":
    print("Админ")
elif role == "manager":
    print("Менеджер")
elif role == "seo":
    print("SEO специалист")
else:
    print("Пользователь")

match role:
    case "admin":
        print("Админ")
    case "manager":
        print("Менеджер")
    case "seo":
        print("SEO специалист")
    case _:
        print("Пользователь")
