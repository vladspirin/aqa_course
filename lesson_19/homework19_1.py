"""
Homework 19.1 Mars Rover “Curiosity” photos.

NASA has an open API that allows retrieving data in JSON format
about photos taken by the “Curiosity” rover on Mars
based on specific parameters.
Among this data, there are links to photos that need to be parsed
and then downloaded and saved as local files
(mars_photo1.jpg, mars_photo2.jpg, etc.) using additional requests.
The task should be implemented using the requests module.
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


class NasaImageParser:
    """
    A class discribed a parser for NASA images.

    Attributes:
        url (str): NASA API link.
        params (dict): dict of the params.
    """

    def __init__(self, url: str, params: dict):
        """Initialize a new NasaImageParser with parameters."""
        self.base_url = self._clean_url(url)
        self.params = self._prepare_params(params)

    @staticmethod
    def _clean_url(url: str) -> str:
        """Clear the URL if additional chars in the start/end of the string."""
        if url.startswith('<') and url.endswith('>'):
            return url[1: -1]
        return url

    def _prepare_params(self, params: dict) -> dict:
        """Check if all required params are available."""
        if not isinstance(params, dict):
            raise ValueError('Params must be a dictionary.')
        if 'api_key' not in params:
            raise ValueError("The 'api_key' parameter is required.")
        return params

    def get_photos(self):
        """Get the photos from remote."""
        try:
            response = requests.get(
                self.base_url,
                params=self.params,
                timeout=10,
            )
            response.raise_for_status()
            data = response.json()
            return data.get('photos', [])
        except (HTTPError, ConnectionError, Timeout) as err:
            _log.error(f'Error fetching photos: {err}')
            return []

    def download_photos(self, photos=None):
        """Download a single or all photos."""
        # If photos not available
        if photos is None:
            photos = self.get_photos()
            if not photos:
                _log.info('No photos available for the given parameters.')
                return  # will close the func in case of no photos

        # Fail downloads counter
        failed_downloads = 0
        for idx, photo in enumerate(photos, start=1):
            photo_url = photo.get('img_src')
            if not photo_url:
                print(f"Photo {idx} has no valid 'img_src'. Skipping.")
                failed_downloads += 1
                continue

            filename = f'mars_photo{idx}.jpg'
            try:
                # Download the photo
                with requests.get(photo_url, stream=True, timeout=10) as resp:
                    resp.raise_for_status()
                    with open(filename, 'wb') as fh:
                        for chunk in resp.iter_content(chunk_size=8192):
                            fh.write(chunk)
                _log.info(f'Downloaded: {filename}')
            except (HTTPError, ConnectionError, Timeout) as err:
                _log.error(f'Error downloading {photo_url}: {err}')
                failed_downloads += 1

        # End message
        if failed_downloads:
            _log.info(f'{failed_downloads} photo(s) could not be downloaded.')
        else:
            _log.info('All photos downloaded successfully!')


url = '<https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos>'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

if __name__ == '__main__':
    downloader = NasaImageParser(url, params)
    photos = downloader.get_photos()
    downloader.download_photos()
