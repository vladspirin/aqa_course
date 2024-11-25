"""
Homework 13.1 Working with files - CSV, JSON, XML.

Task 2:
Validate whether all files in the folder
ideas_for_test/work_with_json are valid JSON files.
Log the results for invalid files using a logger
at the error level into a file named json__<your_second_name>.log.
"""

import logging
from pathlib import Path


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
_log = logging.getLogger(__name__)

