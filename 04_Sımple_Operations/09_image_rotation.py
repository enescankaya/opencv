import cv2,numpy as np

img=cv2.imread("osmanli.jpg",0)
row,col=img.shape
M=cv2.getRotationMatrix2D((col/2,row/2),180,1)#kaç derece döndürmek istiyorsak 180 yerine onu yazıyoruz-
dst=cv2.warpAffine(img,M,(col,row))

cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()