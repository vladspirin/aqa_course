"""
Homework 13.1 Working with files - CSV, JSON, XML.

Task 3:
For the file ideas_for_test/work_with_xml/groups.xml,
create a function to search by group/number and return the
value of timingExbytes/incoming.
Output the result to the console using a logger at the info level.
"""

import logging
import xml.etree.ElementTree as ET

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
_log = logging.getLogger(__name__)

