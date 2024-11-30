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
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)
_log = logging.getLogger(__name__)

xml_file_path = Path('my_downloads/xml/groups.xml')


def search_group(file_path, group_number):
    """
    Search for a group by its number in the specified XML.

    Args:
        file_path (str or Path): The path to the XML file.
        group_number (str or int): The group number to search for.

    Returns:
        str or None: The value of 'timingExbytes/incoming' if found,
                    otherwise None.
    """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        for group in root.findall('.//group'):
            number_tag = group.find('number')
            if number_tag is None:
                _log.warning('Group without <number> tag found, skipping.')
                continue

            if str(group_number) == number_tag.text.strip():
                timing_exbytes = group.find('.//timingExbytes/incoming')
                if timing_exbytes is not None:
                    _log.info(f'Found incoming: {timing_exbytes.text}')
                    return timing_exbytes.text

                _log.warning('Group found but <incoming> tag is missing.')
                return None

        _log.info(f'Group {group_number} not found in the XML.')
        return None

    except Exception as err:
        _log.error(f'Error occurred while processing the file: {err}')
        return None


if __name__ == '__main__':
    search_group(xml_file_path, 4)
