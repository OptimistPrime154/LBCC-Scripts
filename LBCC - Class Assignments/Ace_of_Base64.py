import base64
import requests
from pyzbar.pyzbar import decode
from PIL import Image

def decode_base64_png(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        decoded_data = base64.b64decode(response.content)

        with open("decoded_image.png", "wb") as file:
            file.write(decoded_data)

        print("Image saved")

    else:
        print("Image failed to save")

url = "https://gist.githubusercontent.com/professor-hillman/3f7f54d1ac36e385da5660ab12e92060/raw/9424fe9e4fcb3c5a53dc4591ceafdfe682534cc4/aceofbase64.txt"
decode_base64_png(url)

image = Image.open("decoded_image.png")

decoded_objects = decode(image)

for obj in decoded_objects:
    print('Flag:', obj.data.decode('utf-8'))