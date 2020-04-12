import os
from PIL import Image
from instabot import Bot
from dotenv import load_dotenv
import time
from operations import DIRECTORY

MIN_ALLOWED_RATIO = 0.8
MAX_ALLOWED_RATIO = 1.91


def image_resize(filename):
    file_path = os.path.join(DIRECTORY, filename)
    image = Image.open(file_path)
    if image.mode == "RGBA":
        return
    ratio = image.width/image.height
    if ratio < MIN_ALLOWED_RATIO:
        new_height = image.width / MIN_ALLOWED_RATIO
        coordinates = (0, (image.height - new_height)/2, image.width, image.height - (image.height - new_height)/2)
        image = image.crop(coordinates)
    elif ratio > MAX_ALLOWED_RATIO:
        new_height = image.width / MAX_ALLOWED_RATIO
        coordinates = (0, (image.height - new_height)/2, image.width, image.height - (image.height - new_height)/2)
        image = image.crop(coordinates)
    dimensions = image.size
    max_size = max(dimensions)
    resize_coefficient = 1080 / max_size
    result_dimensions = [round(resize_coefficient * x) for x in dimensions]
    image.thumbnail(result_dimensions)
    new_filename = f"{filename.split('.')[0]}resized.jpg"
    file_path = os.path.join(DIRECTORY, new_filename)
    image.save(file_path, format="JPEG")


def resize_all_files():
    files = os.listdir(DIRECTORY)
    for file in files:
        image_resize(file)


def main():
    load_dotenv()
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")

    bot = Bot()
    bot.login(username=user, password=password)

    resize_all_files()

    files_to_upload = filter(lambda x: x.endswith('resized.jpg'), os.listdir(DIRECTORY))
    for file in files_to_upload:
        try:
            file_path = os.path.join(DIRECTORY, file)
            bot.upload_photo(file_path)
            if bot.api.last_response.status_code != 200:
                print(bot.api.last_response)
            time.sleep(3600)
        except Exception:
            print(f'Fail to upload picture: {file}')


if __name__ == '__main__':
    main()
