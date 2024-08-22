import cv2
img = cv2.imread("bodies.png")
body_cascade = cv2.CascadeClassifier("D:\\opencv\OpencvProjects\\haarCascades\\haarcascade_fullbody.xml")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
bodies = body_cascade.detectMultiScale(gray,1.1,1)
for (x,y,w,h) in bodies:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow("body",img)
cv2.waitKey(0)
cv2.destroyAllWindows()