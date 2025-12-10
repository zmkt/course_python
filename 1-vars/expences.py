foodStr = input("Введите расходы на еду: ")
transportationStr = input("Введите расходы на транспорт: ")
entertainmentStr = input("Введите расходы на развлечения: ")

food = int(foodStr)
transportation = int(transportationStr)
entertainment = int(entertainmentStr)

result = food + transportation + entertainment

print(result)