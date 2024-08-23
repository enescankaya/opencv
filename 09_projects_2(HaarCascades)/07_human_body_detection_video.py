import cv2
vid = cv2.VideoCapture("body.mp4")
body_cascade = cv2.CascadeClassifier("D:\\opencv\\OpencvProjects\\haarCascades\\fullbody2.xml")


while True:
    ret,frame=vid.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    bodies = body_cascade.detectMultiScale(gray,1.3,2)
    
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("bodies",frame)
    
    if cv2.waitKey(20) == 27: break
vid.release()
cv2.destroyAllWindows()
