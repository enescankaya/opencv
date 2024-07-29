import cv2
cap=cv2.VideoCapture(0)#0 demek kamera nuamrası gibi 2 kamera varsa 1 yazılabilir
fileName="D:\opencv\OpencvProjects\myVideo.avi"#\ yanına \u şeklinde yan yana yazamayız hata verir
codec=cv2.VideoWriter.fourcc('W','M','V','2')
frameRate=30
resolution=(640,480)
videoFileOutput=cv2.VideoWriter(fileName,codec,frameRate,resolution)
while True:
    ret, frame=cap.read()
    frame=cv2.flip(frame,1)#1 yazan yere -1,1,0 gibi değerler verebiliriz bu bize videonun eksenlere göre yönünü değiştirir.1 normal görüntüyü sağlar
    videoFileOutput.write(frame)
    cv2.imshow("wab cam",frame)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break
videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()
      