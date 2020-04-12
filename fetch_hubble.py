import requests
import os
from operations import image_download, create_directory

HUBBLE_FILENAME = 'hubble'
DIRECTORY = 'images'
URL_HUBBLE = 'http://hubblesite.org/api/v3/image'
HUBBLE_COLLECTIONS = ["holiday_cards", "wallpaper", "spacecraft", "news", "printshop", "stsci_gallery"]


def fetch_collection_image_ids(collection):
    payload = {"page": "all", "collection_name": collection}
    response = requests.get(URL_HUBBLE + 's', payload)
    response.raise_for_status()
    image_ids = [x['id'] for x in response.json()]
    return image_ids


def fetch_hubble_image(image_id):
    url = '/'.join([URL_HUBBLE, str(image_id)])
    response = requests.get(url)
    response.raise_for_status()
    image_data = response.json()['image_files']
    url_list = [x['file_url'] for x in image_data]
    file_url = url_list[-1].replace('//imgsrc.hubblesite.org/hvi', 'https://hubblesite.org')
    file_name = str(image_id).join([HUBBLE_FILENAME, os.path.splitext(file_url)[1]])
    image_download(file_url, file_name)


def main():
    create_directory()
    try:
        image_ids = fetch_collection_image_ids(HUBBLE_COLLECTIONS[1])
        for _id in image_ids:
            print(f"downloading hubble image {_id}...")
            fetch_hubble_image(_id)
    except requests.exceptions.HTTPError as error:
        print(f"Not possible to download Hubble images: {error}")


if __name__ == '__main__':
    main()
