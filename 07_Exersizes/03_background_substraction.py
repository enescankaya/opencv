import cv2
import numpy as np

# Video dosyasını açar. 'car.mp4' adlı dosyanın yolunu belirtir.
cap = cv2.VideoCapture("car.mp4")

# İlk kareyi okur ve iki değer döndürür: bir boolean (başarı durumu) ve ilk kare.
_, first_frame = cap.read()

# İlk kareyi 640x480 boyutuna yeniden boyutlandırır.
first_frame = cv2.resize(first_frame, (640, 480))

# İlk kareyi gri tonlamalıya çevirir. BGR renk formatından GRAY renk formatına dönüştürür.
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

# Gri tonlamalı görüntüye Gaussian Blur uygular. (5,5) çekirdek boyutu kullanılır.
first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)

# Video akışını işlemek için sonsuz bir döngü başlatır.
while 1:
    # Bir sonraki kareyi okur ve iki değer döndürür: bir boolean (başarı durumu) ve kare.
    _, frame = cap.read()
    
    # Kareyi 640x480 boyutuna yeniden boyutlandırır.
    frame = cv2.resize(frame, (640, 480))
    
    # Kareyi gri tonlamalıya çevirir.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Gri tonlamalı görüntüye Gaussian Blur uygular. (5,5) çekirdek boyutu kullanılır.
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # İlk gri tonlamalı kare ile mevcut gri tonlamalı kare arasındaki mutlak farkı hesaplar.
    diff = cv2.absdiff(first_gray, gray)
    
    # Fark görüntüsünü, belirli bir eşik değeri kullanarak ikili (binary) görüntüye dönüştürür.
    # 30, eşik değerini; 220, maksimum değeri; cv2.THRESH_BINARY, eşikleme türünü belirtir.
    _, diff = cv2.threshold(diff, 30, 220, cv2.THRESH_BINARY)
    
    # Sonuçları pencerelerde görüntüler.
    cv2.imshow("frame", frame)        # Orijinal kareyi gösterir.
    cv2.imshow("first_frame", first_frame)  # İlk kareyi gösterir.
    cv2.imshow("diff", diff)          # Fark görüntüsünü gösterir.
    
    # 'q' tuşuna basılmadıkça döngüyü devam ettirir.
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

# Video akışını serbest bırakır ve tüm pencereleri kapatır.
cap.release()
cv2.destroyAllWindows()
