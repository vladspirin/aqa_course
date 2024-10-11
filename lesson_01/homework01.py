"""
Summary: Lesson 1-2.

Description:
Task 1-6:
Fix errors and mistakes
Task 7-10:
Step by step simple math for kids.
"""

# task 01 == Виправте синтаксичні помилки
print('Hello', end=' ')
print('world!')

# task 02 == Виправте синтаксичні помилки
hello = 'Hello'
world = 'world'
if True:
    print(f'{hello} {world}!')

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in 'Hello world!':
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук

apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
storona1 = 1
storona2 = 2
storona3 = 3
storona4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача

perimetery = storona1 + storona2 + storona3 + storona4
print(perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""


apple_tree = 4
print(f'Посаджено яблунь: {apple_tree}')
pear_tree = apple_tree + 5
print(f'Посаджено груш на 5 більше, тож додаємо ще 5: {pear_tree}')
plum_tree = apple_tree - 2
print(f'Посаджено слив на 2 менше, віднімаємо 2 та маємо: {plum_tree}')
result_in_garden = apple_tree + pear_tree + plum_tree
print(f'Сумуємо результати та маємо кількість дерев: {result_in_garden}')

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""


until_noon_temperature = 5
print(f'Температура до обіду на 5 вище за 0, маємо: {until_noon_temperature}')
afternoon_temperature = until_noon_temperature - 10
print(f'Віднімаємо з попередньої температури 10: {afternoon_temperature}')
evening_temperature = afternoon_temperature + 4
print(f'До післяобіднього результату плюс 4, та маємо: {evening_temperature}')

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""


boys = 24
print(f'Хлопчиків: {boys}')
girls = int(boys / 2)
print(f'Ділемо кількість хлопців на 2, та маємо: {girls}')
children_all = boys + girls
print(f'Додаємо кількість хлопців до кількості дівчат: {children_all}')
children_today = children_all - 3
print(f'Віднімаємо від заг кількості дітей, 3х відсутніх: {children_today}')

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""

txt = "З'ясувати скільки коштує кожний примірник. Примірник, це 1 шт."
print(txt)
book1 = 8
print(f'Примірник першої книги: {book1} грн')
book2 = book1 + 2
print(f'Додаємо до вартості першої 2: {book2} грн')
book3 = int((book1 + book2) / 2)
txt1 = """Щоб дізнатися скільки коштує примірник третьої книги,
треба спочатку додати ціну першох до другої,
а далі, щоб побачити половину вартості перших двох разом, розлілити їх на 2."""
print(f'{txt1} Результат: {book3} грн')
txt2 = """Тепер знаючи скільки коштує кожен примірник окремо,
можемо рахувати фінальний результат."""
txt3 = 'Сумуємо ціни за примірник 1-ї, 2-ї, та 3-ї книги відповідно треба:'
result = book1 + book2 + book3
print(f'{txt2} {txt3} {result} грн, щоб купити 3 книги')
