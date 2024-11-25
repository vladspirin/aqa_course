"""
Homework 13.1 Working with files - CSV, JSON, XML.

Task 1:
Take two files from the folder ideas_for_test/work_with_csv,
compare them for duplicates, and remove them.
Save the result to a file named result_<your_second_name>.csv.
"""

import csv
import os
from pathlib import Path

EXPECTED_FILENAME = 'result_combined.csv'
# Need to run download_files_helper before this module


def get_downloads_file_path(filename):
    """Get file path from downloads."""
    return Path('downloads') / 'csv' / filename


def read_csv(filename):
    """Read the CSV file and return list."""
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def merge_and_remove_duplicates(file1, file2):
    """
    Merge two CSV files, and removes duplicate rows.

    Args:
        file1 (str): Path to the first CSV file.
        file2 (str): Path to the second CSV file.

    Returns:
        list: A list of rows representing the merged data.
              The first row contains the combined headers.
    """
    # Read csv files
    data1 = read_csv(file1)
    data2 = read_csv(file2)

    # Grab just headers for next manupulations
    header1 = data1[0]
    header2 = data2[0]

    # Compare two headers
    if header1 != header2:
        # Create a header for combined file
        combined_header = list(set(header1) | set(header2))

        # Add columns where no columns exist
        data1 = [
            row + [''] * (len(combined_header) - len(row)) for row in data1
        ]
        data2 = [
            row + [''] * (len(combined_header) - len(row)) for row in data2
        ]

        # Change header in both files
        data1[0] = combined_header
        data2[0] = combined_header

    # Merge data from two files
    combined_data = data1 + data2

    # Delete duplicates, return one list
    seen = set()
    return [
        row for row in combined_data
        if tuple(row) not in seen and not seen.add(tuple(row))
    ]


def write_to_csv(data, filename):
    """Write list to CSV file."""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(data)
        return f'Data has been written to {filename}'
    except Exception as err:
        return f'Error writing to file: {err}'


def delete_file(filename):
    """Delete file by path."""
    if os.path.exists(filename):
        os.remove(filename)
        print(f"The file '{filename}' has been deleted.")
    else:
        print(f"The file '{filename}' does not exist.")


filepath1 = get_downloads_file_path('random.csv')
filepath2 = get_downloads_file_path('random-michaels.csv')
combined_files = merge_and_remove_duplicates(filepath1, filepath2)
delete_file(filepath1)
delete_file(filepath2)
expected_result = write_to_csv(combined_files, EXPECTED_FILENAME)
