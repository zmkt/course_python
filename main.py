visitors_day1 = [101, 102, 103, 101, 104, 102, 105, 101]
visitors_day2 = [101, 108, 100, 101, 105, 107]

# 1 задание

all_visits_day1 = len(visitors_day1)
all_visits_day2 = len(visitors_day2)

unic_visits_day1 = set(visitors_day1)
unic_visits_day2 = set(visitors_day2)

print(f"Всего визитов в 1 день: {all_visits_day1}")
print(f"Всего визитов во 2 день: {all_visits_day2}")
print(f"Уникальные визиты в 1 день: {unic_visits_day1}")
print(f"Уникальные визиты во 2 день: {unic_visits_day2}")


# 2 задание

two_day = unic_visits_day1.intersection(unic_visits_day2)

print(f"Посетил 2 дня: {two_day}")

# 3 задание

one_day_visit = set(visitors_day1)
print(f"Посетил только в 1 день: {one_day_visit}")

# 4 задание

two_day_visit = set(visitors_day2)
print(f"Посетил только во 2 день: {two_day_visit}")

# 4 задание

one_visits = unic_visits_day1.symmetric_difference(unic_visits_day2)
print(f"Кто был 1 раз: {one_visits}")
