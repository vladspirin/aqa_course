"""Homework9.

We have two lists with equal or different size
ex. l1=[1,3,5,7]  l2=[1,4,5]

Task:
create list that will store such values
list_target = [(1,1), (3,4), (5,5), (7,0)]
zero (0) is our default value that we set
if no such element by index was found in certain list.
code should work and vise versa
ex. l1=[1,4,5] l2=[1,3,5,7] input data should produce
list_target = [(1,1), (4,3), (5,5), (0,7)]
your solution should include comprehension constructions

Advices:
set of (list1 indexes union list2 indexes) could be
helpful to get larger indexes scope ( or use if-else)
dict as you remember has default value if key was not found d1.get(key, 0)
"""

import logging
from itertools import zip_longest

# Configure logging
logging.basicConfig(level=logging.INFO, format='')
_log = logging.getLogger(__name__)


# my shortest solution using itertools
def zip_and_fill(lst1, lst2):
    """
    Combine two lists by pairing their elements using zip_longest.

    Filling empty spots with zeros.
    """
    return list(zip_longest(lst1, lst2, fillvalue=0))


l1 = [2, 4, 6, 8, 10]
l2 = [1, 2, 3]
expected_result1 = zip_and_fill(l1, l2)
expected_result2 = zip_and_fill(l2, l1)
_log.info(expected_result1)
_log.info(expected_result2)
