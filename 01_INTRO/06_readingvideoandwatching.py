import cv2
cap = cv2.VideoCapture(0)#hazır video varsa buraya video adresi yazılır
while True:
    ret, frame =cap.read()#cap.read() toplam 2 değer döndürür. ilki eğer video okursa true okumuyorsa false döndürür.ikincisi ise framelerdir
    #şimdi buradaki durum return değeri true ise cap.read() değer okuyordur yani devam et çünkü while true diyoruz. false ise döngünder çıkar.
    frame = cv2.flip(frame,1)#flip fonksiyonu görüş açısını değiştirir eksenlere göre 1 ayna yansıması gibi gösterir
    cv2.imshow("webcam",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    # cv2.waitKey(1) her frame'in ekranda durmasüresidir yani her foroğraf ekranda ne kadar duracak onun süresidir. ne kadar az o kadar hızlı görüntü demek 
    #eğer 0 girersek ilk frame gözükür resim olarak kalır yani resimlerde 0 yazıyoruz buraya
    #0xFF == ord("q") demek klavyeden q uşuna basılırsa demektir.
cap.release()
cv2.destroyAllWindows()