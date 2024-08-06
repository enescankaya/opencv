import cv2,numpy as np
img=cv2.imread("klon.jpg")
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#BGR DAN RGB YE DÖNÜŞTÜRÜYORUZ
img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#HSV DÖNÜŞÜM
img3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#GRAY DÖNÜŞÜM
#RESİMLER BOZUK ÇÜNKÜ CHANNEL 3 GÖRÜNTÜYÜ DÖNÜŞTÜRMEK ZORDUR
cv2.imshow("HSV",img2)
cv2.imshow("RGB",img1)
cv2.imshow("BGR",img)
cv2.imshow("GRAY",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()