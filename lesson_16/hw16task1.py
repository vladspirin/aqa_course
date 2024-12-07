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

SEP = '=' * 50


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
        self.department = department
        super().__init__(name, salary)


class Developer(Employee):
    """The class creates a Developer."""

    def __init__(self, name, salary, programming_language=None):
        """Initialize a Developer role with parameters."""
        self.programming_language = programming_language
        super().__init__(name, salary)


class TeamLead(Manager, Developer):
    """The class creates a TeamLead."""

    def __init__(self, name, salary, department, team_size):
        """Initialize a TeamLead role with parameters."""
        self.team_size = team_size
        super().__init__(name, salary, department)


if __name__ == '__main__':
    employee = Employee('Bob', 2000)
    print(employee.__dict__)
    print(SEP)

    manager = Manager('Marta', 9000, 'Engineering')
    print(manager.__dict__)
    print(SEP)

    developer = Developer('Robert', 6000, 'Python')
    print(developer.__dict__)
    print(SEP)

    team_lead = TeamLead('Eve', 7000, 'Engineering', 6)
    print(team_lead.__dict__)
