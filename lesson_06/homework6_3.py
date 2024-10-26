"""This is homework 6.3."""


import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='')
_log = logging.getLogger(__name__)

lst1 = [
    '1', '2', 3, True, 'False',
    5, '6', 7, 8, 'Python',
    9, 0, 'Lorem Ipsum']
# Longest variant
lst2 = []
for i in lst1:
    if isinstance(i, str):
        lst2.append(i)
_log.info(lst2)
# a bit advanced variant
lst3 = [i for i in lst1 if isinstance(i, str)]
_log.info(lst3)
