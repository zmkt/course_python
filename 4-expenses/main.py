number = input("Введите число: ")

rub, _, cop, _ = number.strip().split(" ")
rub = float(rub)
cop = int(cop) / 100
total = rub + cop

print(f"{total:.2f} ₽")
