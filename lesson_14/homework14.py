"""Homework 14.1 Student object."""


class Student:
    """
    A class to represent a student.

    Attributes:
        name (str): The student's first name.
        surname (str): The student's last name.
        average_point (float): The student's average grade.
    """

    # Use the constructor __init__ here
    def __init__(self, name, surname, average_grade):
        """Initialize a new student with parameters."""
        self.name = name
        self.surname = surname
        self.average_grade = average_grade

    def average_grade_update(self, new_ave_grade):
        """Update the student's average grade to the new value."""
        self.average_grade = new_ave_grade


my_student = Student('Roberto', 'Firmino', 10)
print(f'Init average grade: {my_student.average_grade}')
my_student.average_grade_update(11)
print(f'New average grade: {my_student.average_grade}')
