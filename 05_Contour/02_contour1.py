import cv2,numpy as np
img=cv2.imread("contour1.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#siyah beyaza çevir
_,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)#binary demek ya siyah ya beyaz olacak herhangi bir ara renk yok!baştaki _ ise ret aslında kullanmadığımız için _ yapıyoruz
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#cordinatları bulduk contours değişkenimize attık
cv2.drawContours(img,contours,1,(0,0,255),2)#1 değerini -1 verirsek her yeri çizer. 0 verirsek dış kısımları çizer, 1 verirsek içeridekini çizer
cv2.imshow("contour",img)
cv2.waitKey(0)
cv2.destroyAllWindows()