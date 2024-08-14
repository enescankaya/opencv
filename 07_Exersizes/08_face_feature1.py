import cv2
import numpy as np
import math

# Kamerayı başlatıyoruz
cap = cv2.VideoCapture(0)  # Parametre 0, bilgisayarın varsayılan kamerasını kullanmak için. Harici bir kamera varsa, 1 veya 2 gibi bir değer kullanılabilir.

# En büyük konturu bulmak için fonksiyon
def findMaxContour(contours):
    max_i = 0
    max_area = 0
    for i in range(len(contours)):
        area_face = cv2.contourArea(contours[i])  # cv2.contourArea, bir konturun kapladığı alanı hesaplar.
        if max_area < area_face:
            max_area = area_face
            max_i = i
    try:
        c = contours[max_i]  # En büyük konturu seçiyoruz.
    except:
        contours = [0]
        c = contours[0]
    return c

while 1:
    # Kameradan kare okuma
    ret, frame = cap.read()  # ret, okumanın başarılı olup olmadığını belirtir. frame ise okunan görüntü karesidir.
    # Aynalama işlemi
    frame = cv2.flip(frame, 1)  # Görüntüyü yatay olarak ters çevirir (ayna efekti).
    
    # İlgi alanını (ROI) belirleme
    roi = frame[50:250, 200:400]  # frame'in [y1:y2, x1:x2] bölgesini alarak, ilgilendiğimiz alanı (ROI) belirliyoruz.
    
    # Ekranda ROI'yi göstermek için kırmızı bir dikdörtgen çiziyoruz
    cv2.rectangle(frame, (200, 50), (400, 250), (0, 0, 255), 0)  
    # (200, 50) sol üst köşe koordinatı, (400, 250) sağ alt köşe koordinatı, (0, 0, 255) renk (BGR formatında kırmızı), 0 çizgi kalınlığı (doldurulmuş dikdörtgen).

    # BGR'den HSV renk uzayına dönüşüm
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)  # BGR formatındaki görüntüyü HSV formatına dönüştürür. HSV (Hue, Saturation, Value) renk uzayıdır.

    # HSV renk aralığını belirleme
    lower_color = np.array([1, 80, 10], dtype=np.uint8)  # Alt sınır HSV değeri (kırmızı tonlar)
    upper_color = np.array([170, 255, 255], dtype=np.uint8)  # Üst sınır HSV değeri (kırmızı tonlar)

    # Belirtilen renk aralığında mask oluşturma
    mask = cv2.inRange(hsv, lower_color, upper_color)  # hsv görüntüsünde lower_color ve upper_color arasındaki renkleri maskeleyerek binary bir görüntü oluşturur.
    
    # Maskeyi genişletme
    kernel = np.ones((11, 11), np.uint8)  # 11x11 boyutunda, tüm elemanları 1 olan bir matris (kernal) oluşturur.
    mask = cv2.dilate(mask, kernel, iterations=1)  # Maskeyi genişletir (dilate), beyaz pikselleri genişleterek gürültüyü azaltır.

    # Maske üzerinde bulanıklaştırma
    mask = cv2.medianBlur(mask, 17)  # Maskeyi bulanıklaştırır, böylece küçük gürültü noktaları ortadan kalkar. 17, bulanıklığın derecesini belirtir.

    # Maskedeki konturları bulma
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.RETR_TREE, kontur hiyerarşisini tamamen döndürür. cv2.CHAIN_APPROX_SIMPLE, kontur noktalarını sadeleştirir.

    if len(contours) > 0:
        # En büyük konturu bulma
        c = findMaxContour(contours)
        
        # Konturun en uç noktalarını bulma
        extLeft = tuple(c[c[:, :, 0].argmin()][0])  # Konturun en sol noktasını bulur.
        extRight = tuple(c[c[:, :, 0].argmax()][0])  # Konturun en sağ noktasını bulur.
        extTop = tuple(c[c[:, :, 1].argmin()][0])  # Konturun en üst noktasını bulur.
        extBot = tuple(c[c[:, :, 1].argmax()][0])  # Konturun en alt noktasını bulur.
        
        # Bu uç noktaları işaretleme
        cv2.circle(roi, extLeft, 5, (0, 255, 0), 2)  # (0, 255, 0) yeşil renkte, 5 piksel yarıçapında bir daire çizilir.
        cv2.circle(roi, extRight, 5, (0, 255, 0), 2)
        cv2.circle(roi, extTop, 5, (0, 255, 0), 2)
        cv2.circle(roi, extBot, 5, (0, 255, 0), 2)
        
        # Uç noktaları birleştiren çizgiler çizme
        cv2.line(roi, extLeft, extTop, (0, 0, 255))  # Uç noktalar arasında kırmızı çizgiler çizilir.
        cv2.line(roi, extTop, extRight, (0, 0, 255))
        cv2.line(roi, extRight, extBot, (0, 0, 255))
        cv2.line(roi, extBot, extLeft, (0, 0, 255))
        
        # Kenar uzunluklarını hesaplama
        a = math.sqrt((extRight[0] - extTop[0]) ** 2 + (extRight[1] - extTop[1]) ** 2)  # Üçgenin bir kenarının uzunluğu.
        b = math.sqrt((extBot[0] - extRight[0]) ** 2 + (extBot[1] - extRight[1]) ** 2)  # Üçgenin bir başka kenarının uzunluğu.
        c = math.sqrt((extBot[0] - extTop[0]) ** 2 + (extBot[1] - extTop[1]) ** 2)  # Üçgenin üçüncü kenarının uzunluğu.
        
        try:
            # Kosinüs teoremi ile açı hesaplama
            angle_ab = int(math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * b * c)) * 57)  # Üçgenin köşe açısını hesaplar ve dereceye çevirir.
            cv2.putText(roi, str(angle_ab), (extRight[0] - 100, extRight[1]), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 0, 255), 1)
            # Açı değeri, roi üzerine yazılır. 
            # (extRight[0] - 100, extRight[1]) koordinatları, yazı pozisyonunu belirtir.
            # cv2.FONT_HERSHEY_SCRIPT_SIMPLEX yazı tipi, 1 yazı boyutu, (0, 0, 255) kırmızı renk, 1 yazı kalınlığı.
        except:
            # Hata durumunda '?' yazdırılır
            cv2.putText(roi, "?", (extRight[0] - 100, extRight[1]), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 0, 255), cv2.LINE_AA)
    
    # Maskeyi, ROI'yi ve tam kareyi gösterme
    cv2.imshow("mask", mask)  # Maskelenmiş görüntüyü gösterir.
    cv2.imshow("roi", roi)  # İlgi alanını (ROI) gösterir.
    cv2.imshow("frame", frame)  # Tam görüntü karesini gösterir.
    
    # 'q' tuşuna basılınca döngüden çıkma
    if cv2.waitKey(20) & 0xFF == ord("q"):  # cv2.waitKey(20) 20 ms boyunca bir tuşun basılıp basılmadığını kontrol eder.
        break  # 'q' tuşuna basıldığında döngüden çıkılır.

# Kaynakları serbest bırakma ve pencereleri kapatma
cap.release()  # Kamerayı serbest bırakır.
cv2.destroyAllWindows()  # Açık tüm OpenCV pencerelerini kapatır.
