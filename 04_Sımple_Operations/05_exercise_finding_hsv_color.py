import cv2
import numpy as np

# Kamera cihazını başlat
cap = cv2.VideoCapture(0)  # 0, varsayılan kamerayı ifade eder; başka bir kamera kullanılıyorsa 1, 2 vb. yazılabilir

# Kullanıcı tarafından ayar değişikliklerini işlemek için boş bir işlev tanımla
def nothing(x):
    pass

# "Trackbar" adlı bir pencere oluştur
cv2.namedWindow("Trackbar")

# Trackbar penceresinin boyutunu ayarla
cv2.resizeWindow("Trackbar", 500, 500)

# HSV renk aralığını ayarlamak için alt ve üst limitler için trackbar'lar oluştur
cv2.createTrackbar("Lower - H", "Trackbar", 0, 180, nothing)  # Hue (renk tonu) için alt sınır
cv2.createTrackbar("Lower - S", "Trackbar", 0, 255, nothing)  # Saturation (doygunluk) için alt sınır
cv2.createTrackbar("Lower - V", "Trackbar", 0, 255, nothing)  # Value (parlaklık) için alt sınır

cv2.createTrackbar("Upper - H", "Trackbar", 0, 180, nothing)  # Hue (renk tonu) için üst sınır
cv2.createTrackbar("Upper - S", "Trackbar", 0, 255, nothing)  # Saturation (doygunluk) için üst sınır
cv2.createTrackbar("Upper - V", "Trackbar", 0, 255, nothing)  # Value (parlaklık) için üst sınır

# Trackbar'ların varsayılan konumlarını ayarla
cv2.setTrackbarPos("Upper - H", "Trackbar", 180)  # Hue (renk tonu) için üst sınır: 180
cv2.setTrackbarPos("Upper - S", "Trackbar", 255)  # Saturation (doygunluk) için üst sınır: 255
cv2.setTrackbarPos("Upper - V", "Trackbar", 255)  # Value (parlaklık) için üst sınır: 255

while True:
    # Kamera görüntüsünü al
    ret, frame = cap.read()
    
    # Görüntüyü yatayda tersten çevir (kamera görüntüsünü ayna gibi yapmak için)
    frame = cv2.flip(frame, 1)
    
    # Görüntüyü BGR'den HSV'ye dönüştür
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Trackbar'lardan HSV sınır değerlerini al
    lower_h = cv2.getTrackbarPos("Lower - H", "Trackbar")
    lower_s = cv2.getTrackbarPos("Lower - S", "Trackbar")
    lower_v = cv2.getTrackbarPos("Lower - V", "Trackbar")
    
    upper_h = cv2.getTrackbarPos("Upper - H", "Trackbar")
    upper_s = cv2.getTrackbarPos("Upper - S", "Trackbar")
    upper_v = cv2.getTrackbarPos("Upper - V", "Trackbar")
    
    # HSV sınır değerlerinden alt ve üst renk aralıklarını oluştur
    lower_color = np.array([lower_h, lower_s, lower_v])
    upper_color = np.array([upper_h, upper_s, upper_v])
    
    # Belirtilen renk aralığına göre mask oluştur
    mask = cv2.inRange(frame_hsv, lower_color, upper_color)
    bitwise=cv2.bitwise_and(frame,frame,mask=mask)
    #bitwise: Maskeye göre filtrelenmiş görüntü. Maskedeki beyaz (255) bölgeler orijinal görüntüdeki piksellerle değiştirilir, siyah (0) bölgeler ise tamamen kaldırılır.
    # Orijinal görüntüyü ve maskelenmiş görüntüyü göster
    cv2.imshow("Original", frame)
    cv2.imshow("Masked", mask)
    cv2.imshow("Bitwise", bitwise)
    
    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

# Kamera ve tüm pencereleri serbest bırak ve kapat
cap.release()
cv2.destroyAllWindows()
