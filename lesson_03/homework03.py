"""This is Homework 3.1."""


# task 01 == Розділіть змінну alice_in_wonderland так,
# щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
alice_in_wonderland = (
    'Would you tell me, please, which way I ought to go from here?\n'
    'That depends a good deal on where you want to get to, said the Cat.\n'
    "I don't much care where —— said Alice.\n"
    "Then it doesn't matter which way you go, said the Cat.\n"
    '—— so long as I get somewhere, Alice added as an explanation.\n'
    "Oh, you're sure to do that, said the Cat, if you only walk long enough."
)
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_sq = 436_402
azov_sea_sq = 37_800
# just need to sum two sq
main_sq = black_sea_sq + azov_sea_sq
print(main_sq)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

all_warehouses = 375_291
# find number of all goods in warehouse N3
warehouse3 = 375_291 - 250_449
# find number of all goods in warehouse N1
warehouse1 = 375_291 - 222_950
# find number of all goods in warehouse N2
warehouse2 = all_warehouses - (warehouse3 + warehouse1)
print(f'Warehouse N1: {warehouse1}')
print(f'Warehouse N2: {warehouse2}')
print(f'Warehouse N3: {warehouse3}')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

payment_per_m = 1179
# payment timeperiod = one year and half
timeperiod_in_m = 18
# pc cost = 1m payment * all m
pc_cost = payment_per_m * timeperiod_in_m
print(pc_cost)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

print(8019 % 8)
print(9907 % 9)
print(2789 % 5)
print(7248 % 6)
print(7128 % 5)
print(19224 % 9)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
# goods price
big_pizza = 274
middle_pizza = 218
juice = 35
cake = 350
water = 21
# sum all
all_needed_money = ((big_pizza * 4) + (middle_pizza * 2) + (
    juice * 4) + cake + (water * 3))
print(f'Sum: {all_needed_money} UAH')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo = 232
one_page = 8
pages_all = int(photo / 8)
print(f'Pages: {pages_all}')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
# gas we need per 1 km
gas_per_km = 9 / 100
print(gas_per_km)
tank = 48
# 1) gas we need for distance between Kharkiv and Budapest
gas_all_distance = distance * gas_per_km
print(f'Gas for all diatance: {gas_all_distance}')
# 2) times to stop in gas station
gas_station = gas_all_distance // tank
print(f'Times to stop in gas station: {gas_station}')
