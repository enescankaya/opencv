import cv2,numpy as np
def nothing(x):
    pass
cap = cv2.VideoCapture(0)
cv2.namedWindow("trackbar")
cv2.createTrackbar("lh","trackbar",0,179,nothing)
cv2.createTrackbar("ls","trackbar",0,255,nothing)
cv2.createTrackbar("lv","trackbar",0,255,nothing)
cv2.createTrackbar("uh","trackbar",0,179,nothing)
cv2.createTrackbar("us","trackbar",0,255,nothing)
cv2.createTrackbar("uv","trackbar",0,255,nothing)
while 1:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    frame=cv2.resize(frame,(500,350))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lh=cv2.getTrackbarPos("lh","trackbar")
    ls=cv2.getTrackbarPos("ls","trackbar")
    lv=cv2.getTrackbarPos("lv","trackbar")
    uh=cv2.getTrackbarPos("uh","trackbar")
    us=cv2.getTrackbarPos("us","trackbar")
    uv=cv2.getTrackbarPos("uv","trackbar")
    lower_blue=np.array([lh,ls,lv])
    upper_blue=np.array([uh,us,uv])
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    bit=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("BitWise",bit)
    if cv2.waitKey(20) & 0xFF==ord("q"):
        break
    

cv2.destroyAllWindows()