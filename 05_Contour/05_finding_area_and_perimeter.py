import cv2

# 1. Görüntüyü yüklüyoruz.
img = cv2.imread("contour.png")

# 2. Görüntüyü gri tonlamalıya çeviriyoruz.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Görüntüdeki pikselleri iki sınıfa (siyah ve beyaz) ayırmak için eşikleme yapıyoruz.
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 4. Görüntüdeki konturları buluyoruz. Bu fonksiyon, bulduğu tüm konturları bir liste içinde döndürüyor.
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 5. İlk konturu (0. indeksteki) seçiyoruz.
cnt = contours[0]
# **Neden 0. indeksteki konturu seçtik?**
# `cv2.findContours` fonksiyonu, görüntüdeki tüm konturları bir liste olarak döner. 
# Bu listede konturlar, görüntüde bulundukları sıraya göre sıralanmıştır.
# 0. indeks, ilk bulunan konturu temsil eder. Bu, genellikle en büyük veya en dıştaki kontur olabilir, 
# ancak bu görüntüye bağlıdır. Eğer belirli bir kontur üzerinde işlem yapmak istiyorsanız,
# bu indeksi değiştirerek farklı konturları seçebilirsiniz.

# 6. Seçtiğimiz konturun alanını hesaplıyoruz.
area = cv2.contourArea(cnt)  # `cv2.contourArea` fonksiyonu, seçilen konturun alanını döner.

# 7. Konturun momentlerini hesaplıyoruz.
M = cv2.moments(cnt)
# Momentler, bir konturun farklı özelliklerini tanımlamak için kullanılan değerlerdir.
# `m00` değeri, konturun alanını temsil eder. Bu değer, `cv2.contourArea` ile hesaplanan alana eşittir.

# 8. Hesaplanan alanı ekrana yazdırıyoruz.
print(area)

# 9. Momentlerden hesaplanan alanı ekrana yazdırıyoruz.
print(M['m00'])

# 10. Konturun çevresini hesaplıyoruz.
perimeter = cv2.arcLength(cnt, True)
# `cv2.arcLength` fonksiyonu, konturun uzunluğunu hesaplar. 
# İkinci parametre `True` ise, konturun kapalı (çevresi tam bir şekil) olduğu varsayılır.

# 11. Hesaplanan çevre uzunluğunu ekrana yazdırıyoruz.
print(perimeter)

# 12. Orijinal görüntüyü ekranda gösteriyoruz.
cv2.imshow("original", img)

# 13. Gri tonlamalı görüntüyü ekranda gösteriyoruz.
cv2.imshow("gray", gray)

# 14. Eşiklenmiş görüntüyü ekranda gösteriyoruz.
cv2.imshow("thresh", thresh)

# 15. Ekrana gösterilen görüntülerin kapanmasını bekliyoruz.
cv2.waitKey(0)

# 16. Tüm pencereleri kapatıyoruz.
cv2.destroyAllWindows()
