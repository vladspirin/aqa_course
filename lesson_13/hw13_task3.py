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

xml_file_path = Path('downloads/xml/groups.xml')


def search_group(file_path, group_number):
    """
    Search for a group by its number in the specified XML.

    Args:
        file_path (str or Path): The path to the XML file.
        group_number (str or int): The group number to search for.
    Returns:
        tuple: A tuple containing the values of 'timingExbytes'
               and 'incoming' if the group is found, otherwise None.
    """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        # Find the element by group/number
        for group in root.findall('.//group'):
            number_tag = group.find('number')
            if number_tag is not None:
                # Strip to avoid trailing spaces
                group_number_text = number_tag.text.strip()
                # Ensure both are strings
                if str(group_number) == group_number_text:
                    timing_exbytes = group.find('timingExbytes')
                    if timing_exbytes is not None:
                        incoming = timing_exbytes.find('incoming')
                        if incoming is not None:
                            _log.info(f"""timingExbytes:
                                    {timing_exbytes.find('micro').text},
                                    incoming: {incoming.text}""")
                            return (timing_exbytes.find('micro').text,
                                    incoming.text)
            else:
                _log.warning(f"""Group with number {group_number}
                does not contain a <number> tag.""")
        _log.info(f'No group with number {group_number} found.')
        return None
    except Exception as err:
        _log.error(f'Error occurred: {str(err)}')
        return None


if __name__ == '__main__':
    search_group(xml_file_path, 4)
