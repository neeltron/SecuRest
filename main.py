# -*- coding: utf-8 -*-
"""
@author: Neel
"""

import cv2
import time
import base64
import requests
import serial
import mysql.connector


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


def insert(link):
    db = mysql.connector.connect(
    host = "remotemysql.com",
    user = "hwW4R6cA0s",
    password = "9bVe4xsxvX",
    database = "hwW4R6cA0s"
    )
    cursor = db.cursor()
    sql = "INSERT INTO SecuRest (link) VALUES ('"+link+"')"
    val = str(link)
    cursor.execute(sql, val)
    db.commit()


distance = serial.Serial('COM5')
distance.flushInput()


iter = 0
err_count = 0
serial_iter = 0
flag = 0
cam = cv2.VideoCapture(0)

while True:
    try:
        ser = distance.readline()
        decoded = float(ser[0:len(ser)-2].decode("utf-8"))
        print(decoded)
        serial_iter += 1
        if decoded < 10 and serial_iter > 2:
            distance.write("M".encode())
            flag = 1
            ret, frame = cam.read()
            cv2.imshow('frame', frame)
            iter += 1
            if iter <= 5:
                time.sleep(1)
                cv2.imwrite(str(iter)+".jpg", frame)
                exist = detect_faces(str(iter)+".jpg")
                
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
                        insert(url)
                else:
                    print("No face")
                
                
                
            else:
                break
    except:
        err_count += 1
        if err_count > 100:
            break


cam.release()
cv2.destroyAllWindows()
distance.close()
