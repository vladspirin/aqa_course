"""Test cases for login event logging function."""


import logging

import pytest

from homework10 import log_event

# Log file name
LOG_FILE = 'login_system.log'

# Setup logger for the test module
_log = logging.getLogger('log_event')
_log.setLevel(logging.INFO)

# Clear previous handlers if exists
if _log.hasHandlers():
    _log.handlers.clear()

# Create a new handler (write to file)
# Added levelname to see correct output
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(
    logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'),
)
_log.addHandler(file_handler)


class TestLogEvent:
    """
    A class for testing the log_event function.

    This class is responsible for logging events in the login system.
    All tests verify different login statuses
    (successful, failed, expired, etc.) and log the results into a file.

    Input data for the tests:
    - username: 'test_user#'
    - status: 'success', 'failed', 'expired', or an invalid status

    Expected result:
    - Logs should contain correct messages with appropriate logging levels
    (info, warning, error).
    """

    # First 4 TCs are similar, all about status
    # Test Case N1
    def test_log_event_success(*args):
        """Checking the correct logging of the successful login event."""
        # Call the function under test
        log_event('test_user', 'success')

        # Read log-file. Error handling added if no file
        try:
            with open(LOG_FILE, 'r') as lf:
                log_txt = lf.read()
        except FileNotFoundError:
            pytest.fail('Log file was not found.')
        # check if success == INFO level
        if 'INFO' not in log_txt:
            pytest.fail("Log output does not contain 'INFO'")

    # Test Case N2
    def test_log_event_expired(*args):
        """
        Check expired system login in log events.

        Expected result:
        'Login event - Username: test_user2, Status: expired' in LOG_FILE
        """
        # Call the function under test
        log_event('test_user2', 'expired')

        # Read log-file. Error handling added if no file
        try:
            with open(LOG_FILE, 'r') as lf:
                log_txt = lf.read()
        except FileNotFoundError:
            pytest.fail('Log file was not found.')
        # check if expired == WARNING level
        if 'WARNING' not in log_txt:
            pytest.fail("Log output does not contain 'WARNING'")

    # Test Case N3
    def test_log_event_failed(*args):
        """
        Check if system login is failed in log events.

        Expected result:
        'Login event - Username: test_user3, Status: failed' in log_file
        """
        # Call the function under test
        log_event('test_user3', 'failed')

        # Read log-file. Error handling added if no file
        try:
            with open(LOG_FILE, 'r') as lf:
                log_txt = lf.read()
        except FileNotFoundError:
            pytest.fail('Log file was not found.')
        # check if failed == ERROR level
        if 'ERROR' not in log_txt:
            pytest.fail("Log output does not contain 'ERROR'")

    # Test Case N4 - Negative scenario
    def test_log_event_invalid_status(*args):
        """Test logging with an invalid status parameter."""
        # Call the function under test
        log_event('test_user4', 'unknown_status')

        # Check if error msg was added and failed == ERROR level
        with open(LOG_FILE, 'r') as lf:
            log_txt = lf.read()
        if 'ERROR' not in log_txt:
            pytest.fail("Log output does not contain 'ERROR'")

    # Test Case N5 - Negative scenario
    def test_log_event_empty_param(*args):
        """Test logging when parameters are missing."""
        # case 1: no parameters
        with pytest.raises(TypeError):
            log_event()

        # case 2: one parameter is present
        with pytest.raises(TypeError):
            log_event('test_user4')
