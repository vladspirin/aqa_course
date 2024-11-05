"""
Homework 9.1 Let's test something.

Task:
Choose from 3 to 5 different homework assignments.
Convert them into functions (if necessary).
Create a file named homeworks.py in a folder
where you will place your functions from the homework and
cover them with no less than 10 tests
(this is the total number for all the homework).
Import and the tests themselves
should be placed in a separate file - test_homeworks08.py.
The evaluation will depend on both the quality of the tests and
the amount of test coverage.
A minimum of 10 points requires one properly designed positive test for a function.
"""

def arithmetic_mean(lst):
    """
    Calculate arithmetic mean of the numbers list.

    Args:
        lst (list): list of numbers.
    Returns:
        float: returns arithmetic mean.
    """
    return (sum(lst) / len(lst))


def longest_word(lst):
    """
    Find and return longest word in the list.

    Args:
        lst (list): list with words.
    Returns:
        str: longest word in the list.
    """
    return max(lst, key=lambda word: len(word))


def even_nums_sum(lst):
    """
    Filter even numbers in list and sum them.

    Args:
        lst (list): list of numbers.
    Returns:
        int: sum of even numbers
    """
    return sum([num for num in lst if num % 2 == 0])


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
