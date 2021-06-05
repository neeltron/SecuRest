import cv2
import time
import base64
import requests


def detect_faces(path):
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')

    for face in faces:
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in face.bounding_poly.vertices])

        print('face bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception('{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(response.error.message))


iter = 0
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        iter += 1
        if iter <= 5:
            cv2.imwrite(str(iter)+".jpg", frame)
            detect_faces(str(iter)+".jpg")
            time.sleep(1)
            with open(str(iter)+".jpg", "rb") as file:
                url = "https://api.imgbb.com/1/upload"
                payload = {
                    "key": "4e8e6f9baef8b46f75ac078d4bded8c1",
                    "image": base64.b64encode(file.read()),
                }
                res = requests.post(url, payload)
                
                dict = res.json()
                url = dict['data']['url']
        
        else:
            break
        
    
    
cam.release()
cv2.destroyAllWindows()
