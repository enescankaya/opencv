import cv2
import numpy as np
import matplotlib as plt
path="TEST_IMAGES\opencv_logo.png"
img=cv2.imread(path,3)#eğer buraya (path,0) yaazarsak yani görüntüyü siyah beyaz greyscaler yaparsak o zaman img.shape[3] değerini alamayız hata verir.
print(img.shape)#height,width,channel(renkli mi değil mi onu ifade eder) değerlerini verir
#channel:3 ise ---> renklidir colorful
#channel:1 veya hiçbişeyse ----> greyscale
print("width: {} pixels".format(img.shape[1]))#0:height,1:width,2:channel verir)
print("height: {} pixels".format(img.shape[0]))#0:height,1:width,2:channel verir)
print("channel: {}".format(img.shape[2]))#0:heigh,1:width,2:channel verir) img.shape[2] içindeki 2 channeli verir ve sadece ve sadece görüntü renkli ise bu değeri döndürür aksi taktirde error alırız.
print("image size: {}".format(img.size))#width*height*channel =size verir yani toplam pixel sayısını. renkli görüntülerde aslında arka arkaya 3 adet matrix vardır.
#o yüzden renkli martixlerde channel 3 olduğu için width*height*3 şeklinde görüntünün size bulabiliriz.
print("Data Type: {}".format(img.dtype))#resim formatını gösterir
cv2.imshow("opencv",img)
cv2.waitKey(0)
cv2.destroyAllWindows()