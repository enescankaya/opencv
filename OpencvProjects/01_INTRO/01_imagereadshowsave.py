import cv2

img=cv2.imread("klon.jpg")#bu img istediğimiz resmi tutuyor. resim eğer ki  proje adresimizin içinde değil ve başka konumdaysa "klon.jpg" yerine 
#"C:\Users\user\Desktop\klon.jpg" şeklinde yazılır. adreste türkçe karakter olmamalıimg=cv2.imread("C:\Users\user\Desktop\klon.jpg"). , yazıp 0 yazarsak görüntüyü gri elde ederiz
#print(img) # resim değerlerini okuma
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)#ilk parametre pencere ismi ikinci parametre ise flagdir yani ne yapmak istediğimizi belirtiriz. pencereyi istediğimiz şekilde
#boyutlandırmak istediğimizde cv2.WINDOW_NORMAL yazarız.
cv2.imshow("Image",img)#resmi gösterir
cv2.imwrite("klon1.jpg",img)#resmi kaydeder.klon1 adında.cv2.imwrite("C:\Users\user\Desktop\klon.jpg",img) şeklinde adres verip oraya da kaydedebiliriz.
cv2.waitKey(0)#ekranda resmi tutar 0 yazılırsa tuşlayana kadar tutar
cv2.destroyAllWindows()#belli tuşa basılırsa tüm açılan pencereleri kapatır önemlidir
