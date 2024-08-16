import cv2,numpy as np
img = cv2.imread("geometric_shapes.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,170,200,cv2.THRESH_BINARY)
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE )
for contour in contours:
    if cv2.contourArea(contour)>100:
        M=cv2.moments(contour)
        if M["m00"]!=0:
            X=int(M["m10"]/M["m00"])
            Y=int(M["m01"]/M["m00"])
            cv2.circle(img,(X,Y),7,(0,0,255),-1)
            cv2.putText(img,f"({X}, {Y})",(X+10,Y-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),2)
            print(str(cv2.contourArea(contour)) + " " + str(X) + " " + str(Y))
        else:
            print("centroid could not found!\n")
cv2.imshow("centroids",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
        