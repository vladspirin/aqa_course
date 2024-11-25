"""
Homework 13.1 Working with files - CSV, JSON, XML.

Task 2:
Validate whether all files in the folder
ideas_for_test/work_with_json are valid JSON files.
Log the results for invalid files using a logger
at the error level into a file named json__<your_second_name>.log.
"""

import json
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    filename='json__cool_logger.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
)
_log = logging.getLogger(__name__)


def get_json_files(dir_path):
    """Return list of JSON files."""
    json_files_lst = list(directory.rglob('*.json'))
    if not json_files_lst:
        _log.warning(f'No JSON files found in {directory}')
    return json_files_lst


def process_json_files(json_files):
    """Process and parse JSON files."""
    # Iterate over JSON files
    for file in json_files:
        try:
            # record to the result value if file Ok
            with open(file, 'r') as json_file:
                # Parse file without saving to result
                json.load(json_file)
            _log.info(f'Successfully processed: {file}')
        except json.decoder.JSONDecodeError as j_err:
            _log.error(f'JSON error in {file}: {j_err}')
        except Exception as err:
            _log.error(f'Error processing {file}: {err}')


if __name__ == '__main__':
    directory = Path('downloads/json/')
    # get the list with files
    json_files = get_json_files(directory)
    # process files if exist
    process_json_files(json_files)
