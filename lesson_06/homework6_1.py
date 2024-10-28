"""Homework 6.1."""


import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='')
_log = logging.getLogger(__name__)

_log.info(len(set(input('Add string: '))) > 10)
