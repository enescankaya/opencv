import cv2
import numpy as np

# Görüntüleri yükleyin
img1 = cv2.imread("coins.jpg")
img2 = cv2.imread("balls.jpg")

# Görüntüleri gri tonlamalı formata çevirin
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Gürültüyü azaltmak için görüntüye medyan bulanıklaştırma (blur) uygulayın
img1_blur = cv2.medianBlur(gray1, 5)
img2_blur = cv2.medianBlur(gray2, 5)

# İlk görüntüde çemberleri tespit edin
# HoughCircles parametreleri:
# - img1_blur: Bulanıklaştırılmış gri tonlamalı görüntü
# - cv2.HOUGH_GRADIENT: Kullanılacak Hough dönüşümü tipi
# - 1: Görüntünün ölçek faktörü, genellikle 1 olarak ayarlanır
# - img1.shape[0]/4: Çemberler arasındaki minimum mesafe (minDist)
# - param1: Canny kenar tespiti için yüksek eşik değeri
# - param2: Merkezleri tespit etmek için kullanılan eşik değeri
# - minRadius: Tespit edilecek minimum yarıçap
# - maxRadius: Tespit edilecek maksimum yarıçap
circles = cv2.HoughCircles(img1_blur, cv2.HOUGH_GRADIENT, 1, img1.shape[0]/4,
                           param1=200, param2=10, minRadius=10, maxRadius=70)

# Eğer çemberler tespit edildiyse
if circles is not None:
    # Çemberlerin koordinatlarını ve yarıçaplarını yuvarlayın ve uint16 formatına çevirin
    circles = np.uint16(np.around(circles))

    # Her bir tespit edilen çember üzerinde işlem yapın
    for i in circles[0, :]:
        # Çemberin merkez noktasını ve yarıçapını kullanarak çember çizin
        # (i[0], i[1]): Çemberin merkezi
        # i[2]: Çemberin yarıçapı
        # (0, 255, 0): Çemberin rengi (yeşil)
        # 2: Çemberin kalınlığı
        cv2.circle(img1, (i[0], i[1]), i[2], (0, 255, 0), 2)

# Orijinal görüntüyü bulanıklaştırılmış haliyle gösterin
cv2.imshow("img1", img1_blur)

# Çemberlerin çizildiği görüntüyü gösterin
cv2.imshow("circles", img1)

# Kullanıcı bir tuşa basana kadar bekleyin ve ardından tüm pencereleri kapatın
cv2.waitKey(0)
cv2.destroyAllWindows()
