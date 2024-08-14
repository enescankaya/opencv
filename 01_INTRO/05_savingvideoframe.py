import cv2  # OpenCV kütüphanesini import ediyoruz

# Kamerayı açmak için VideoCapture nesnesi oluşturuyoruz. 
# '0' değeri, birden fazla kamera varsa varsayılan kamerayı seçer. 
cap = cv2.VideoCapture(0)

# Kaydedilecek video dosyasının yolunu ve adını belirtiyoruz.
# 'D:\opencv\OpencvProjects\myVideo.avi' olarak kaydedilecek.
# Dikkat edilmesi gereken nokta, \ işaretini kullanırken hata almamak için çift \ kullanmak gerekiyor (\\)
fileName = "D:\\opencv\\OpencvProjects\\myVideo.avi"

# Video codec tanımlaması yapıyoruz. 
# fourcc, bir video dosyasını sıkıştırmak için kullanılan dört karakterlik bir kod formatıdır.
# 'WMV2' codec formatını kullanıyoruz.
codec = cv2.VideoWriter.fourcc('W', 'M', 'V', '2')

# Video karesi (frame) başına düşen kare sayısını belirtiyoruz. 
# Bu durumda video 30 FPS (frame per second) olacak.
frameRate = 30

# Videonun çözünürlüğünü (genişlik x yükseklik) belirliyoruz.
resolution = (640, 480)

# VideoWriter nesnesi oluşturuyoruz.
# Bu nesne, video dosyasına görüntüleri yazmak için kullanılır.
videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution)

# Bir döngü başlatıyoruz. Bu döngü, kameradan görüntü alıp işleyerek video dosyasına yazacak.
while True:
    # Kameradan bir kare (frame) okuyup 'frame' değişkenine atıyoruz.
    # 'ret' değişkeni, okuma işleminin başarılı olup olmadığını belirten bir boolean (True/False) değeri döner.
    ret, frame = cap.read()

    # Çerçeveyi yatay olarak ters çeviriyoruz (ayna görüntüsü oluşturmak için). 
    # 1 değeri, görüntüyü y ekseninde çevirir.
    # 0, x ekseninde çevirir, -1 ise her iki eksende de çevirir.
    frame = cv2.flip(frame, 1)

    # Frame'i video dosyasına yazıyoruz.
    videoFileOutput.write(frame)

    # Frame'i bir pencere içinde gösteriyoruz.
    cv2.imshow("web cam", frame)

    # Her bir kare arasında 1 milisaniyelik bekleme yapıyoruz ve 'q' tuşuna basılırsa döngüden çıkıyoruz.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Video dosyasını kapatıyoruz ve yazmayı durduruyoruz.
videoFileOutput.release()

# Kamerayı serbest bırakıyoruz.
cap.release()

# Tüm açık pencereleri kapatıyoruz.
cv2.destroyAllWindows()
