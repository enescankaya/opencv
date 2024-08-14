import cv2
import numpy as np

# Video dosyasını açar ('hsv.mp4' adlı dosya).
cap = cv2.VideoCapture("hsv.mp4")

# Trackbar fonksiyonu. Trackbar hareket ettiğinde bu fonksiyon çalışır.
# Şu anlık boş, çünkü hiçbir işlem yapmıyoruz.
def nothing(x):
    pass

# "Trackbar" adlı bir pencere oluşturur.
cv2.namedWindow("Trackbar")

# HSV renk aralığının alt ve üst sınırlarını belirlemek için trackbar'lar oluşturulur.
cv2.createTrackbar("LH", "Trackbar", 0, 179, nothing)  # LH: Lower Hue
cv2.createTrackbar("LS", "Trackbar", 0, 255, nothing)  # LS: Lower Saturation
cv2.createTrackbar("LV", "Trackbar", 0, 255, nothing)  # LV: Lower Value
cv2.createTrackbar("UH", "Trackbar", 0, 179, nothing)  # UH: Upper Hue
cv2.createTrackbar("US", "Trackbar", 0, 255, nothing)  # US: Upper Saturation
cv2.createTrackbar("UV", "Trackbar", 0, 255, nothing)  # UV: Upper Value

# Video akışını işlemek için sonsuz bir döngü başlatır.
while 1:
    # Video akışından bir kare okur. 'ret' başarılı olup olmadığını gösterir, 'frame' ise kareyi içerir.
    ret, frame = cap.read()

    # Eğer video biterse, başa sarmak için akışı sıfırlar.
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Videoyu başa sarar.
        continue  # Döngünün başına döner ve yeni bir kare okur.

    # Kareyi 640x480 boyutuna yeniden boyutlandırır.
    frame = cv2.resize(frame, (640, 480))

    # BGR renk uzayından HSV renk uzayına dönüştürür.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Trackbar'dan alınan HSV değerlerini okur.
    lh = cv2.getTrackbarPos("LH", "Trackbar")  # Lower Hue değeri
    ls = cv2.getTrackbarPos("LS", "Trackbar")  # Lower Saturation değeri
    lv = cv2.getTrackbarPos("LV", "Trackbar")  # Lower Value değeri
    uh = cv2.getTrackbarPos("UH", "Trackbar")  # Upper Hue değeri
    us = cv2.getTrackbarPos("US", "Trackbar")  # Upper Saturation değeri
    uv = cv2.getTrackbarPos("UV", "Trackbar")  # Upper Value değeri

    # Alt ve üst HSV sınırlarını bir numpy array olarak tanımlar.
    lower_blue = np.array([lh, ls, lv])
    upper_blue = np.array([uh, us, uv])

    # HSV görüntüsünü bu sınırlar arasında maskeleme yapar.
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Maskeyi kullanarak orijinal görüntü üzerinde bitwise AND işlemi yapar.
    bitWise = cv2.bitwise_and(frame, frame, mask=mask)

    # Orijinal kareyi gösterir.
    cv2.imshow("Frame", frame)

    # Maske görüntüsünü gösterir.
    cv2.imshow("Mask", mask)

    # Bitwise AND işlemi uygulanmış görüntüyü gösterir.
    cv2.imshow("bitWise", bitWise)

    # 'q' tuşuna basıldığında döngüden çıkar.
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

# Video akışını serbest bırakır ve tüm pencereleri kapatır.
cap.release()
cv2.destroyAllWindows()
