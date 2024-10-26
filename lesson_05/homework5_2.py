"""This is Homework 5.2."""

import logging
from operator import itemgetter

SEPARATOR = '=' * 75
# Configure logging
logging.basicConfig(level=logging.INFO, format='')
_log = logging.getLogger(__name__)
# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix'),
]

# Task 1
# Copy original list - Just in case
working_list = people_records[:]
# Updating the list copy with new data
new_data = ('Eve', 'Green', 31, 'QA Engineer', 'Totonto')
working_list.insert(0, new_data)
_log.info(working_list)
_log.info(SEPARATOR)

# Task 2
working_list[1], working_list[5] = working_list[5], working_list[1]
_log.info(working_list)
_log.info(SEPARATOR)

# Task 3
# Filtering list by required indexes
tmp_list = list(itemgetter(6, 10, 13)(working_list))
# Check if person age is >= 30
result = all(person_age[2] >= 30 for person_age in tmp_list)
_log.info(f'Is people in list position 6, 10, 13, have an age >=30? {result}')
_log.info(SEPARATOR)
