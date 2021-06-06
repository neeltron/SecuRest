# SecuRest

It is a well-known fact that illegal logging accounts for 15-30% of the global timber trade and cutting down trees is the main reason behind deforestation. SecuRest is a device that can be placed on a tree at a certain height and it can detect illegal logging happening in the forest, near the range of that tree. When motion is detected around that region, SecuRest will trigger an alert for the camera, and the servo will rotate it to capture images of the area. It is then sent to google cloud vision for face detection. If a face is detected around there, that image will be logged and uploaded to the cloud and it can then be reviewed by the forest authority. Web backend is developed in PHP, face detection is performed using Google Cloud Vision API and Images are stored using ImgBB API.

## Hardware

+ Arduino Nano
+ Servomechanism Motor
+ HC-SR04 Distance Sensor
+ Camera

## Installation

```
git clone https://github.com/neeltron/SecuRest.git
```
Install Arduino IDE here: https://www.arduino.cc/en/software/
<br>
For Modules:<br>
```
pip install pyserial
pip install google-cloud
pip install google-cloud-vision
pip install python-opencv
pip install mysql.connector
```

## Relevant Links

Devpost: https://devpost.com/software/securest<br>
Project Demo: https://www.youtube.com/watch?v=lKXvgFC5nzo
