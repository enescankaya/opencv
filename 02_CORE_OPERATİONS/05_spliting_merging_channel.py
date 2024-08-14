import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntü dosyasının yolunu belirtiyoruz
path = "TEST_IMAGES/opencv_logo.png"

# cv2.imread() fonksiyonu ile resmi yüklüyoruz
img = cv2.imread(path)

# img.shape komutuyla resmin boyutlarını yazdırıyoruz (yükseklik, genişlik, kanal sayısı)
print("Shape: {}".format(img.shape))

# cv2.split() fonksiyonu ile görüntüyü üç ayrı kanala (B, G, R) bölüyoruz
# Bu, görüntünün mavi, yeşil ve kırmızı bileşenlerini ayrı ayrı elde etmemizi sağlar
(B, G, R) = cv2.split(img)

# cv2.merge() fonksiyonu ile üç renk kanalını birleştirip orijinal görüntüyü yeniden oluşturuyoruz
merged = cv2.merge([B, G, R])

# RGB olarak, BGR kanallarını sıralama şekli değiştiriyoruz (BGR'den RGB'ye dönüştürüyoruz)
RGB = cv2.merge([R, G, B])

# Siyah bir görüntü oluşturuyoruz, boyut olarak orijinal resmin yüksekliği ve genişliğiyle aynı
# dtype="uint8" kullanarak veri tipini belirliyoruz
black = np.zeros(img.shape[:2], dtype="uint8")

# Oluşturduğumuz siyah görüntüyü gösteriyoruz
cv2.imshow("black", black)

# Kırmızı kanal görüntüsü, diğer iki kanal siyah olacak şekilde birleştiriyoruz
cv2.imshow("Red", cv2.merge([black, black, R]))

# Yeşil kanal görüntüsü, diğer iki kanal siyah olacak şekilde birleştiriyoruz
cv2.imshow("Green", cv2.merge([black, G, black]))

# Mavi kanal görüntüsü, diğer iki kanal siyah olacak şekilde birleştiriyoruz
cv2.imshow("Blue", cv2.merge([B, black, black]))

# Orijinal görüntünün yeniden oluşturulmuş halini gösteriyoruz
cv2.imshow("MERGED", merged)

# Orijinal görüntüyü gösteriyoruz
cv2.imshow("image", img)

# BGR'den RGB'ye dönüştürülmüş görüntüyü gösteriyoruz
cv2.imshow("RGB", RGB)

# Bir tuşa basılmasını bekliyoruz, böylece pencereler kapanmaz
cv2.waitKey(0)

# Tüm açık pencereleri kapatıyoruz
cv2.destroyAllWindows()
