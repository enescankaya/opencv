import cv2
cap=cv2.VideoCapture("video.mp4")

while True:
    ret,frame=cap.read()
    if not ret:
        #break yazarsak videoyu bitirir
        cap.set(cv2.CAP_PROP_POS_AVI_RATIO, 0) # videyu başa sarar.
        continue
    frame= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)#burada yakalanan her frami gri tona çevirir. ve video gri olur.
    cv2.imshow("Video",frame)
    if cv2.waitKey(30) & 0xFF==ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()