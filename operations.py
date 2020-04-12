import requests
import os

DIRECTORY = 'images'


def create_directory():
    os.makedirs(DIRECTORY, exist_ok=True)


def image_download(url, filename):
    file_path = os.path.join(DIRECTORY, filename)
    response = requests.get(url)
    response.raise_for_status()
    with open(file_path, 'wb') as _file:
        _file.write(response.content)
