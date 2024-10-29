"""Homework 7.1."""


SEPARATOR = ('=' * 75)
# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та виправити або доповнити.
"""


def multiplication_table(number):
    """
    Print the multiplication table for the number.

    Args:
        number (int): integer
    """
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number or multiplier > number:
        # second solution only (while multiplier:)
        # it will be always True before the break
        result = (number * multiplier)
        # десь тут помилка, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(f'{number} x {multiplier} = {result}')

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15
print(SEPARATOR)

# task 2
"""Написати функцію, яка обчислює суму двох чисел."""


def sum_of_two(a, b):
    """
    Sum of two numbers.

    Args:
        a (int): first number.
        b (int): second number.
    Returns:
        int: sum.
    """
    return a + b


# task 3
"""Написати функцію, яка розрахує середнє арифметичне списку чисел."""


def arithmetic_mean(lst):
    """
    Calculate arithmetic mean of the numbers list.

    Args:
        lst (list): list of numbers.
    Returns:
        float: returns arithmetic mean.
    """
    return (sum(lst) / len(lst))


# task 4
"""Написати функцію, яка приймає рядок та повертає його
    у зворотному порядку."""


def reverse_string(txt):
    """
    Reverse string.

    Args:
        txt (str): some string.
    Returns:
        str: reversed string.
    """
    return txt[::-1]


# task 5
"""Написати функцію, яка приймає список слів та
    повертає найдовше слово у списку."""


def longest_word(lst):
    """
    Find and return longest word in the list.

    Args:
        lst (list): list with words.
    Returns:
        str: longest word in the list.
    """
    return max(lst, key=lambda word: len(word))


# task 6
"""  Написати функцію, яка приймає два рядки та
повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка,
та -1, якщо другий рядок не є підрядком першого рядка."""


def find_substring(str1, str2):
    """
    Check if substring in string.

    Args:
        str1 (str): main string.
        str2 (str): substring.
    Returns:
        int: substring index or -1
    """
    if str2 in str1:
        return str1.index(str2)
    return -1


str1 = 'Hello, world!'
str2 = 'world'
print(find_substring(str1, str2))  # поверне 7
print(SEPARATOR)

str1 = 'The quick brown fox jumps over the lazy dog'
str2 = 'cat'
print(find_substring(str1, str2))  # поверне -1
print(SEPARATOR)

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7 from HW 6.3


def list_of_strings(lst):
    """
    Filter of the no string elements.

    Args:
        lst (list): list of data.
    Returns:
        list: with strings only.
    """
    return [item for item in lst if isinstance(item, str)]


# task 8 from HW6.4
def even_nums_sum(lst):
    """
    Filter even numbers in list and sum them.

    Args:
        lst (list): list of numbers.
    Returns:
        int: sum of even numbers
    """
    return sum([num for num in lst if num % 2 == 0])


# task 9 from HW1
def perimetery(a, b, c, d):
    """
    Sum of the figure sides.

    Args:
        a (int): first num.
        b (int): second num.
        c (int): third num.
        d (int): forth num.
    Returns:
        int: perimetery of the figure.
    """
    return (a + b + c + d)


# task 10 from HW5.2, this one can be improved
def list_elem_pos_change(lst, old_index, new_index):
    """
    Change elements position by indexes.

    Args:
        lst (list): list with elements.
        old_index (int): previous index position.
        new_index (int): new index position.
    Returns:
        list: list of elements with the new indexes.
    """
    element = lst.pop(old_index)
    lst.insert(new_index, element)
    return lst
