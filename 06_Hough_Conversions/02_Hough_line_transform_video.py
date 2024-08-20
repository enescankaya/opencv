import cv2
import numpy as np

# Video dosyasını yükleyin
vid = cv2.VideoCapture("line.mp4")

while 1:
    # Her bir kareyi okuyun
    ret, frame = vid.read()

    # Videonun sonunda, kare alınamıyorsa döngüyü kırın
    if not ret:
        break

    # Kareyi 640x480 boyutlarına yeniden boyutlandırın
    frame = cv2.resize(frame, (640, 480))

    # Görüntüyü BGR'den HSV renk uzayına dönüştürün
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Sarı rengin alt ve üst HSV değer aralıklarını belirleyin
    lower_yellow = np.array([15, 100, 100], np.uint8)
    upper_yellow = np.array([35, 255, 255], np.uint8)

    # HSV görüntüsünde sadece sarı renkleri içeren bir maske oluşturun
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Kenarları tespit etmek için Canny algoritmasını uygulayın
    # 75 ve 250, düşük ve yüksek eşik değerleridir
    edges = cv2.Canny(mask, 75, 250)

    # HoughLinesP algoritması ile kenarları kullanarak çizgileri tespit edin
    # Parametreler:
    # - edges: Kenarları belirlenmiş görüntü
    # - 1: Parametre uzayında pikseller arası çözünürlük (rho)
    # - np.pi/180: Parametre uzayında açısal çözünürlük (theta)
    # - 50: Bir çizgi olarak kabul edilmesi için gereken minimum oy sayısı (threshold)
    # - maxLineGap=50: Kesintili olan çizgileri birleştirmek için kullanılan maksimum boşluk miktarı
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 60, maxLineGap=50)

    # Eğer çizgiler tespit edildiyse, her birini çizdir
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]  # Çizginin başlangıç ve bitiş noktalarını al
            # Çizgiyi KIRMIZI renkte ve 1 piksel kalınlığında çizdir
            cv2.line(frame, (x1, y1), (x2, y2), (2, 0, 255), 1)

    # İşlenen kareyi ekranda gösterin
    cv2.imshow("lined", frame)

    # Eğer 'q' tuşuna basılırsa döngüyü kırın ve videoyu sonlandırın
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

# Video dosyasını serbest bırakın ve tüm açık pencereleri kapatın
vid.release()
cv2.destroyAllWindows()
