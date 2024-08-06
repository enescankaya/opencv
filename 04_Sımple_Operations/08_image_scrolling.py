#image scrolling=resim kaydırma
import cv2,numpy as np
img= cv2.imread("osmanli.jpg",0)#0 verdik gri oldu
row,col=img.shape#matrix satır sutün sayılarını aldık
M=np.float32([[1,0,0],[0,1,70]])#burada kaydırma değerlerini giriyoruz, 150 ile 200 değerleri değiştikçe kaydırma oranı değişir 150:x 200:y
dst=cv2.warpAffine(img,M,(row,col))#burda kaydırma işlemini warpAffine fonksiyonu ile yapıyoruz
cv2.imshow("original",img)
cv2.imshow("scrolled",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()