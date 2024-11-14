"""Test cases for login event logging function."""


import logging
import os

import pytest

from homework10 import log_event


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
        # Clear log-file if exists in folder. Use os.path to find file
        if os.path.exists(log_file):
            with open(log_file, 'w'):
                pass

        # Setup logger for the TC
        _log = logging.getLogger('log_event')
        _log.setLevel(logging.INFO)

        # Clear previous handlers if exists
        if _log.hasHandlers():
            _log.handlers.clear()

        # Create a new handler (write to file)
        # Added levelname to see correct output
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'),
        )
        _log.addHandler(file_handler)

        # Call the function under test
        log_event('test_user', 'success')

        # Main logic here. Read log-file. Error handling added if no file
        try:
            with open(log_file, 'r') as lf:
                log_txt = lf.read()
        except FileNotFoundError:
            raise AssertionError('Log file was not found.')
        # check if success == INFO level
        if 'INFO' not in log_txt:
            raise AssertionError("Log output does not contain 'INFO'")

    # Test Case N2
    def test_log_event_expired(*args):
        """
        Check expired system login in log events.

        Expected result:
        'Login event - Username: test_user2, Status: expired' in log_file
        """
        # Clear log-file if exists in folder. Use os.path to find file
        if os.path.exists(log_file):
            with open(log_file, 'w'):
                pass

        # Setup logger for the TC
        _log = logging.getLogger('log_event')
        _log.setLevel(logging.INFO)

        # Clear previous handlers if exists
        if _log.hasHandlers():
            _log.handlers.clear()

        # Create a new handler (write to file)
        # Added levelname to see correct output
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'),
        )
        _log.addHandler(file_handler)

        # Call the function under test
        log_event('test_user2', 'expired')

        # Main logic here. Read log-file. Error handling added if no file
        try:
            with open(log_file, 'r') as lf:
                log_txt = lf.read()
        except FileNotFoundError:
            raise AssertionError('Log file was not found.')
        # check if expired == WARNING level
        if 'WARNING' not in log_txt:
            raise AssertionError("Log output does not contain 'WARNING'")

    # Test Case N3
    def test_log_event_failed(*args):
        """
        Check if system login is failed in log events.

        Expected result:
        'Login event - Username: test_user3, Status: failed' in log_file
        """
        # Clear log-file if exists in folder. Use os.path to find file
        if os.path.exists(log_file):
            with open(log_file, 'w'):
                pass

        # Setup logger for the TC
        _log = logging.getLogger('log_event')
        _log.setLevel(logging.INFO)

        # Clear previous handlers if exists
        if _log.hasHandlers():
            _log.handlers.clear()

        # Create a new handler (write to file)
        # Added levelname to see correct output
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'),
        )
        _log.addHandler(file_handler)

        # Call the function under test
        log_event('test_user3', 'failed')

        # Main logic here. Read log-file. Error handling added if no file
        try:
            with open(log_file, 'r') as lf:
                log_txt = lf.read()
        except FileNotFoundError:
            raise AssertionError('Log file was not found.')
        # check if failed == ERROR level
        if 'ERROR' not in log_txt:
            raise AssertionError("Log output does not contain 'ERROR'")

    # Test Case N4 - Negative scenario
    def test_log_event_invalid_status(*args):
        """Test logging with an invalid status parameter."""
        # Clear log-file if exists in folder. Use os.path to find file
        if os.path.exists(log_file):
            with open(log_file, 'w'):
                pass

        # Setup logger for the TC
        _log = logging.getLogger('log_event')
        _log.setLevel(logging.INFO)

        # Clear previous handlers if exists
        if _log.hasHandlers():
            _log.handlers.clear()

        # Create a new handler (write to file)
        # Added levelname to see correct output
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'),
        )
        _log.addHandler(file_handler)

        # Call the function under test
        log_event('test_user4', 'unknown_status')

        # Check if error msg was added and failed == ERROR level
        with open(log_file, 'r') as lf:
            log_txt = lf.read()
        if 'ERROR' not in log_txt:
            raise AssertionError("Log output does not contain 'ERROR'")

    # Test Case N5 - Negative scenario
    def test_log_event_empty_param(*args):
        """Test logging when parameters are missing."""
        # case 1: no parameters
        with pytest.raises(TypeError):
            log_event()

        # case 2: one parameter is present
        with pytest.raises(TypeError):
            log_event('test_user4')


# Log file name
log_file = 'login_system.log'
