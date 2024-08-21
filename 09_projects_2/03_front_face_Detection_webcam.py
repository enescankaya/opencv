import cv2
cap =cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("D:\\opencv\\OpencvProjects\\haarCascades\\frontalface.xml")
while 1:
    ret,frame =cap.read()
    frame =cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.4,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,244),2)
    cv2.imshow("frame",frame)
    if cv2.waitKey(20) == 27: break
cap.release()
cv2.destroyAllWindows()