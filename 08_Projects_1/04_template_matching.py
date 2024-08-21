import cv2
import numpy as np

# Şablon (template) ve ana resmin dosya yollarını belirtiyoruz
template_path = "starwars2.jpg"
image_path = "starwars.jpg"

# Ana resmi yükleyip, gri tonlamaya (grayscale) çeviriyoruz
img = cv2.imread(image_path)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Şablon resmini gri tonlamada (grayscale) yüklüyoruz
template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

# Şablonun genişlik (w) ve yüksekliğini (h) alıyoruz
w, h = template.shape[::-1]  # .shape normalde (yükseklik, genişlik) verir, bu yüzden ters çeviriyoruz

# .shape ile şablonun boyutlarını kontrol edebiliriz.
# Eğer iki boyutlu değer dönüyorsa, resim gri tonlamadadır (grayscale).
# print(template.shape)

# Gri tonlamaya çevrilmiş ana resimle şablonu karşılaştırıyoruz
# Bu karşılaştırma sonucu, 'result' matrisi oluşur.
result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)

# Belirli bir eşik değerine (threshold) göre şablonun nerede olduğunu buluyoruz
# 0.95 burada çok yüksek bir eşik değeri, yani şablonun ana resimde neredeyse tamamen aynı olması gerekir.
location = np.where(result >= 0.95)

# Bulunan konumları döngü ile geziyoruz
# *location[::-1] ifadesi, (x, y) koordinatlarını elde etmek için location verilerini ters çevirir
for point in zip(*location[::-1]):
    # Bulunan her konum için bir dikdörtgen çiziyoruz
    # cv2.rectangle fonksiyonu, resim üzerine bir dikdörtgen çizer
    # (point[0], point[1]) dikdörtgenin sol üst köşesini belirtir
    # (point[0] + w, point[1] + h) dikdörtgenin sağ alt köşesini belirtir
    # (0, 255, 0) dikdörtgenin rengini (yeşil) belirler
    # 2, dikdörtgenin kalınlığını belirtir
    cv2.rectangle(img, point, (point[0] + w, point[1] + h), (0, 255, 0), 2)

    # Bulunan noktaları terminale yazdırıyoruz
    print(point)

# Sonuç olarak ana resmi (içinde şablon işaretlenmiş halde) ve şablon resmini gösteriyoruz
cv2.imshow("image", img)
cv2.imshow("template", template)

# Bir tuşa basılmasını bekler ve ardından tüm pencereleri kapatır
cv2.waitKey(0)
cv2.destroyAllWindows()
