import os
from dotenv import load_dotenv
import requests
import datetime
from operations import image_download, create_directory

NASA_URL = "https://api.nasa.gov/planetary/apod"
NASA_FILENAME = "nasa"
NUMBER_OF_DAYS = 7


def fetch_image_of_the_day(url, api_key, date):
    payload = {'api_key': api_key, "date": date}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()['hdurl']


def main():
    create_directory()
    load_dotenv()
    api_key = os.getenv("API_KEY")
    for day in range(NUMBER_OF_DAYS):
        date = datetime.date.today() - datetime.timedelta(days=day)
        date = str(date)
        file_url = fetch_image_of_the_day(NASA_URL, api_key, date)
        file_name = ''.join([NASA_FILENAME, date, os.path.splitext(file_url)[1]])
        image_download(file_url, file_name)


if __name__ == '__main__':
    main()
