import cv2
import numpy as np
from matplotlib import pyplot as plt

# "osmanli.jpg" adlı resmi gri tonlamalı olarak oku (0 parametresi bu anlama gelir)
img = cv2.imread("osmanli.jpg", 0)

# 1. Threshold işlemi: Bu işlem, verilen sabit bir threshold değerine göre görüntüyü ikili (binary) hale getirir.
# ret: Threshold işlemi sonucu elde edilen değer.
# th1: İşlemden sonra elde edilen görüntü.
# İlk parametre: Girdi görüntüsü.
# İkinci parametre: Threshold değeri. Bu değerin altındaki pikseller siyah (0), üstündekiler beyaz (200) yapılır.
# Üçüncü parametre: Threshold sonrası beyaz olan piksellerin alacağı maksimum değer.
# Dördüncü parametre: Thresholding türü (THRESH_BINARY burada siyah-beyaz olarak ikiye ayırır).
ret, th1 = cv2.threshold(img, 100, 200, cv2.THRESH_BINARY)

# 2. Adaptive Threshold işlemi (Mean C): Bu işlem, her bir pikselin çevresindeki belirli bir bölgenin ortalamasına göre threshold uygular.
# th2: İşlemden sonra elde edilen görüntü.
# İlk parametre: Girdi görüntüsü.
# İkinci parametre: Beyaz olacak piksellerin alacağı maksimum değer (255).
# Üçüncü parametre: Adaptive thresholding yöntemi (ADAPTIVE_THRESH_MEAN_C burada, piksellerin çevresindeki değerlerin ortalamasını alır).
# Dördüncü parametre: Thresholding türü (THRESH_BINARY).
# Beşinci parametre: Blok boyutu (21, her bir piksel için değerlendirilecek çevresel bölgenin boyutunu belirler).
# Altıncı parametre: Ortalamadan çıkarılacak sabit değer (2). Bu değerin artırılması veya azaltılması, görüntüdeki karanlık veya aydınlık alanları etkiler.
th2 = cv2.adaptiveThreshold(img,150, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 109, 2)

# 3. Adaptive Threshold işlemi (Gaussian C): Bu işlem, her bir pikselin çevresindeki belirli bir bölgenin ağırlıklı ortalamasına göre threshold uygular.
# th3: İşlemden sonra elde edilen görüntü.
# Diğer parametreler yukarıdakiyle aynıdır, tek fark üçüncü parametrenin ADAPTIVE_THRESH_GAUSSIAN_C olmasıdır.
# Bu yöntem, piksellerin çevresindeki değerleri Gaussian ağırlıklı ortalama ile değerlendirir ve daha yumuşak bir geçiş sağlar.
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)

# Orijinal ve işlenmiş görüntüleri ekranda göster
cv2.imshow("img", img)          # Orijinal gri tonlamalı görüntü
cv2.imshow("img_th1", th1)      # Sabit threshold işlemi ile elde edilen görüntü
cv2.imshow("img-th2", th2)      # Mean C adaptive threshold işlemi ile elde edilen görüntü
cv2.imshow("img-th3", th3)      # Gaussian C adaptive threshold işlemi ile elde edilen görüntü

# Bir tuşa basılana kadar bekle
cv2.waitKey(0)

# Tüm pencereleri kapat
cv2.destroyAllWindows()
