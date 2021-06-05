import cv2
import time
import base64
import requests

iter = 0
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        iter += 1
        if iter <= 5:
            cv2.imwrite(str(iter)+".jpg", frame)
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
