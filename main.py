import cv2
import time

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
        else:
            break
    
    
cam.release()
cv2.destroyAllWindows()
