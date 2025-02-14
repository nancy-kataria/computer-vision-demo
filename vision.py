from google.cloud import vision
import io

# Creating an authenticated Vision API client.
client = vision.ImageAnnotatorClient.from_service_account_file('computer-vision.json')

image_path = "Cat_image.jpg"

# Reading the image file as binary content, rb- read binary
with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

# creating an instance of the image class and binary data is fed in
image = vision.Image(content=content)

try:
    response = client.label_detection(image=image)

    # getting all label tags
    labels = response.label_annotations

    for label in labels:
        print(label.description, label.score)

except Exception as e:
    print(f"Error:{e}")

text_image_path = "text_image.jpeg"

with io.open(text_image_path, 'rb') as text_image_file:
    content_in_image = text_image_file.read()

text_image = vision.Image(content=content_in_image)

try:
    response = client.text_detection(image=text_image)

    texts = response.text_annotations

    for text in texts:
        print(text)

    print(texts[0].description)

except Exception as e:
    print(f"Error:{e}")

