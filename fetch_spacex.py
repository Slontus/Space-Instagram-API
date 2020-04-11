import requests
import os

SPACEX_FILENAME = 'spacex'
URL_LAST_LAUNCH = 'https://api.spacexdata.com/v3/launches/latest'
DIRECTORY = 'images'


def fetch_file_extension(url):
    extension = url.split('.')[-1]
    return '.' + extension


def fetch_spacex_launch(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['links']['flickr_images']


def crete_download_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def image_download(url, filename):
    file_path = os.path.join(DIRECTORY, filename)
    response = requests.get(url)
    response.raise_for_status()
    with open(file_path, 'wb') as _file:
        _file.write(response.content)


def main():
    crete_download_directory(DIRECTORY)
    try:
        for i, link in enumerate(fetch_spacex_launch(URL_LAST_LAUNCH)):
            file = str(i + 1).join([SPACEX_FILENAME, '.jpg'])
            image_download(link, file)
    except requests.exceptions.HTTPError as error:
        print(f"Not possible to download SpaceX photos: {error}")


if __name__ == '__main__':
    main()
