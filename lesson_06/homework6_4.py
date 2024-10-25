"""Homework 6.4."""


import logging

SEPARATOR = '=' * 75
# Configure logging
logging.basicConfig(level=logging.INFO, format='')
_log = logging.getLogger(__name__)

# I know how to do this in one line but I'll use info from lesson
# 1. Generate the list with numbers
list_with_nums = []
for i in range(50):
    list_with_nums.append(i)
_log.info(list_with_nums)
_log.info(SEPARATOR)
# 2. Find even numbers and calculate sum
even_num_list = []
for i in list_with_nums:
    if i % 2 == 0:
        even_num_list.append(i)
_log.info(sum(even_num_list))
