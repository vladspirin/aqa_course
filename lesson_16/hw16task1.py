"""Homework 16.1. Diamond inheritance and Geometric problem.

Task 1:
Create a class Employee that has attributes name and salary.
Then, create two classes, Manager and Developer,
which inherit from Employee.
The Manager class should have an additional attribute department,
while the Developer class should have an attribute programming_language.

Now, create a class TeamLead,
which inherits from both Manager and Developer.
This class represents the leader of a development team.
The TeamLead class should have all the attributes of Manager
(name, salary, department), as well as an attribute team_size,
which indicates the number of developers in the team managed by the leader.

Write a test that checks the presence of attributes
from both Manager and Developer in the TeamLead class.
"""


class Employee:
    """The class creates an Employee."""

    def __init__(self, name, salary):
        """Initialize an Employee role with parameters."""
        self.name = name
        self.salary = salary


class Manager(Employee):
    """The class creates a Manager."""

    def __init__(self, name, salary, department):
        """Initialize a Magager role with parameters."""
        super().__init__(name, salary)
        self.department = department


class Developer(Employee):
    """The class creates a Developer."""

    def __init__(self, name, salary, programming_language):
        """Initialize a Developer role with parameters."""
        super().__init__(name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    """The class creates a TeamLead."""

    def __init__(self, name, salary, department, team_size):
        """Initialize a TeamLead role with parameters."""
        super().__init__(name, salary, department)
        self.team_size = team_size


employee = Employee()
manager = Manager()
developer = Developer()
team_lead = TeamLead()
