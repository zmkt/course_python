import random

secret_number = random.randint(0, 99)

number = int(input("Введите число: "))

while secret_number != number:
    if secret_number > number:
        print("Больше")
    elif secret_number < number:
        print("Меньше")
    number = int(input("Введите число: "))

print("Угадал")
