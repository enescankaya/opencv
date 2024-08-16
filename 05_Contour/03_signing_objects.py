import cv2,numpy as np
cap=cv2.VideoCapture("dog.mp4")
while(1):
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#BGR ÜZERİNDEN NESNE TAKİBİ VS YAPILAMIYOR BU YÜZDEN HSV FORMATINA RENK BİÇİMİNE ÇEVİRİYORUZ
    sensivity = 15#bu değer internetten hsv beyaz renk değerini arattığımızda verilen değerdir. renk reğerlerini internetten bulmak en doğru çözümdür.
    lower_while=np.array([0,0,255-sensivity])#hsv code for white
    upper_white=np.array([255,sensivity,255])
    mask=cv2.inRange(hsv,lower_while,upper_white)#mask demek istenilen yeri maskele geri kalanını sil demektir. burda bu beyaz aralıktaki yeri bırak geri kalanını siler.
    res=cv2.bitwise_and(frame,frame,mask=mask)#bu mask için özel bir ifadedir. her mask işleminden sonra bu ifade yazılır.
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",res)
    
    k=cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
    