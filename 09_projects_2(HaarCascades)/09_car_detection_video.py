import cv2
vid = cv2.VideoCapture("D:\\opencv\\OpencvProjects\\07_Exersizes\\car.mp4")
car_cascade=cv2.CascadeClassifier("D:\\opencv\\OpencvProjects\\haarCascades\\cars.xml")

while 1:
    ret,frame=vid.read()
    frame = cv2.resize(frame,(640,640))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars=car_cascade.detectMultiScale(gray,1.1,3)
    
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("cars",frame)
    if cv2.waitKey(5) == 27:break
    
vid.release()
cv2.destroyAllWindows()