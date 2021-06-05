import cv2

iter = 0
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    cv2.imshow('frame', frame)
    iter += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite()
        break
    
    
cam.release()
cv2.destroyAllWindows()
