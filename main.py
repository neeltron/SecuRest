from picamera import PiCamera
from time import sleep

cam = PiCamera()

cam.start_preview()
sleep(5)
for i in range(0, 5):
    cam.capture(str(i)+".jpg")
    sleep(1)
    
cam.stop_preview()
