import cv2,numpy as np
img=cv2.imread("text.png")
img1=cv2.imread("contour.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray=np.float32(gray)#fonksiyon gri ve float tipi istiyor
corners=cv2.goodFeaturesToTrack(gray,2000,0.01,10)#burada cornerları belirliyoruz değerlerle oynayıp corner sayısını ve özelliklerini değiştirebiliriz

corners=np.int0(corners)#şimdi kordinatlar bizde ama float cinsinden. bunları inte tekrar çevirmemiz gerekiyor nokta eklemek için tam kordinat int tipi gerekli
for corner in corners:
    x,y=corner.ravel()#corner içinde belirlenen cornerlar var bunları x,y kordinatlarını almamız gerekiyor o yerlere circle yerleştirebilmek için.
    cv2.circle(img,(x,y),3,(0,0,255),-1)#belirtilen cordination lara circle yerleştiriyoruz
cv2.imshow("corner",img)
cv2.waitKey(0)
cv2.destroyAllWindows()