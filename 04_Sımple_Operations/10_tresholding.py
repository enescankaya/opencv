#threshold fonksiyonu resimleri karartmamızı  ve bazı yerleri siyah beyaz olarak daha belirgin göstermemizi sağlar
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("osmanli.jpg",0)#gray scale
ret,th1=cv2.threshold(img,150,200,cv2.THRESH_BINARY)#girdiğimiz 2 değer threshold değerleridir. oynamalar yaparak karartmaları ayarlayabiliriz.(en az ayrıntılı)
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,2)#DAHA ADAPTİVE YANİ daha belirgin ayrıntılar gösterir 21 değeriyle oynanırsa
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,2)#gaussian daha da belirgin ayrıntılar gösteriyor 

cv2.imshow("img",img)
cv2.imshow("img_th1",th1)
cv2.imshow("img-th2",th2)
cv2.imshow("img-th3",th3)
cv2.waitKey(0)
cv2.destroyAllWindows()