"""This is homework 6.2."""


import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='')
_log = logging.getLogger(__name__)

while True:
    if 'h' in input('Please enter your word(s): ').lower():
        _log.info('h is in the word(s)')
        break
