# Google Cloud Vision API - Image Label & Text Detection

This project demonstrates how to use the **Google Cloud Vision API** to perform **label detection** (object recognition) and **text detection** (OCR) on images using Python.

## Prerequisites

Before running the script, ensure you have the following setup:

### 1. Install Dependencies
Make sure you have **Python 3.x** installed and install the required Google Cloud Vision library:

```bash
pip install google-cloud-vision
```

### 2. Set Up Google Cloud Vision API
- Create a Google Cloud project in the [Google Cloud Console](https://console.cloud.google.com/).
- Enable the **Cloud Vision API** for your project.
- Create a **service account** with "Cloud Vision API User" role.
- Download the JSON **service account key file** and store it securely.

### 3. Set the Authentication Credentials
Ensure the service account key is correctly referenced in your script:

```python
client = vision.ImageAnnotatorClient.from_service_account_file('/path/to/your/service-account-file.json')
```

## How It Works

### **1. Label Detection (Object Recognition)**
This script reads an image file (`Cat_image.jpg`) and sends it to the Vision API to detect objects and labels.

### **2. Text Detection (OCR)**
It reads another image (`text_image.jpeg`) to extract and print the text found in the image.

## Usage

1. Place your images (`Cat_image.jpg` and `text_image.jpeg`) in the same directory as the script.
2. Run the script:

```bash
python vision.py
```


