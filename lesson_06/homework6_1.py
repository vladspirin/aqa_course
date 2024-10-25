"""Homework 6.1."""


import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='')
_log = logging.getLogger(__name__)

if len(set(input('Add string: '))) > 10:
    _log.info('True')
else:
    _log.info('False')
