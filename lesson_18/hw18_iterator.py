"""
Homework 18.1 A decorator for every iterator and generator.

Task 'Iterators':
- Implement an iterator for reversing the elements of a list.
- Write an iterator that returns all even numbers in the range from 0 to N.
"""


class ReverseListIterator:
    """The class creates a reverse list iterator."""

    def __init__(self, lst: list):
        """Initialize a reverse list iterator with parameters."""
        self.lst = lst
        self.indx = len(lst) - 1

    def __iter__(self):
      """Return iterator object."""
      return self

    def __next__(self):
        """Return the next item in the iteration."""
        # stop itertion in case index less than 0
        if self.indx < 0:
            raise StopIteration
        result = self.lst[self.indx]
        self.indx -= 1
        return result


class EvenNumsIterator:
    """The class creates an even numbers iterator."""

    def __init__(self, n):
        """Initialize an even numbers iterator with parameters."""
        self.n = n
        self.current_val = 0  # starting value

    def __iter__(self):
        """Return iterator object."""
        return self

    def __next__(self):
        """Return the next even number in the iteration."""
        while self.current_val <= self.n:
            if self.current_val % 2 == 0:
                val = self.current_val
                self.current_val += 1
                return val
            self.current_val += 1
        raise StopIteration


data = ['Apple', 'Google', 'Amazon', 'IBM', 'Microsoft', 'OpenAI']

if __name__ == '__main__':
    # reverse
    reversed_iter = ReverseListIterator(data)
    for item in reversed_iter:
        print(item)

    print('=' * 50)
    # even nums
    even_iter = EvenNumsIterator(12)
    for num in even_iter:
        print(num)
