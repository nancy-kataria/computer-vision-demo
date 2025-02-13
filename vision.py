from google.cloud import vision
import io

client = vision.ImageAnnotatorClient.from_service_account_file('/Users/nancy/Downloads/computer-vision-450304-1614d2eda8c3.json')

image_path = "sailboat.jpg"

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

response =client.label_detection(image=image)

