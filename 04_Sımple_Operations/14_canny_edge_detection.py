import cv2

cap=cv2.VideoCapture(0)
while 1:
    ret,frame= cap.read()
    frame=cv2.flip(frame,1)#bize yansımasını değiştiriyoruz. ayna yansıması için 1 değeri giriyoruz.y eksenine göre görüntünün tersini verir
    edges=cv2.Canny(frame,50,100)
    cv2.imshow("frame",frame)
    cv2.imshow("edges",edges)
    if cv2.waitKey(5) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()