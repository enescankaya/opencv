import cv2,numpy as np,math
cap=cv2.VideoCapture(0)
def findMaxContour(contours):
    max_i=0
    max_area=0
    for i in range(len(contours)):
        area_hand=cv2.contourArea(contours[i])
        if max_area < area_hand:
            max_area=area_hand
            max_i=i
        try:
           c=contours[max_i] 
        except:
            contours=[0]
            c=contours[0]
        return c
while 1:
    ret,frame=cap.read()
    frame = cv2.flip(frame,1)
    roi=frame[50:250,200:400]#frame in şu aralıklardaki kısımlarını roi ye veriyoruz
    cv2.rectangle(frame,(200,50),(400,250),(0,0,255),0)
    
    hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    lower_color=np.array([1,80,10],dtype=np.uint8)
    upper_color=np.array([170,255,255],dtype=np.uint8)
    
    mask=cv2.inRange(hsv,lower_color,upper_color)
    kernel=np.ones((11,11),np.uint8)
    mask=cv2.dilate(mask,kernel,iterations=1)
    mask=cv2.medianBlur(mask,17)
    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) >0:
            c=findMaxContour(contours)
            extLeft=tuple(c[c[:,:,0].argmin()][0])
            extRight=tuple(c[c[:,:,0].argmax()][0])
            extTop=tuple(c[c[:,:,1].argmin()][0])
            
            cv2.circle(roi,extLeft,5,(0,255,0),2)
            cv2.circle(roi,extRight,5,(0,255,0),2)
            cv2.circle(roi,extTop,5,(0,255,0),2)
            cv2.line(roi,extLeft,extTop,(0,0,255))
            cv2.line(roi,extTop,extRight,(0,0,255))
            cv2.line(roi,extRight,extLeft,(0,0,255))
            a=math.sqrt((extRight[0]-extTop[0])**2 + (extRight[1]-extTop[1])**2)
            b=math.sqrt((extLeft[0]-extRight[0])**2 + (extLeft[1]-extRight[1])**2)
            c=math.sqrt((extLeft[0]-extTop[0])**2 + (extLeft[1]-extTop[1])**2)
            try:
                angle_ab=int(math.acos((a**2+b**2-c**2)/(2*b*c))*57)
                cv2.putText(roi,str(angle_ab),(extRight[0]-100,extRight[1]),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,0,255),1)
                if angle_ab >70:
                    cv2.rectangle(frame,(0,0),(100,100),(255,0,2),-1)
                else:
                    pass
            except:
                cv2.putText(roi,"?",(extRight[0]-100,extRight[1]),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,0,255),1)
    cv2.imshow("mask",mask)
    cv2.imshow("roi",roi)
    cv2.imshow("frame",frame)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()