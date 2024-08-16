import cv2

# Görüntüyü yükle
img = cv2.imread("contour.png")

# Görüntüyü gri tonlamaya çevir (gri tonlama, daha kolay işlenebilen bir formattır)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Eşikleme işlemi uygula (gri tonlamalı görüntüyü ikili (binary) bir görüntüye dönüştür)
_, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
print(_)
# Görüntünün momentlerini hesapla
# Momentler, bir şeklin geometrik özelliklerini tanımlamak için kullanılan niceliklerdir.
M = cv2.moments(thresh)

# Ağırlık merkezinin X koordinatını hesapla
# m10 ve m00 momentlerini kullanarak hesaplanır.
# X = m10 / m00 formülü ağırlık merkezinin X koordinatını verir.
X = int(M["m10"] / M["m00"])

# Ağırlık merkezinin Y koordinatını hesapla
# m01 ve m00 momentlerini kullanarak hesaplanır.
# Y = m01 / m00 formülü ağırlık merkezinin Y koordinatını verir.
Y = int(M["m01"] / M["m00"])

# Ağırlık merkezini görüntüde bir daire ile işaretle
# cv2.circle fonksiyonu ile (X, Y) koordinatında, yarıçapı 3 olan yeşil bir daire çizilir.
# (-1) değeri, dairenin dolu olmasını sağlar.
cv2.circle(img, (X, Y), 3, (0, 255, 0), -1)

# İşaretlenmiş görüntüyü ekranda göster
cv2.imshow("img", img)
cv2.imshow("thresh",thresh)
# Kullanıcı bir tuşa basana kadar görüntüyü göster
cv2.waitKey(0)

# Tüm pencereleri kapat ve belleği temizle
cv2.destroyAllWindows()
