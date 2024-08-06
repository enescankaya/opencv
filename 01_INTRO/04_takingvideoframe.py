import cv2
cap=cv2.VideoCapture(0)#0 demek kamera nuamrası gibi 2 kamera varsa 1 yazılabilir
while True:
    ret, frame=cap.read()
    frame=cv2.flip(frame,1)#1 yazan yere -1,1,0 gibi değerler verebiliriz bu bize videonun eksenlere göre yönünü değiştirir.1 normal görüntüyü sağlar
    cv2.imshow("wab cam",frame)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
      