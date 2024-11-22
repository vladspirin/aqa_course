"""Download files (depends on format) from remote server."""


import os

import requests


def save_remote_file_to_local(url, data_format, timeout, base_dir='downloads'):
    """
    Download a file from a remote URL and saves it locally.

    Args:
        url (str): The URL of the file to be downloaded.
        data_format (str): The format of the file (e.g., 'csv', 'json', 'xml').
        timeout (int): timeout for the request.
        base_dir (str, optional):
                The base directory where the file will be saved.
                This defaults to "downloads".
    Returns:
        str: The absolute path to the saved file,
            or None if there was an error during the process.
    """
    try:
        # Get file by the URL
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()

        # Understand which folder need by the file format
        target_dir = os.path.join(base_dir, data_format.lower())

        # Create folder if not exist
        os.makedirs(target_dir, exist_ok=True)

        # Check the file by the URL
        file_name = url.split('/')[-1]
        file_path = os.path.join(target_dir, file_name)

        # Write file to the memory
        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f'File saved: {file_path}')
        return file_path

    except requests.exceptions.RequestException as err:
        print(f'Download file error: {err}')
        return None
