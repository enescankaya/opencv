import cv2
import numpy as np

def nothing(x):
    pass  # Trackbar callback fonksiyonu. Bu fonksiyon trackbar değişikliklerinde hiçbir şey yapmıyor.

# Kamerayı açıyoruz.
cap = cv2.VideoCapture(0)

# "Settings" isimli bir pencere oluşturuyoruz.
cv2.namedWindow("Settings")

# Trackbarlar (kaydırma çubukları) oluşturuyoruz. Bu trackbarlar alt ve üst HSV değerlerini ayarlamak için kullanılıyor.
cv2.createTrackbar("Lower-Hue", "Settings", 0, 180, nothing)
cv2.createTrackbar("Lower-Saturation", "Settings", 0, 255, nothing)
cv2.createTrackbar("Lower-Value", "Settings", 0, 255, nothing)
cv2.createTrackbar("Upper-Hue", "Settings", 0, 180, nothing)
cv2.createTrackbar("Upper-Saturation", "Settings", 0, 255, nothing)
cv2.createTrackbar("Upper-Value", "Settings", 0, 255, nothing)

# Metin yazdırmak için kullanılan fontu belirliyoruz.
font = cv2.FONT_HERSHEY_SIMPLEX

# Sonsuz bir döngü ile her kareyi işliyoruz.
while 1:
    ret, frame = cap.read()  # Kameradan bir kare okuyoruz.
    frame = cv2.flip(frame, 1)  # Aynalama (flip) işlemi uyguluyoruz. Bu, görüntüyü yatay olarak çevirir.
    
    # BGR formatından HSV formatına dönüştürüyoruz.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Trackbar üzerinden alt ve üst HSV değerlerini alıyoruz.
    lh = cv2.getTrackbarPos("Lower-Hue", "Settings")
    ls = cv2.getTrackbarPos("Lower-Saturation", "Settings")
    lv = cv2.getTrackbarPos("Lower-Value", "Settings")
    uh = cv2.getTrackbarPos("Upper-Hue", "Settings")
    us = cv2.getTrackbarPos("Upper-Saturation", "Settings")
    uv = cv2.getTrackbarPos("Upper-Value", "Settings")
    
    # Alt ve üst renk sınırlarını birer NumPy dizisi olarak tanımlıyoruz.
    lower_color = np.array([lh, ls, lv])
    upper_color = np.array([uh, us, uv])
    
    # Renk aralığındaki pikselleri bulmak için maske oluşturuyoruz.
    mask = cv2.inRange(hsv, lower_color, upper_color)
    
    # Maske üzerine erozyon işlemi uyguluyoruz. Bu işlem küçük parazitleri yok eder.
    kernel = np.ones((5, 5), np.uint8)  # 5x5 boyutunda bir kernel tanımlıyoruz.
    mask = cv2.erode(mask, kernel)  # Erozyon işlemini uyguluyoruz.
    
    # Maskenin konturlarını (sınırlarını) buluyoruz.
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Bulunan her kontur üzerinde işlem yapıyoruz.
    for cnt in contours:
        area = cv2.contourArea(cnt)  # Kontur alanını hesaplıyoruz.
        epsilon = 0.1 * cv2.arcLength(cnt, True)  # Konturun kenarlarının uzunluğuna göre bir yaklaşık değer hesaplıyoruz.
        approx = cv2.approxPolyDP(cnt, epsilon, True)  # Konturun köşe noktalarını belirleyip yaklaşık çokgen çiziyoruz.
        
        # Konturun x ve y koordinatlarını alıyoruz.
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        
        # Sadece belirli bir alandan büyük konturlarla işlem yapıyoruz.
        if area > 400:
            cv2.drawContours(frame, [approx], 0, (0, 0, 255), 5)  # Konturu kırmızı renkte çiziyoruz.
            
            # Konturün kaç kenarlı olduğunu kontrol ederek şekli belirliyoruz.
            if len(approx) == 3:
                cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0))  # Üçgen ise "Triangle" yazıyoruz.
            elif len(approx) == 4:
                cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0))  # Dörtgen ise "Rectangle" yazıyoruz.
            elif len(approx) >4:
                cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))  # Diğer durumlarda "Circle" yazıyoruz.
    
    # İşlenmiş görüntüyü ve maskeyi ekranda gösteriyoruz.
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    
    # Kullanıcı "q" tuşuna bastığında döngüden çıkıyoruz.
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

# Kamerayı serbest bırakıyoruz ve tüm pencereleri kapatıyoruz.
cap.release()
cv2.destroyAllWindows()