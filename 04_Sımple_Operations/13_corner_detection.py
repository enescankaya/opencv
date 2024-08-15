import cv2
import numpy as np

# 1. Görüntüleri Okuma
img = cv2.imread("text.png")
img1 = cv2.imread("contour.png")  # Bu görüntü kullanılmıyor, ancak belki ileride kullanılabilir

# 2. Gri Tonlamalı Görüntüye Dönüştürme
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Görüntüyü gri tonlamalıya dönüştürmek, renk bilgilerini kaldırır ve sadece yoğunluk bilgilerini tutar.
# Bu işlem, köşe tespiti gibi işlemler için daha basit ve etkili bir giriş sağlar.

# 3. Veri Tipi Dönüştürme
gray = np.float32(gray)
# `cv2.goodFeaturesToTrack` fonksiyonu, gri tonlamalı görüntü üzerinde köşe tespiti yapabilmek için `float32` veri tipinde bir görüntü bekler.
# Bu dönüşüm, fonksiyonun daha iyi performans göstermesine yardımcı olur.

# 4. Köşe Tespiti
corners = cv2.goodFeaturesToTrack(gray, 2000, 0.01, 10)
# `cv2.goodFeaturesToTrack`: Köşe (corner) noktalarını tespit eder.
# - `2000`: Maksimum köşe sayısı. Daha fazla köşe aramak istiyorsanız bu değeri artırabilirsiniz.
# - `0.01`: Köşelerin belirginlik eşiği. Daha yüksek bir değer daha belirgin köşeleri tespit eder.
# - `10`: Köşeler arasında minimum uzaklık. Bu, köşelerin birbirine ne kadar yakın olabileceğini belirler.

# 5. Köşe Koordinatlarını Tam Sayılara Dönüştürme
corners = np.int0(corners)
# Köşe koordinatları, köşe tespitinin sonucunda `float32` türünde olur.
# Görüntü üzerinde daireler çizerken tam sayı koordinatları gerektiğinden, bu koordinatları `int` türüne dönüştürürüz.

# 6. Köşe Noktalarını Görüntü Üzerinde Çizme
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
    # `corner.ravel()`: Köşe koordinatlarını düzleştirir ve x, y olarak ayırır.
    # `cv2.circle`: Belirtilen koordinatlarda, kırmızı renkte ve yarıçapı 3 olan daireler çizer.
    # Bu işlem, tespit edilen köşeleri görsel olarak vurgular.

# 7. Sonuç Görüntüsünü Gösterme
cv2.imshow("corner", img)
# `cv2.imshow`: Köşe noktalarının üzerine daireler çizilmiş olan görüntüyü gösterir.
# Bu adım, köşe tespitinin sonuçlarını görsel olarak incelemenizi sağlar.

# 8. Görüntü Pencerelerini Kapatma
cv2.waitKey(0)
cv2.destroyAllWindows()
# `cv2.waitKey(0)`: Bir tuşa basılmasını bekler. Tuşa basıldığında görüntü pencerelerini kapatır.
# `cv2.destroyAllWindows()`: Açık olan tüm OpenCV pencerelerini kapatır.
# Bu, programın sonunda tüm kaynakları serbest bırakır ve kullanıcıya temiz bir kapanış sağlar.