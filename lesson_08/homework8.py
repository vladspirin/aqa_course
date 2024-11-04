"""
Homework 8.1 Catch incorrect symbols in the list of numbers.

Task:
Create an array of strings, each consisting of numbers separated by commas.
For example:
['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']
For each element in the list, print the sum of all the numbers.
(Create a new function for this.)
If there are any characters that are not numbers (as in "qwerty1,2,3"),
you need to catch an exception and print “I can’t do that!”
Use the try/except block to handle any non-numeric characters in the list.
For this example, the correct output will be:
10, 60, "I can't do that!"
"""


import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='')
_log = logging.getLogger(__name__)

req_lst = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']
# create a copy of the list
lst_copy = req_lst[:]


# split elements by comma separator
def separate_elements(lst):
    """
    Separate elements in the list.

    Args:
        lst (list): list with string elements.
    Returns:
        list: return list with sublists.
    """
    return [elem.split(',') for elem in lst]


# convert string digits to int
def convert_str_to_int(lst):
    """
    Convert string nums to int.

    Args:
        lst (list): list with string digit elements.
    Returns:
        list: return list with int.
    """
    return [int(num) for num in lst]


# put try/except to func for better scalability
def convert_and_replace(lst):
    """
    Convert list with different type of elements.

    Args:
        lst (list): list with string elements.
    Returns:
        list: return list with converted replaced element(s).
    """
    for item, sublist in enumerate(lst):
        try:
            # sum only sublists where all int
            lst[item] = sum(convert_str_to_int(sublist))
        except ValueError:
            # in case of ValueError replace to the text
            lst[item] = "I can't do that!"
        except Exception as g_exc:
            _log.info('Global error occurred:')
            _log.info(g_exc)
    return lst


result = convert_and_replace(separate_elements(lst_copy))

# Expected result
value1, value2, value3 = result
_log.info(f'{value1}, {value2}, {value3}')
