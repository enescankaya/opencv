import cv2
import numpy as np
# Web kameradan video almak için VideoCapture nesnesini oluşturuyoruz
cap = cv2.VideoCapture(0)  # 0: Bilgisayarın ilk web kamerası
while True:
    # Kameradan bir görüntü alıyoruz
    ret, frame = cap.read()  # ret: işlem sonucunu belirtir (True/False), frame: alınan görüntü
    if not ret:
        break  # Görüntü alınamadıysa döngüden çık
    # Görüntüyü HSV renk uzayına dönüştürüyoruz
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # BGR'den HSV'ye dönüşüm
    # Görüntü üzerinde bulanıklık (blur) uyguluyoruz
    blur = cv2.GaussianBlur(hsv, (5, 5), 1)  # (5, 5): Bulanıklık penceresi boyutu, 1: Sigma değeri
    # İnsan ten rengini tespit etmek için HSV renk aralığı belirliyoruz
    lower_hsv = np.array([0, 120, 0], dtype=np.uint8)   # Alt sınır: [H, S, V] formatında
    upper_hsv = np.array([20, 255, 255], dtype=np.uint8)  # Üst sınır: [H, S, V] formatında
    # Belirlenen renk aralığında bir maske oluşturuyoruz
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)  # hsv: Giriş görüntüsü, lower_hsv ve upper_hsv: Alt ve üst renk sınırları
    # Maske üzerinde morfolojik işlemler uyguluyoruz
    kernel = np.ones((5, 5), np.uint8)  # Morfolojik işlemler için kullanılacak bir şablon (5x5 piksellik)
    # Küçük nesneleri temizlemek için Erozyon uyguluyoruz
    #mask = cv2.morphologyEx(mask, cv2.MORPH_ERODE, kernel)  # Erozyon: Küçük nesneleri temizler
    # Maskeyi genişletmek için Genişletme uyguluyoruz
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)  # Genişletme: Boşlukları doldurur
    # Maske üzerinde konturları buluyoruz
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  
    # mask: Giriş maske, cv2.RETR_TREE: Kontur hiyerarşisini elde eder, cv2.CHAIN_APPROX_SIMPLE: Kontur noktalarını sıkıştırır
    if contours:
        # En büyük konturu buluyoruz
        max_contour = max(contours, key=cv2.contourArea)  # En büyük konturu alanına göre seçer
        # En büyük kontur için dışbükey gövde (convex hull) oluşturuyoruz
        hull = cv2.convexHull(max_contour, returnPoints=True)  # max_contour: Giriş konturu, returnPoints=True: Noktaları döndürür
        # Dışbükeylik kusurlarını hesaplıyoruz
        hull_points = cv2.convexHull(max_contour, returnPoints=False)  # Dışbükey gövde noktalarını döndürmez
        if hull_points.size > 0:
            defects = cv2.convexityDefects(max_contour, hull_points)  # max_contour: Giriş konturu, hull_points: Dışbükey gövde noktaları
            if defects is not None:
                for i in range(defects.shape[0]):  # Kusurları döngüye alıyoruz
                    s, e, f, d = defects[i, 0]  # Kusur bilgilerini alıyoruz (başlangıç, bitiş, derinlik)
                    start = tuple(max_contour[s][0])  # Kusur başlangıç noktası
                    end = tuple(max_contour[e][0])    # Kusur bitiş noktası
                    far = tuple(max_contour[f][0])    # Kusur derinlik noktası
                    # Kusurları çiziyoruz
                    cv2.line(frame, start, end, (255, 0, 0), 2)  # Kusur çizgisi (kırmızı)
                    cv2.circle(frame, far, 5, (0, 255, 255), -1)  # Kusur noktası (sarı)
        # En büyük konturu çiziyoruz
        #cv2.drawContours(frame, [max_contour], -1, (0, 255, 0), 2)  # frame: Giriş görüntüsü, [max_contour]: Çizilecek kontur, -1: Tüm konturlar, (0, 255, 0): Renk (yeşil), 2: Kalınlık
    # Maske ve orijinal görüntüleri gösteriyoruz
    cv2.imshow("Mask", mask)  # Maske penceresi
    cv2.imshow("Frame", frame)  # Orijinal görüntü penceresi
    # 'q' tuşuna basılınca döngüden çıkıyoruz
    if cv2.waitKey(2) & 0xFF == ord("q"):
        break
# VideoCapture ve pencereyi kapatıyoruz
cap.release()  # Web kamerasını serbest bırakır
cv2.destroyAllWindows()  # Tüm OpenCV pencerelerini kapatır