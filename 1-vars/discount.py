priceStr = input("Введите цену товара: ")
descStr = input("Какой процент скидки: ")

price = int(priceStr)
desc = int(descStr)

result = price - price * (desc / 100)

print(result)