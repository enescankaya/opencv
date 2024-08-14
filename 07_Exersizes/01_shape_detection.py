import cv2
import numpy as np

# Farklı yazı tipleri ayarlanıyor
font = cv2.FONT_HERSHEY_COMPLEX
font1 = cv2.FONT_HERSHEY_SIMPLEX  # Farklı fontlar kullanılabilir

# Görüntüyü okuma ve gri tonlamaya dönüştürme
img = cv2.imread("polygons.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Görüntüdeki pikselleri iki seviyeye ayırarak (binarization) binary bir görüntü elde etme
_, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# Konturları bulma
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Bulunan konturlar üzerinde döngü
for cnt in contours:
    # Konturu yaklaştırarak (approximation) daha az sayıda köşe noktası ile temsil etme
    epsilon = 0.01 * cv2.arcLength(cnt, True)  
    # epsilon: Konturun çevresinin %1'i kadar bir hata payı belirler. Bu değer, konturun ne kadar sadelikle temsil edileceğini belirler.
    
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    # approxPolyDP: Konturu yaklaşık olarak belirtilen hata payı ile daha az sayıda köşe noktası ile temsil eder.
    # Bu, şeklin sadeleştirilmiş halini elde etmemizi sağlar. 

    # Yaklaştırılmış konturu çizme
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    # drawContours: Bulunan konturu orijinal görüntü üzerine çizer. 
    # [approx]: Bu, yaklaşık kontur koordinatlarını içerir.
    # (0, 0, 0): Siyah renkte çizilir.
    # 5: Konturun çizgi kalınlığı.

    # İlk köşe noktasının koordinatlarını alıyoruz
    x = approx.ravel()[0]
    y = approx.ravel()[1]
     # Şeklin kütle merkezini (merkez noktasını) hesaplamak için moment hesapla
    M = cv2.moments(cnt)
    if M["m00"] != 0:
        x = int(M["m10"] / M["m00"])-23
        y = int(M["m01"] / M["m00"])
    else:
        cX, cY = x, y
    # approx.ravel() fonksiyonu, kontur noktalarını tek bir düz diziye indirger ve 
    # [0] ve [1] indexleri ilk köşe noktasının x ve y koordinatlarını verir.

    # Şeklin kaç köşesi olduğunu kontrol ederek tipini belirleme
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), font, 0.4, (0,0,255))
        # Eğer kontur 3 köşe içeriyorsa, bu bir üçgen olarak kabul edilir.
        # Şeklin adını görüntüde bu köşeye yazdırır.

    elif len(approx) == 4:
        cv2.putText(img, "Rectangle", (x, y), font, 0.4, (0,0,255))
        # Eğer 4 köşe varsa, bu bir dikdörtgen (ya da kare) olarak kabul edilir.
    
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), font1, 0.4, (0,0,255))
        # 5 köşe, şeklin bir beşgen olduğunu belirtir.

    elif len(approx) == 6:
        cv2.putText(img, "Hexagon", (x, y), font1, 0.4, (0,0,255))
        # 6 köşe, altıgen olduğunu belirtir.
    
    else:
        cv2.putText(img, "Ellipse", (x, y), font1, 0.4, (0,0,255))
        # Eğer daha fazla köşe varsa (genellikle 7 ve üstü), bu şekil bir elips ya da daire olarak kabul edilir.

# Görüntüyü ekranda göster
cv2.imshow("image", img)

# Bir tuşa basılmasını bekle ve ardından pencereleri kapat
cv2.waitKey(0)
cv2.destroyAllWindows()
