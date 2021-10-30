import os, io
from google.cloud import vision_v1
from google.cloud.vision_v1 import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'/home/neha/Documents/Sem-5_Mini-project/DOCR/DOCR/docr/nice-limiter-327917-abe220beaea5.json'
client = vision_v1.ImageAnnotatorClient()


def gcs(path):
  # FOLDER_PATH = r'media/img'
  # IMAGE_FILE = 'img2.png'
  # FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)

  with io.open(path, 'rb') as image_file:
    content = image_file.read()

  image = vision_v1.Image(content = content)
  response = client.document_text_detection(image=image)
  print(response)
  response = str(response)

  a,b = response.rsplit('text: "', 1)
  b = str(b)
  return b

