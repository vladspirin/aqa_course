"""
Homework 18.1 A decorator for every iterator and generator.

Task 'Generators':
- Write a generator that returns a sequence of even numbers from 0 to N.
- Create a generator that produces the Fibonacci sequence
up to a certain number N.
"""


def generate_even_nums(n: int):
    """Generate even numbers util N."""
    for num in range(0, n + 1):
        if num % 2 == 0:
            yield num


def generate_fibonacci_nums(n: int):
    """Generate Fibonacci sequence until N."""
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    # task 1 output
    print('Even nums: (case 1)')
    gen1 = generate_even_nums(12)
    for i in gen1:
        print(i)
    print('=' * 25)

    # task 2 output
    print('Fibonacci nums: ')
    for i in generate_fibonacci_nums(12):
        print(i)
