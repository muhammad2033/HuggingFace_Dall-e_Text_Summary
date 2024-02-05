import io
import openai
import requests
from PIL import Image

openai.api_key = "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"

def generative_image(text):

    # generate the image using openai's DALL-E model
    response = openai.Image.create(
        prompts = text,
        n = 1,
        size = "512x512"
    )
    # get the image URL from the response 

    image_url = response.data[0]['url']

    # get the image and convert it to a PIL image 
    image_content = requests.get(image_url).content 
    image = Image.open(io.BytesIO(image_content))
    image.show()

prompts = input(" enter the prompts for getting the image from the DALL-e :")
generative_image(prompts)