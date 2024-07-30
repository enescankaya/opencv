import cv2
import numpy as np
import matplotlib.pyplot as plt

path="TEST_IMAGES/opencv_logo.png"
img=cv2.imread(path)
print(  "Shape: {}".format(img.shape))
(B,G,R)=cv2.split(img)#cv2.split komutu channeldaki 3 rengi çıkarıp yeni resme atayabilmemizi sağlar. burada b,g,r adlı yeni değişkenlere sırasıyla maviyi,yeşili ve kırmızı
#rengi çıkarıp onlara atadık
#bu renkleri tekrar birleştirip orjinal görüntü elde edebiliriz. aşşağıdaki gibi merge komutu kullanarak
merged=cv2.merge([B,G,R])
black=np.zeros(img.shape[:2],dtype="uint8")#siyah pencere oluşturur/görüntüyü siyaha çevirir
cv2.imshow("black",black)
cv2.imshow("Red",cv2.merge([black,black,R]))
cv2.imshow("Green",cv2.merge([black,G,black]))
cv2.imshow("Blue",cv2.merge([B,black,black]))
# cv2.imshow("MERGED",merged)
cv2.imshow("image",img)
# cv2.imshow("B",B)
# cv2.imshow("G",G)
# cv2.imshow("R",R)
cv2.waitKey(0)
cv2.destroyAllWindows()