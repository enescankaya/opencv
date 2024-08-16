import cv2
import numpy as np

# Resmi yükle
img = cv2.imread("map.jpg")

# Resmi gri tonlamaya çevir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Görüntüye bulanıklık (blur) uygulayarak gürültüyü azalt
blur = cv2.GaussianBlur(gray, (3, 3),5)

# Threshold işlemi ile görüntüyü ikili (binary) hale getir
# Eğer bazı yerler fazladan kararıyorsa, min threshold değerini düşürebilirsiniz (30 iyi bir başlangıç)
ret, thresh = cv2.threshold(blur, 30, 255, cv2.THRESH_BINARY)

# İkili görüntüdeki konturları bul
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Her kontur için convex hull (dışbükey kılıf) hesapla
hull = []
for i in range(len(contours)):  # 0'dan kontur sayısına kadar döngü oluştur
    hull.append(cv2.convexHull(contours[i], returnPoints=True))  # Convex hull hesapla ve listeye ekle

# Boş bir arkaplan (siyah görüntü) oluştur
bg = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
# Konturları ve convex hull'ları çiz
for i in range(len(contours)):
    cv2.drawContours(bg, contours, i, (255, 0, 0), 1, 64, hierarchy)  # Orijinal konturları mavi çiz
    cv2.drawContours(bg, hull, i, (0, 255, 0), 1, 64)  # Convex hull'ları yeşil çiz

# Görüntüleri ekranda göster
cv2.imshow("bg", bg)
cv2.imshow("original",img)
# Bir tuşa basılana kadar bekle ve ardından tüm pencereleri kapat
cv2.waitKey(0)
cv2.destroyAllWindows()
