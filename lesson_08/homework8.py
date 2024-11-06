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


# Now, only one function for split and convert to int
def split_and_convert(lst):
    """
    Split elements by comma and convert to integers.

    Args:
        lst (list): List of strings.
    Returns:
        list: List of sublists with converted integers or replacement message.
    """
    result = []
    for elem in lst:
        try:
            # Added strip() in case of unpredictable spaces
            result.append([int(num.strip()) for num in elem.split(',')])
        except ValueError:
            result.append("I can't do that!")  # Add msg if unable to convert
    return result


def convert_and_replace(lst):
    """
    Process a list by summing sublists or replacing with a message.

    Args:
        lst (list): List of sublists or messages.
    Returns:
        list: List with either sums of integers or replacement message.
    """
    for indx, sublist in enumerate(lst):
        if isinstance(sublist, list):  # Check if sublist is list
            try:
                lst[indx] = sum(sublist)  # Sum if list with int
            except TypeError:
                lst[indx] = "I can't do that!"
    return lst


# My data
req_lst = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']
# Call the functions
result = convert_and_replace(split_and_convert(req_lst))

# Additional check if more than 3 list elements
if len(result) == 3:
    value1, value2, value3 = result
    _log.info(f'{value1}, {value2}, {value3}')
else:
    _log.info(f'Unexpected result length: {result}')
