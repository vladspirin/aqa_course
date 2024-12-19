"""
HW 19.2. POST/GET/DELETE.

In the Python virtual environment (venv),
install Flask using the command pip install flask.
Create a file named app.py in a separate directory
and copy the code for app.py provided in the initial data.
Run the HTTP server using the command python app.py.
The server will start at the base address http://127.0.0.1:8080.

Using the documentation provided below, write code that:
1. Uses the requests module to perform a POST request
to upload an image to the server.
2. Retrieves the link to this file using a GET request.
3. Deletes the file from the server using a DELETE request.
"""

import logging

import requests
from requests.exceptions import HTTPError, Timeout

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)
_log = logging.getLogger(__name__)


def upload_to_server(base_url: str, file: str):
    """Upload file to the server."""
    try:
        with open(file, 'rb') as fh:
            files = {'image': (file, fh, 'image/png')}
            upload_url = f'{base_url}/upload'
            response = requests.post(upload_url, files=files, timeout=5)
            response.raise_for_status()
            _log.info(f'Server response: {response.json()}')
            return response

    except HTTPError as http_err:
        _log.error(f'HTTP error: {http_err}')
    except Timeout as time_err:
        _log.error(f'Timeout error: {time_err}')
    except FileNotFoundError as file_err:
        _log.error(f'File not found: - {file_err}')
    except Exception as err:
        _log.error(f'An unexpected error occurred: {err}')


def get_file_info(base_url: str, file: str, content_type: str):
    """Get file info from the server."""
    try:
        full_url = f'{base_url}/image/{file}'
        headers = {'Content-Type': content_type}
        response = requests.get(full_url, headers=headers, timeout=5)
        response.raise_for_status()

        if content_type == 'text':
            _log.info(f'Server response: {response.json()}')
            return response.json()

        elif content_type == 'image':
            with open(file, 'wb') as img_fh:
                img_fh.write(response.content)
            _log.info(f'File downloaded: {file}')
            return file

    except HTTPError as http_err:
        _log.error(f'HTTP error: {http_err}')
    except Timeout as time_err:
        _log.error(f'Timeout error: {time_err}')
    except Exception as err:
        _log.error(f'An unexpected error occurred: {err}')


def delete_from_server(base_url: str, file: str):
    """Delete file from server."""
    try:
        headers = {'Content-Type': 'image'}
        full_url = f'{base_url}/delete/{file}'
        response = requests.delete(full_url, headers=headers, timeout=5)
        response.raise_for_status()
        _log.info(f'Server response: {response.json()}')
        return response.json()

    except HTTPError as http_err:
        _log.error(f'HTTP error: {http_err}')
    except Timeout as time_err:
        _log.error(f'Timeout error: {time_err}')
    except Exception as err:
        _log.error(f'An unexpected error occurred: {err}')


if __name__ == '__main__':
    base_addr = 'http://127.0.0.1:8080'
    filename = 'HLIT.png'

    _log.info('POST request')
    upload_to_server(base_addr, filename)

    _log.info('GET request')
    get_file_info(base_addr, filename, 'text')

    _log.info('DELETE request')
    delete_from_server(base_addr, filename)
