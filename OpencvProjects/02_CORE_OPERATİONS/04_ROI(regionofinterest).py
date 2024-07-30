#ROI: REGION OF INTEREST --> İLGİ ALANI
import cv2
import numpy as np
import matplotlib.pyplot as plt

path="TEST_IMAGES/basketball.jpg"
img=cv2.imread(path)
roi=img[100:200,0:50]#soldaki adamın yüz kordinatları
img[300:400,300:350]=roi#adamın yüzü roi değişkenindeydi biz belirtilen kordinatlara roi değişkenini attık yani yapıştırdık birnevi
#roi boyutu x y aynı olmak şartıyla img verdiğimiz değer aynı olmak zorunda ki görsel oraya sığdırılsın yoksa aşağıdaki hatayı verir
#ValueError: could not broadcast input array from shape (100,50,3) into shape (50,100,3)
print("Shape: {}".format(img.shape))
cv2.imshow("basketball",img)
cv2.imshow("basketball ROI",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()