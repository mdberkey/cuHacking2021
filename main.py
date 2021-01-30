import io
import os
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] - R'api.json'

client - vision.ImageAnnotatorClient()

