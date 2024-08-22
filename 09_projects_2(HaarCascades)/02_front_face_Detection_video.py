import cv2
vid=cv2.VideoCapture("faces.mp4")
face_cascade=cv2.CascadeClassifier("D:\\opencv\\OpencvProjects\\haarCascades\\frontalface.xml")

while 1:
    _,frame=vid.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces=face_cascade.detectMultiScale(gray,1.1,2)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) == 27: break
    
vid.release()
cv2.destroyAllWindows()
    