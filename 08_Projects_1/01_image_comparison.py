import cv2,numpy as np
img = cv2.imread("aircraft.jpg")
img1=cv2.imread("coins.jpg")
img2=cv2.imread("aircraft.jpg")
img=cv2.resize(img,(540,540))
img1=cv2.resize(img1,(540,540))#iki resim de aynı boyutta olmalı
img2=cv2.resize(img2,(540,540))
if img.shape==img1.shape:#ikisinin de boyutu aynıysa
    print("same size")
else:
    print("not same size")

diff=cv2.subtract(img1,img)
diff2=cv2.subtract(img,img2)
#bunların eşit olup  olmadığını kontrol etmek için tüm piksellerin eşitliğine bakıcaaz
b,g,r=cv2.split(diff)
b1,g1,r1=cv2.split(diff2)
if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    print("img1 and img is equal")
else:
    print("img1 and img is not equal")
if cv2.countNonZero(b1) == 0 and cv2.countNonZero(g1) == 0 and cv2.countNonZero(r1) == 0:
    print("img and img2 is equal")
else:
    print("img and img2 is not equal")
    
    
cv2.imshow("difference 2",diff2)
cv2.imshow("difference",diff)
# cv2.imshow("img",img)
# cv2.imshow("img1",)
cv2.waitKey(0)
cv2.destroyAllWindows()