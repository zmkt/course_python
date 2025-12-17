import random
import string
from typing import Dict

passwords: Dict[str, str] = {}


def generate_password(length: int = 8, use_symbols: bool = True):
    if length < 3:
        return ""
    letters = string.ascii_letters
    digint = string.digits
    symbols = "!@#$%&*?"

    pool = letters + digint + (symbols if use_symbols else "")

    password_chars: list[str] = []

    while len(password_chars) < length:
        password_chars.append(random.choice(pool))

    return "".join(password_chars)
# print(generate_password())
# print(generate_password(10, False))
# print(generate_password(10))


def show_passwords():
    print(passwords)


def add_password():
    name_password = input("Введитель название: ")
    if name_password in passwords:
        print("Пароль с таким названием уже есть!")
        return
    passwords[name_password] = generate_password(10, True)
    print("Успешно добавлено!")
    print(passwords)


def delete_password():
    name_password = input("Введитель название: ")
    if name_password not in passwords:
        print("Пароля с таким названием нет!")
        return
    del passwords[name_password]
    print("Успешно удалено!")
    print(passwords)


def update_password():
    name_password = input("Введитель название: ")
    if name_password not in passwords:
        print("Пароля с таким названием нет!")
        return
    passwords[name_password] = generate_password(10, True)
    print("Успешно изменено!")
    print(passwords)


def exit_show_menu():
    exit()


def show_menu():

    print("1. Показать пароли")
    print("2. Добавить пароль")
    print("3. Удалить пароль")
    print("4. Обновить пароль")
    print("5. Выход")

    user_select = input("Ваш выбор: (1, 2, 3, 4, 5): ")

    match user_select:
        case "1":
            show_passwords()
        case "2":
            add_password()
        case "3":
            delete_password()
        case "4":
            update_password()
        case "5":
            exit_show_menu()
        case _:
            print("Несоответствующий выбор")


while True:
    show_menu()
