import requests
from operations import create_directory, image_download

SPACEX_FILENAME = 'spacex'
URL_LAST_LAUNCH = 'https://api.spacexdata.com/v3/launches/latest'


def fetch_spacex_launch(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['links']['flickr_images']


def main():
    create_directory()
    try:
        for i, link in enumerate(fetch_spacex_launch(URL_LAST_LAUNCH)):
            file = str(i + 1).join([SPACEX_FILENAME, '.jpg'])
            image_download(link, file)
    except requests.exceptions.HTTPError as error:
        print(f"Not possible to download SpaceX photos: {error}")


if __name__ == '__main__':
    main()
