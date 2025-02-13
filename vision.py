from google.cloud import vision
import io

client = vision.ImageAnnotatorClient.from_service_account_file('/Users/nancy/Downloads/computer-vision-450304-1614d2eda8c3.json')

