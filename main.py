import cv2
import time
import base64
import requests
import serial


def detect_faces(path):
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()
    exist = 0

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    if faces:
        exist = 1
    else:
        exist = 0
    
    return exist


distance = serial.Serial('COM5')
distance.flushInput()

iter = 0
cam = cv2.VideoCapture(0)

while True:
    ser = distance.readline()
    decoded = float(ser[0:len(ser)-2].decode("utf-8"))
    print(decoded)
    ret, frame = cam.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        iter += 1
        if iter <= 5:
            cv2.imwrite(str(iter)+".jpg", frame)
            exist = detect_faces(str(iter)+".jpg")
            time.sleep(1)
            if exist == 1:
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
                print("No face")
        
        else:
            break
        
    
    
cam.release()
cv2.destroyAllWindows()
