import cv2, numpy as np

img= cv2.imread("geometric_shapes.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray,50,0.01,80)
corners =np.int0(corners)
i = len(corners)
for corner in corners:
    x,y=corner.ravel()
    cv2.circle(img,(x,y),7,(0,0,255),-1)
    cv2.putText(img,str(i),(x-10,y-20),cv2.FONT_HERSHEY_TRIPLEX,1,(255,0,0),2)
    i-=1
cv2.imshow("corners",img)
cv2.waitKey(0)
cv2.destroyAllWindows()