
#genellikle buradaki fonksiyonları kullanıcaz substract,ion için
import cv2,numpy as np
cap = cv2.VideoCapture("car.mp4")
substractor = cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=120,detectShadows=True)


while 1:
    _,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    mask=substractor.apply(frame)
    cv2.imshow("frame",frame)    
    cv2.imshow("mask",mask)
    
    if cv2.waitKey(20) & 0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()