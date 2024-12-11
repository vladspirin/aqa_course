"""
Homework 18.1 A decorator for every iterator and generator.

Task 'Decorators':
- Write a decorator that logs the arguments and results of the called function.
- Create a decorator that intercepts and handles exceptions
occurring during the function execution.
"""

import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

_log = logging.getLogger(__name__)


# case 1
def log_args_and_res_deco(func):
    """Log the arguments passed to the function."""
    def wrapper(*args, **kwargs):
        """Log the arguments passed to the decorated function."""
        _log.info(f'Arguments: {args}, {kwargs}')
        result = func(*args, **kwargs)
        _log.info(f'Result: {result}')
    return wrapper


# case 2
def handle_exceptions(func):
    """Catches and handles exceptions raised during the execution."""
    def wrapper(*args, **kwargs):
        """Handle any exceptions raised during execution, logs the error."""
        try:
            return func(*args, **kwargs)
        except Exception as exc_err:
            _log.error(f'Error occured: {exc_err}')
            return None  # return default value
    return wrapper


@log_args_and_res_deco
def calculate_power_of_num(num, x):
    """Calculate the result of a number raised to the power of x."""
    return num ** x


@handle_exceptions
def calculate_devision(a, b):
    """Perform division of two numbers."""
    return a / b


if __name__ == '__main__':
    calculate_power_of_num(6, 2)
    calculate_devision(8, 0)
