import cv2
import numpy as np
img = np.zeros((10,10,3),np.uint8)#renkli resim oluşturduk 3 channel verisi veridğiimiz için hiç bir şey yazmassak 3 yerine gri boyutta yani renksiz olurdu
# ama eğer channel değerini boş bırakırsak aşağıda verdiğimiz 3 değer yerine sadece 1 değer yazıcaz.
img[0,0]=(255,255,255)
img[0,1]=(255,255,200)
img[0,2]=(255,255,150)
img[0,3]=(255,255,15)#pixelleri tek  tek boyuyoruz bu şekilde
img=cv2.resize(img,(1000,1000),interpolation=cv2.INTER_AREA)#pixel boyutunu arttırıyoruz. np.zeros içine yazdığımız 10 değerlerini 100 yaptık yani
cv2.imshow("canvas",img)
cv2.waitKey(0)
cv2.destroyAllWindows()