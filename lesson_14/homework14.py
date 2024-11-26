"""Homework 14.1 Student object.

Create a "Student" class with the attributes "first name",
"last name", "age" and "GPA".
Create an object for this class by introducing the student.
Then, add a method to the "Student" class that allows you
to change the student's GPA.
Display the student's information and change their GPA.
"""


class Student:
    """
    A class to represent a student.

    Attributes:
        name (str): The student's first name.
        surname (str): The student's last name.
        average_point (float): The student's average grade.
    """

    # Use the constructor __init__ here
    def __init__(self, name, surname, age, average_grade):
        """Initialize a new student with parameters."""
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def average_grade_update(self, new_ave_grade):
        """Update the student's average grade to the new value."""
        self.average_grade = new_ave_grade


my_student = Student('Roberto', 'Firmino', 16, 10)
print(f'Init average grade: {my_student.average_grade}')
my_student.average_grade_update(11)
print(f'New average grade: {my_student.average_grade}')
