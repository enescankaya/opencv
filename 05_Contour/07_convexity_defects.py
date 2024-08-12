import cv2
import numpy as np

# Resmi yükle
img = cv2.imread("star.png")

# Resmi gri tonlamalı hale getir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Görüntüyü ikili (binary) hale getir
ret, thresh = cv2.threshold(gray, 127, 255, 0)
# Konturları bul (RETR_TREE = tüm hiyerarşiyi bul, CHAIN_APPROX_SIMPLE = sadece gerekli noktaları bul) normalde böyle ama kodda hata verdi
contours, ret = cv2.findContours(thresh, 2, 1)

# İlk bulunan konturu al
cnt = contours[0]

# Dışbükey kılıfı (convex hull) hesapla, returnPoints=False ile sadece nokta indekslerini al
hull = cv2.convexHull(cnt, returnPoints=False)

# Dışbükey kılıfa uymayan noktaları (defects) bul
defects = cv2.convexityDefects(cnt, hull)

# Bulunan tüm kusurları (defects) dolaş
for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]  # Başlangıç, bitiş, en uzak nokta ve mesafe bilgilerini al
    start = tuple(cnt[s][0])     # Başlangıç noktasını al
    end = tuple(cnt[e][0])       # Bitiş noktasını al
    far = tuple(cnt[f][0])       # En uzak noktayı al
    
    # Başlangıç ve bitiş noktaları arasında bir çizgi çiz (yeşil renkte)
    cv2.line(img, start, end, [0, 255, 0], 2)
    
    # En uzak noktada bir daire çiz (yeşil renkte)
    cv2.circle(img, far, 5, [0, 5, 250], -1)

# Sonuç görüntüsünü ekranda göster
cv2.imshow("original", img)

# Bir tuşa basılana kadar bekle ve ardından tüm pencereleri kapat
cv2.waitKey(0)
cv2.destroyAllWindows()
