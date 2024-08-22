import cv2 
img = cv2.imread("face.png")
face_cascade = cv2.CascadeClassifier("D:\\opencv\\OpencvProjects\\haarCascades\\frontalface.xml")
eye_cascade = cv2.CascadeClassifier("D:\\opencv\\OpencvProjects\\haarCascades\\haarcascade_eye.xml")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
img2=img[y:y+h,x:x+w]
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#gray2=gray[y:y+h,x:x+w]

eyes = eye_cascade.detectMultiScale(gray2)
for (x,y,w,h) in eyes:
    cv2.circle(img2,(int(x+(w/2)),int(y+(h/2))),int(w/2),(255,0,0),2)
    
cv2.imshow("image",img2)
cv2.imshow("gray2",gray2)
cv2.waitKey(0)
cv2.destroyAllWindows()