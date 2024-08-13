import cv2
import numpy as np
img = cv2.imread("h_line.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,75,150,)

cv2.imshow("original",img)
cv2.imshow("edged",edges)

lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=1000)#MAXLİNEGAP ASLINDA DOLU OLAN ŞEKİLLER ARASINDAKİ BOŞLUKLARI DOLDURMAK İÇİN KULLANILIYOR. KULLANMAYA DA BİLİRİZ
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,100),2)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
