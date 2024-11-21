"""
Your team and you are developing a login system for a web application.

You need to implement tests for the function
that logs events in the login system.
Given the function, write a set of tests for it.
"""

import logging


def log_event(username: str, status: str):
    """
    Log a login event.

    username: The username that is logging in.

    status: The status of the login event:

    * success - successful, logged at the info level
    * expired - password is expired and needs to be changed,
                logged at the warning level
    * failed - password is incorrect, logged at the error level
    """
    log_message = f'Login event - Username: {username}, Status: {status}'

    # Create and setup logger
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
    )
    logger = logging.getLogger('log_event')

    # Event logging
    if status == 'success':
        logger.info(log_message)
    elif status == 'expired':
        logger.warning(log_message)
    else:
        logger.error(log_message)
