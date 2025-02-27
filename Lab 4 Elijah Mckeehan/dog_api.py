import requests
from PIL import Image
from io import BytesIO

BASE_URL = "https://dog.ceo/api"

def show_image(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img.show()
    else:
        print("Error displaying the image.")

def get_random_dog():
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    if response.status_code == 200:
        image_url = response.json()["message"]
        show_image(image_url)
    else:
        print("Error fetching random dog image.")

def get_dog_by_breed(breed):
    response = requests.get(f"{BASE_URL}/breed/{breed}/images/random")
    if response.status_code == 200:
        image_url = response.json()["message"]
        show_image(image_url)
    else:
        print("Breed not found. Please check the spelling.")

def list_all_breeds():
    response = requests.get(f"{BASE_URL}/breeds/list/all")
    if response.status_code == 200:
        breeds = response.json()["message"]
        return ", ".join(breeds.keys())
    return "Error fetching breed list."