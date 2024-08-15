import cv2, numpy as np

# "osmanli.jpg" dosyasını gri tonlamalı olarak oku (0 parametresi bu anlama gelir)
img = cv2.imread("osmanli.jpg", 0)

# Görüntünün satır ve sütun boyutlarını al
row, col = img.shape

# Döndürme matrisi oluştur. Görüntünün merkezine göre (col/2, row/2) 180 derece döndürme işlemi yapılacak.
# Üçüncü parametre scale (ölçek) faktörüdür. 1 olduğu için orijinal boyutlar korunur.
M = cv2.getRotationMatrix2D((col/2, row/2), 180, 1)

# Görüntüyü döndürmek için warpAffine fonksiyonu kullanılır.
# İlk parametre orijinal görüntü, ikinci parametre döndürme matrisi, üçüncü parametre ise döndürülen görüntünün boyutlarıdır.
dst = cv2.warpAffine(img, M, (col, row))

# Döndürülen görüntüyü "dst" adlı bir pencerede göster
cv2.imshow("dst", dst)

# Kullanıcının bir tuşa basmasını bekle
cv2.waitKey(0)

# Tüm pencereleri kapat
cv2.destroyAllWindows()
