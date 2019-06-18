import base64
import requests


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    image_file.close()
    return encoded_string.decode("utf-8")


def encode_image_from_url(url):
    return base64.b64encode(requests.get(url).content).decode("utf-8")
