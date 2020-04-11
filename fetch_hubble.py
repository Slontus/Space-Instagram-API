import requests
import os

HUBBLE_FILENAME = 'hubble'
DIRECTORY = 'images'
URL_HUBBLE = 'http://hubblesite.org/api/v3/image'
HUBBLE_COLLECTIONS = ["holiday_cards", "wallpaper", "spacecraft", "news", "printshop", "stsci_gallery"]


def fetch_collection_image_ids(collection):
    payload = {"page": "all", "collection_name": collection}
    response = requests.get(URL_HUBBLE + 's', payload)
    response.raise_for_status()
    print(response.status_code)
    image_ids = [x['id'] for x in response.json()]
    return image_ids


def fetch_hubble_image(image_id):
    url = '/'.join([URL_HUBBLE, str(image_id)])
    response = requests.get(url)
    response.raise_for_status()
    image_data = response.json()['image_files']
    url_list = [x['file_url'] for x in image_data]
    file_url = url_list[-1].replace('//imgsrc.hubblesite.org/hvi', 'https://hubblesite.org')
    file_name = str(image_id).join([HUBBLE_FILENAME, fetch_file_extension(file_url)])
    image_download(file_url, file_name)


def fetch_file_extension(url):
    extension = url.split('.')[-1]
    return '.' + extension


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
        image_ids = fetch_collection_image_ids(HUBBLE_COLLECTIONS[1])
        for _id in image_ids:
            print(f"downloading hubble image {_id}...")
            fetch_hubble_image(_id)
    except requests.exceptions.HTTPError as error:
        print(f"Not possible to download Hubble images: {error}")


if __name__ == '__main__':
    main()
