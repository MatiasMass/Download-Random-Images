import requests
import json
import os

def create_directory(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print("Error: the folder already exists")

def download_random_images(url, directory_name):
    try:
        request = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("There was an error connection")
        return None

    images = json.loads(request.text)

    url_images = []

    for i, image in enumerate(images):
        url_images.append(image["download_url"])

    images_directory = os.path.join(os.getcwd(), directory_name)

    for i, image in enumerate(url_images):
        url_image = requests.get(image)
        print("Downloading...", image)
        with open(f"{images_directory}/{i}.jpg", "wb") as image:
            image.write(url_image.content)

    print("Done")

url = "https://picsum.photos/v2/list?page=3&limit=100"

directory_name = "images6"
create_directory(directory_name)

download_random_images(url, directory_name)