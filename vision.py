from google.cloud import vision
import io

client = vision.ImageAnnotatorClient.from_service_account_file('computer-vision.json')

image_path = "Cat_image.jpg"

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

try:
    response = client.label_detection(image=image)

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

