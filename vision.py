import io
import os
from spotify import give_keyword

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
pic = 'face.jpg'
def run_vision(picture):
    file_name = os.path.join(
        os.path.dirname(__file__),
        pic)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    f_response = client.face_detection(image=image)
    faces = f_response.face_annotations

    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                           'LIKELY', 'VERY_LIKELY')
    for face in faces:
        if face.anger_likelihood > 3:
            return 'anger'
        elif face.joy_likelihood > 3:
            return 'joy'
        elif face.sorrow_likelihood > 3:
            return 'sorrow'
        elif face.surprise_likelihood > 3:
            return 'surprise'
        else:
            return labels[0].description
keyword = run_vision(pic)
print(keyword)

give_keyword(keyword)
